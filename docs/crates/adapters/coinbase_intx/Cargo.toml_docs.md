# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/Cargo.toml`
- **Size**: 2,554 bytes
- **Lines**: 100
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-coinbase-intx"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Coinbase International exchange integration adapter for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_coinbase_intx"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "nautilus-network/extension-module",
  "python",
  "pyo3/extension-module",
]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-model/python",
  "nautilus-network/python",
  "pyo3",
  "pyo3-async-runtimes",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-model = { workspace = true }
nautilus-network = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
async-stream = { workspace = true }
aws-lc-rs = { workspace = true }
base64 = { workspace = true }
chrono = { workspace = true }
dashmap = { workspace = true }
derive_builder = { workspace = true }
futures-util = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
reqwest = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
serde_urlencoded = { workspace = true }
strum = { workspace = true }
thiserror = { workspace = true }
tokio = { workspace = true }
tokio-tungstenite = { workspace = true }
tracing = { workspace = true }
tracing-subscriber = { workspace = true } # Needed for example binaries
ustr = { workspace = true }
uuid = { workspace = true }
zeroize = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }
rstest = { workspace = true }
tracing-test = { workspace = true }

[[bin]]
name = "coinbase-intx-http-private"
path = "bin/http_private.rs"
required-features = ["python"]

[[bin]]
name = "coinbase-intx-http-public"
path = "bin/http_public.rs"
required-features = ["python"]

[[bin]]
name = "coinbase-intx-ws"
path = "bin/websocket.rs"
required-features = ["python"]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 54


**Keys**: `ahash`, `all-features`, `anyhow`, `async-stream`, `aws-lc-rs`, `base64`, `chrono`, `crate-type`, `dashmap`, `default`, `derive_builder`, `description`, `extension-module`, `futures-util`, `indexmap`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-model`, `nautilus-network`, `nautilus-testkit`, `path`, `pyo3`, `pyo3-async-runtimes`, `python`, `readme`, `required-features`, `reqwest`, `rstest` *(+16 more)*
**Sections**: `[bin`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/adapters/coinbase_intx/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.559884Z*
