# Documentation: fill.rs

## File Metadata

- **Path**: `crates/model/src/python/reports/fill.rs`
- **Size**: 6,731 bytes
- **Lines**: 228
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

use nautilus_core::{
    UUID4,
    python::{IntoPyObjectNautilusExt, serialization::from_dict_pyo3},
};
use pyo3::{basic::CompareOp, prelude::*, types::PyDict};

use crate::{
    enums::{LiquiditySide, OrderSide},
    identifiers::{AccountId, ClientOrderId, InstrumentId, PositionId, TradeId, VenueOrderId},
    reports::fill::FillReport,
    types::{Money, Price, Quantity},
};

#[pymethods]
impl FillReport {
    #[new]
    #[allow(clippy::too_many_arguments)]
    #[pyo3(signature = (
        account_id,
        instrument_id,
        venue_order_id,
        trade_id,
        order_side,
        last_qty,
        last_px,
        commission,
        liquidity_side,
        ts_event,
        ts_init,
        client_order_id=None,
        venue_position_id=None,
        report_id=None,
    ))]
    fn py_new(
        account_id: AccountId,
        instrument_id: InstrumentId,
        venue_order_id: VenueOrderId,
        trade_id: TradeId,
        order_side: OrderSide,
        last_qty: Quantity,
        last_px: Price,
        commission: Money,
        liquidity_side: LiquiditySide,
        ts_event: u64,
        ts_init: u64,
        client_order_id: Option<ClientOrderId>,
        venue_position_id: Option<PositionId>,
        report_id: Option<UUID4>,
    ) -> PyResult<Self> {
        Ok(Self::new(
            account_id,
            instrument_id,
            venue_order_id,
            trade_id,
            order_side,
            last_qty,
            last_px,
            commission,
            liquidity_side,
            client_order_id,
            venue_position_id,
            ts_event.into(),
            ts_init.into(),
            report_id,
        ))
    }

    fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        match op {
            CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
            CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
            _ => py.NotImplemented(),
        }
    }

    fn __repr__(&self) -> String {
        self.to_string()
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "account_id")]
    const fn py_account_id(&self) -> AccountId {
        self.account_id
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    const fn py_instrument_id(&self) -> InstrumentId {
        self.instrument_id
    }

    #[getter]
    #[pyo3(name = "venue_order_id")]
    const fn py_venue_order_id(&self) -> VenueOrderId {
        self.venue_order_id
    }

    #[getter]
    #[pyo3(name = "trade_id")]
    const fn py_trade_id(&self) -> TradeId {
        self.trade_id
    }

    #[getter]
    #[pyo3(name = "order_side")]
    const fn py_order_side(&self) -> OrderSide {
        self.order_side
    }

    #[getter]
    #[pyo3(name = "last_qty")]
    const fn py_last_qty(&self) -> Quantity {
        self.last_qty
    }

    #[getter]
    #[pyo3(name = "last_px")]
    const fn py_last_px(&self) -> Price {
        self.last_px
    }

    #[getter]
    #[pyo3(name = "commission")]
    const fn py_commission(&self) -> Money {
        self.commission
    }

    #[getter]
    #[pyo3(name = "liquidity_side")]
    const fn py_liquidity_side(&self) -> LiquiditySide {
        self.liquidity_side
    }

    #[getter]
    #[pyo3(name = "report_id")]
    const fn py_report_id(&self) -> UUID4 {
        self.report_id
    }

    #[getter]
    #[pyo3(name = "ts_event")]
    const fn py_ts_event(&self) -> u64 {
        self.ts_event.as_u64()
    }

    #[getter]
    #[pyo3(name = "ts_init")]
    const fn py_ts_init(&self) -> u64 {
        self.ts_init.as_u64()
    }

    #[getter]
    #[pyo3(name = "client_order_id")]
    const fn py_client_order_id(&self) -> Option<ClientOrderId> {
        self.client_order_id
    }

    #[getter]
    #[pyo3(name = "venue_position_id")]
    const fn py_venue_position_id(&self) -> Option<PositionId> {
        self.venue_position_id
    }

    /// Creates a `FillReport` from a Python dictionary.
    ///
    /// # Errors
    ///
    /// Returns a Python exception if conversion from dict fails.
    #[staticmethod]
    #[pyo3(name = "from_dict")]
    pub fn py_from_dict(py: Python<'_>, values: Py<PyDict>) -> PyResult<Self> {
        from_dict_pyo3(py, values)
    }

    /// Converts the `FillReport` to a Python dictionary.
    ///
    /// # Errors
    ///
    /// Returns a Python exception if conversion to dict fails.
    #[pyo3(name = "to_dict")]
    pub fn py_to_dict(&self, py: Python<'_>) -> PyResult<Py<PyAny>> {
        let dict = PyDict::new(py);
        dict.set_item("type", stringify!(FillReport))?;
        dict.set_item("account_id", self.account_id.to_string())?;
        dict.set_item("instrument_id", self.instrument_id.to_string())?;
        dict.set_item("venue_order_id", self.venue_order_id.to_string())?;
        dict.set_item("trade_id", self.trade_id.to_string())?;
        dict.set_item("order_side", self.order_side.to_string())?;
        dict.set_item("last_qty", self.last_qty.to_string())?;
        dict.set_item("last_px", self.last_px.to_string())?;
        dict.set_item("commission", self.commission.to_string())?;
        dict.set_item("liquidity_side", self.liquidity_side.to_string())?;
        dict.set_item("report_id", self.report_id.to_string())?;
        dict.set_item("ts_event", self.ts_event.as_u64())?;
        dict.set_item("ts_init", self.ts_init.as_u64())?;

        match &self.client_order_id {
            Some(id) => dict.set_item("client_order_id", id.to_string())?,
            None => dict.set_item("client_order_id", py.None())?,
        }
        match &self.venue_position_id {
            Some(id) => dict.set_item("venue_position_id", id.to_string())?,
            None => dict.set_item("venue_position_id", py.None())?,
        }

        Ok(dict.into())
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 20 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__richcmp__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`py_account_id()`**: Function defined in this file
- **`py_instrument_id()`**: Function defined in this file
- **`py_venue_order_id()`**: Function defined in this file
- **`py_trade_id()`**: Function defined in this file
- **`py_order_side()`**: Function defined in this file
- **`py_last_qty()`**: Function defined in this file
- **`py_last_px()`**: Function defined in this file
- **`py_commission()`**: Function defined in this file
- **`py_liquidity_side()`**: Function defined in this file
- **`py_report_id()`**: Function defined in this file
- **`py_ts_event()`**: Function defined in this file
- **`py_ts_init()`**: Function defined in this file
- **`py_client_order_id()`**: Function defined in this file
- **`py_venue_position_id()`**: Function defined in this file
- **`py_from_dict()`**: Function defined in this file
- **`py_to_dict()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 21


**Functions**: `__repr__`, `__richcmp__`, `__str__`, `py_account_id`, `py_client_order_id`, `py_commission`, `py_from_dict`, `py_instrument_id`, `py_last_px`, `py_last_qty`, `py_liquidity_side`, `py_new`, `py_order_side`, `py_report_id`, `py_to_dict`, `py_trade_id`, `py_ts_event`, `py_ts_init`, `py_venue_order_id`, `py_venue_position_id`
**Impls**: `FillReport`

## Related Files

This file is located in `crates/model/src/python/reports/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.196623Z*
