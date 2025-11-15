# Documentation: `crates/model/src/identifiers/macros.rs`
**Generated:** 2025-11-15T19:40:02.764310Z
**File Size:** 2181 bytes
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

- **Path:** `crates/model/src/identifiers/macros.rs`
- **Size:** 2,181 bytes
- **Lines:** 66
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 5

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

//! Provides macros for generating identifier functionality.

macro_rules! impl_serialization_for_identifier {
    ($ty:ty) => {
        impl Serialize for $ty {
            fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
            where
                S: Serializer,
            {
                self.inner().serialize(serializer)
            }
        }

        impl<'de> Deserialize<'de> for $ty {
            fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
            where
                D: Deserializer<'de>,
            {
                let value_str: &str = Deserialize::deserialize(deserializer)?;
                let value: $ty = value_str.into();
                Ok(value)
            }
        }
    };
}

macro_rules! impl_from_str_for_identifier {
    ($ty:ty) => {
        impl From<&str> for $ty {
            fn from(value: &str) -> Self {
                Self::new(value)
            }
        }

        impl From<String> for $ty {
            fn from(value: String) -> Self {
                Self::new(value)
            }
        }
    };
}

macro_rules! impl_as_ref_for_identifier {
    ($ty:ty) => {
        impl AsRef<str> for $ty {
            fn as_ref(&self) -> &str {
                self.as_str()
            }
        }
    };
}
```


---

## Overview

This file is located at `crates/model/src/identifiers/macros.rs` within the repository.

**Classes defined:** Serialize, From, From, AsRef

**Functions defined:** serialize, deserialize, from, from, as_ref


---

## Detailed Analysis

### Classes

#### `Serialize`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `AsRef`

**Type:** impl


### Functions

#### `serialize(&self, serializer: S)`


#### `deserialize(deserializer: D)`


#### `from(value: &str)`


#### `from(value: String)`


#### `as_ref(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/identifiers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


