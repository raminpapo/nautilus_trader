# Documentation: README.md

## File Metadata

- **Path**: `crates/pyo3/README.md`
- **Size**: 1,508 bytes
- **Lines**: 28
- **Language**: Markdown

## Original Source

```markdown
# nautilus-pyo3

A temporary crate to provide all Python bindings for the main `nautilus_trader` Python package.

## Platform

[NautilusTrader](http://nautilustrader.io) is an open-source, high-performance, production-grade
algorithmic trading platform, providing quantitative traders with the ability to backtest
portfolios of automated trading strategies on historical data with an event-driven engine,
and also deploy those same strategies live, with no code changes.

NautilusTrader's design, architecture, and implementation philosophy prioritizes software correctness and safety at the
highest level, with the aim of supporting mission-critical, trading system backtesting and live deployment workloads.

## Feature flags

This crate is primarily intended to be built for Python via
[maturin](https://github.com/PyO3/maturin) and therefore provides a broad set of feature flags
to toggle bindings and optional dependencies:

- `extension-module`: Builds the crate as a Python extension module (automatically enabled by `maturin`).
- `ffi`: Enables the C foreign function interface (FFI) support in dependent crates.
- `high-precision`: Uses 128-bit value types throughout the workspace.
- `cython-compat`: Adjusts the module name so it can be imported from Cython generated code.
- `postgres`: Enables PostgreSQL (sqlx) back-ends in dependent crates.
- `redis`: Enables Redis based infrastructure in dependent crates.
- `hypersync`: Enables hypersync support (fast parallel hash maps) where available.

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 14


**Identifiers**: `Adjusts`, `Builds`, `Cython`, `Enables`, `FFI`, `Feature`, `NautilusTrader`, `Platform`, `PostgreSQL`, `PyO3`, `Python`, `Redis`, `This`, `Uses`

## Related Files

This file is located in `crates/pyo3/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.625409Z*
