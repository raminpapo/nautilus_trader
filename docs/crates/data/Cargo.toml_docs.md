# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/data/Cargo.toml`
- **Size**: 1,748 bytes
- **Lines**: 72
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-data"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core data handling machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_data"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "nautilus-persistence/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = [
  "nautilus-common/ffi",
  "nautilus-core/ffi",
  "nautilus-model/ffi",
  "nautilus-persistence/ffi",
]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-model/python",
  "nautilus-persistence/python",
  "pyo3",
]
high-precision = ["nautilus-model/high-precision"]
defi = ["nautilus-common/defi", "nautilus-model/defi", "alloy-primitives"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-persistence = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
async-trait = { workspace = true }
chrono = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
ustr = { workspace = true }

alloy-primitives = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }

[dev-dependencies]
rstest = { workspace = true }

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 34


**Keys**: `ahash`, `all-features`, `alloy-primitives`, `anyhow`, `async-trait`, `chrono`, `crate-type`, `default`, `defi`, `description`, `extension-module`, `ffi`, `high-precision`, `indexmap`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-model`, `nautilus-persistence`, `pyo3`, `python`, `readme`, `rstest`, `rustdoc-args`, `ustr`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/data/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.473871Z*
