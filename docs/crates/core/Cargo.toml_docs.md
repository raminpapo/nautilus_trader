# Documentation: `crates/core/Cargo.toml`
**Generated:** 2025-11-15T19:40:01.857738Z
**File Size:** 1784 bytes
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

- **Path:** `crates/core/Cargo.toml`
- **Size:** 1,784 bytes
- **Lines:** 77
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-core"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core functionality for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_core"
crate-type = ["rlib", "staticlib"]

[features]
default = []
extension-module = ["python", "pyo3/extension-module"]
ffi = ["cbindgen"]
python = ["pyo3", "pyo3-stub-gen", "strum"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
ahash = { workspace = true }
anyhow = { workspace = true }
bytes = { workspace = true }
chrono = { workspace = true }
heck = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
rand = { workspace = true }
rmp-serde = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-stub-gen = { workspace = true, optional = true }
strum = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
iai = { workspace = true }
proptest = { workspace = true }
rstest = { workspace = true }
static_assertions = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }
toml = { workspace = true }

[[bench]]
name = "correctness"
path = "benches/correctness.rs"
harness = false

[[bench]]
name = "time"
path = "benches/time.rs"
harness = false

[[bench]]
name = "uuid"
path = "benches/uuid.rs"
harness = false
```


---

## Overview

This file is located at `crates/core/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


