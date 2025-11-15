# Documentation: `crates/adapters/databento/src/python/historical.rs`
**Generated:** 2025-11-15T19:40:00.878618Z
**File Size:** 12698 bytes
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

- **Path:** `crates/adapters/databento/src/python/historical.rs`
- **Size:** 12,698 bytes
- **Lines:** 391
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 10

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

//! Python bindings for the Databento historical client.

use std::path::PathBuf;

use nautilus_core::{
    python::{IntoPyObjectNautilusExt, to_pyvalue_err},
    time::get_atomic_clock_realtime,
};
use nautilus_model::{
    enums::BarAggregation, identifiers::InstrumentId,
    python::instruments::instrument_any_to_pyobject,
};
use pyo3::{
    IntoPyObjectExt,
    exceptions::PyException,
    prelude::*,
    types::{PyDict, PyList},
};

use crate::historical::{
    DatabentoHistoricalClient as CoreDatabentoHistoricalClient, RangeQueryParams,
};

/// Python wrapper for the core Databento historical client.
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.databento")
)]
#[derive(Debug)]
pub struct DatabentoHistoricalClient {
    #[pyo3(get)]
    pub key: String,
    inner: CoreDatabentoHistoricalClient,
}

#[pymethods]
impl DatabentoHistoricalClient {
    #[new]
    fn py_new(
        key: String,
        publishers_filepath: PathBuf,
        use_exchange_as_venue: bool,
    ) -> PyResult<Self> {
        let clock = get_atomic_clock_realtime();
        let inner = CoreDatabentoHistoricalClient::new(
            key.clone(),
            publishers_filepath,
            clock,
            use_exchange_as_venue,
        )
        .map_err(to_pyvalue_err)?;

        Ok(Self { key, inner })
    }

    #[pyo3(name = "get_dataset_range")]
    fn py_get_dataset_range<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let response = inner.get_dataset_range(&dataset).await;
            match response {
                Ok(res) => Python::attach(|py| {
                    let dict = PyDict::new(py);
                    dict.set_item("start", res.start)?;
                    dict.set_item("end", res.end)?;
                    dict.into_py_any(py)
                }),
                Err(e) => Err(PyErr::new::<PyException, _>(format!(
                    "Error handling response: {e}"
                ))),
            }
        })
    }

    #[pyo3(name = "get_range_instruments")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, limit=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_instruments<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision: None,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let instruments = inner
                .get_range_instruments(params)
                .await
                .map_err(to_pyvalue_err)?;

            Python::attach(|py| -> PyResult<Py<PyAny>> {
                let objs: Vec<Py<PyAny>> = instruments
                    .into_iter()
                    .map(|inst| instrument_any_to_pyobject(py, inst))
                    .collect::<PyResult<Vec<Py<PyAny>>>>()?;

                let list = PyList::new(py, &objs).expect("Invalid `ExactSizeIterator`");
                Ok(list.into_py_any_unwrap(py))
            })
        })
    }

    #[pyo3(name = "get_range_quotes")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, limit=None, price_precision=None, schema=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_quotes<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
        schema: Option<String>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let quotes = inner
                .get_range_quotes(params, schema)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| quotes.into_py_any(py))
        })
    }

    #[pyo3(name = "get_range_trades")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, limit=None, price_precision=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_trades<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let trades = inner
                .get_range_trades(params)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| trades.into_py_any(py))
        })
    }

    #[pyo3(name = "get_range_bars")]
    #[pyo3(signature = (dataset, instrument_ids, aggregation, start, end=None, limit=None, price_precision=None, timestamp_on_close=true))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_bars<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        aggregation: BarAggregation,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
        timestamp_on_close: bool,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let bars = inner
                .get_range_bars(params, aggregation, timestamp_on_close)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| bars.into_py_any(py))
        })
    }

    #[pyo3(name = "get_order_book_depth10")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, depth=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_order_book_depth10<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        depth: Option<usize>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit: None,
            price_precision: None,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let depths = inner
                .get_range_order_book_depth10(params, depth)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| depths.into_py_any(py))
        })
    }

    #[pyo3(name = "get_range_imbalance")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, limit=None, price_precision=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_imbalance<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let imbalances = inner
                .get_range_imbalance(params)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| imbalances.into_py_any(py))
        })
    }

    #[pyo3(name = "get_range_statistics")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, limit=None, price_precision=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_statistics<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let statistics = inner
                .get_range_statistics(params)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| statistics.into_py_any(py))
        })
    }

    #[pyo3(name = "get_range_status")]
    #[pyo3(signature = (dataset, instrument_ids, start, end=None, limit=None))]
    #[allow(clippy::too_many_arguments)]
    fn py_get_range_status<'py>(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let inner = self.inner.clone();
        let symbols = inner
            .prepare_symbols_from_instrument_ids(&instrument_ids)
            .map_err(to_pyvalue_err)?;

        let params = RangeQueryParams {
            dataset,
            symbols,
            start: start.into(),
            end: end.map(Into::into),
            limit,
            price_precision: None,
        };

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            let statuses = inner
                .get_range_status(params)
                .await
                .map_err(to_pyvalue_err)?;
            Python::attach(|py| statuses.into_py_any(py))
        })
    }
}
```


---

## Overview

This file is located at `crates/adapters/databento/src/python/historical.rs` within the repository.

**Classes defined:** DatabentoHistoricalClient, DatabentoHistoricalClient

**Functions defined:** py_new, py_get_dataset_range, py_get_range_instruments, py_get_range_quotes, py_get_range_trades, py_get_range_bars, py_get_order_book_depth10, py_get_range_imbalance, py_get_range_statistics, py_get_range_status


---

## Detailed Analysis

### Classes

#### `DatabentoHistoricalClient`

**Type:** struct


#### `DatabentoHistoricalClient`

**Type:** impl


### Functions

#### `py_new(
        key: String,
        publishers_filepath: PathBuf,
        use_exchange_as_venue: bool,
    )`


#### `py_get_dataset_range(
        &self,
        py: Python<'py>,
        dataset: String,
    )`


#### `py_get_range_instruments(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
    )`


#### `py_get_range_quotes(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
        schema: Option<String>,
    )`


#### `py_get_range_trades(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
    )`


#### `py_get_range_bars(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        aggregation: BarAggregation,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
        timestamp_on_close: bool,
    )`


#### `py_get_order_book_depth10(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        depth: Option<usize>,
    )`


#### `py_get_range_imbalance(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
    )`


#### `py_get_range_statistics(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
        price_precision: Option<u8>,
    )`


#### `py_get_range_status(
        &self,
        py: Python<'py>,
        dataset: String,
        instrument_ids: Vec<InstrumentId>,
        start: u64,
        end: Option<u64>,
        limit: Option<u64>,
    )`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


