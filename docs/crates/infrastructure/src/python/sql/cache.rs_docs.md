# Documentation: `crates/infrastructure/src/python/sql/cache.rs`
**Generated:** 2025-11-15T19:40:02.312482Z
**File Size:** 11522 bytes
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

- **Path:** `crates/infrastructure/src/python/sql/cache.rs`
- **Size:** 11,522 bytes
- **Lines:** 326
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 31

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

use std::collections::HashMap;

use bytes::Bytes;
use nautilus_common::{
    cache::database::CacheDatabaseAdapter, custom::CustomData, runtime::get_runtime, signal::Signal,
};
use nautilus_core::python::to_pyruntime_err;
use nautilus_model::{
    data::{Bar, DataType, QuoteTick, TradeTick},
    events::{OrderSnapshot, PositionSnapshot},
    identifiers::{AccountId, ClientId, ClientOrderId, InstrumentId, PositionId},
    python::{
        account::{account_any_to_pyobject, pyobject_to_account_any},
        events::order::pyobject_to_order_event,
        instruments::{instrument_any_to_pyobject, pyobject_to_instrument_any},
        orders::{order_any_to_pyobject, pyobject_to_order_any},
    },
    types::Currency,
};
use pyo3::{IntoPyObjectExt, prelude::*};

use crate::sql::{cache::PostgresCacheDatabase, queries::DatabaseQueries};

#[pymethods]
impl PostgresCacheDatabase {
    #[staticmethod]
    #[pyo3(name = "connect")]
    #[pyo3(signature = (host=None, port=None, username=None, password=None, database=None))]
    fn py_connect(
        host: Option<String>,
        port: Option<u16>,
        username: Option<String>,
        password: Option<String>,
        database: Option<String>,
    ) -> PyResult<Self> {
        let result = get_runtime()
            .block_on(async { Self::connect(host, port, username, password, database).await });
        result.map_err(to_pyruntime_err)
    }

    #[pyo3(name = "close")]
    fn py_close(&mut self) -> PyResult<()> {
        self.close().map_err(to_pyruntime_err)
    }

    #[pyo3(name = "flush_db")]
    fn py_flush_db(&mut self) -> PyResult<()> {
        self.flush().map_err(to_pyruntime_err)
    }

    #[pyo3(name = "load")]
    fn py_load(&self) -> PyResult<HashMap<String, Vec<u8>>> {
        get_runtime()
            .block_on(async { DatabaseQueries::load(&self.pool).await })
            .map_err(to_pyruntime_err)
    }

    #[pyo3(name = "load_currency")]
    fn py_load_currency(&self, code: &str) -> PyResult<Option<Currency>> {
        let result = get_runtime()
            .block_on(async { DatabaseQueries::load_currency(&self.pool, code).await });
        result.map_err(to_pyruntime_err)
    }

    #[pyo3(name = "load_currencies")]
    fn py_load_currencies(&self) -> PyResult<Vec<Currency>> {
        let result =
            get_runtime().block_on(async { DatabaseQueries::load_currencies(&self.pool).await });
        result.map_err(to_pyruntime_err)
    }

