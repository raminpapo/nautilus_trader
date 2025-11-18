# Documentation: trade.rs

## File Metadata

- **Path**: `crates/model/src/python/data/trade.rs`
- **Size**: 13,821 bytes
- **Lines**: 422
- **Language**: Rust

## Original Source

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
//  https://nautechsystems.io
//
//  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
//  You may not use this file except in compliance with the License.
//  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
// -------------------------------------------------------------------------------------------------

use std::{
    collections::{HashMap, hash_map::DefaultHasher},
    hash::{Hash, Hasher},
    str::FromStr,
};

use nautilus_core::{
    UnixNanos,
    python::{
        IntoPyObjectNautilusExt,
        serialization::{from_dict_pyo3, to_dict_pyo3},
        to_pyvalue_err,
    },
    serialization::{
        Serializable,
        msgpack::{FromMsgPack, ToMsgPack},
    },
};
use pyo3::{
    IntoPyObjectExt,
    prelude::*,
    pyclass::CompareOp,
    types::{PyDict, PyInt, PyString, PyTuple},
};

use super::data_to_pycapsule;
use crate::{
    data::{Data, TradeTick},
    enums::{AggressorSide, FromU8},
    identifiers::{InstrumentId, TradeId},
    python::common::PY_MODULE_MODEL,
    types::{
        price::{Price, PriceRaw},
        quantity::{Quantity, QuantityRaw},
    },
};

impl TradeTick {
    /// Creates a new [`TradeTick`] from a Python object.
    ///
    /// # Panics
    ///
    /// Panics if converting `aggressor_side_u8` to `AggressorSide` fails.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if attribute extraction or type conversion fails.
    pub fn from_pyobject(obj: &Bound<'_, PyAny>) -> PyResult<Self> {
        let instrument_id_obj: Bound<'_, PyAny> = obj.getattr("instrument_id")?.extract()?;
        let instrument_id_str: String = instrument_id_obj.getattr("value")?.extract()?;
        let instrument_id =
            InstrumentId::from_str(instrument_id_str.as_str()).map_err(to_pyvalue_err)?;

        let price_py: Bound<'_, PyAny> = obj.getattr("price")?.extract()?;
        let price_raw: PriceRaw = price_py.getattr("raw")?.extract()?;
        let price_prec: u8 = price_py.getattr("precision")?.extract()?;
        let price = Price::from_raw(price_raw, price_prec);

        let size_py: Bound<'_, PyAny> = obj.getattr("size")?.extract()?;
        let size_raw: QuantityRaw = size_py.getattr("raw")?.extract()?;
        let size_prec: u8 = size_py.getattr("precision")?.extract()?;
        let size = Quantity::from_raw(size_raw, size_prec);

        let aggressor_side_obj: Bound<'_, PyAny> = obj.getattr("aggressor_side")?.extract()?;
        let aggressor_side_u8 = aggressor_side_obj.getattr("value")?.extract()?;
        let aggressor_side = AggressorSide::from_u8(aggressor_side_u8).unwrap();

        let trade_id_obj: Bound<'_, PyAny> = obj.getattr("trade_id")?.extract()?;
        let trade_id_str: String = trade_id_obj.getattr("value")?.extract()?;
        let trade_id = TradeId::from(trade_id_str.as_str());

        let ts_event: u64 = obj.getattr("ts_event")?.extract()?;
        let ts_init: u64 = obj.getattr("ts_init")?.extract()?;

        Ok(Self::new(
            instrument_id,
            price,
            size,
            aggressor_side,
            trade_id,
            ts_event.into(),
            ts_init.into(),
        ))
    }
}

#[pymethods]
impl TradeTick {
    #[new]
    fn py_new(
        instrument_id: InstrumentId,
        price: Price,
        size: Quantity,
        aggressor_side: AggressorSide,
        trade_id: TradeId,
        ts_event: u64,
        ts_init: u64,
    ) -> PyResult<Self> {
        Self::new_checked(
            instrument_id,
            price,
            size,
            aggressor_side,
            trade_id,
            ts_event.into(),
            ts_init.into(),
        )
        .map_err(to_pyvalue_err)
    }

