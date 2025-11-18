# Documentation: signing.rs

## File Metadata

- **Path**: `crates/cryptography/src/python/signing.rs`
- **Size**: 2,127 bytes
- **Lines**: 50
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

use nautilus_core::python::to_pyvalue_err;
use pyo3::prelude::*;

use crate::signing::{ed25519_signature, hmac_signature, rsa_signature};

/// HMAC-SHA256 signature of `data` using the provided `secret`.
///
/// # Errors
///
/// Returns an error if signature generation fails due to key or cryptographic errors.
#[pyfunction(name = "hmac_signature")]
pub fn py_hmac_signature(secret: &str, data: &str) -> PyResult<String> {
    hmac_signature(secret, data).map_err(to_pyvalue_err)
}

/// RSA PKCS#1 SHA-256 signature of `data` using the provided private key in PEM format.
///
/// # Errors
///
/// Returns an error if signature generation fails, e.g., due to empty data or invalid key PEM.
#[pyfunction(name = "rsa_signature")]
pub fn py_rsa_signature(private_key_pem: &str, data: &str) -> PyResult<String> {
    rsa_signature(private_key_pem, data).map_err(to_pyvalue_err)
}

/// Ed25519 signature of `data` using the provided private key seed.
///
/// # Errors
///
/// Returns an error if the private key seed is invalid or signature creation fails.
#[pyfunction(name = "ed25519_signature")]
pub fn py_ed25519_signature(private_key: &[u8], data: &str) -> PyResult<String> {
    ed25519_signature(private_key, data).map_err(to_pyvalue_err)
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`py_hmac_signature()`**: Function defined in this file
- **`py_rsa_signature()`**: Function defined in this file
- **`py_ed25519_signature()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `py_ed25519_signature`, `py_hmac_signature`, `py_rsa_signature`

## Related Files

This file is located in `crates/cryptography/src/python/`. Related files may include:
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

---
*Generated on 2025-11-18T21:55:01.464457Z*
