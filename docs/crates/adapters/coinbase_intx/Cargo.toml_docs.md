# Documentation: `crates/adapters/coinbase_intx/Cargo.toml`
**Generated:** 2025-11-15T19:40:00.745869Z
**File Size:** 2554 bytes
**Extension:** .toml
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `crates/adapters/coinbase_intx/Cargo.toml`
- **Size:** 2,554 bytes
- **Lines:** 99
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/coinbase_intx/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/coinbase_intx`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


