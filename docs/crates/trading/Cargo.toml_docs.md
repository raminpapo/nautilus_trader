# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/trading/Cargo.toml`
- **Size**: 1,603 bytes
- **Lines**: 67
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-trading"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Strategy machinery and controllers for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_trading"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-common/extension-module",
  "nautilus-core/extension-module",
  "nautilus-data/extension-module",
  "nautilus-execution/extension-module",
  "nautilus-model/extension-module",
  "python",
  "pyo3/extension-module",
]
python = [
  "nautilus-common/python",
  "nautilus-core/python",
  "nautilus-data/python",
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
nautilus-portfolio = { workspace = true }
nautilus-risk = { workspace = true }

anyhow = { workspace = true }
chrono = { workspace = true }
chrono-tz = { workspace = true }
log = { workspace = true }
strum = { workspace = true }
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

Total unique keywords extracted: 32


**Keys**: `all-features`, `anyhow`, `chrono`, `chrono-tz`, `crate-type`, `default`, `description`, `extension-module`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-execution`, `nautilus-model`, `nautilus-portfolio`, `nautilus-risk`, `pyo3`, `python`, `readme`, `rstest`, `rustdoc-args`, `strum`, `ustr`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/trading/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.189616Z*
