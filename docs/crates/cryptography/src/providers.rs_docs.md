# Documentation: `crates/cryptography/src/providers.rs`
**Generated:** 2025-11-15T19:40:01.955438Z
**File Size:** 1842 bytes
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

- **Path:** `crates/cryptography/src/providers.rs`
- **Size:** 1,842 bytes
- **Lines:** 39
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

use std::sync::Once;

use rustls::crypto::{CryptoProvider, aws_lc_rs};

// Static flag to ensure the provider is installed only once
static INSTALL_PROVIDER: Once = Once::new();

/// Installs the AWS-LC cryptographic provider as the default for rustls.
///
/// This function ensures that the cryptographic provider is installed only once
/// using a static guard. If no default provider is already set, it will install
/// the AWS-LC provider and log the result.
pub fn install_cryptographic_provider() {
    INSTALL_PROVIDER.call_once(|| {
        if CryptoProvider::get_default().is_none() {
            tracing::debug!("Installing aws_lc_rs cryptographic provider");

            match aws_lc_rs::default_provider().install_default() {
                Ok(()) => tracing::debug!("Cryptographic provider installed successfully"),
                Err(e) => tracing::debug!("Error installing cryptographic provider: {e:?}"),
            }
        }
    });
}
```


---

## Overview

This file is located at `crates/cryptography/src/providers.rs` within the repository.

**Functions defined:** install_cryptographic_provider


---

## Detailed Analysis

### Functions

#### `install_cryptographic_provider()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cryptography/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