    #[pyo3(name = "load_instrument")]
    fn py_load_instrument(
        &self,
        py: Python,
        instrument_id: InstrumentId,
    ) -> PyResult<Option<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_instrument(&self.pool, &instrument_id)
                .await
                .unwrap();
            match result {
                Some(instrument) => {
                    let py_object = instrument_any_to_pyobject(py, instrument)?;
                    Ok(Some(py_object))
                }
                None => Ok(None),
            }
        })
    }

    #[pyo3(name = "load_instruments")]
    fn py_load_instruments(&self, py: Python) -> PyResult<Vec<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_instruments(&self.pool).await.unwrap();
            let mut instruments = Vec::new();
            for instrument in result {
                let py_object = instrument_any_to_pyobject(py, instrument)?;
                instruments.push(py_object);
            }
            Ok(instruments)
        })
    }

    #[pyo3(name = "load_order")]
    fn py_load_order(
        &self,
        py: Python,
        client_order_id: ClientOrderId,
    ) -> PyResult<Option<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_order(&self.pool, &client_order_id)
                .await
                .unwrap();
            match result {
                Some(order) => {
                    let py_object = order_any_to_pyobject(py, order)?;
                    Ok(Some(py_object))
                }
                None => Ok(None),
            }
        })
    }

    #[pyo3(name = "load_account")]
    fn py_load_account(&self, py: Python, account_id: AccountId) -> PyResult<Option<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_account(&self.pool, &account_id)
                .await
                .unwrap();
            match result {
                Some(account) => {
                    let py_object = account_any_to_pyobject(py, account)?;
                    Ok(Some(py_object))
                }
                None => Ok(None),
            }
        })
    }

    #[pyo3(name = "load_quotes")]
    fn py_load_quotes(&self, py: Python, instrument_id: InstrumentId) -> PyResult<Vec<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_quotes(&self.pool, &instrument_id)
                .await
                .unwrap();
            let mut quotes = Vec::new();
            for quote in result {
                let py_object = quote.into_py_any(py)?;
                quotes.push(py_object);
            }
            Ok(quotes)
        })
    }

    #[pyo3(name = "load_trades")]
    fn py_load_trades(&self, py: Python, instrument_id: InstrumentId) -> PyResult<Vec<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_trades(&self.pool, &instrument_id)
                .await
                .unwrap();
            let mut trades = Vec::new();
            for trade in result {
                let py_object = trade.into_py_any(py)?;
                trades.push(py_object);
            }
            Ok(trades)
        })
    }

    #[pyo3(name = "load_bars")]
    fn py_load_bars(&self, py: Python, instrument_id: InstrumentId) -> PyResult<Vec<Py<PyAny>>> {
        get_runtime().block_on(async {
            let result = DatabaseQueries::load_bars(&self.pool, &instrument_id)
                .await
                .unwrap();
            let mut bars = Vec::new();
            for bar in result {
                let py_object = bar.into_py_any(py)?;
                bars.push(py_object);
            }
            Ok(bars)
        })
    }

    #[pyo3(name = "load_signals")]
    fn py_load_signals(&self, name: &str) -> PyResult<Vec<Signal>> {
        get_runtime().block_on(async {
            DatabaseQueries::load_signals(&self.pool, name)
                .await
                .map_err(to_pyruntime_err)
        })
    }

    #[pyo3(name = "load_custom_data")]
    fn py_load_custom_data(&self, data_type: DataType) -> PyResult<Vec<CustomData>> {
        get_runtime().block_on(async {
            DatabaseQueries::load_custom_data(&self.pool, &data_type)
                .await
                .map_err(to_pyruntime_err)
        })
    }

    #[pyo3(name = "load_order_snapshot")]
    fn py_load_order_snapshot(
        &self,
        client_order_id: ClientOrderId,
    ) -> PyResult<Option<OrderSnapshot>> {
        get_runtime().block_on(async {
            DatabaseQueries::load_order_snapshot(&self.pool, &client_order_id)
                .await
                .map_err(to_pyruntime_err)
        })
    }

    #[pyo3(name = "load_position_snapshot")]
    fn py_load_position_snapshot(
        &self,
        position_id: PositionId,
    ) -> PyResult<Option<PositionSnapshot>> {
        get_runtime().block_on(async {
            DatabaseQueries::load_position_snapshot(&self.pool, &position_id)
                .await
                .map_err(to_pyruntime_err)
        })
    }

    #[pyo3(name = "add")]
    fn py_add(&self, key: String, value: Vec<u8>) -> PyResult<()> {
        self.add(key, Bytes::from(value)).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_currency")]
    fn py_add_currency(&self, currency: Currency) -> PyResult<()> {
        self.add_currency(&currency).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_instrument")]
    fn py_add_instrument(&self, py: Python, instrument: Py<PyAny>) -> PyResult<()> {
        let instrument_any = pyobject_to_instrument_any(py, instrument)?;
        self.add_instrument(&instrument_any)
            .map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_order")]
    #[pyo3(signature = (order, client_id=None))]
    fn py_add_order(
        &self,
        py: Python,
        order: Py<PyAny>,
        client_id: Option<ClientId>,
    ) -> PyResult<()> {
        let order_any = pyobject_to_order_any(py, order)?;
        self.add_order(&order_any, client_id)
            .map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_order_snapshot")]
    fn py_add_order_snapshot(&self, snapshot: OrderSnapshot) -> PyResult<()> {
        self.add_order_snapshot(&snapshot).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_position_snapshot")]
    fn py_add_position_snapshot(&self, snapshot: PositionSnapshot) -> PyResult<()> {
        self.add_position_snapshot(&snapshot)
            .map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_account")]
    fn py_add_account(&self, py: Python, account: Py<PyAny>) -> PyResult<()> {
        let account_any = pyobject_to_account_any(py, account)?;
        self.add_account(&account_any).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_quote")]
    fn py_add_quote(&self, quote: QuoteTick) -> PyResult<()> {
        self.add_quote(&quote).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_trade")]
    fn py_add_trade(&self, trade: TradeTick) -> PyResult<()> {
        self.add_trade(&trade).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_bar")]
    fn py_add_bar(&self, bar: Bar) -> PyResult<()> {
        self.add_bar(&bar).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_signal")]
    fn py_add_signal(&self, signal: Signal) -> PyResult<()> {
        self.add_signal(&signal).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "add_custom_data")]
    fn py_add_custom_data(&self, data: CustomData) -> PyResult<()> {
        self.add_custom_data(&data).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "update_order")]
    fn py_update_order(&self, py: Python, order_event: Py<PyAny>) -> PyResult<()> {
        let event = pyobject_to_order_event(py, order_event)?;
        self.update_order(&event).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "update_account")]
    fn py_update_account(&self, py: Python, order: Py<PyAny>) -> PyResult<()> {
        let order_any = pyobject_to_account_any(py, order)?;
        self.update_account(&order_any).map_err(to_pyruntime_err)
    }
}
```


---

## Overview

This file is located at `crates/infrastructure/src/python/sql/cache.rs` within the repository.

**Classes defined:** PostgresCacheDatabase

**Functions defined:** py_connect, py_close, py_flush_db, py_load, py_load_currency, py_load_currencies, py_load_instrument, py_load_instruments, py_load_order, py_load_account and 21 more


---

## Detailed Analysis

### Classes

#### `PostgresCacheDatabase`

**Type:** impl


### Functions

#### `py_connect(
        host: Option<String>,
        port: Option<u16>,
        username: Option<String>,
        password: Option<String>,
        database: Option<String>,
    )`


#### `py_close(&mut self)`


#### `py_flush_db(&mut self)`


#### `py_load(&self)`


#### `py_load_currency(&self, code: &str)`


#### `py_load_currencies(&self)`


#### `py_load_instrument(
        &self,
        py: Python,
        instrument_id: InstrumentId,
    )`


#### `py_load_instruments(&self, py: Python)`


#### `py_load_order(
        &self,
        py: Python,
        client_order_id: ClientOrderId,
    )`


#### `py_load_account(&self, py: Python, account_id: AccountId)`


#### `py_load_quotes(&self, py: Python, instrument_id: InstrumentId)`


#### `py_load_trades(&self, py: Python, instrument_id: InstrumentId)`


#### `py_load_bars(&self, py: Python, instrument_id: InstrumentId)`


#### `py_load_signals(&self, name: &str)`


#### `py_load_custom_data(&self, data_type: DataType)`


#### `py_load_order_snapshot(
        &self,
        client_order_id: ClientOrderId,
    )`


#### `py_load_position_snapshot(
        &self,
        position_id: PositionId,
    )`


#### `py_add(&self, key: String, value: Vec<u8>)`


#### `py_add_currency(&self, currency: Currency)`


#### `py_add_instrument(&self, py: Python, instrument: Py<PyAny>)`


#### `py_add_order(
        &self,
        py: Python,
        order: Py<PyAny>,
        client_id: Option<ClientId>,
    )`


#### `py_add_order_snapshot(&self, snapshot: OrderSnapshot)`


#### `py_add_position_snapshot(&self, snapshot: PositionSnapshot)`


#### `py_add_account(&self, py: Python, account: Py<PyAny>)`


#### `py_add_quote(&self, quote: QuoteTick)`


#### `py_add_trade(&self, trade: TradeTick)`


#### `py_add_bar(&self, bar: Bar)`


#### `py_add_signal(&self, signal: Signal)`


#### `py_add_custom_data(&self, data: CustomData)`


#### `py_update_order(&self, py: Python, order_event: Py<PyAny>)`


#### `py_update_account(&self, py: Python, order: Py<PyAny>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/infrastructure/src/python/sql`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password. Ensure proper handling of secrets.


