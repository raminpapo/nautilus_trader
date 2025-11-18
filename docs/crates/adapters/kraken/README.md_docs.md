# Documentation: README.md

## File Metadata

- **Path**: `crates/adapters/kraken/README.md`
- **Size**: 3,178 bytes
- **Lines**: 69
- **Language**: Markdown

## Original Source

```markdown
# nautilus-kraken

[![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml)
[![Documentation](https://img.shields.io/docsrs/nautilus-kraken)](https://docs.rs/nautilus-kraken/latest/nautilus-kraken/)
[![crates.io version](https://img.shields.io/crates/v/nautilus-kraken.svg)](https://crates.io/crates/nautilus-kraken)
![license](https://img.shields.io/github/license/nautechsystems/nautilus_trader?color=blue)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.gg/NautilusTrader)

[NautilusTrader](http://nautilustrader.io) adapter for the [Kraken](https://www.kraken.com/) exchange.

The `nautilus-kraken` crate provides client bindings (HTTP & WebSocket), data models,
and helper utilities that wrap the official **Kraken API v2**.

The official Kraken API reference can be found at <https://docs.kraken.com/api/>.

## Platform

[NautilusTrader](http://nautilustrader.io) is an open-source, high-performance, production-grade
algorithmic trading platform, providing quantitative traders with the ability to backtest
portfolios of automated trading strategies on historical data with an event-driven engine,
and also deploy those same strategies live, with no code changes.

NautilusTrader's design, architecture, and implementation philosophy prioritizes software correctness and safety at the
highest level, with the aim of supporting mission-critical, trading system backtesting and live deployment workloads.

## Features

- HTTP REST API v2 client for market data.
- WebSocket v2 client for real-time data feeds.
- Support for both Spot and Futures markets.
- Instrument, ticker, trade, orderbook, and OHLC data.
- Prepared for execution support (orders, positions, balances) - WIP.

## Examples

See the `bin/` directory for example usage:

```bash
cargo run --bin kraken-http-raw
cargo run --bin kraken-http-public
cargo run --bin kraken-ws-data
```

## Feature flags

This crate provides feature flags to control source code inclusion during compilation:

- `python`: Enables Python bindings from [PyO3](https://pyo3.rs).
- `extension-module`: Builds as a Python extension module (used with `python`).

## Documentation

See [the docs](https://docs.rs/nautilus-kraken) for more detailed usage.

## License

The source code for NautilusTrader is available on GitHub under the [GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html).
Contributions to the project are welcome and require the completion of a standard [Contributor License Agreement (CLA)](https://github.com/nautechsystems/nautilus_trader/blob/develop/CLA.md).

---

NautilusTrader is developed and maintained by Nautech Systems, a technology
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

Total unique keywords extracted: 42


**Identifiers**: `API`, `Agreement`, `All`, `Builds`, `CLA`, `Contributions`, `Contributor`, `Discord`, `Documentation`, `Enables`, `Examples`, `Feature`, `Features`, `For`, `Futures`, `GNU`, `General`, `GitHub`, `HTTP`, `Instrument`, `Kraken`, `Lesser`, `License`, `Ltd`, `Nautech`, `NautilusTrader`, `OHLC`, `Platform`, `Prepared`, `Pty` *(+12 more)*

## Related Files

This file is located in `crates/adapters/kraken/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.144002Z*
