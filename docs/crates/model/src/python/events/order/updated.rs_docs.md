# Documentation: `crates/model/src/python/events/order/updated.rs`
**Generated:** 2025-11-15T19:40:03.042238Z
**File Size:** 6223 bytes
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

- **Path:** `crates/model/src/python/events/order/updated.rs`
- **Size:** 6,223 bytes
- **Lines:** 198
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 19

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

use nautilus_core::{
    UUID4,
    python::{IntoPyObjectNautilusExt, serialization::from_dict_pyo3},
};
use pyo3::{basic::CompareOp, prelude::*, types::PyDict};

use crate::{
    events::OrderUpdated,
    identifiers::{AccountId, ClientOrderId, InstrumentId, StrategyId, TraderId, VenueOrderId},
    types::{Price, Quantity},
};

#[pymethods]
impl OrderUpdated {
    #[allow(clippy::too_many_arguments)]
    #[new]
    #[pyo3(signature = (trader_id, strategy_id, instrument_id, client_order_id, quantity, event_id, ts_event, ts_init, reconciliation, venue_order_id=None, account_id=None, price=None, trigger_price=None, protection_price=None))]
    fn py_new(
        trader_id: TraderId,
        strategy_id: StrategyId,
        instrument_id: InstrumentId,
        client_order_id: ClientOrderId,
        quantity: Quantity,
        event_id: UUID4,
        ts_event: u64,
        ts_init: u64,
        reconciliation: bool,
        venue_order_id: Option<VenueOrderId>,
        account_id: Option<AccountId>,
        price: Option<Price>,
        trigger_price: Option<Price>,
        protection_price: Option<Price>,
    ) -> Self {
        Self::new(
            trader_id,
            strategy_id,
            instrument_id,
            client_order_id,
            quantity,
            event_id,
            ts_event.into(),
            ts_init.into(),
            reconciliation,
            venue_order_id,
            account_id,
            price,
            trigger_price,
            protection_price,
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
    #[pyo3(name = "venue_order_id")]
    fn py_venue_order_id(&self) -> Option<VenueOrderId> {
        self.venue_order_id
    }

    #[getter]
    #[pyo3(name = "account_id")]
    fn py_account_id(&self) -> Option<AccountId> {
        self.account_id
    }

    #[getter]
    #[pyo3(name = "quantity")]
    fn py_quantity(&self) -> Quantity {
        self.quantity
    }

    #[getter]
    #[pyo3(name = "price")]
    fn py_price(&self) -> Option<Price> {
        self.price
    }

    #[getter]
    #[pyo3(name = "trigger_price")]
    fn py_trigger_price(&self) -> Option<Price> {
        self.trigger_price
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

    #[getter]
    #[pyo3(name = "reconciliation")]
    fn py_reconciliation(&self) -> bool {
        self.reconciliation != 0
    }

    #[pyo3(name = "to_dict")]
    fn py_to_dict(&self, py: Python<'_>) -> PyResult<Py<PyAny>> {
        let dict = PyDict::new(py);
        dict.set_item("type", stringify!(OrderUpdated))?;
        dict.set_item("trader_id", self.trader_id.to_string())?;
        dict.set_item("strategy_id", self.strategy_id.to_string())?;
        dict.set_item("instrument_id", self.instrument_id.to_string())?;
        dict.set_item("client_order_id", self.client_order_id.to_string())?;
        dict.set_item("quantity", self.quantity.to_string())?;
        dict.set_item("event_id", self.event_id.to_string())?;
        dict.set_item("ts_event", self.ts_event.as_u64())?;
        dict.set_item("ts_init", self.ts_init.as_u64())?;
        dict.set_item("reconciliation", self.reconciliation)?;
        match self.venue_order_id {
            Some(venue_order_id) => dict.set_item("venue_order_id", venue_order_id.to_string())?,
            None => dict.set_item("venue_order_id", py.None())?,
        }
        match self.account_id {
            Some(account_id) => dict.set_item("account_id", account_id.to_string())?,
            None => dict.set_item("account_id", py.None())?,
        }
        match self.price {
            Some(price) => dict.set_item("price", price.to_string())?,
            None => dict.set_item("price", py.None())?,
        }
        match self.trigger_price {
            Some(trigger_price) => dict.set_item("trigger_price", trigger_price.to_string())?,
            None => dict.set_item("trigger_price", py.None())?,
        }
        Ok(dict.into())
    }
}
```


---

## Overview

This file is located at `crates/model/src/python/events/order/updated.rs` within the repository.

**Classes defined:** OrderUpdated

**Functions defined:** py_new, __richcmp__, __repr__, __str__, py_from_dict, py_trader_id, py_strategy_id, py_instrument_id, py_client_order_id, py_venue_order_id and 9 more


---

## Detailed Analysis

### Classes

#### `OrderUpdated`

**Type:** impl


### Functions

#### `py_new(
        trader_id: TraderId,
        strategy_id: StrategyId,
        instrument_id: InstrumentId,
        client_order_id: ClientOrderId,
        quantity: Quantity,
        event_id: UUID4,
        ts_event: u64,
        ts_init: u64,
        reconciliation: bool,
        venue_order_id: Option<VenueOrderId>,
        account_id: Option<AccountId>,
        price: Option<Price>,
        trigger_price: Option<Price>,
        protection_price: Option<Price>,
    )`


#### `__richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_from_dict(py: Python<'_>, values: Py<PyDict>)`


#### `py_trader_id(&self)`


#### `py_strategy_id(&self)`


#### `py_instrument_id(&self)`


#### `py_client_order_id(&self)`


#### `py_venue_order_id(&self)`


#### `py_account_id(&self)`


#### `py_quantity(&self)`


#### `py_price(&self)`


#### `py_trigger_price(&self)`


#### `py_event_id(&self)`


#### `py_ts_event(&self)`


#### `py_ts_init(&self)`


#### `py_reconciliation(&self)`


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


