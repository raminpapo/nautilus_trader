# Documentation: build.rs

## File Metadata

- **Path**: `crates/serialization/build.rs`
- **Size**: 2,718 bytes
- **Lines**: 81
- **Language**: Rust

## Original Source

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
//  https://nautechsystems.io
//
//  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
//  You may not use this file except in compliance with the License.
//  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
// -------------------------------------------------------------------------------------------------

fn main() {
    println!("cargo::rustc-check-cfg=cfg(docs_rs)");

    #[cfg(feature = "capnp")]
    {
        compile_capnp_schemas();
    }
}

#[cfg(feature = "capnp")]
fn compile_capnp_schemas() {
    use std::{env, path::PathBuf};

    // Skip schema compilation when building docs (docs.rs doesn't have capnp compiler)
    if env::var("DOCS_RS").is_ok() {
        println!("cargo:rustc-cfg=docs_rs");
        return;
    }

    let manifest_dir = env::var("CARGO_MANIFEST_DIR").expect("CARGO_MANIFEST_DIR not set");
    let manifest_path = PathBuf::from(&manifest_dir);

    // Schemas are bundled with the crate for self-contained builds
    let schema_dir = manifest_path.join("schemas/capnp");
    let out_dir = PathBuf::from(env::var("OUT_DIR").expect("OUT_DIR not set"));

    println!("cargo:rerun-if-changed={}", schema_dir.display());

    // Collect all .capnp files
    let schema_files: Vec<PathBuf> = walkdir::WalkDir::new(&schema_dir)
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| {
            e.path()
                .extension()
                .and_then(|s| s.to_str())
                .is_some_and(|s| s == "capnp")
        })
        .map(|e| e.path().to_path_buf())
        .collect();

    if schema_files.is_empty() {
        println!("cargo:warning=No Cap'n Proto schema files found");
        return;
    }

    // Compile all schema files
    let mut command = capnpc::CompilerCommand::new();
    command.src_prefix(&schema_dir).output_path(&out_dir);

    {
        let import_path = &(&schema_dir);
        command.import_path(import_path);
    }

    for file in &schema_files {
        command.file(file);
    }

    command
        .run()
        .expect("Failed to compile Cap'n Proto schemas");

    println!("Cap'n Proto schemas compiled to: {}", out_dir.display());
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`main()`**: Function defined in this file
- **`compile_capnp_schemas()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `compile_capnp_schemas`, `main`

## Related Files

This file is located in `crates/serialization/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.680830Z*
