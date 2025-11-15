# Documentation: `crates/backtest/Cargo.toml`
**Generated:** 2025-11-15T19:40:01.584112Z
**File Size:** 1857 bytes
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

- **Path:** `crates/backtest/Cargo.toml`
- **Size:** 1,857 bytes
- **Lines:** 77
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-backtest"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core backtesting machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_backtest"
crate-type = ["rlib", "staticlib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-execution/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = [
  "cbindgen",
  "nautilus-core/ffi",
  "nautilus-common/ffi",
  "nautilus-execution/ffi",
  "nautilus-model/ffi",
]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-execution/python",
  "nautilus-model/python",
  "pyo3",
]

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
chrono = { workspace = true }
log = { workspace = true }
rust_decimal = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
tempfile = { workspace = true }
rstest = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }
```


---

## Overview

This file is located at `crates/backtest/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


