# Documentation: `crates/cryptography/src/python/signing.rs`
**Generated:** 2025-11-15T19:40:01.957983Z
**File Size:** 2127 bytes
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

- **Path:** `crates/cryptography/src/python/signing.rs`
- **Size:** 2,127 bytes
- **Lines:** 49
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 3

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


---

## Overview

This file is located at `crates/cryptography/src/python/signing.rs` within the repository.

**Functions defined:** py_hmac_signature, py_rsa_signature, py_ed25519_signature


---

## Detailed Analysis

### Functions

#### `py_hmac_signature(secret: &str, data: &str)`


#### `py_rsa_signature(private_key_pem: &str, data: &str)`


#### `py_ed25519_signature(private_key: &[u8], data: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cryptography/src/python`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, private_key. Ensure proper handling of secrets.


