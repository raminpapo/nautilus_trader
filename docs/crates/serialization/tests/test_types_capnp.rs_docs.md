# Documentation: `crates/serialization/tests/test_types_capnp.rs`
**Generated:** 2025-11-15T19:40:03.753232Z
**File Size:** 6524 bytes
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

- **Path:** `crates/serialization/tests/test_types_capnp.rs`
- **Size:** 6,524 bytes
- **Lines:** 177
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 9

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

//! Cap'n Proto serialization integration tests for value types.

#![cfg(feature = "capnp")]

use nautilus_model::types::{Price, Quantity};
use nautilus_serialization::capnp::{FromCapnp, ToCapnp, types_capnp};
use rstest::rstest;

#[rstest]
#[case(Price::from("100.50"), 2)]
#[case(Price::from("0.00001"), 5)]
#[case(Price::from("99999.999"), 3)]
#[case(Price::from("1.0"), 1)]
fn test_price_roundtrip(#[case] price: Price, #[case] _precision: u8) {
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::price::Builder>();
    price.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::price::Reader>().unwrap();
    let decoded = Price::from_capnp(root).unwrap();

    assert_eq!(price, decoded);
}

#[rstest]
#[case(Quantity::from("1000.5"), 1)]
#[case(Quantity::from("0.0001"), 4)]
#[case(Quantity::from("999999.999"), 3)]
#[case(Quantity::from("1.0"), 1)]
fn test_quantity_roundtrip(#[case] qty: Quantity, #[case] _precision: u8) {
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::quantity::Builder>();
    qty.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::quantity::Reader>().unwrap();
    let decoded = Quantity::from_capnp(root).unwrap();

    assert_eq!(qty, decoded);
}

#[rstest]
fn test_price_with_helper_functions() {
    let price = Price::from("123.45");
    let bytes = nautilus_serialization::capnp::conversions::serialize_price(&price).unwrap();
    let decoded = nautilus_serialization::capnp::conversions::deserialize_price(&bytes).unwrap();
    assert_eq!(price, decoded);
}

#[rstest]
fn test_quantity_with_helper_functions() {
    let qty = Quantity::from("100.5");
    let bytes = nautilus_serialization::capnp::conversions::serialize_quantity(&qty).unwrap();
    let decoded = nautilus_serialization::capnp::conversions::deserialize_quantity(&bytes).unwrap();
    assert_eq!(qty, decoded);
}

#[rstest]
fn test_price_zero() {
    let price = Price::from("0.0");
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::price::Builder>();
    price.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::price::Reader>().unwrap();
    let decoded = Price::from_capnp(root).unwrap();

    assert_eq!(price, decoded);
}

#[rstest]
fn test_quantity_zero() {
    let qty = Quantity::from("0.0");
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::quantity::Builder>();
    qty.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::quantity::Reader>().unwrap();
    let decoded = Quantity::from_capnp(root).unwrap();

    assert_eq!(qty, decoded);
}

#[rstest]
fn test_price_negative() {
    let price = Price::from("-50.25");
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::price::Builder>();
    price.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::price::Reader>().unwrap();
    let decoded = Price::from_capnp(root).unwrap();

    assert_eq!(price, decoded);
}

#[rstest]
fn test_price_max_precision() {
    let price = Price::from("123.123456789");
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::price::Builder>();
    price.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::price::Reader>().unwrap();
    let decoded = Price::from_capnp(root).unwrap();

    assert_eq!(price, decoded);
}

#[rstest]
fn test_quantity_max_precision() {
    let qty = Quantity::from("100.123456789");
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<types_capnp::quantity::Builder>();
    qty.to_capnp(builder);

    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    let reader =
        capnp::serialize::read_message(&mut &bytes[..], capnp::message::ReaderOptions::new())
            .unwrap();
    let root = reader.get_root::<types_capnp::quantity::Reader>().unwrap();
    let decoded = Quantity::from_capnp(root).unwrap();

    assert_eq!(qty, decoded);
}
```


---

## Overview

This file is located at `crates/serialization/tests/test_types_capnp.rs` within the repository.

**Functions defined:** test_price_roundtrip, test_quantity_roundtrip, test_price_with_helper_functions, test_quantity_with_helper_functions, test_price_zero, test_quantity_zero, test_price_negative, test_price_max_precision, test_quantity_max_precision


---

## Detailed Analysis

### Functions

#### `test_price_roundtrip(#[case] price: Price, #[case] _precision: u8)`


#### `test_quantity_roundtrip(#[case] qty: Quantity, #[case] _precision: u8)`


#### `test_price_with_helper_functions()`


#### `test_quantity_with_helper_functions()`


#### `test_price_zero()`


#### `test_quantity_zero()`


#### `test_price_negative()`


#### `test_price_max_precision()`


#### `test_quantity_max_precision()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/serialization/tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


