# Documentation: `crates/adapters/bybit/Cargo.toml`
**Generated:** 2025-11-15T19:40:00.595564Z
**File Size:** 2789 bytes
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

- **Path:** `crates/adapters/bybit/Cargo.toml`
- **Size:** 2,789 bytes
- **Lines:** 104
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/bybit/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


