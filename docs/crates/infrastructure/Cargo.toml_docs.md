# Documentation: `crates/infrastructure/Cargo.toml`
**Generated:** 2025-11-15T19:40:02.297404Z
**File Size:** 2166 bytes
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

- **Path:** `crates/infrastructure/Cargo.toml`
- **Size:** 2,166 bytes
- **Lines:** 81
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/infrastructure/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/infrastructure`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


