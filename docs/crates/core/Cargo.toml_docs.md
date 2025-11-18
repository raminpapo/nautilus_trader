# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/core/Cargo.toml`
- **Size**: 1,784 bytes
- **Lines**: 78
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-core"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core functionality for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_core"
crate-type = ["rlib", "staticlib"]

[features]
default = []
extension-module = ["python", "pyo3/extension-module"]
ffi = ["cbindgen"]
python = ["pyo3", "pyo3-stub-gen", "strum"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
ahash = { workspace = true }
anyhow = { workspace = true }
bytes = { workspace = true }
chrono = { workspace = true }
heck = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
rand = { workspace = true }
rmp-serde = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

pyo3 = { workspace = true, optional = true }
pyo3-stub-gen = { workspace = true, optional = true }
strum = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
iai = { workspace = true }
proptest = { workspace = true }
rstest = { workspace = true }
static_assertions = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }
toml = { workspace = true }

[[bench]]
name = "correctness"
path = "benches/correctness.rs"
harness = false

[[bench]]
name = "time"
path = "benches/time.rs"
harness = false

[[bench]]
name = "uuid"
path = "benches/uuid.rs"
harness = false

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 46


**Keys**: `ahash`, `all-features`, `anyhow`, `bytes`, `cbindgen`, `chrono`, `crate-type`, `criterion`, `default`, `description`, `extension-module`, `ffi`, `harness`, `heck`, `iai`, `indexmap`, `log`, `name`, `path`, `proptest`, `pyo3`, `pyo3-stub-gen`, `python`, `rand`, `readme`, `rmp-serde`, `rstest`, `rust_decimal`, `rustdoc-args`, `serde` *(+7 more)*
**Sections**: `[bench`, `build-dependencies`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/core/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.327936Z*
