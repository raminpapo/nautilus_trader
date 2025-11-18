# Documentation: Cargo.toml

## File Metadata

- **Path**: `crates/common/Cargo.toml`
- **Size**: 2,764 bytes
- **Lines**: 106
- **Language**: TOML

## Original Source

```toml
[package]
name = "nautilus-common"
readme = "README.md"
version.workspace = true
edition.workspace = true
rust-version.workspace = true
authors.workspace = true
license.workspace = true
description = "Common functionality and machinery for the Nautilus trading engine"
categories.workspace = true
keywords.workspace = true
documentation.workspace = true
repository.workspace = true
homepage.workspace = true

[lints]
workspace = true

[lib]
name = "nautilus_common"
crate-type = ["rlib", "staticlib"]

[features]
default = ["indicators", "rstest"]
extension-module = [
  "nautilus-core/extension-module",
  "nautilus-model/extension-module",
  "nautilus-indicators/extension-module",
  "python",
  "pyo3/extension-module",
]
ffi = ["nautilus-core/ffi", "nautilus-model/ffi", "cbindgen"]
indicators = ["nautilus-indicators"]
python = [
  "nautilus-core/python",
  "nautilus-model/python",
  "pyo3",
  "pyo3-async-runtimes",
]
defi = ["nautilus-model/defi", "alloy-primitives"]
capnp = ["nautilus-serialization/capnp"]

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--cfg", "docsrs"]

[dependencies]
nautilus-core = { workspace = true }
nautilus-indicators = { workspace = true, optional = true }
nautilus-model = { workspace = true, features = ["stubs"] }
nautilus-serialization = { workspace = true, optional = true }

ahash = { workspace = true }
anyhow = { workspace = true }
async-stream = { workspace = true }
async-trait = { workspace = true }
bytes = { workspace = true }
chrono = { workspace = true }
derive_builder = { workspace = true }
futures = { workspace = true }
indexmap = { workspace = true }
log = { workspace = true }
pyo3-stub-gen = { workspace = true }
regex = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
strum = { workspace = true }
sysinfo = { workspace = true }
thousands = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
tracing-subscriber = { workspace = true }
ustr = { workspace = true }
uuid = { workspace = true }

alloy-primitives = { workspace = true, optional = true }
pyo3 = { workspace = true, optional = true }
pyo3-async-runtimes = { workspace = true, optional = true }
rstest = { workspace = true, optional = true }

[dev-dependencies]
capnp = { workspace = true }
criterion = { workspace = true }
proptest = { workspace = true }
rand = { workspace = true }
regex = { workspace = true }
tempfile = { workspace = true }

[build-dependencies]
cbindgen = { workspace = true, optional = true }

[[bench]]
name = "cache_orders"
path = "benches/cache/orders.rs"
harness = false

[[bench]]
name = "matching"
path = "benches/matching.rs"
harness = false

[[bench]]
name = "cache_query_sets"
path = "benches/cache/query_sets.rs"
harness = false

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a TOML configuration file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 60


**Keys**: `ahash`, `all-features`, `alloy-primitives`, `anyhow`, `async-stream`, `async-trait`, `bytes`, `capnp`, `cbindgen`, `chrono`, `crate-type`, `criterion`, `default`, `defi`, `derive_builder`, `description`, `extension-module`, `ffi`, `futures`, `harness`, `indexmap`, `indicators`, `log`, `name`, `nautilus-core`, `nautilus-indicators`, `nautilus-model`, `nautilus-serialization`, `path`, `proptest` *(+21 more)*
**Sections**: `[bench`, `build-dependencies`, `dependencies`, `dev-dependencies`, `features`, `lib`, `lints`, `package`, `package.metadata.docs.rs`

## Related Files

This file is located in `crates/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.947576Z*
