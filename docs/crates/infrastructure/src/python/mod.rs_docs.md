# Documentation: mod.rs

## File Metadata

- **Path**: `crates/infrastructure/src/python/mod.rs`
- **Size**: 1,728 bytes
- **Lines**: 43
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

//! Python bindings from [PyO3](https://pyo3.rs).

#[cfg(feature = "redis")]
pub mod redis;

#[cfg(feature = "postgres")]
pub mod sql;

use pyo3::{prelude::*, pymodule};

/// Python module initializer for the `infrastructure` package.
///
/// # Errors
///
/// Returns a `PyErr` if the module initialization fails, e.g., when adding classes to the module.
#[pymodule]
pub fn infrastructure(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    #[cfg(feature = "redis")]
    m.add_class::<crate::redis::cache::RedisCacheDatabase>()?;
    #[cfg(feature = "redis")]
    m.add_class::<crate::redis::msgbus::RedisMessageBusDatabase>()?;
    #[cfg(feature = "postgres")]
    m.add_class::<crate::sql::cache::PostgresCacheDatabase>()?;
    #[cfg(feature = "postgres")]
    m.add_class::<crate::sql::pg::PostgresConnectOptions>()?;
    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`infrastructure()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `infrastructure`

## Related Files

This file is located in `crates/infrastructure/src/python/`. Related files may include:
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

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:55:01.993265Z*
