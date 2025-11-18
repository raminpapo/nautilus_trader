# Documentation: README.md

## File Metadata

- **Path**: `crates/execution/README.md`
- **Size**: 3,854 bytes
- **Lines**: 65
- **Language**: Markdown

## Original Source

```markdown
# nautilus-execution

[![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml)
[![Documentation](https://img.shields.io/docsrs/nautilus-execution)](https://docs.rs/nautilus-execution/latest/nautilus-execution/)
[![crates.io version](https://img.shields.io/crates/v/nautilus-execution.svg)](https://crates.io/crates/nautilus-execution)
![license](https://img.shields.io/github/license/nautechsystems/nautilus_trader?color=blue)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.gg/NautilusTrader)

Order execution engine for [NautilusTrader](http://nautilustrader.io).

The `nautilus-execution` crate provides a comprehensive order execution system that handles the complete
order lifecycle from submission to fill processing. This includes sophisticated order matching,
execution venue integration, and advanced order type emulation:

- **Execution engine**: Central orchestration of order routing and position management.
- **Order matching engine**: High-fidelity market simulation for backtesting and paper trading.
- **Order emulator**: Advanced order types not natively supported by venues (trailing stops, contingent orders).
- **Execution clients**: Abstract interfaces for connecting to trading venues and brokers.
- **Order manager**: Local order lifecycle management and state tracking.
- **Matching core**: Low-level order book and price-time priority matching algorithms.
- **Fee and fill models**: Configurable execution cost simulation and realistic fill behavior.

The crate supports both live trading environments (with real execution clients) and simulated
environments (with matching engines), making it suitable for production trading, strategy
development, and comprehensive backtesting.

## Platform

[NautilusTrader](http://nautilustrader.io) is an open-source, high-performance, production-grade
algorithmic trading platform, providing quantitative traders with the ability to backtest
portfolios of automated trading strategies on historical data with an event-driven engine,
and also deploy those same strategies live, with no code changes.

NautilusTrader's design, architecture, and implementation philosophy prioritizes software correctness and safety at the
highest level, with the aim of supporting mission-critical, trading system backtesting and live deployment workloads.

## Feature flags

This crate provides feature flags to control source code inclusion during compilation,
depending on the intended use case, i.e. whether to provide Python bindings
for the [nautilus_trader](https://pypi.org/project/nautilus_trader) Python package,
or as part of a Rust only build.

- `ffi`: Enables the C foreign function interface (FFI) from [cbindgen](https://github.com/mozilla/cbindgen).
- `python`: Enables Python bindings from [PyO3](https://pyo3.rs).

## Documentation

See [the docs](https://docs.rs/nautilus-execution) for more detailed usage.

## License

The source code for NautilusTrader is available on GitHub under the [GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html).
Contributions to the project are welcome and require the completion of a standard [Contributor License Agreement (CLA)](https://github.com/nautechsystems/nautilus_trader/blob/develop/CLA.md).

---

NautilusTrader™ is developed and maintained by Nautech Systems, a technology
company specializing in the development of high-performance trading systems.
For more information, visit <https://nautilustrader.io>.

<img src="https://github.com/nautechsystems/nautilus_trader/raw/develop/assets/nautilus-logo-white.png" alt="logo" width="400" height="auto"/>

© 2015-2025 Nautech Systems Pty Ltd. All rights reserved.

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 40


**Identifiers**: `Abstract`, `Advanced`, `Agreement`, `All`, `CLA`, `Central`, `Configurable`, `Contributions`, `Contributor`, `Discord`, `Documentation`, `Enables`, `Execution`, `FFI`, `Feature`, `Fee`, `For`, `GNU`, `General`, `GitHub`, `High`, `Lesser`, `License`, `Local`, `Low`, `Ltd`, `Matching`, `Nautech`, `NautilusTrader`, `Order` *(+10 more)*

## Related Files

This file is located in `crates/execution/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.572133Z*
