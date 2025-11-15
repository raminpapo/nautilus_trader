# Documentation: `crates/adapters/blockchain/Cargo.toml`
**Generated:** 2025-11-15T19:40:00.431919Z
**File Size:** 2744 bytes
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

- **Path:** `crates/adapters/blockchain/Cargo.toml`
- **Size:** 2,744 bytes
- **Lines:** 96
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/blockchain/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


