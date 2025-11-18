# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/cli/Cargo.toml`
- **Size**: 1,197 bytes
- **Lines**: 52
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-cli"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Command-line interface for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[features]
default = []
defi = [
  "dep:alloy-primitives",
  "dep:nautilus-blockchain",
  "nautilus-model/defi",
]

[dependencies]
nautilus-infrastructure = { workspace = true, features = ["postgres"] }
nautilus-model = { workspace = true }
nautilus-blockchain = { workspace = true, features = [
  "hypersync",
], optional = true }

anyhow = { workspace = true }
clap = { workspace = true }
dotenvy = { workspace = true }
futures-util = { workspace = true }
log = { workspace = true }
simple_logger = { workspace = true }
tokio = { workspace = true }
tokio-util = { workspace = true }

alloy-primitives = { workspace = true, optional = true }

[[bin]]
name = "nautilus"
path = "src/bin/cli.rs"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 27


**Keys**: `all-features`, `alloy-primitives`, `anyhow`, `clap`, `default`, `defi`, `description`, `dotenvy`, `futures-util`, `log`, `name`, `nautilus-blockchain`, `nautilus-infrastructure`, `nautilus-model`, `path`, `readme`, `rustdoc-args`, `simple_logger`, `tokio`, `tokio-util`, `workspace`
**Sections**: `[bin`, `dependencies`, `features`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/cli/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.926516Z*
