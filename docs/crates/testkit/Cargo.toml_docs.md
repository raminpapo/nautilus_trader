# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/testkit/Cargo.toml`
- **Size**: 1,400 bytes
- **Lines**: 60
- **Language**: TOML

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 30


**Keys**: `anyhow`, `aws-lc-rs`, `axum`, `crate-type`, `default`, `description`, `extension-module`, `hex`, `high-precision`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-model`, `nautilus-network`, `pyo3`, `python`, `rand`, `readme`, `reqwest`, `rstest`, `serde_json`, `tempfile`, `tokio`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`

## Related Files

This file is located in `crates/testkit/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/testkit/Cargo.toml

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.176603Z*
