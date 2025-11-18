# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/python/mod.rs`
- **Size**: 3,435 bytes
- **Lines**: 92
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`extract_blockchain_factory()`**: Function defined in this file
- **`extract_blockchain_config()`**: Function defined in this file
- **`blockchain()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `blockchain`, `extract_blockchain_config`, `extract_blockchain_factory`

## Related Files

This file is located in `crates/adapters/blockchain/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.318217Z*
