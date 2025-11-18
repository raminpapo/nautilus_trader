# Documentation: test_client.rs

## File Metadata

- **Path**: `crates/network/benches/test_client.rs`
- **Size**: 1,663 bytes
- **Lines**: 46
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`main()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `main`

## Related Files

This file is located in `crates/network/benches/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/network/benches/test_client.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:03.324801Z*
