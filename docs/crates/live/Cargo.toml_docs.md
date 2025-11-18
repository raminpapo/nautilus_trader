# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/live/Cargo.toml`
- **Size**: 2,261 bytes
- **Lines**: 87
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-live"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core live trading components and machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_live"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-data/extension-module",
  "nautilus-execution/extension-module",
  "nautilus-model/extension-module",
  "nautilus-portfolio/extension-module",
  "nautilus-risk/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-common/ffi", "nautilus-core/ffi", "nautilus-model/ffi"]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-data/python",
  "nautilus-execution/python",
  "nautilus-model/python",
  "nautilus-portfolio/python",
  "nautilus-risk/python",
  "nautilus-system/python",
  "pyo3",
]
defi = ["nautilus-common/defi"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true }
nautilus-data = { workspace = true }
nautilus-execution = { workspace = true }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-persistence = { workspace = true }
nautilus-portfolio = { workspace = true }
nautilus-risk = { workspace = true }
nautilus-system = { workspace = true }

anyhow = { workspace = true }
async-trait = { workspace = true }
log = { workspace = true }
rust_decimal = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
criterion = { workspace = true }
rstest = { workspace = true }
rust_decimal_macros = { workspace = true }
ustr = { workspace = true }

# Run with `cargo bench -p nautilus-live --bench runner`
[[bench]]
name = "runner"
harness = false

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 43


**Keys**: `all-features`, `anyhow`, `async-trait`, `crate-type`, `criterion`, `default`, `defi`, `description`, `extension-module`, `ffi`, `harness`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-execution`, `nautilus-model`, `nautilus-persistence`, `nautilus-portfolio`, `nautilus-risk`, `nautilus-system`, `pyo3`, `python`, `readme`, `rstest`, `rust_decimal`, `rust_decimal_macros`, `rustdoc-args`, `serde` *(+5 more)*
**Sections**: `[bench`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/live/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.093805Z*
