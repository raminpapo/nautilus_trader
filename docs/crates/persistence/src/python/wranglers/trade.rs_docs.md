# Documentation: trade.rs

## File Metadata

- **Path**: `crates/persistence/src/python/wranglers/trade.rs`
- **Size**: 2,945 bytes
- **Lines**: 87
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

use std::{collections::HashMap, io::Cursor, str::FromStr};

use datafusion::arrow::ipc::reader::StreamReader;
use nautilus_core::python::to_pyvalue_err;
use nautilus_model::{data::TradeTick, identifiers::InstrumentId};
use nautilus_serialization::arrow::DecodeFromRecordBatch;
use pyo3::prelude::*;

#[pyclass]
pub struct TradeTickDataWrangler {
    instrument_id: InstrumentId,
    price_precision: u8,
    size_precision: u8,
    metadata: HashMap<String, String>,
}

#[pymethods]
impl TradeTickDataWrangler {
    #[new]
    fn py_new(instrument_id: &str, price_precision: u8, size_precision: u8) -> PyResult<Self> {
        let instrument_id = InstrumentId::from_str(instrument_id).map_err(to_pyvalue_err)?;
        let metadata = TradeTick::get_metadata(&instrument_id, price_precision, size_precision);

        Ok(Self {
            instrument_id,
            price_precision,
            size_precision,
            metadata,
        })
    }

    #[getter]
    fn instrument_id(&self) -> String {
        self.instrument_id.to_string()
    }

    #[getter]
    const fn price_precision(&self) -> u8 {
        self.price_precision
    }

    #[getter]
    const fn size_precision(&self) -> u8 {
        self.size_precision
    }

    fn process_record_batch_bytes(&self, data: &[u8]) -> PyResult<Vec<TradeTick>> {
        // Create a StreamReader (from Arrow IPC)
        let cursor = Cursor::new(data);
        let reader = match StreamReader::try_new(cursor, None) {
            Ok(reader) => reader,
            Err(e) => return Err(to_pyvalue_err(e)),
        };

        let mut ticks = Vec::new();

        // Read the record batches
        for maybe_batch in reader {
            let record_batch = match maybe_batch {
                Ok(record_batch) => record_batch,
                Err(e) => return Err(to_pyvalue_err(e)),
            };

            let batch_deltas =
                TradeTick::decode_batch(&self.metadata, record_batch).map_err(to_pyvalue_err)?;
            ticks.extend(batch_deltas);
        }

        Ok(ticks)
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`instrument_id()`**: Function defined in this file
- **`price_precision()`**: Function defined in this file
- **`size_precision()`**: Function defined in this file
- **`process_record_batch_bytes()`**: Function defined in this file

### Classes
- **`TradeTickDataWrangler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `instrument_id`, `price_precision`, `process_record_batch_bytes`, `py_new`, `size_precision`
**Impls**: `TradeTickDataWrangler`
**Structs**: `TradeTickDataWrangler`

## Related Files

This file is located in `crates/persistence/src/python/wranglers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.573298Z*
