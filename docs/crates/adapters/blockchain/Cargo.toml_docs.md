# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/adapters/blockchain/Cargo.toml`
- **Size**: 2,744 bytes
- **Lines**: 97
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-blockchain"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Blockchain and DeFi integration adapter for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_blockchain"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-data/extension-module",
  "nautilus-model/extension-module",
  "nautilus-network/extension-module",
  "python",
  "pyo3/extension-module",
]
hypersync = ["hypersync-client", "hypersync-schema"]
python = [
  "nautilus-infrastructure/python",
  "nautilus-network/python",
  "nautilus-system/python",
  "pyo3",
  "pyo3-stub-gen",
]
turmoil = ["dep:turmoil", "nautilus-network/turmoil"]

[package.metadata.docs.rs]
features = ["python"]
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true, features = ["defi"] }
nautilus-core = { workspace = true }
nautilus-data = { workspace = true, features = ["defi"] }
nautilus-infrastructure = { workspace = true, features = ["postgres"] }
nautilus-live = { workspace = true, features = ["defi"] }
nautilus-model = { workspace = true, features = ["defi"] }
nautilus-network = { workspace = true }
nautilus-system = { workspace = true }

ahash = { workspace = true }
alloy = { workspace = true }
anyhow = { workspace = true }
async-stream = { workspace = true }
async-trait = { workspace = true }
bytes = { workspace = true }
dotenvy = { workspace = true }
enum_dispatch = { workspace = true }
futures-util = { workspace = true }
hex = { workspace = true }
log = { workspace = true }
reqwest = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
sqlx = { workspace = true }
strum = { workspace = true }
thiserror = { workspace = true }
thousands = { workspace = true }
tokio = { workspace = true }
tokio-tungstenite = { workspace = true }
tokio-util = { workspace = true }
tracing = { workspace = true }
ustr = { workspace = true }

hypersync-client = { workspace = true, optional = true }
hypersync-schema = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }
pyo3-stub-gen = { workspace = true, optional = true }
turmoil = { workspace = true, optional = true }

[dev-dependencies]
rstest = { workspace = true }
turmoil = { workspace = true }

[[bin]]
name = "node_test"
path = "bin/node_test.rs"
required-features = ["hypersync"]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 58


**Keys**: `ahash`, `alloy`, `anyhow`, `async-stream`, `async-trait`, `bytes`, `crate-type`, `default`, `description`, `dotenvy`, `enum_dispatch`, `extension-module`, `features`, `futures-util`, `hex`, `hypersync`, `hypersync-client`, `hypersync-schema`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-infrastructure`, `nautilus-live`, `nautilus-model`, `nautilus-network`, `nautilus-system`, `path`, `pyo3` *(+21 more)*
**Sections**: `[bin`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/adapters/blockchain/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.146168Z*
