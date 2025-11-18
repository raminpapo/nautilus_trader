# Documentation: funding.rs

## File Metadata

- **Path**: `crates/model/src/python/data/funding.rs`
- **Size**: 11,453 bytes
- **Lines**: 360
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

//! Python bindings for funding rate data types.

use std::{
    collections::HashMap,
    hash::{Hash, Hasher},
    str::FromStr,
};

use nautilus_core::{
    UnixNanos,
    python::{IntoPyObjectNautilusExt, to_pyvalue_err},
    serialization::{
        Serializable,
        msgpack::{FromMsgPack, ToMsgPack},
    },
};
use pyo3::{
    exceptions::PyKeyError,
    prelude::*,
    pyclass::CompareOp,
    types::{PyString, PyTuple},
};
use rust_decimal::Decimal;

use crate::{data::FundingRateUpdate, identifiers::InstrumentId, python::common::PY_MODULE_MODEL};

#[pymethods]
impl FundingRateUpdate {
    #[new]
    #[pyo3(signature = (instrument_id, rate, ts_event, ts_init, next_funding_ns=None))]
    fn py_new(
        instrument_id: InstrumentId,
        rate: Decimal,
        ts_event: u64,
        ts_init: u64,
        next_funding_ns: Option<u64>,
    ) -> Self {
        let ts_event_nanos = UnixNanos::from(ts_event);
        let ts_init_nanos = UnixNanos::from(ts_init);
        let next_funding_nanos = next_funding_ns.map(UnixNanos::from);

        Self::new(
            instrument_id,
            rate,
            next_funding_nanos,
            ts_event_nanos,
            ts_init_nanos,
        )
    }

    fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        match op {
            CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
            CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
            _ => py.NotImplemented(),
        }
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }

    fn __str__(&self) -> String {
        format!("{self}")
    }

    fn __hash__(&self) -> isize {
        let mut hasher = std::collections::hash_map::DefaultHasher::new();
        Hash::hash(self, &mut hasher);
        Hasher::finish(&hasher) as isize
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    fn py_instrument_id(&self) -> InstrumentId {
        self.instrument_id
    }

    #[getter]
    #[pyo3(name = "rate")]
    fn py_rate(&self) -> Decimal {
        self.rate
    }

    #[getter]
    #[pyo3(name = "next_funding_ns")]
    fn py_next_funding_ns(&self) -> Option<u64> {
        self.next_funding_ns.map(|ts| ts.as_u64())
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
        format!("{}:{}", PY_MODULE_MODEL, stringify!(FundingRateUpdate))
    }

    #[staticmethod]
    #[pyo3(name = "get_metadata")]
    fn py_get_metadata(instrument_id: &InstrumentId) -> HashMap<String, String> {
        Self::get_metadata(instrument_id)
    }

    #[staticmethod]
    #[pyo3(name = "get_fields")]
    fn py_get_fields() -> HashMap<String, String> {
        Self::get_fields().into_iter().collect()
    }

    #[pyo3(name = "to_dict")]
    fn py_to_dict(&self, py: Python<'_>) -> PyResult<Py<PyAny>> {
        let mut dict = HashMap::new();
        dict.insert(
            "type".to_string(),
            "FundingRateUpdate".into_py_any_unwrap(py),
        );
        dict.insert(
            "instrument_id".to_string(),
            self.instrument_id.to_string().into_py_any_unwrap(py),
        );
        dict.insert(
            "rate".to_string(),
            self.rate.to_string().into_py_any_unwrap(py),
        );
        if let Some(next_funding_ns) = self.next_funding_ns {
            dict.insert(
                "next_funding_ns".to_string(),
                next_funding_ns.as_u64().into_py_any_unwrap(py),
            );
        }
        dict.insert(
            "ts_event".to_string(),
            self.ts_event.as_u64().into_py_any_unwrap(py),
        );
        dict.insert(
            "ts_init".to_string(),
            self.ts_init.as_u64().into_py_any_unwrap(py),
        );
        Ok(dict.into_py_any_unwrap(py))
    }

    #[staticmethod]
    #[pyo3(name = "from_dict")]
    fn py_from_dict(py: Python<'_>, values: Py<PyAny>) -> PyResult<Self> {
        let dict = values.cast_bound::<pyo3::types::PyDict>(py)?;

        let instrument_id_str: String = dict
            .get_item("instrument_id")?
            .ok_or_else(|| PyErr::new::<PyKeyError, _>("Missing 'instrument_id' field"))?
            .extract()?;
        let instrument_id = InstrumentId::from_str(&instrument_id_str).map_err(to_pyvalue_err)?;

        let rate_str: String = dict
            .get_item("rate")?
            .ok_or_else(|| PyErr::new::<PyKeyError, _>("Missing 'rate' field"))?
            .extract()?;
        let rate = Decimal::from_str(&rate_str).map_err(to_pyvalue_err)?;

        let ts_event: u64 = dict
            .get_item("ts_event")?
            .ok_or_else(|| PyErr::new::<PyKeyError, _>("Missing 'ts_event' field"))?
            .extract()?;

        let ts_init: u64 = dict
            .get_item("ts_init")?
            .ok_or_else(|| PyErr::new::<PyKeyError, _>("Missing 'ts_init' field"))?
            .extract()?;

        let next_funding_ns: Option<u64> = dict
            .get_item("next_funding_ns")
            .ok()
            .flatten()
            .and_then(|v| v.extract().ok());

        Ok(Self::new(
            instrument_id,
            rate,
            next_funding_ns.map(UnixNanos::from),
            UnixNanos::from(ts_event),
            UnixNanos::from(ts_init),
        ))
    }

    #[pyo3(name = "from_json")]
    #[staticmethod]
    fn py_from_json(data: Vec<u8>) -> PyResult<Self> {
        Self::from_json_bytes(&data).map_err(to_pyvalue_err)
    }

    #[pyo3(name = "from_msgpack")]
    #[staticmethod]
    fn py_from_msgpack(data: Vec<u8>) -> PyResult<Self> {
        Self::from_msgpack_bytes(&data).map_err(to_pyvalue_err)
    }

    #[pyo3(name = "to_json")]
    fn py_to_json(&self) -> PyResult<Vec<u8>> {
        self.to_json_bytes()
            .map(|b| b.to_vec())
            .map_err(to_pyvalue_err)
    }

    #[pyo3(name = "to_msgpack")]
    fn py_to_msgpack(&self) -> PyResult<Vec<u8>> {
        self.to_msgpack_bytes()
            .map(|b| b.to_vec())
            .map_err(to_pyvalue_err)
    }

    fn __setstate__(&mut self, state: &Bound<'_, PyAny>) -> PyResult<()> {
        let py_tuple: &Bound<'_, PyTuple> = state.cast::<PyTuple>()?;

        let item0 = py_tuple.get_item(0)?;
        let instrument_id_str: String = item0.cast::<PyString>()?.extract()?;

        let item1 = py_tuple.get_item(1)?;
        let rate_str: String = item1.cast::<PyString>()?.extract()?;

        let next_funding_ns: Option<u64> = py_tuple.get_item(2).ok().and_then(|item| {
            if item.is_none() {
                None
            } else {
                item.extract().ok()
            }
        });
        let ts_event: u64 = py_tuple.get_item(3)?.extract()?;
        let ts_init: u64 = py_tuple.get_item(4)?.extract()?;

        self.instrument_id = InstrumentId::from_str(&instrument_id_str).map_err(to_pyvalue_err)?;
        self.rate = Decimal::from_str(&rate_str).map_err(to_pyvalue_err)?;
        self.next_funding_ns = next_funding_ns.map(UnixNanos::from);
        self.ts_event = UnixNanos::from(ts_event);
        self.ts_init = UnixNanos::from(ts_init);

        Ok(())
    }

    fn __getstate__(&self, py: Python) -> PyResult<Py<PyAny>> {
        Ok((
            self.instrument_id.to_string(),
            self.rate.to_string(),
            self.next_funding_ns.map(|ts| ts.as_u64()),
            self.ts_event.as_u64(),
            self.ts_init.as_u64(),
        )
            .into_py_any_unwrap(py))
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let safe_constructor = py.get_type::<Self>().getattr("_safe_constructor")?;
        let state = self.__getstate__(py)?;
        Ok((safe_constructor, PyTuple::empty(py), state).into_py_any_unwrap(py))
    }

    #[staticmethod]
    #[pyo3(name = "_safe_constructor")]
    fn py_safe_constructor() -> Self {
        Self::new(
            InstrumentId::from("NULL.NULL"),
            Decimal::ZERO,
            None,
            UnixNanos::default(),
            UnixNanos::default(),
        )
    }
}

