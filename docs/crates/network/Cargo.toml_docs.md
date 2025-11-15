# Documentation: `crates/network/Cargo.toml`
**Generated:** 2025-11-15T19:40:03.189153Z
**File Size:** 2143 bytes
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

- **Path:** `crates/network/Cargo.toml`
- **Size:** 2,143 bytes
- **Lines:** 80
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-network"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Network communication machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_network"
crate-type = ["rlib", "staticlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "python",
  "pyo3/extension-module",
]
python = ["nautilus-core/python", "pyo3", "pyo3-async-runtimes"]
turmoil = ["dep:turmoil"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }
nautilus-cryptography = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
bytes = { workspace = true }
dashmap = { workspace = true }
futures = { workspace = true }
futures-util = { workspace = true }
http = { workspace = true }
memchr = { workspace = true }
nonzero_ext = { workspace = true }
rand = { workspace = true }
reqwest = { workspace = true }
rustls = { workspace = true }
serde = { workspace = true }
serde_urlencoded = { workspace = true }
rustls-pemfile = { workspace = true }
strum = { workspace = true }
thiserror = { workspace = true }
tokio = { workspace = true }
tokio-rustls = { workspace = true }
tokio-tungstenite = { workspace = true }
tokio-util = { workspace = true }
tracing = { workspace = true }
url = { workspace = true }
ustr = { workspace = true }
webpki-roots = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }
turmoil = { workspace = true, optional = true }

[dev-dependencies]
nautilus-common = { workspace = true }

axum = { workspace = true }
criterion = { workspace = true }
proptest = { workspace = true }
rstest = { workspace = true }
serde_json = { workspace = true }
tracing-test = { workspace = true }
turmoil = { workspace = true }
```


---

## Overview

This file is located at `crates/network/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/network`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


