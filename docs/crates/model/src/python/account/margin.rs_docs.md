# Documentation: margin.rs

## File Metadata

- **Path**: `crates/model/src/python/account/margin.rs`
- **Size**: 9,990 bytes
- **Lines**: 252
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

use nautilus_core::python::{IntoPyObjectNautilusExt, to_pyvalue_err};
use pyo3::{IntoPyObjectExt, basic::CompareOp, prelude::*, types::PyDict};
use rust_decimal::Decimal;

use crate::{
    accounts::MarginAccount,
    events::AccountState,
    identifiers::{AccountId, InstrumentId},
    instruments::InstrumentAny,
    python::instruments::pyobject_to_instrument_any,
    types::{Money, Price, Quantity},
};

#[pymethods]
impl MarginAccount {
    #[new]
    fn py_new(event: AccountState, calculate_account_state: bool) -> Self {
        Self::new(event, calculate_account_state)
    }

    fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        match op {
            CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
            CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
            _ => py.NotImplemented(),
        }
    }

    #[getter]
    fn id(&self) -> AccountId {
        self.id
    }

    #[getter]
    fn default_leverage(&self) -> Decimal {
        self.default_leverage
    }

    #[getter]
    #[pyo3(name = "calculate_account_state")]
    fn py_calculate_account_state(&self) -> bool {
        self.calculate_account_state
    }

    fn __repr__(&self) -> String {
        format!(
            "{}(id={}, type={}, base={})",
            stringify!(MarginAccount),
            self.id,
            self.account_type,
            self.base_currency.map_or_else(
                || "None".to_string(),
                |base_currency| format!("{}", base_currency.code)
            ),
        )
    }

    #[pyo3(name = "set_default_leverage")]
    fn py_set_default_leverage(&mut self, default_leverage: Decimal) {
        self.set_default_leverage(default_leverage);
    }

    #[pyo3(name = "leverages")]
    fn py_leverages(&self, py: Python) -> PyResult<Py<PyAny>> {
        let leverages = PyDict::new(py);
        for (key, &value) in &self.leverages {
            leverages
                .set_item(key.into_py_any_unwrap(py), value)
                .unwrap();
        }
        leverages.into_py_any(py)
    }

    #[pyo3(name = "leverage")]
    fn py_leverage(&self, instrument_id: &InstrumentId) -> Decimal {
        self.get_leverage(instrument_id)
    }

    #[pyo3(name = "set_leverage")]
    fn py_set_leverage(&mut self, instrument_id: InstrumentId, leverage: Decimal) {
        self.set_leverage(instrument_id, leverage);
    }

    #[pyo3(name = "is_unleveraged")]
    fn py_is_unleveraged(&self, instrument_id: InstrumentId) -> PyResult<bool> {
        Ok(self.is_unleveraged(instrument_id))
    }

    #[pyo3(name = "initial_margins")]
    fn py_initial_margins(&self, py: Python) -> PyResult<Py<PyAny>> {
        let initial_margins = PyDict::new(py);
        for (key, &value) in &self.initial_margins() {
            initial_margins
                .set_item(key.into_py_any_unwrap(py), value.into_py_any_unwrap(py))
                .unwrap();
        }
        initial_margins.into_py_any(py)
    }

    #[pyo3(name = "maintenance_margins")]
    fn py_maintenance_margins(&self, py: Python) -> PyResult<Py<PyAny>> {
        let maintenance_margins = PyDict::new(py);
        for (key, &value) in &self.maintenance_margins() {
            maintenance_margins
                .set_item(key.into_py_any_unwrap(py), value.into_py_any_unwrap(py))
                .unwrap();
        }
        maintenance_margins.into_py_any(py)
    }

    #[pyo3(name = "update_initial_margin")]
    fn py_update_initial_margin(
        &mut self,
        instrument_id: InstrumentId,
        initial_margin: Money,
    ) -> PyResult<()> {
        self.update_initial_margin(instrument_id, initial_margin);
        Ok(())
    }

    #[pyo3(name = "initial_margin")]
    fn py_initial_margin(&self, instrument_id: InstrumentId) -> PyResult<Money> {
        Ok(self.initial_margin(instrument_id))
    }

    #[pyo3(name = "update_maintenance_margin")]
    fn py_update_maintenance_margin(
        &mut self,
        instrument_id: InstrumentId,
        maintenance_margin: Money,
    ) -> PyResult<()> {
        self.update_maintenance_margin(instrument_id, maintenance_margin);
        Ok(())
    }

    #[pyo3(name = "maintenance_margin")]
    fn py_maintenance_margin(&self, instrument_id: InstrumentId) -> PyResult<Money> {
        Ok(self.maintenance_margin(instrument_id))
    }

    #[pyo3(name = "calculate_initial_margin")]
    #[pyo3(signature = (instrument, quantity, price, use_quote_for_inverse=None))]
    /// Calculates the initial margin for a given instrument and quantity at the specified price.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if the Python `instrument` object cannot be converted to a supported internal instrument,
    /// or if the instrument type is unsupported.
    pub fn py_calculate_initial_margin(
        &mut self,
        instrument: Py<PyAny>,
        quantity: Quantity,
        price: Price,
        use_quote_for_inverse: Option<bool>,
        py: Python,
    ) -> PyResult<Money> {
        let instrument_type = pyobject_to_instrument_any(py, instrument)?;
        match instrument_type {
            InstrumentAny::CryptoPerpetual(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::CryptoFuture(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::CryptoOption(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::CurrencyPair(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::Equity(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::FuturesContract(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::OptionContract(inst) => self
                .calculate_initial_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            _ => Err(to_pyvalue_err("Unsupported instrument type")),
        }
    }

    /// Calculates the maintenance margin for a given instrument and quantity at the specified price.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if the Python `instrument` object cannot be converted to a supported internal instrument,
    /// or if the instrument type is unsupported.
    #[pyo3(name = "calculate_maintenance_margin")]
    #[pyo3(signature = (instrument, quantity, price, use_quote_for_inverse=None))]
    pub fn py_calculate_maintenance_margin(
        &mut self,
        instrument: Py<PyAny>,
        quantity: Quantity,
        price: Price,
        use_quote_for_inverse: Option<bool>,
        py: Python,
    ) -> PyResult<Money> {
        let instrument_type = pyobject_to_instrument_any(py, instrument)?;
        match instrument_type {
            InstrumentAny::CryptoFuture(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::CryptoPerpetual(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::CryptoOption(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::CurrencyPair(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::Equity(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::FuturesContract(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            InstrumentAny::OptionContract(inst) => self
                .calculate_maintenance_margin(inst, quantity, price, use_quote_for_inverse)
                .map_err(to_pyvalue_err),
            _ => Err(to_pyvalue_err("Unsupported instrument type")),
        }
    }

    #[pyo3(name = "to_dict")]
    fn py_to_dict(&self, py: Python<'_>) -> PyResult<Py<PyAny>> {
        let dict = PyDict::new(py);
        dict.set_item("calculate_account_state", self.calculate_account_state)?;
        let events_list: PyResult<Vec<Py<PyAny>>> =
            self.events.iter().map(|item| item.py_to_dict(py)).collect();
        dict.set_item("events", events_list.unwrap())?;
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
- **`id()`**: Function defined in this file
- **`default_leverage()`**: Function defined in this file
- **`py_calculate_account_state()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_set_default_leverage()`**: Function defined in this file
- **`py_leverages()`**: Function defined in this file
- **`py_leverage()`**: Function defined in this file
- **`py_set_leverage()`**: Function defined in this file
- **`py_is_unleveraged()`**: Function defined in this file
- **`py_initial_margins()`**: Function defined in this file
- **`py_maintenance_margins()`**: Function defined in this file
- **`py_update_initial_margin()`**: Function defined in this file
- **`py_initial_margin()`**: Function defined in this file
- **`py_update_maintenance_margin()`**: Function defined in this file
- **`py_maintenance_margin()`**: Function defined in this file
- **`py_calculate_initial_margin()`**: Function defined in this file
- **`py_calculate_maintenance_margin()`**: Function defined in this file
- **`py_to_dict()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 21


**Functions**: `__repr__`, `__richcmp__`, `default_leverage`, `id`, `py_calculate_account_state`, `py_calculate_initial_margin`, `py_calculate_maintenance_margin`, `py_initial_margin`, `py_initial_margins`, `py_is_unleveraged`, `py_leverage`, `py_leverages`, `py_maintenance_margin`, `py_maintenance_margins`, `py_new`, `py_set_default_leverage`, `py_set_leverage`, `py_to_dict`, `py_update_initial_margin`, `py_update_maintenance_margin`
**Impls**: `MarginAccount`

## Related Files

This file is located in `crates/model/src/python/account/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.941923Z*
