# Documentation: `crates/network/benches/test_client.rs`
**Generated:** 2025-11-15T19:40:03.194262Z
**File Size:** 1663 bytes
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

- **Path:** `crates/network/benches/test_client.rs`
- **Size:** 1,663 bytes
- **Lines:** 45
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

use nautilus_network::http::InnerHttpClient;
use reqwest::Method;

const CONCURRENCY: usize = 256;
const TOTAL: usize = 1_000_000;

#[tokio::main]
async fn main() {
    let client = InnerHttpClient::default();
    let mut reqs = Vec::new();
    for _ in 0..(TOTAL / CONCURRENCY) {
        for _ in 0..CONCURRENCY {
            reqs.push(client.send_request(
                Method::GET,
                "http://127.0.0.1:3000".to_string(),
                None,
                None,
                None,
                None,
            ));
        }

        let resp = futures::future::join_all(reqs.drain(0..)).await;
        assert!(resp.iter().all(|res| if let Ok(resp) = res {
            resp.status.is_success()
        } else {
            false
        }));
    }
}
```


---

## Overview

This file is located at `crates/network/benches/test_client.rs` within the repository.

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


