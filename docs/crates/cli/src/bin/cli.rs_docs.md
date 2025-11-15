# Documentation: `crates/cli/src/bin/cli.rs`
**Generated:** 2025-11-15T19:40:01.616653Z
**File Size:** 1322 bytes
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

- **Path:** `crates/cli/src/bin/cli.rs`
- **Size:** 1,322 bytes
- **Lines:** 31
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

use clap::Parser;
use log::LevelFilter;
use nautilus_cli::opt::NautilusCli;

#[tokio::main]
async fn main() {
    dotenvy::dotenv().ok();
    simple_logger::SimpleLogger::new()
        .with_level(LevelFilter::Info)
        .with_module_level("sqlx", LevelFilter::Off)
        .init()
        .unwrap();
    if let Err(e) = nautilus_cli::run(NautilusCli::parse()).await {
        log::error!("Error executing Nautilus CLI: {e}");
    }
}
```


---

## Overview

This file is located at `crates/cli/src/bin/cli.rs` within the repository.

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

**Directory:** `crates/cli/src/bin`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


