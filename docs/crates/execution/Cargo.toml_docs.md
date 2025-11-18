# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/execution/Cargo.toml`
- **Size**: 1,528 bytes
- **Lines**: 63
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-execution"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core execution machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_execution"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-common/ffi", "nautilus-core/ffi", "nautilus-model/ffi"]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }

anyhow = { workspace = true }
async-trait = { workspace = true }
chrono = { workspace = true }
criterion = { workspace = true }
log = { workspace = true }
rand = { workspace = true }
rstest = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

pyo3 = { workspace = true, optional = true }

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 33


**Keys**: `all-features`, `anyhow`, `async-trait`, `chrono`, `crate-type`, `criterion`, `default`, `description`, `extension-module`, `ffi`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-model`, `pyo3`, `python`, `rand`, `readme`, `rstest`, `rust_decimal`, `rust_decimal_macros`, `rustdoc-args`, `serde`, `ustr`, `uuid`, `workspace`
**Sections**: `dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/execution/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.569529Z*
