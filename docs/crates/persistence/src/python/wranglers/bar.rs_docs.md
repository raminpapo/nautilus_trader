# Documentation: bar.rs

## File Metadata

- **Path**: `crates/persistence/src/python/wranglers/bar.rs`
- **Size**: 2,839 bytes
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
use nautilus_model::data::bar::{Bar, BarType};
use nautilus_serialization::arrow::DecodeFromRecordBatch;
use pyo3::prelude::*;

#[pyclass]
pub struct BarDataWrangler {
    bar_type: BarType,
    price_precision: u8,
    size_precision: u8,
    metadata: HashMap<String, String>,
}

#[pymethods]
impl BarDataWrangler {
    #[new]
    fn py_new(bar_type: &str, price_precision: u8, size_precision: u8) -> PyResult<Self> {
        let bar_type = BarType::from_str(bar_type).map_err(to_pyvalue_err)?;
        let metadata = Bar::get_metadata(&bar_type, price_precision, size_precision);

        Ok(Self {
            bar_type,
            price_precision,
            size_precision,
            metadata,
        })
    }

    #[getter]
    fn bar_type(&self) -> String {
        self.bar_type.to_string()
    }

    #[getter]
    const fn price_precision(&self) -> u8 {
        self.price_precision
    }

    #[getter]
    const fn size_precision(&self) -> u8 {
        self.size_precision
    }

    fn process_record_batch_bytes(&self, data: &[u8]) -> PyResult<Vec<Bar>> {
        // Create a StreamReader (from Arrow IPC)
        let cursor = Cursor::new(data);
        let reader = match StreamReader::try_new(cursor, None) {
            Ok(reader) => reader,
            Err(e) => return Err(to_pyvalue_err(e)),
        };

        let mut bars = Vec::new();

        // Read the record batches
        for maybe_batch in reader {
            let record_batch = match maybe_batch {
                Ok(record_batch) => record_batch,
                Err(e) => return Err(to_pyvalue_err(e)),
            };

            let batch_bars =
                Bar::decode_batch(&self.metadata, record_batch).map_err(to_pyvalue_err)?;
            bars.extend(batch_bars);
        }

        Ok(bars)
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`bar_type()`**: Function defined in this file
- **`price_precision()`**: Function defined in this file
- **`size_precision()`**: Function defined in this file
- **`process_record_batch_bytes()`**: Function defined in this file

### Classes
- **`BarDataWrangler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `bar_type`, `price_precision`, `process_record_batch_bytes`, `py_new`, `size_precision`
**Impls**: `BarDataWrangler`
**Structs**: `BarDataWrangler`

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
*Generated on 2025-11-18T21:55:03.564731Z*
