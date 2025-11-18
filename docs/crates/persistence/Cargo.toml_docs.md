# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/persistence/Cargo.toml`
- **Size**: 2,402 bytes
- **Lines**: 99
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-persistence"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Data persistence and storage for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_persistence"
crate-type = ["rlib", "staticlib", "cdylib"]

[features]
default = []
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "nautilus-serialization/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-core/ffi", "nautilus-model/ffi"]
python = [
  "nautilus-core/ffi",
  "nautilus-core/python",
  "nautilus-model/python",
  "nautilus-serialization/python",
  "pyo3",
]
high-precision = [
  "nautilus-model/high-precision",
  "nautilus-serialization/high-precision",
]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-common = { workspace = true }
nautilus-core = { workspace = true, features = ["ffi"] }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-serialization = { workspace = true }

anyhow = { workspace = true }
arrow = { workspace = true }
binary-heap-plus = { workspace = true }
chrono = { workspace = true }
compare = { workspace = true }
datafusion = { workspace = true }
futures = { workspace = true }
heck = { workspace = true }
itertools = { workspace = true }
log = { workspace = true }
object_store = { workspace = true }
parquet = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true }
unbounded-interval-tree = { workspace = true }
url = { workspace = true }

pyo3 = { workspace = true, optional = true }

[dev-dependencies]
nautilus-testkit = { workspace = true }

criterion = { workspace = true }
pretty_assertions = { workspace = true }
proptest = { workspace = true }
rand = { workspace = true }
rstest = { workspace = true }
tempfile = { workspace = true }

[[bench]]
name = "persistence"
path = "benches/persistence.rs"
harness = false

[[bin]]
name = "to_json"
path = "bin/to_json.rs"
required-features = ["python"]

[[bin]]
name = "to_parquet"
path = "bin/to_parquet.rs"
required-features = ["python"]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 53


**Keys**: `all-features`, `anyhow`, `arrow`, `binary-heap-plus`, `chrono`, `compare`, `crate-type`, `criterion`, `datafusion`, `default`, `description`, `extension-module`, `ffi`, `futures`, `harness`, `heck`, `high-precision`, `itertools`, `log`, `name`, `nautilus-common`, `nautilus-core`, `nautilus-model`, `nautilus-serialization`, `nautilus-testkit`, `object_store`, `parquet`, `path`, `pretty_assertions`, `proptest` *(+14 more)*
**Sections**: `[bench`, `[bin`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/persistence/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.489506Z*
