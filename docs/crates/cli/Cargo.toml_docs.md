# Documentation: `crates/cli/Cargo.toml`
**Generated:** 2025-11-15T19:40:01.612707Z
**File Size:** 1197 bytes
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

- **Path:** `crates/cli/Cargo.toml`
- **Size:** 1,197 bytes
- **Lines:** 51
- **Extension:** `.toml`
- **Type:** text

---

## Source Code

```toml
[package]
name = "nautilus-cli"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Command-line interface for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[features]
default = []
defi = [
  "dep:alloy-primitives",
  "dep:nautilus-blockchain",
  "nautilus-model/defi",
]

[dependencies]
nautilus-infrastructure = { workspace = true, features = ["postgres"] }
nautilus-model = { workspace = true }
nautilus-blockchain = { workspace = true, features = [
  "hypersync",
], optional = true }

anyhow = { workspace = true }
clap = { workspace = true }
dotenvy = { workspace = true }
futures-util = { workspace = true }
log = { workspace = true }
simple_logger = { workspace = true }
tokio = { workspace = true }
tokio-util = { workspace = true }

alloy-primitives = { workspace = true, optional = true }

[[bin]]
name = "nautilus"
path = "src/bin/cli.rs"
```


---

## Overview

This file is located at `crates/cli/Cargo.toml` within the repository.

This is a Rust package configuration file managed by Cargo.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cli`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


