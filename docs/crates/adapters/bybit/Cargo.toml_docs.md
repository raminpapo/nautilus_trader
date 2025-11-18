# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/adapters/bybit/Cargo.toml`
- **Size**: 2,789 bytes
- **Lines**: 105
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-bybit"
readme = "README.md"
publish = false # Do not publish to crates.io for now
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Bybit exchange integration adapter for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_bybit"
crate-type = ["rlib", "cdylib"]

[features]
default = []
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-data/python",
  "nautilus-model/python",
  "nautilus-network/python",
  "pyo3",
  "pyo3-async-runtimes",
]
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-data/extension-module",
  "nautilus-model/extension-module",
  "nautilus-network/extension-module",
  "python",
  "pyo3/extension-module",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-data = { workspace = true }
nautilus-execution = { workspace = true }
nautilus-model = { workspace = true }
nautilus-network = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
arc-swap = { workspace = true }
async-stream = { workspace = true }
async-trait = { workspace = true }
aws-lc-rs = { workspace = true }
chrono = { workspace = true }
dashmap = { workspace = true }
derive_builder = { workspace = true }
futures-util = { workspace = true }
hex = { workspace = true }
reqwest = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
serde_repr = { workspace = true }
serde_urlencoded = { workspace = true }
strum = { workspace = true }
thiserror = { workspace = true }
tokio = { workspace = true }
tokio-tungstenite = { workspace = true }
tokio-util = { workspace = true }
tracing = { workspace = true }
tracing-subscriber = { workspace = true }
ustr = { workspace = true }
zeroize = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }
criterion = { workspace = true }
rstest = { workspace = true }
rust_decimal_macros = { workspace = true }
tracing-test = { workspace = true }
url = { workspace = true }
axum = { workspace = true }

# Run with `cargo run -p nautilus-bybit --bin bybit-http`.
[[bin]]
name = "bybit-http"
path = "bin/http.rs"

# Run with `cargo run -p nautilus-bybit --bin bybit-ws-data`.
[[bin]]
name = "bybit-ws-data"
path = "bin/ws_data.rs"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 61


**Keys**: `ahash`, `all-features`, `anyhow`, `arc-swap`, `async-stream`, `async-trait`, `aws-lc-rs`, `axum`, `chrono`, `crate-type`, `criterion`, `dashmap`, `default`, `derive_builder`, `description`, `extension-module`, `futures-util`, `hex`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-execution`, `nautilus-model`, `nautilus-network`, `nautilus-testkit`, `path`, `publish`, `pyo3`, `pyo3-async-runtimes` *(+23 more)*
**Sections**: `[bin`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/adapters/bybit/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.344053Z*
