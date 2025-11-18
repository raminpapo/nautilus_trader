# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/backtest/Cargo.toml`
- **Size**: 1,857 bytes
- **Lines**: 78
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-backtest"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Core backtesting machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_backtest"
crate-type = ["rlib", "staticlib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-execution/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = [
  "cbindgen",
  "nautilus-core/ffi",
  "nautilus-common/ffi",
  "nautilus-execution/ffi",
  "nautilus-model/ffi",
]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-execution/python",
  "nautilus-model/python",
  "pyo3",
]

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
chrono = { workspace = true }
log = { workspace = true }
rust_decimal = { workspace = true }
ustr = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
tempfile = { workspace = true }
rstest = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 38


**Keys**: `all-features`, `anyhow`, `async-trait`, `cbindgen`, `chrono`, `crate-type`, `default`, `description`, `extension-module`, `ffi`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-execution`, `nautilus-model`, `nautilus-persistence`, `nautilus-portfolio`, `nautilus-risk`, `nautilus-system`, `pyo3`, `python`, `readme`, `rstest`, `rust_decimal`, `rustdoc-args`, `tempfile`, `ustr`, `workspace`
**Sections**: `build-dependencies`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/backtest/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/backtest/Cargo.toml

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.880488Z*
