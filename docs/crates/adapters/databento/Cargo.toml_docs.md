# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/adapters/databento/Cargo.toml`
- **Size**: 2,408 bytes
- **Lines**: 90
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-databento"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Databento data integration adapter for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_databento"
crate-type = ["rlib", "cdylib"]

[features]
default = ["live"]
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
live = ["nautilus-live", "nautilus-system", "dotenvy", "tracing-subscriber"]
python = [
  "nautilus-core/ffi", # Temporary as python currently relies on the ffi CVec
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
  "pyo3-async-runtimes",
]
high-precision = ["nautilus-model/high-precision"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-data = { workspace = true }
nautilus-live = { workspace = true, optional = true }
nautilus-model = { workspace = true }
nautilus-network = { workspace = true }
nautilus-system = { workspace = true, optional = true }

ahash = { workspace = true }
anyhow = { workspace = true }
async-trait = { workspace = true }
databento = { workspace = true }
fallible-streaming-iterator = { workspace = true }
indexmap = { workspace = true }
itoa = { workspace = true }
log = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
strum = { workspace = true }
time = { workspace = true }
tokio = { workspace = true }
tokio-util = { workspace = true }
tracing = { workspace = true }
ustr = { workspace = true }

dotenvy = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }
tracing-subscriber = { workspace = true, optional = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }
rstest = { workspace = true }
tracing-test = { workspace = true }

[[bin]]
name = "databento-sandbox"
path = "bin/sandbox.rs"
required-features = ["python"]

[[bin]]
name = "databento-node-test"
path = "bin/node_test.rs"
required-features = ["live"]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 52


**Keys**: `ahash`, `all-features`, `anyhow`, `async-trait`, `crate-type`, `databento`, `default`, `description`, `dotenvy`, `extension-module`, `fallible-streaming-iterator`, `high-precision`, `indexmap`, `itoa`, `live`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-live`, `nautilus-model`, `nautilus-network`, `nautilus-system`, `nautilus-testkit`, `path`, `pyo3`, `pyo3-async-runtimes`, `python`, `readme` *(+14 more)*
**Sections**: `[bin`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/adapters/databento/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.670921Z*
