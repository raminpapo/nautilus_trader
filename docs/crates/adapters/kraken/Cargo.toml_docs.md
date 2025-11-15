# Documentation: `crates/adapters/kraken/Cargo.toml`
**Generated:** 2025-11-15T19:40:01.113709Z
**File Size:** 2821 bytes
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

- **Path:** `crates/adapters/kraken/Cargo.toml`
- **Size:** 2,821 bytes
- **Lines:** 104
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/kraken/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


