# Documentation: `crates/pyo3/bin/stub_gen.rs`
**Generated:** 2025-11-15T19:40:03.396183Z
**File Size:** 1142 bytes
**Extension:** .rs
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `crates/pyo3/bin/stub_gen.rs`
- **Size:** 1,142 bytes
- **Lines:** 27
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

---

## Source Code

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

use pyo3_stub_gen::Result;

fn main() -> Result<()> {
    println!("Starting Python type stub generation...");

    let stub_info = nautilus_pyo3::stub_info()?;
    stub_info.generate()?;

    println!("Python type stub generation completed");

    Ok(())
}
```


---

## Overview

This file is located at `crates/pyo3/bin/stub_gen.rs` within the repository.

**Functions defined:** main


---

## Detailed Analysis

### Functions

#### `main()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/pyo3/bin`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


