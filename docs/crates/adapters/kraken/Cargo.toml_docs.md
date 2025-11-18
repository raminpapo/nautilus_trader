# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/adapters/kraken/Cargo.toml`
- **Size**: 2,821 bytes
- **Lines**: 105
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-kraken"
readme = "README.md"
version.workspace = true
edition.workspace = true
authors.workspace = true
documentation.workspace = true
homepage.workspace = true
repository.workspace = true
license.workspace = true
description = "Kraken Pro exchange integration adapter for the Nautilus trading engine"
keywords.workspace = true
categories.workspace = true
publish = false # Do not publish to crates.io for now

[lib]
name = "nautilus_kraken"
crate-type = ["rlib", "cdylib"]

[features]
default = []
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-data/python",
  "nautilus-execution/python",
  "nautilus-model/python",
  "nautilus-network/python",
  "pyo3",
  "pyo3-async-runtimes",
]
extension-module = [
  "python",
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-data/extension-module",
  "nautilus-execution/extension-module",
  "nautilus-model/extension-module",
  "nautilus-network/extension-module",
  "pyo3/extension-module",
]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-data = { workspace = true }
nautilus-execution = { workspace = true }
nautilus-live = { workspace = true }
nautilus-model = { workspace = true }
nautilus-network = { workspace = true }
nautilus-serialization = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
arc-swap = { workspace = true }
async-stream = { workspace = true }
async-trait = { workspace = true }
aws-lc-rs = { workspace = true }
base64 = { workspace = true }
chrono = { workspace = true }
dashmap = { workspace = true }
derive_builder = { workspace = true }
futures-util = { workspace = true }
hex = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
reqwest = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
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
axum = { workspace = true }
criterion = { workspace = true }
rstest = { workspace = true }
tracing-test = { workspace = true }
url = { workspace = true }

[[bin]]
name = "kraken-http-raw"
path = "bin/http_raw.rs"

[[bin]]
name = "kraken-http-public"
path = "bin/http_public.rs"

[[bin]]
name = "kraken-ws-data"
path = "bin/ws_data.rs"

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 60


**Keys**: `ahash`, `anyhow`, `arc-swap`, `async-stream`, `async-trait`, `aws-lc-rs`, `axum`, `base64`, `chrono`, `crate-type`, `criterion`, `dashmap`, `default`, `derive_builder`, `description`, `extension-module`, `futures-util`, `hex`, `indexmap`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-execution`, `nautilus-live`, `nautilus-model`, `nautilus-network`, `nautilus-serialization`, `nautilus-testkit` *(+24 more)*
**Sections**: `[bin`, `dependencies`, `dev-dependencies`, `features`, `lib`, `package`

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
*Generated on 2025-11-18T21:55:00.142245Z*
