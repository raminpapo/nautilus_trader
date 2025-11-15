# Documentation: `crates/live/Cargo.toml`
**Generated:** 2025-11-15T19:40:02.378940Z
**File Size:** 2261 bytes
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

- **Path:** `crates/live/Cargo.toml`
- **Size:** 2,261 bytes
- **Lines:** 86
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-live"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core live trading components and machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_live"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-data/extension-module",
  "nautilus-execution/extension-module",
  "nautilus-model/extension-module",
  "nautilus-portfolio/extension-module",
  "nautilus-risk/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-common/ffi", "nautilus-core/ffi", "nautilus-model/ffi"]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-data/python",
  "nautilus-execution/python",
  "nautilus-model/python",
  "nautilus-portfolio/python",
  "nautilus-risk/python",
  "nautilus-system/python",
  "pyo3",
]
defi = ["nautilus-common/defi"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-data = { workspace = true }
nautilus-execution = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-persistence = { workspace = true }
nautilus-portfolio = { workspace = true }
nautilus-risk = { workspace = true }
nautilus-system = { workspace = true }

anyhow = { workspace = true }
async-trait = { workspace = true }
log = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
rstest = { workspace = true }
rust_decimal_macros = { workspace = true }
ustr = { workspace = true }

# Run with `cargo bench -p nautilus-live --bench runner`
[[bench]]
name = "runner"
harness = false
```


---

## Overview

This file is located at `crates/live/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/live`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


