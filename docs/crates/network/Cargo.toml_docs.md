# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/network/Cargo.toml`
- **Size**: 2,143 bytes
- **Lines**: 81
- **Language**: TOML

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 54


**Keys**: `ahash`, `all-features`, `anyhow`, `axum`, `bytes`, `crate-type`, `criterion`, `dashmap`, `default`, `description`, `extension-module`, `futures`, `futures-util`, `http`, `memchr`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-cryptography`, `nonzero_ext`, `proptest`, `pyo3`, `pyo3-async-runtimes`, `python`, `rand`, `readme`, `reqwest`, `rstest`, `rustdoc-args`, `rustls` *(+17 more)*
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/network/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.314681Z*
