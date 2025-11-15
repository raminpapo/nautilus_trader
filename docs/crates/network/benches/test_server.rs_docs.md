# Documentation: `crates/network/benches/test_server.rs`
**Generated:** 2025-11-15T19:40:03.195598Z
**File Size:** 1374 bytes
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

- **Path:** `crates/network/benches/test_server.rs`
- **Size:** 1,374 bytes
- **Lines:** 33
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

use axum::{Router, routing::get};

#[tokio::main]
async fn main() {
    // Construct our SocketAddr to listen on...
    let router = Router::new().route("/", get(|| async { "Hello World" }));

    // Create a listener and serve...
    let listener = tokio::net::TcpListener::bind("127.0.0.1:3000")
        .await
        .unwrap();
    let server = axum::serve(listener, router);

    // And run forever...
    if let Err(e) = server.await {
        eprintln!("server error: {e}");
    }
}
```


---

## Overview

This file is located at `crates/network/benches/test_server.rs` within the repository.

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

**Directory:** `crates/network/benches`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


