# Documentation: `crates/system/Cargo.toml`
**Generated:** 2025-11-15T19:40:03.756984Z
**File Size:** 1304 bytes
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

- **Path:** `crates/system/Cargo.toml`
- **Size:** 1,304 bytes
- **Lines:** 52
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-system"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "System orchestration for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_system"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = ["python", "pyo3/extension-module"]
python = ["pyo3"]

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
nautilus-trading = { workspace = true }

anyhow = { workspace = true }
futures = { workspace = true }
hostname = { workspace = true }
log = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
rstest = { workspace = true }
```


---

## Overview

This file is located at `crates/system/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/system`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


