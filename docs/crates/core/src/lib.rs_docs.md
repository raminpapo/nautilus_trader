# Documentation: lib.rs

## File Metadata

- **Path**: `crates/core/src/lib.rs`
- **Size**: 4,093 bytes
- **Lines**: 102
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

//! Core foundational types and utilities for [NautilusTrader](http://nautilustrader.io).
//!
//! The `nautilus-core` crate is designed to be lightweight, efficient, and to provide zero-cost abstractions
//! wherever possible. It supplies the essential building blocks used across the NautilusTrader
//! ecosystem, including:
//!
//! - Time handling and atomic clock functionality.
//! - UUID generation and management.
//! - Mathematical functions and interpolation utilities.
//! - Correctness validation functions.
//! - Serialization traits and helpers.
//! - Cross-platform environment utilities.
//! - Abstractions over common collections.
//!
//! # Platform
//!
//! [NautilusTrader](http://nautilustrader.io) is an open-source, high-performance, production-grade
//! algorithmic trading platform, providing quantitative traders with the ability to backtest
//! portfolios of automated trading strategies on historical data with an event-driven engine,
//! and also deploy those same strategies live, with no code changes.
//!
//! NautilusTrader's design, architecture, and implementation philosophy prioritizes software correctness and safety at the
//! highest level, with the aim of supporting mission-critical, trading system backtesting and live deployment workloads.
//!
//! # Feature flags
//!
//! This crate provides feature flags to control source code inclusion during compilation,
//! depending on the intended use case, i.e. whether to provide Python bindings
//! for the [nautilus_trader](https://pypi.org/project/nautilus_trader) Python package,
//! or as part of a Rust only build.
//!
//! - `ffi`: Enables the C foreign function interface (FFI) from [cbindgen](https://github.com/mozilla/cbindgen).
//! - `python`: Enables Python bindings from [PyO3](https://pyo3.rs).
//! - `extension-module`: Builds the crate as a Python extension module.

#![warn(rustc::all)]
#![deny(unsafe_code)]
#![deny(unsafe_op_in_unsafe_fn)]
#![deny(nonstandard_style)]
#![deny(missing_debug_implementations)]
#![deny(missing_docs)]
#![deny(rustdoc::broken_intra_doc_links)]

pub mod collections;
pub mod consts;
pub mod correctness;
pub mod datetime;
pub mod drop;
pub mod env;
pub mod math;
pub mod message;
pub mod nanos;

pub mod parsing;
pub mod paths;
pub mod serialization;
pub mod shared;
pub mod time;
pub mod uuid;

#[cfg(feature = "ffi")]
pub mod ffi;

#[cfg(feature = "python")]
pub mod python;

#[cfg(not(any(target_os = "linux", target_os = "macos", target_os = "windows")))]
compile_error!("Unsupported platform: Nautilus supports only Linux, macOS, and Windows");

// Re-exports
pub use crate::{
    drop::CleanDrop,
    nanos::UnixNanos,
    shared::{SharedCell, WeakCell},
    time::AtomicTime,
    uuid::UUID4,
};

/// Message for when a mutex guard cannot be acquired due to poisoning.
///
/// Mutex guards should use `expect` rather than handle poison errors.
/// A poisoned mutex indicates a thread panicked while holding the lock,
/// meaning protected data may be in an inconsistent state. Propagating
/// the panic is the idiomatic and safe approach, as continuing with
/// potentially corrupted data would violate safety invariants.
pub const MUTEX_POISONED: &str = "Mutex poisoned";

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/core/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.389770Z*
