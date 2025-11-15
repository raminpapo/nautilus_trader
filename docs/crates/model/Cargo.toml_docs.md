# Documentation: `crates/model/Cargo.toml`
**Generated:** 2025-11-15T19:40:02.421252Z
**File Size:** 2340 bytes
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

- **Path:** `crates/model/Cargo.toml`
- **Size:** 2,340 bytes
- **Lines:** 92
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-model"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Domain model for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_model"
crate-type = ["rlib", "staticlib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["cbindgen", "nautilus-core/ffi"]
python = ["nautilus-core/python", "pyo3", "pyo3-stub-gen"]
stubs = ["rstest"]
high-precision = []
# DeFi domain model requires 18-decimal wei precision, implying `high-precision`
defi = ["alloy-primitives", "high-precision"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
chrono = { workspace = true }
derive_builder = { workspace = true }
enum_dispatch = { workspace = true }
evalexpr = { workspace = true }
hex = { workspace = true }
implied-vol = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
strum = { workspace = true }
tabled = { workspace = true }
thiserror = { workspace = true }
thousands = { workspace = true }
ustr = { workspace = true }
tracing = { workspace = true }

alloy-primitives = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }
pyo3-stub-gen = { workspace = true, optional = true }
rstest = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
iai = { workspace = true }
proptest = { workspace = true }
rstest = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }

[[bench]]
name = "book_iai"
path = "benches/book_iai.rs"
harness = false

[[bench]]
name = "fixed_precision_criterion"
path = "benches/fixed_precision_criterion.rs"
harness = false

[[bench]]
name = "fixed_precision_iai"
path = "benches/fixed_precision_iai.rs"
harness = false
```


---

## Overview

This file is located at `crates/model/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


