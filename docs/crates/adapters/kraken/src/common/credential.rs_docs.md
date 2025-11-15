# Documentation: `crates/adapters/kraken/src/common/credential.rs`
**Generated:** 2025-11-15T19:40:01.124350Z
**File Size:** 3397 bytes
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

- **Path:** `crates/adapters/kraken/src/common/credential.rs`
- **Size:** 3,397 bytes
- **Lines:** 97
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 4

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

//! Request signing and authentication credentials for the Kraken API.

use std::collections::HashMap;

use aws_lc_rs::{digest, hmac};
use base64::{Engine, engine::general_purpose::STANDARD};
use serde_urlencoded;
use zeroize::{Zeroize, ZeroizeOnDrop};

#[derive(Clone, Debug, Zeroize, ZeroizeOnDrop)]
pub struct KrakenCredential {
    api_key: String,
    api_secret: String,
}

impl KrakenCredential {
    pub fn new(api_key: impl Into<String>, api_secret: impl Into<String>) -> Self {
        Self {
            api_key: api_key.into(),
            api_secret: api_secret.into(),
        }
    }

    pub fn api_key(&self) -> &str {
        &self.api_key
    }

    /// Sign a request for Kraken REST API.
    ///
    /// Kraken uses HMAC-SHA512 with the following message:
    /// - path + SHA256(nonce + POST data)
    /// - The secret is base64 decoded before signing
    pub fn sign_request(
        &self,
        path: &str,
        nonce: u64,
        params: &HashMap<String, String>,
    ) -> anyhow::Result<(String, String)> {
        // Decode the secret from base64
        let secret = STANDARD
            .decode(&self.api_secret)
            .map_err(|e| anyhow::anyhow!("Failed to decode API secret: {e}"))?;

        // Create POST data string
        let mut post_data = format!("nonce={nonce}");
        if !params.is_empty() {
            let encoded = serde_urlencoded::to_string(params)
                .map_err(|e| anyhow::anyhow!("Failed to encode params: {e}"))?;
            post_data.push('&');
            post_data.push_str(&encoded);
        }

        // Hash the nonce + POST data with SHA256
        let hash = digest::digest(&digest::SHA256, post_data.as_bytes());

        // Concatenate path + hash
        let mut message = path.as_bytes().to_vec();
        message.extend_from_slice(hash.as_ref());

        // Sign with HMAC-SHA512
        let key = hmac::Key::new(hmac::HMAC_SHA512, &secret);
        let signature = hmac::sign(&key, &message);

        // Encode signature as base64 and return with post_data
        Ok((STANDARD.encode(signature.as_ref()), post_data))
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_credential_creation() {
        let cred = KrakenCredential::new("test_key", "test_secret");
        assert_eq!(cred.api_key(), "test_key");
    }
}
```


---

## Overview

This file is located at `crates/adapters/kraken/src/common/credential.rs` within the repository.

**Classes defined:** KrakenCredential, KrakenCredential, Into, Into

**Functions defined:** new, api_key, sign_request, test_credential_creation


---

## Detailed Analysis

### Classes

#### `KrakenCredential`

**Type:** struct


#### `KrakenCredential`

**Type:** impl


#### `Into`

**Type:** impl


#### `Into`

**Type:** impl


### Functions

#### `new(api_key: impl Into<String>, api_secret: impl Into<String>)`


#### `api_key(&self)`


#### `sign_request(
        &self,
        path: &str,
        nonce: u64,
        params: &HashMap<String, String>,
    )`


#### `test_credential_creation()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key, credential, auth. Ensure proper handling of secrets.


