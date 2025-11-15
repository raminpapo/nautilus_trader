# Documentation: `crates/model/src/macros.rs`
**Generated:** 2025-11-15T19:40:02.825450Z
**File Size:** 1595 bytes
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

- **Path:** `crates/model/src/macros.rs`
- **Size:** 1,595 bytes
- **Lines:** 40
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 2

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

//! Model specific macros.

#[macro_export]
macro_rules! enum_strum_serde {
    ($type:ty) => {
        impl Serialize for $type {
            fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
            where
                S: Serializer,
            {
                serializer.serialize_str(&self.to_string())
            }
        }

        impl<'de> Deserialize<'de> for $type {
            fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
            where
                D: Deserializer<'de>,
            {
                let s = String::deserialize(deserializer)?;
                <$type>::from_str(&s).map_err(serde::de::Error::custom)
            }
        }
    };
}
```


---

## Overview

This file is located at `crates/model/src/macros.rs` within the repository.

**Classes defined:** Serialize

**Functions defined:** serialize, deserialize


---

## Detailed Analysis

### Classes

#### `Serialize`

**Type:** impl


### Functions

#### `serialize(&self, serializer: S)`


#### `deserialize(deserializer: D)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


