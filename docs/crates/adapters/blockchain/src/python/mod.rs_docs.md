# Documentation: `crates/adapters/blockchain/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:00.572145Z
**File Size:** 3435 bytes
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

- **Path:** `crates/adapters/blockchain/src/python/mod.rs`
- **Size:** 3,435 bytes
- **Lines:** 91
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

//! Python bindings from [PyO3](https://pyo3.rs).

pub mod config;

#[cfg(feature = "hypersync")]
pub mod factories;

#[cfg(feature = "hypersync")]
use nautilus_system::{
    factories::{ClientConfig, DataClientFactory},
    get_global_pyo3_registry,
};
use pyo3::prelude::*;

/// Extractor function for `BlockchainDataClientFactory`.
#[cfg(feature = "hypersync")]
fn extract_blockchain_factory(
    py: Python<'_>,
    factory: Py<PyAny>,
) -> PyResult<Box<dyn DataClientFactory>> {
    match factory.extract::<crate::factories::BlockchainDataClientFactory>(py) {
        Ok(concrete_factory) => Ok(Box::new(concrete_factory)),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(format!(
            "Failed to extract BlockchainDataClientFactory: {e}"
        ))),
    }
}

/// Extractor function for `BlockchainDataClientConfig`.
#[cfg(feature = "hypersync")]
fn extract_blockchain_config(py: Python<'_>, config: Py<PyAny>) -> PyResult<Box<dyn ClientConfig>> {
    match config.extract::<crate::config::BlockchainDataClientConfig>(py) {
        Ok(concrete_config) => Ok(Box::new(concrete_config)),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(format!(
            "Failed to extract BlockchainDataClientConfig: {e}"
        ))),
    }
}

/// Loaded as `nautilus_pyo3.blockchain`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn blockchain(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<crate::config::BlockchainDataClientConfig>()?;
    m.add_class::<crate::config::DexPoolFilters>()?;
    #[cfg(feature = "hypersync")]
    m.add_class::<crate::factories::BlockchainDataClientFactory>()?;

    // Register extractors with the global registry
    #[cfg(feature = "hypersync")]
    {
        let registry = get_global_pyo3_registry();

        if let Err(e) = registry
            .register_factory_extractor("BLOCKCHAIN".to_string(), extract_blockchain_factory)
        {
            return Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!(
                "Failed to register blockchain factory extractor: {e}"
            )));
        }

        if let Err(e) = registry.register_config_extractor(
            "BlockchainDataClientConfig".to_string(),
            extract_blockchain_config,
        ) {
            return Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!(
                "Failed to register blockchain config extractor: {e}"
            )));
        }
    }

    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/python/mod.rs` within the repository.

**Functions defined:** extract_blockchain_factory, extract_blockchain_config, blockchain


---

## Detailed Analysis

### Functions

#### `extract_blockchain_factory(
    py: Python<'_>,
    factory: Py<PyAny>,
)`


#### `extract_blockchain_config(py: Python<'_>, config: Py<PyAny>)`


#### `blockchain(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


