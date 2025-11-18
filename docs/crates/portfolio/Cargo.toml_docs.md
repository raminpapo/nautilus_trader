# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/portfolio/Cargo.toml`
- **Size**: 1,483 bytes
- **Lines**: 63
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-portfolio"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Portfolio components and functionality for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_portfolio"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-analysis/extension-module",
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
python = [
  "nautilus-analysis/python",
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-analysis = { workspace = true }
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }

log = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
thiserror = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
rstest = { workspace = true }

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 30


**Keys**: `all-features`, `crate-type`, `default`, `description`, `extension-module`, `log`, `name`, `nautilus-analysis`, `nautilus-common`, `nautilus-core`, `nautilus-model`, `pyo3`, `python`, `readme`, `rstest`, `rust_decimal`, `rust_decimal_macros`, `rustdoc-args`, `serde`, `serde_json`, `thiserror`, `ustr`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/portfolio/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.586391Z*