impl FundingRateUpdate {
    /// Creates a new [`FundingRateUpdate`] from a Python object.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if extracting any attribute or converting types fails.
    pub fn from_pyobject(obj: &Bound<'_, PyAny>) -> PyResult<Self> {
        let instrument_id_obj: Bound<'_, PyAny> = obj.getattr("instrument_id")?.extract()?;
        let instrument_id_str: String = instrument_id_obj.getattr("value")?.extract()?;
        let instrument_id =
            InstrumentId::from_str(instrument_id_str.as_str()).map_err(to_pyvalue_err)?;

        let rate: Decimal = obj.getattr("rate")?.extract()?;
        let ts_event: u64 = obj.getattr("ts_event")?.extract()?;
        let ts_init: u64 = obj.getattr("ts_init")?.extract()?;

        let next_funding_ns: Option<u64> = obj
            .getattr("next_funding_ns")
            .ok()
            .and_then(|x| x.extract().ok());

        Ok(Self::new(
            instrument_id,
            rate,
            next_funding_ns.map(UnixNanos::from),
            UnixNanos::from(ts_event),
            UnixNanos::from(ts_init),
        ))
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_py_funding_rate_update_new() {
        Python::initialize();
        Python::attach(|_py| {
            let instrument_id = InstrumentId::from("BTCUSDT-PERP.BINANCE");
            let rate = Decimal::new(1, 4); // 0.0001
            let ts_event = UnixNanos::from(1_640_000_000_000_000_000_u64);
            let ts_init = UnixNanos::from(1_640_000_000_000_000_000_u64);

            let funding_rate = FundingRateUpdate::py_new(
                instrument_id,
                rate,
                ts_event.as_u64(),
                ts_init.as_u64(),
                None,
            );

            assert_eq!(funding_rate.instrument_id, instrument_id);
            assert_eq!(funding_rate.rate, rate);
            assert_eq!(funding_rate.next_funding_ns, None);
            assert_eq!(funding_rate.ts_event, ts_event);
            assert_eq!(funding_rate.ts_init, ts_init);
        });
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 25 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__richcmp__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`__hash__()`**: Function defined in this file
- **`py_instrument_id()`**: Function defined in this file
- **`py_rate()`**: Function defined in this file
- **`py_next_funding_ns()`**: Function defined in this file
- **`py_ts_event()`**: Function defined in this file
- **`py_ts_init()`**: Function defined in this file
- **`py_fully_qualified_name()`**: Function defined in this file
- **`py_get_metadata()`**: Function defined in this file
- **`py_get_fields()`**: Function defined in this file
- **`py_to_dict()`**: Function defined in this file
- **`py_from_dict()`**: Function defined in this file
- **`py_from_json()`**: Function defined in this file
- **`py_from_msgpack()`**: Function defined in this file
- **`py_to_json()`**: Function defined in this file
- **`py_to_msgpack()`**: Function defined in this file
- **`__setstate__()`**: Function defined in this file

*...and 5 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 26


**Functions**: `__getstate__`, `__hash__`, `__reduce__`, `__repr__`, `__richcmp__`, `__setstate__`, `__str__`, `from_pyobject`, `py_from_dict`, `py_from_json`, `py_from_msgpack`, `py_fully_qualified_name`, `py_get_fields`, `py_get_metadata`, `py_instrument_id`, `py_new`, `py_next_funding_ns`, `py_rate`, `py_safe_constructor`, `py_to_dict`, `py_to_json`, `py_to_msgpack`, `py_ts_event`, `py_ts_init`, `test_py_funding_rate_update_new`
**Impls**: `FundingRateUpdate`

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
*Generated on 2025-11-18T21:55:02.977371Z*
