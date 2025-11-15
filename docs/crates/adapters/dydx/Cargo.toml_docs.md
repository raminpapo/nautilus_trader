# Documentation: `crates/adapters/dydx/Cargo.toml`
**Generated:** 2025-11-15T19:40:00.893163Z
**File Size:** 2561 bytes
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

- **Path:** `crates/adapters/dydx/Cargo.toml`
- **Size:** 2,561 bytes
- **Lines:** 95
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-dydx"
readme = "README.md"
publish = false # Do not publish to crates.io for now
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "dYdX v4 exchange integration adapter for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_dydx"
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
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-data/python",
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
nautilus-data = { workspace = true }
nautilus-execution = { workspace = true }
nautilus-live = { workspace = true }
nautilus-model = { workspace = true }
nautilus-network = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
arc-swap = { workspace = true }
async-trait = { workspace = true }
bip32 = { workspace = true }
chrono = { workspace = true }
cosmrs = { workspace = true }
dashmap = { workspace = true }
derive_builder = { workspace = true }
hex = { workspace = true }
prost = { workspace = true }
prost-types = { workspace = true }
rand = { workspace = true }
reqwest = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
serde_with = { workspace = true }
strum = { workspace = true }
thiserror = { workspace = true }
tokio = { workspace = true }
tokio-tungstenite = { workspace = true }
tokio-util = { workspace = true }
tonic = { workspace = true }
tracing = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }
axum = { workspace = true }
criterion = { workspace = true }
rstest = { workspace = true }
rust_decimal_macros = { workspace = true }
tracing-test = { workspace = true }
url = { workspace = true }
```


---

## Overview

This file is located at `crates/adapters/dydx/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


