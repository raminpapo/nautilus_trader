# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/cryptography/Cargo.toml`
- **Size**: 1,268 bytes
- **Lines**: 55
- **Language**: TOML

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Keys**: `all-features`, `anyhow`, `aws-lc-rs`, `base64`, `crate-type`, `criterion`, `default`, `description`, `ed25519-dalek`, `extension-module`, `hex`, `name`, `nautilus-core`, `pem`, `pyo3`, `python`, `rand`, `readme`, `rstest`, `rustdoc-args`, `rustls`, `tracing`, `webpki-roots`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/cryptography/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:01.454029Z*
