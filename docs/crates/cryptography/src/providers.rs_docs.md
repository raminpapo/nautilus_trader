# Documentation: providers.rs

## File Metadata

- **Path**: `crates/cryptography/src/providers.rs`
- **Size**: 1,842 bytes
- **Lines**: 40
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`install_cryptographic_provider()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `install_cryptographic_provider`

## Related Files

This file is located in `crates/cryptography/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.460373Z*
