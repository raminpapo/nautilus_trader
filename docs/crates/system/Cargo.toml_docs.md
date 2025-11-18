# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/system/Cargo.toml`
- **Size**: 1,304 bytes
- **Lines**: 53
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-system"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "System orchestration for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_system"
crate-type = ["rlib", "cdylib"]

[features]
default = []
extension-module = ["python", "pyo3/extension-module"]
python = ["pyo3"]

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
nautilus-trading = { workspace = true }

anyhow = { workspace = true }
futures = { workspace = true }
hostname = { workspace = true }
log = { workspace = true }
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

Total unique keywords extracted: 33


**Keys**: `all-features`, `anyhow`, `crate-type`, `default`, `description`, `extension-module`, `futures`, `hostname`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-data`, `nautilus-execution`, `nautilus-model`, `nautilus-persistence`, `nautilus-portfolio`, `nautilus-risk`, `nautilus-trading`, `pyo3`, `python`, `readme`, `rstest`, `rustdoc-args`, `ustr`, `workspace`
**Sections**: `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/system/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.152277Z*
