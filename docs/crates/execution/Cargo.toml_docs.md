# Documentation: `crates/execution/Cargo.toml`
**Generated:** 2025-11-15T19:40:02.023991Z
**File Size:** 1528 bytes
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

- **Path:** `crates/execution/Cargo.toml`
- **Size:** 1,528 bytes
- **Lines:** 62
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-execution"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core execution machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_execution"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-common/ffi", "nautilus-core/ffi", "nautilus-model/ffi"]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }

anyhow = { workspace = true }
async-trait = { workspace = true }
chrono = { workspace = true }
criterion = { workspace = true }
log = { workspace = true }
rand = { workspace = true }
rstest = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

pyo3 = { workspace = true, optional = true }
```


---

## Overview

This file is located at `crates/execution/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


