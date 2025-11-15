# Documentation: `crates/adapters/blockchain/src/cache/types.rs`
**Generated:** 2025-11-15T19:40:00.458465Z
**File Size:** 5229 bytes
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

- **Path:** `crates/adapters/blockchain/src/cache/types.rs`
- **Size:** 5,229 bytes
- **Lines:** 166
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 12
- **Functions:** 16

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

use std::str::FromStr;

use alloy::primitives::{I256, U160, U256};
use sqlx::{
    Database, Decode, Encode, Postgres, Type,
    encode::IsNull,
    error::BoxDynError,
    postgres::{PgHasArrayType, PgTypeInfo},
};

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct I256Pg(pub I256);

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct U256Pg(pub U256);

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct U160Pg(pub U160);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct U128Pg(pub u128);

// Implement Type trait for SqlI256
impl Type<Postgres> for I256Pg {
    fn type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("i256")
    }
}

// Implement Type trait for SqlU256
impl Type<Postgres> for U256Pg {
    fn type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("u256")
    }
}

// Implement Type trait for U160Pg
impl Type<Postgres> for U160Pg {
    fn type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("u160")
    }
}

// Implement Type trait for U128Pg
impl Type<Postgres> for U128Pg {
    fn type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("u128")
    }
}

impl<'q> Encode<'q, Postgres> for I256Pg {
    fn encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    ) -> Result<IsNull, BoxDynError> {
        let s = self.0.to_string();
        <&str as Encode<Postgres>>::encode(&s, buf)
    }
}

impl<'q> Encode<'q, Postgres> for U256Pg {
    fn encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    ) -> Result<IsNull, BoxDynError> {
        // Ensure we send decimal format, not hex format to PostgreSQL
        let decimal_str = format!("{}", self.0);
        <&str as Encode<Postgres>>::encode(&decimal_str, buf)
    }
}

impl<'q> Encode<'q, Postgres> for U160Pg {
    fn encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    ) -> Result<IsNull, BoxDynError> {
        let decimal_str = format!("{}", self.0);
        <&str as Encode<Postgres>>::encode(&decimal_str, buf)
    }
}

impl<'q> Encode<'q, Postgres> for U128Pg {
    fn encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    ) -> Result<IsNull, BoxDynError> {
        let decimal_str = self.0.to_string();
        <&str as Encode<Postgres>>::encode(&decimal_str, buf)
    }
}

// Implement Decode trait for SqlI256
impl<'r> Decode<'r, Postgres> for I256Pg {
    fn decode(value: sqlx::postgres::PgValueRef<'r>) -> Result<Self, sqlx::error::BoxDynError> {
        let s = <String as Decode<Postgres>>::decode(value)?;
        let i256 = I256::from_str(&s).map_err(|e| format!("Failed to parse I256: {}", e))?;
        Ok(Self(i256))
    }
}

// Implement Decode trait for SqlU256
impl<'r> Decode<'r, Postgres> for U256Pg {
    fn decode(value: sqlx::postgres::PgValueRef<'r>) -> Result<Self, sqlx::error::BoxDynError> {
        let s = <String as Decode<Postgres>>::decode(value)?;
        let u256 = U256::from_str(&s).map_err(|e| format!("Failed to parse U256: {}", e))?;
        Ok(Self(u256))
    }
}

// Implement Decode trait for U160Pg
impl<'r> Decode<'r, Postgres> for U160Pg {
    fn decode(value: sqlx::postgres::PgValueRef<'r>) -> Result<Self, sqlx::error::BoxDynError> {
        let s = <String as Decode<Postgres>>::decode(value)?;
        let u160 = U160::from_str(&s).map_err(|e| format!("Failed to parse U160: {}", e))?;
        Ok(Self(u160))
    }
}

// Implement Decode trait for U128Pg
impl<'r> Decode<'r, Postgres> for U128Pg {
    fn decode(value: sqlx::postgres::PgValueRef<'r>) -> Result<Self, sqlx::error::BoxDynError> {
        let s = <String as Decode<Postgres>>::decode(value)?;
        let u128_val = u128::from_str(&s).map_err(|e| format!("Failed to parse U128: {}", e))?;
        Ok(Self(u128_val))
    }
}

// Implement PgHasArrayType for array support
impl PgHasArrayType for I256Pg {
    fn array_type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("_i256")
    }
}

impl PgHasArrayType for U256Pg {
    fn array_type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("_u256")
    }
}

impl PgHasArrayType for U160Pg {
    fn array_type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("_u160")
    }
}

impl PgHasArrayType for U128Pg {
    fn array_type_info() -> PgTypeInfo {
        PgTypeInfo::with_name("_u128")
    }
}
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/cache/types.rs` within the repository.

**Classes defined:** I256Pg, U256Pg, U160Pg, U128Pg, Type, Type, Type, Type, PgHasArrayType, PgHasArrayType and 2 more

**Functions defined:** type_info, type_info, type_info, type_info, encode_by_ref, encode_by_ref, encode_by_ref, encode_by_ref, decode, decode and 6 more


---

## Detailed Analysis

### Classes

#### `I256Pg`

**Type:** struct


#### `U256Pg`

**Type:** struct


#### `U160Pg`

**Type:** struct


#### `U128Pg`

**Type:** struct


#### `Type`

**Type:** impl


#### `Type`

**Type:** impl


#### `Type`

**Type:** impl


#### `Type`

**Type:** impl


#### `PgHasArrayType`

**Type:** impl


#### `PgHasArrayType`

**Type:** impl


#### `PgHasArrayType`

**Type:** impl


#### `PgHasArrayType`

**Type:** impl


### Functions

#### `type_info()`


#### `type_info()`


#### `type_info()`


#### `type_info()`


#### `encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    )`


#### `encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    )`


#### `encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    )`


#### `encode_by_ref(
        &self,
        buf: &mut <Postgres as Database>::ArgumentBuffer<'_>,
    )`


#### `decode(value: sqlx::postgres::PgValueRef<'r>)`


#### `decode(value: sqlx::postgres::PgValueRef<'r>)`


#### `decode(value: sqlx::postgres::PgValueRef<'r>)`


#### `decode(value: sqlx::postgres::PgValueRef<'r>)`


#### `array_type_info()`


#### `array_type_info()`


#### `array_type_info()`


#### `array_type_info()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/cache`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


