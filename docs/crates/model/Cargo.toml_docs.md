# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/model/Cargo.toml`
- **Size**: 2,340 bytes
- **Lines**: 93
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-model"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Domain model for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_model"
crate-type = ["rlib", "staticlib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["cbindgen", "nautilus-core/ffi"]
python = ["nautilus-core/python", "pyo3", "pyo3-stub-gen"]
stubs = ["rstest"]
high-precision = []
# DeFi domain model requires 18-decimal wei precision, implying `high-precision`
defi = ["alloy-primitives", "high-precision"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }

ahash = { workspace = true }
anyhow = { workspace = true }
chrono = { workspace = true }
derive_builder = { workspace = true }
enum_dispatch = { workspace = true }
evalexpr = { workspace = true }
hex = { workspace = true }
implied-vol = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
rust_decimal = { workspace = true }
rust_decimal_macros = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
strum = { workspace = true }
tabled = { workspace = true }
thiserror = { workspace = true }
thousands = { workspace = true }
ustr = { workspace = true }
tracing = { workspace = true }

alloy-primitives = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }
pyo3-stub-gen = { workspace = true, optional = true }
rstest = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
iai = { workspace = true }
proptest = { workspace = true }
rstest = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }

[[bench]]
name = "book_iai"
path = "benches/book_iai.rs"
harness = false

[[bench]]
name = "fixed_precision_criterion"
path = "benches/fixed_precision_criterion.rs"
harness = false

[[bench]]
name = "fixed_precision_iai"
path = "benches/fixed_precision_iai.rs"
harness = false

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 54


**Keys**: `ahash`, `all-features`, `alloy-primitives`, `anyhow`, `cbindgen`, `chrono`, `crate-type`, `criterion`, `default`, `defi`, `derive_builder`, `description`, `enum_dispatch`, `evalexpr`, `extension-module`, `ffi`, `harness`, `hex`, `high-precision`, `iai`, `implied-vol`, `indexmap`, `log`, `name`, `nautilus-core`, `path`, `proptest`, `pyo3`, `pyo3-stub-gen`, `python` *(+15 more)*
**Sections**: `[bench`, `build-dependencies`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/model/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.154562Z*
