# Documentation: `crates/persistence/Cargo.toml`
**Generated:** 2025-11-15T19:40:03.299418Z
**File Size:** 2402 bytes
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

- **Path:** `crates/persistence/Cargo.toml`
- **Size:** 2,402 bytes
- **Lines:** 98
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-persistence"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Data persistence and storage for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_persistence"
crate-type = ["rlib", "staticlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "nautilus-serialization/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-core/ffi", "nautilus-model/ffi"]
python = [
  "nautilus-core/ffi",
  "nautilus-core/python",
  "nautilus-model/python",
  "nautilus-serialization/python",
  "pyo3",
]
high-precision = [
  "nautilus-model/high-precision",
  "nautilus-serialization/high-precision",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true, features = ["ffi"] }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-serialization = { workspace = true }

anyhow = { workspace = true }
arrow = { workspace = true }
binary-heap-plus = { workspace = true }
chrono = { workspace = true }
compare = { workspace = true }
datafusion = { workspace = true }
futures = { workspace = true }
heck = { workspace = true }
itertools = { workspace = true }
log = { workspace = true }
object_store = { workspace = true }
parquet = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true }
unbounded-interval-tree = { workspace = true }
url = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }

criterion = { workspace = true }
pretty_assertions = { workspace = true }
proptest = { workspace = true }
rand = { workspace = true }
rstest = { workspace = true }
tempfile = { workspace = true }

[[bench]]
name = "persistence"
path = "benches/persistence.rs"
harness = false

[[bin]]
name = "to_json"
path = "bin/to_json.rs"
required-features = ["python"]

[[bin]]
name = "to_parquet"
path = "bin/to_parquet.rs"
required-features = ["python"]
```


---

## Overview

This file is located at `crates/persistence/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/persistence`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


