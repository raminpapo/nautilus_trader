# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/infrastructure/Cargo.toml`
- **Size**: 2,166 bytes
- **Lines**: 82
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-infrastructure"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Infrastructure components for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_infrastructure"
crate-type = ["rlib", "cdylib"]

[features]
default = ["redis"] # redis needed by `nautilus_trader` by default for now
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
  "pyo3-async-runtimes",
  "pyo3-stub-gen",
]
redis = ["dep:redis"]
postgres = ["dep:sqlx"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-cryptography = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }

ahash = { workspace = true }
anyhow = { workspace = true }
async-stream = { workspace = true }
async-trait = { workspace = true }
bytes = { workspace = true }
chrono = { workspace = true }
derive_builder = { workspace = true }
futures = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
regex = { workspace = true }
rmp-serde = { workspace = true }
rust_decimal = { workspace = true }
semver = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }
pyo3-stub-gen = { workspace = true, optional = true }
redis = { workspace = true, optional = true }
sqlx = { workspace = true, optional = true }

[dev-dependencies]
rstest = { workspace = true }
serde = { workspace = true }

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 47


**Keys**: `ahash`, `all-features`, `anyhow`, `async-stream`, `async-trait`, `bytes`, `chrono`, `crate-type`, `default`, `derive_builder`, `description`, `extension-module`, `futures`, `indexmap`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-cryptography`, `nautilus-model`, `postgres`, `pyo3`, `pyo3-async-runtimes`, `pyo3-stub-gen`, `python`, `readme`, `redis`, `regex`, `rmp-serde`, `rstest` *(+10 more)*
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/infrastructure/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.986154Z*