    fn __setstate__(&mut self, state: &Bound<'_, PyAny>) -> PyResult<()> {
        let py_tuple: &Bound<'_, PyTuple> = state.cast::<PyTuple>()?;
        let binding = py_tuple.get_item(0)?;
        let instrument_id_str = binding.cast::<PyString>()?.extract::<&str>()?;
        let price_raw = py_tuple
            .get_item(1)?
            .cast::<PyInt>()?
            .extract::<PriceRaw>()?;
        let price_prec = py_tuple.get_item(2)?.cast::<PyInt>()?.extract::<u8>()?;
        let size_raw = py_tuple
            .get_item(3)?
            .cast::<PyInt>()?
            .extract::<QuantityRaw>()?;
        let size_prec = py_tuple.get_item(4)?.cast::<PyInt>()?.extract::<u8>()?;

        let aggressor_side_u8 = py_tuple.get_item(5)?.cast::<PyInt>()?.extract::<u8>()?;
        let binding = py_tuple.get_item(6)?;
        let trade_id_str = binding.cast::<PyString>()?.extract::<&str>()?;
        let ts_event = py_tuple.get_item(7)?.cast::<PyInt>()?.extract::<u64>()?;
        let ts_init = py_tuple.get_item(8)?.cast::<PyInt>()?.extract::<u64>()?;

        self.instrument_id = InstrumentId::from_str(instrument_id_str).map_err(to_pyvalue_err)?;
        self.price = Price::from_raw(price_raw, price_prec);
        self.size = Quantity::from_raw(size_raw, size_prec);
        self.aggressor_side = AggressorSide::from_u8(aggressor_side_u8).unwrap();
        self.trade_id = TradeId::from(trade_id_str);
        self.ts_event = ts_event.into();
        self.ts_init = ts_init.into();

        Ok(())
    }

    fn __getstate__(&self, py: Python) -> PyResult<Py<PyAny>> {
        (
            self.instrument_id.to_string(),
            self.price.raw,
            self.price.precision,
            self.size.raw,
            self.size.precision,
            self.aggressor_side as u8,
            self.trade_id.to_string(),
            self.ts_event.as_u64(),
            self.ts_init.as_u64(),
        )
            .into_py_any(py)
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let safe_constructor = py.get_type::<Self>().getattr("_safe_constructor")?;
        let state = self.__getstate__(py)?;
        (safe_constructor, PyTuple::empty(py), state).into_py_any(py)
    }

    #[staticmethod]
    fn _safe_constructor() -> Self {
        Self::new(
            InstrumentId::from("NULL.NULL"),
            Price::zero(0),
            Quantity::from(1), // size cannot be zero
            AggressorSide::NoAggressor,
            TradeId::from("NULL"),
            UnixNanos::default(),
            UnixNanos::default(),
        )
    }

    fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        match op {
            CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
            CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
            _ => py.NotImplemented(),
        }
    }

    fn __hash__(&self) -> isize {
        let mut h = DefaultHasher::new();
        self.hash(&mut h);
        h.finish() as isize
    }

    fn __repr__(&self) -> String {
        format!("{}({})", stringify!(TradeTick), self)
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    fn py_instrument_id(&self) -> InstrumentId {
        self.instrument_id
    }

    #[getter]
    #[pyo3(name = "price")]
    fn py_price(&self) -> Price {
        self.price
    }

    #[getter]
    #[pyo3(name = "size")]
    fn py_size(&self) -> Quantity {
        self.size
    }

    #[getter]
    #[pyo3(name = "aggressor_side")]
    fn py_aggressor_side(&self) -> AggressorSide {
        self.aggressor_side
    }

    #[getter]
    #[pyo3(name = "trade_id")]
    fn py_trade_id(&self) -> TradeId {
        self.trade_id
    }

    #[getter]
    #[pyo3(name = "ts_event")]
    fn py_ts_event(&self) -> u64 {
        self.ts_event.as_u64()
    }

    #[getter]
    #[pyo3(name = "ts_init")]
    fn py_ts_init(&self) -> u64 {
        self.ts_init.as_u64()
    }

    #[staticmethod]
    #[pyo3(name = "fully_qualified_name")]
    fn py_fully_qualified_name() -> String {
        format!("{}:{}", PY_MODULE_MODEL, stringify!(TradeTick))
    }

    #[staticmethod]
    #[pyo3(name = "get_metadata")]
    fn py_get_metadata(
        instrument_id: &InstrumentId,
        price_precision: u8,
        size_precision: u8,
    ) -> PyResult<HashMap<String, String>> {
        Ok(Self::get_metadata(
            instrument_id,
            price_precision,
            size_precision,
        ))
    }

    #[staticmethod]
    #[pyo3(name = "get_fields")]
    fn py_get_fields(py: Python<'_>) -> PyResult<Bound<'_, PyDict>> {
        let py_dict = PyDict::new(py);
        for (k, v) in Self::get_fields() {
            py_dict.set_item(k, v)?;
        }

        Ok(py_dict)
    }

    /// Returns a new object from the given dictionary representation.
    #[staticmethod]
    #[pyo3(name = "from_dict")]
    fn py_from_dict(py: Python<'_>, values: Py<PyDict>) -> PyResult<Self> {
        from_dict_pyo3(py, values)
    }

    #[staticmethod]
    #[pyo3(name = "from_json")]
    fn py_from_json(data: Vec<u8>) -> PyResult<Self> {
        Self::from_json_bytes(&data).map_err(to_pyvalue_err)
    }

    #[staticmethod]
    #[pyo3(name = "from_msgpack")]
    fn py_from_msgpack(data: Vec<u8>) -> PyResult<Self> {
        Self::from_msgpack_bytes(&data).map_err(to_pyvalue_err)
    }

    /// Creates a `PyCapsule` containing a raw pointer to a `Data::Trade` object.
    ///
    /// This function takes the current object (assumed to be of a type that can be represented as
    /// `Data::Trade`), and encapsulates a raw pointer to it within a `PyCapsule`.
    ///
    /// # Safety
    ///
    /// This function is safe as long as the following conditions are met:
    /// - The `Data::Trade` object pointed to by the capsule must remain valid for the lifetime of the capsule.
    /// - The consumer of the capsule must ensure proper handling to avoid dereferencing a dangling pointer.
    ///
    /// # Panics
    ///
    /// The function will panic if the `PyCapsule` creation fails, which can occur if the
    /// `Data::Trade` object cannot be converted into a raw pointer.
    #[pyo3(name = "as_pycapsule")]
    fn py_as_pycapsule(&self, py: Python<'_>) -> Py<PyAny> {
        data_to_pycapsule(py, Data::Trade(*self))
    }

    /// Return a dictionary representation of the object.
    #[pyo3(name = "to_dict")]
    fn py_to_dict(&self, py: Python<'_>) -> PyResult<Py<PyDict>> {
        to_dict_pyo3(py, self)
    }

    /// Return JSON encoded bytes representation of the object.
    #[pyo3(name = "to_json_bytes")]
    fn py_to_json_bytes(&self, py: Python<'_>) -> Py<PyAny> {
        // SAFETY: Unwrap safe when serializing a valid object
        self.to_json_bytes().unwrap().into_py_any_unwrap(py)
    }

    /// Return MsgPack encoded bytes representation of the object.
    #[pyo3(name = "to_msgpack_bytes")]
    fn py_to_msgpack_bytes(&self, py: Python<'_>) -> Py<PyAny> {
        // SAFETY: Unwrap safe when serializing a valid object
        self.to_msgpack_bytes().unwrap().into_py_any_unwrap(py)
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use nautilus_core::python::IntoPyObjectNautilusExt;
    use pyo3::Python;
    use rstest::rstest;

    use crate::{
        data::{TradeTick, stubs::stub_trade_ethusdt_buyer},
        enums::AggressorSide,
        identifiers::{InstrumentId, TradeId},
        types::{Price, Quantity},
    };

    #[rstest]
    fn test_trade_tick_py_new_with_zero_size() {
        let instrument_id = InstrumentId::from("ETH-USDT-SWAP.OKX");
        let price = Price::from("10000.00");
        let zero_size = Quantity::from(0);
        let aggressor_side = AggressorSide::Buyer;
        let trade_id = TradeId::from("123456789");
        let ts_event = 1;
        let ts_init = 2;

        let result = TradeTick::py_new(
            instrument_id,
            price,
            zero_size,
            aggressor_side,
            trade_id,
            ts_event,
            ts_init,
        );

        assert!(result.is_err());
    }

    #[rstest]
    fn test_to_dict(stub_trade_ethusdt_buyer: TradeTick) {
        let trade = stub_trade_ethusdt_buyer;

        Python::initialize();
        Python::attach(|py| {
            let dict_string = trade.py_to_dict(py).unwrap().to_string();
            let expected_string = r"{'type': 'TradeTick', 'instrument_id': 'ETHUSDT-PERP.BINANCE', 'price': '10000.0000', 'size': '1.00000000', 'aggressor_side': 'BUYER', 'trade_id': '123456789', 'ts_event': 0, 'ts_init': 1}";
            assert_eq!(dict_string, expected_string);
        });
    }

    #[rstest]
    fn test_from_dict(stub_trade_ethusdt_buyer: TradeTick) {
        let trade = stub_trade_ethusdt_buyer;

        Python::initialize();
        Python::attach(|py| {
            let dict = trade.py_to_dict(py).unwrap();
            let parsed = TradeTick::py_from_dict(py, dict).unwrap();
            assert_eq!(parsed, trade);
        });
    }

    #[rstest]
    fn test_from_pyobject(stub_trade_ethusdt_buyer: TradeTick) {
        let trade = stub_trade_ethusdt_buyer;

        Python::initialize();
        Python::attach(|py| {
            let tick_pyobject = trade.into_py_any_unwrap(py);
            let parsed_tick = TradeTick::from_pyobject(tick_pyobject.bind(py)).unwrap();
            assert_eq!(parsed_tick, trade);
        });
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 31 function(s).

## Detailed Walkthrough

### Functions
- **`from_pyobject()`**: Function defined in this file
- **`py_new()`**: Function defined in this file
- **`__setstate__()`**: Function defined in this file
- **`__getstate__()`**: Function defined in this file
- **`__reduce__()`**: Function defined in this file
- **`_safe_constructor()`**: Function defined in this file
- **`__richcmp__()`**: Function defined in this file
- **`__hash__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`py_instrument_id()`**: Function defined in this file
- **`py_price()`**: Function defined in this file
- **`py_size()`**: Function defined in this file
- **`py_aggressor_side()`**: Function defined in this file
- **`py_trade_id()`**: Function defined in this file
- **`py_ts_event()`**: Function defined in this file
- **`py_ts_init()`**: Function defined in this file
- **`py_fully_qualified_name()`**: Function defined in this file
- **`py_get_metadata()`**: Function defined in this file
- **`py_get_fields()`**: Function defined in this file

*...and 11 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 32


**Functions**: `__getstate__`, `__hash__`, `__reduce__`, `__repr__`, `__richcmp__`, `__setstate__`, `__str__`, `_safe_constructor`, `from_pyobject`, `py_aggressor_side`, `py_as_pycapsule`, `py_from_dict`, `py_from_json`, `py_from_msgpack`, `py_fully_qualified_name`, `py_get_fields`, `py_get_metadata`, `py_instrument_id`, `py_new`, `py_price`, `py_size`, `py_to_dict`, `py_to_json_bytes`, `py_to_msgpack_bytes`, `py_trade_id`, `py_ts_event`, `py_ts_init`, `test_from_dict`, `test_from_pyobject`, `test_to_dict` *(+1 more)*
**Impls**: `TradeTick`

## Related Files

This file is located in `crates/model/src/python/data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:02.999948Z*
