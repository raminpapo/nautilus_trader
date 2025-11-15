# Documentation: `crates/model/src/ffi/identifiers/instrument_id.rs`
**Generated:** 2025-11-15T19:40:02.719779Z
**File Size:** 4260 bytes
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

- **Path:** `crates/model/src/ffi/identifiers/instrument_id.rs`
- **Size:** 4,260 bytes
- **Lines:** 137
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 11

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

use std::{
    collections::hash_map::DefaultHasher,
    ffi::c_char,
    hash::{Hash, Hasher},
    str::FromStr,
};

use nautilus_core::ffi::string::{cstr_as_str, str_to_cstr};

use crate::identifiers::{InstrumentId, Symbol, Venue};

#[unsafe(no_mangle)]
pub extern "C" fn instrument_id_new(symbol: Symbol, venue: Venue) -> InstrumentId {
    InstrumentId::new(symbol, venue)
}

/// Returns any [`InstrumentId`] parsing error from the provided C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn instrument_id_check_parsing(ptr: *const c_char) -> *const c_char {
    let value = unsafe { cstr_as_str(ptr) };
    match InstrumentId::from_str(value) {
        Ok(_) => str_to_cstr(""),
        Err(e) => str_to_cstr(&e.to_string()),
    }
}

/// Returns a Nautilus identifier from a C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn instrument_id_from_cstr(ptr: *const c_char) -> InstrumentId {
    let value = unsafe { cstr_as_str(ptr) };
    InstrumentId::from(value)
}

/// Returns an [`InstrumentId`] as a C string pointer.
#[unsafe(no_mangle)]
pub extern "C" fn instrument_id_to_cstr(instrument_id: &InstrumentId) -> *const c_char {
    str_to_cstr(&instrument_id.to_string())
}

#[unsafe(no_mangle)]
pub extern "C" fn instrument_id_hash(instrument_id: &InstrumentId) -> u64 {
    let mut h = DefaultHasher::new();
    instrument_id.hash(&mut h);
    h.finish()
}

#[unsafe(no_mangle)]
pub extern "C" fn instrument_id_is_synthetic(instrument_id: &InstrumentId) -> u8 {
    u8::from(instrument_id.is_synthetic())
}

#[cfg(test)]
pub mod stubs {
    use std::str::FromStr;

    use rstest::fixture;

    use crate::identifiers::{InstrumentId, Symbol, Venue, stubs::*};

    #[fixture]
    pub fn btc_usdt_perp_binance() -> InstrumentId {
        InstrumentId::from_str("BTCUSDT-PERP.BINANCE").unwrap()
    }

    #[fixture]
    pub fn audusd_sim(symbol_aud_usd: Symbol, venue_sim: Venue) -> InstrumentId {
        InstrumentId {
            symbol: symbol_aud_usd,
            venue: venue_sim,
        }
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use std::ffi::CStr;

    use rstest::rstest;

    use super::{InstrumentId, *};
    use crate::identifiers::{Symbol, Venue};

    #[rstest]
    fn test_to_cstr() {
        unsafe {
            let id = InstrumentId::from("ETH/USDT.BINANCE");
            let result = instrument_id_to_cstr(&id);
            assert_eq!(CStr::from_ptr(result).to_str().unwrap(), "ETH/USDT.BINANCE");
        }
    }

    #[rstest]
    fn test_to_cstr_and_back() {
        unsafe {
            let id = InstrumentId::from("ETH/USDT.BINANCE");
            let result = instrument_id_to_cstr(&id);
            let id2 = instrument_id_from_cstr(result);
            assert_eq!(id, id2);
        }
    }

    #[rstest]
    fn test_from_symbol_and_back() {
        unsafe {
            let id = InstrumentId::new(Symbol::from("ETH/USDT"), Venue::from("BINANCE"));
            let result = instrument_id_to_cstr(&id);
            let id2 = instrument_id_from_cstr(result);
            assert_eq!(id, id2);
        }
    }
}
```


---

## Overview

This file is located at `crates/model/src/ffi/identifiers/instrument_id.rs` within the repository.

**Functions defined:** instrument_id_new, instrument_id_check_parsing, instrument_id_from_cstr, instrument_id_to_cstr, instrument_id_hash, instrument_id_is_synthetic, btc_usdt_perp_binance, audusd_sim, test_to_cstr, test_to_cstr_and_back and 1 more


---

## Detailed Analysis

### Functions

#### `instrument_id_new(symbol: Symbol, venue: Venue)`


#### `instrument_id_check_parsing(ptr: *const c_char)`


#### `instrument_id_from_cstr(ptr: *const c_char)`


#### `instrument_id_to_cstr(instrument_id: &InstrumentId)`


#### `instrument_id_hash(instrument_id: &InstrumentId)`


#### `instrument_id_is_synthetic(instrument_id: &InstrumentId)`


#### `btc_usdt_perp_binance()`


#### `audusd_sim(symbol_aud_usd: Symbol, venue_sim: Venue)`


#### `test_to_cstr()`


#### `test_to_cstr_and_back()`


#### `test_from_symbol_and_back()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/ffi/identifiers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


