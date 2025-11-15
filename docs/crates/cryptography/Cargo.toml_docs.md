# Documentation: `crates/cryptography/Cargo.toml`
**Generated:** 2025-11-15T19:40:01.949551Z
**File Size:** 1268 bytes
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

- **Path:** `crates/cryptography/Cargo.toml`
- **Size:** 1,268 bytes
- **Lines:** 54
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-cryptography"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Cryptographic primitives and management for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_cryptography"
crate-type = ["rlib", "staticlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "python",
  "pyo3/extension-module",
]
python = ["nautilus-core/python", "pyo3"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }

anyhow = { workspace = true }
aws-lc-rs = { workspace = true }
base64 = { workspace = true }
ed25519-dalek = { workspace = true }
hex = { workspace = true }
pem = { workspace = true }
rand = { workspace = true }
rustls = { workspace = true }
tracing = { workspace = true }
webpki-roots = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
rstest = { workspace = true }
```


---

## Overview

This file is located at `crates/cryptography/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cryptography`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


