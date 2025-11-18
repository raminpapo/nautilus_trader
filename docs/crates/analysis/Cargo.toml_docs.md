# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/analysis/Cargo.toml`
- **Size**: 1,102 bytes
- **Lines**: 48
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-analysis"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Performance analysis and statistics for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_analysis"
crate-type = ["rlib", "staticlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
python = ["nautilus-core/python", "nautilus-model/python", "pyo3"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }

anyhow = { workspace = true }
rust_decimal = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
rstest = { workspace = true }

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 23


**Keys**: `all-features`, `anyhow`, `crate-type`, `default`, `description`, `extension-module`, `name`, `nautilus-core`, `nautilus-model`, `pyo3`, `python`, `readme`, `rstest`, `rust_decimal`, `rustdoc-args`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/analysis/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.773249Z*
