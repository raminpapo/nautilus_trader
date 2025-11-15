# Documentation: `crates/serialization/Cargo.toml`
**Generated:** 2025-11-15T19:40:03.426766Z
**File Size:** 1709 bytes
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

- **Path:** `crates/serialization/Cargo.toml`
- **Size:** 1,709 bytes
- **Lines:** 71
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-serialization"
readme = "README.md"
build = "build.rs"
include = [
  "src/**/*",
  "schemas/**/*",
  "generated/**/*",
  "build.rs",
  "Cargo.toml",
  "README.md",
]
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Serialization functionality for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_serialization"
crate-type = ["rlib", "staticlib", "cdylib"]

[features]
default = []
capnp = ["dep:capnp"]
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
python = ["nautilus-core/python", "nautilus-model/python", "pyo3"]
high-precision = ["nautilus-model/high-precision"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }

arrow = { workspace = true }
indexmap = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
thiserror = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

capnp = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }

[build-dependencies]
capnpc = { workspace = true }
walkdir = { workspace = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }
pretty_assertions = { workspace = true }
rstest = { workspace = true }
```


---

## Overview

This file is located at `crates/serialization/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/serialization`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


