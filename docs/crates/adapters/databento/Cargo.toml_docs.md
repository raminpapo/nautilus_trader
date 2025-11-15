# Documentation: `crates/adapters/databento/Cargo.toml`
**Generated:** 2025-11-15T19:40:00.835738Z
**File Size:** 2408 bytes
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

- **Path:** `crates/adapters/databento/Cargo.toml`
- **Size:** 2,408 bytes
- **Lines:** 89
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/databento/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


