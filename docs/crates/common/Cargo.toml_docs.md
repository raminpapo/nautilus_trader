# Documentation: `crates/common/Cargo.toml`
**Generated:** 2025-11-15T19:40:01.626537Z
**File Size:** 2764 bytes
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

- **Path:** `crates/common/Cargo.toml`
- **Size:** 2,764 bytes
- **Lines:** 105
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-common"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Common functionality and machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_common"
crate-type = ["rlib", "staticlib"]

[features]
default = ["indicators", "rstest"]
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "nautilus-indicators/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-core/ffi", "nautilus-model/ffi", "cbindgen"]
indicators = ["nautilus-indicators"]
python = [
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
  "pyo3-async-runtimes",
]
defi = ["nautilus-model/defi", "alloy-primitives"]
capnp = ["nautilus-serialization/capnp"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }
nautilus-indicators = { workspace = true, optional = true }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-serialization = { workspace = true, optional = true }

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
pyo3-stub-gen = { workspace = true }
regex = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
strum = { workspace = true }
sysinfo = { workspace = true }
thousands = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
tracing-subscriber = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

alloy-primitives = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }
rstest = { workspace = true, optional = true }

[dev-dependencies]
capnp = { workspace = true }
criterion = { workspace = true }
proptest = { workspace = true }
rand = { workspace = true }
regex = { workspace = true }
tempfile = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }

[[bench]]
name = "cache_orders"
path = "benches/cache/orders.rs"
harness = false

[[bench]]
name = "matching"
path = "benches/matching.rs"
harness = false

[[bench]]
name = "cache_query_sets"
path = "benches/cache/query_sets.rs"
harness = false
```


---

## Overview

This file is located at `crates/common/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


