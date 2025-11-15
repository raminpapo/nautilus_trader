# Documentation: `crates/model/src/python/events/order/denied.rs`
**Generated:** 2025-11-15T19:40:03.014839Z
**File Size:** 4208 bytes
**Extension:** .rs
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `crates/model/src/python/events/order/denied.rs`
- **Size:** 4,208 bytes
- **Lines:** 141
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 14

---

## Source Code

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

use std::str::FromStr;

use nautilus_core::{
    UUID4,
    python::{IntoPyObjectNautilusExt, serialization::from_dict_pyo3, to_pyvalue_err},
};
use pyo3::{basic::CompareOp, prelude::*, types::PyDict};
use ustr::Ustr;

use crate::{
    events::OrderDenied,
    identifiers::{ClientOrderId, InstrumentId, StrategyId, TraderId},
};

#[pymethods]
impl OrderDenied {
    #[allow(clippy::too_many_arguments)]
    #[new]
    fn py_new(
        trader_id: TraderId,
        strategy_id: StrategyId,
        instrument_id: InstrumentId,
        client_order_id: ClientOrderId,
        reason: &str,
        event_id: UUID4,
        ts_event: u64,
        ts_init: u64,
    ) -> PyResult<Self> {
        let reason = Ustr::from_str(reason).map_err(to_pyvalue_err)?;
        Ok(Self::new(
            trader_id,
            strategy_id,
            instrument_id,
            client_order_id,
            reason,
            event_id,
            ts_event.into(),
            ts_init.into(),
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
        format!("{self:?}")
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[staticmethod]
    #[pyo3(name = "from_dict")]
    fn py_from_dict(py: Python<'_>, values: Py<PyDict>) -> PyResult<Self> {
        from_dict_pyo3(py, values)
    }

    #[getter]
    #[pyo3(name = "trader_id")]
    fn py_trader_id(&self) -> TraderId {
        self.trader_id
    }

    #[getter]
    #[pyo3(name = "strategy_id")]
    fn py_strategy_id(&self) -> StrategyId {
        self.strategy_id
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    fn py_instrument_id(&self) -> InstrumentId {
        self.instrument_id
    }

    #[getter]
    #[pyo3(name = "client_order_id")]
    fn py_client_order_id(&self) -> ClientOrderId {
        self.client_order_id
    }

    #[getter]
    #[pyo3(name = "reason")]
    fn py_reason(&self) -> String {
        self.reason.to_string()
    }

    #[getter]
    #[pyo3(name = "event_id")]
    fn py_event_id(&self) -> UUID4 {
        self.event_id
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

    #[pyo3(name = "to_dict")]
    fn py_to_dict(&self, py: Python<'_>) -> PyResult<Py<PyAny>> {
        let dict = PyDict::new(py);
        dict.set_item("type", stringify!(OrderDenied))?;
        dict.set_item("trader_id", self.trader_id.to_string())?;
        dict.set_item("strategy_id", self.strategy_id.to_string())?;
        dict.set_item("instrument_id", self.instrument_id.to_string())?;
        dict.set_item("client_order_id", self.client_order_id.to_string())?;
        dict.set_item("reason", self.reason.to_string())?;
        dict.set_item("event_id", self.event_id.to_string())?;
        dict.set_item("ts_event", self.ts_event.as_u64())?;
        dict.set_item("ts_init", self.ts_init.as_u64())?;
        Ok(dict.into())
    }
}
```


---

## Overview

This file is located at `crates/model/src/python/events/order/denied.rs` within the repository.

**Classes defined:** OrderDenied

**Functions defined:** py_new, __richcmp__, __repr__, __str__, py_from_dict, py_trader_id, py_strategy_id, py_instrument_id, py_client_order_id, py_reason and 4 more


---

## Detailed Analysis

### Classes

#### `OrderDenied`

**Type:** impl


### Functions

#### `py_new(
        trader_id: TraderId,
        strategy_id: StrategyId,
        instrument_id: InstrumentId,
        client_order_id: ClientOrderId,
        reason: &str,
        event_id: UUID4,
        ts_event: u64,
        ts_init: u64,
    )`


#### `__richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_from_dict(py: Python<'_>, values: Py<PyDict>)`


#### `py_trader_id(&self)`


#### `py_strategy_id(&self)`


#### `py_instrument_id(&self)`


#### `py_client_order_id(&self)`


#### `py_reason(&self)`


#### `py_event_id(&self)`


#### `py_ts_event(&self)`


#### `py_ts_init(&self)`


#### `py_to_dict(&self, py: Python<'_>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/events/order`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


