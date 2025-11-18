# Documentation: test_types_capnp.rs

## File Metadata

- **Path**: `crates/serialization/tests/test_types_capnp.rs`
- **Size**: 6,524 bytes
- **Lines**: 178
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 9 function(s).

## Detailed Walkthrough

### Functions
- **`test_price_roundtrip()`**: Function defined in this file
- **`test_quantity_roundtrip()`**: Function defined in this file
- **`test_price_with_helper_functions()`**: Function defined in this file
- **`test_quantity_with_helper_functions()`**: Function defined in this file
- **`test_price_zero()`**: Function defined in this file
- **`test_quantity_zero()`**: Function defined in this file
- **`test_price_negative()`**: Function defined in this file
- **`test_price_max_precision()`**: Function defined in this file
- **`test_quantity_max_precision()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `test_price_max_precision`, `test_price_negative`, `test_price_roundtrip`, `test_price_with_helper_functions`, `test_price_zero`, `test_quantity_max_precision`, `test_quantity_roundtrip`, `test_quantity_with_helper_functions`, `test_quantity_zero`

## Related Files

This file is located in `crates/serialization/tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/serialization/tests/test_types_capnp.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.149751Z*
