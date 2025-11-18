# Documentation: pg.rs

## File Metadata

- **Path**: `crates/infrastructure/src/python/sql/pg.rs`
- **Size**: 2,258 bytes
- **Lines**: 74
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

use pyo3::prelude::*;

use crate::sql::pg::PostgresConnectOptions;

#[pymethods]
#[pyo3_stub_gen::derive::gen_stub_pymethods(module = "nautilus_trader.infrastructure")]
impl PostgresConnectOptions {
    /// Creates a new `PostgresConnectOptions` instance.
    #[new]
    #[pyo3(signature = (host, port, user, password, database))]
    const fn py_new(
        host: String,
        port: u16,
        user: String,
        password: String,
        database: String,
    ) -> Self {
        Self::new(host, port, user, password, database)
    }

    /// Returns a string representation of the configuration.
    fn __repr__(&self) -> String {
        format!(
            "PostgresConnectOptions(host={}, port={}, username={}, database={})",
            self.host, self.port, self.username, self.database
        )
    }

    /// Returns the host.
    #[getter]
    fn host(&self) -> String {
        self.host.clone()
    }

    /// Returns the port.
    #[getter]
    const fn port(&self) -> u16 {
        self.port
    }

    /// Returns the username.
    #[getter]
    fn username(&self) -> String {
        self.username.clone()
    }

    /// Returns the password.
    #[getter]
    fn password(&self) -> String {
        self.password.clone()
    }

    /// Returns the database.
    #[getter]
    fn database(&self) -> String {
        self.database.clone()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`host()`**: Function defined in this file
- **`port()`**: Function defined in this file
- **`username()`**: Function defined in this file
- **`password()`**: Function defined in this file
- **`database()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `__repr__`, `database`, `host`, `password`, `port`, `py_new`, `username`
**Impls**: `PostgresConnectOptions`

## Related Files

This file is located in `crates/infrastructure/src/python/sql/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:55:02.005503Z*
