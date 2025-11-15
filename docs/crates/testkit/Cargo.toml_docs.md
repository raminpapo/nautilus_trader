# Documentation: `crates/testkit/Cargo.toml`
**Generated:** 2025-11-15T19:40:03.776526Z
**File Size:** 1400 bytes
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

- **Path:** `crates/testkit/Cargo.toml`
- **Size:** 1,400 bytes
- **Lines:** 59
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-testkit"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Testing utilities for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_testkit"
crate-type = ["rlib", "staticlib"]

[features]
default = []
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
]
high-precision = ["nautilus-model/high-precision"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-network = { workspace = true }

anyhow = { workspace = true }
aws-lc-rs = { workspace = true }
hex = { workspace = true }
rand = { workspace = true }
reqwest = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
axum = { workspace = true }
rstest = { workspace = true }
tempfile = { workspace = true }
```


---

## Overview

This file is located at `crates/testkit/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/testkit`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


