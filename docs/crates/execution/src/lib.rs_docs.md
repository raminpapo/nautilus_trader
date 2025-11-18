# Documentation: lib.rs

## File Metadata

- **Path**: `crates/execution/src/lib.rs`
- **Size**: 3,788 bytes
- **Lines**: 72
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

//! Order execution engine for [NautilusTrader](http://nautilustrader.io).
//!
//! The `nautilus-execution` crate provides a comprehensive order execution system that handles the complete
//! order lifecycle from submission to fill processing. This includes sophisticated order matching,
//! execution venue integration, and advanced order type emulation:
//!
//! - **Execution engine**: Central orchestration of order routing and position management.
//! - **Order matching engine**: High-fidelity market simulation for backtesting and paper trading.
//! - **Order emulator**: Advanced order types not natively supported by venues (trailing stops, contingent orders).
//! - **Execution clients**: Abstract interfaces for connecting to trading venues and brokers.
//! - **Order manager**: Local order lifecycle management and state tracking.
//! - **Matching core**: Low-level order book and price-time priority matching algorithms.
//! - **Fee and fill models**: Configurable execution cost simulation and realistic fill behavior.
//!
//! The crate supports both live trading environments (with real execution clients) and simulated
//! environments (with matching engines), making it suitable for production trading, strategy
//! development, and comprehensive backtesting.
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
#![deny(nonstandard_style)]
#![deny(missing_debug_implementations)]
#![deny(clippy::missing_errors_doc)]
#![deny(clippy::missing_panics_doc)]
#![deny(rustdoc::broken_intra_doc_links)]

pub mod client;
pub mod engine;
pub mod matching_core;
pub mod matching_engine;
pub mod models;
pub mod order_emulator;
pub mod order_manager;
pub mod protection;
pub mod trailing;

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/execution/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.651009Z*
