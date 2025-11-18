# Documentation: types.capnp

## File Metadata

- **Path**: `crates/serialization/schemas/capnp/common/types.capnp`
- **Size**: 2,083 bytes
- **Lines**: 70
- **Language**: Unknown

## Original Source

```
@0xa1b2c3d4e5f60718;
# Cap'n Proto schema for Nautilus value types

using Identifiers = import "identifiers.capnp";
using Enums = import "enums.capnp";

# 128-bit integer representation using hi/lo uint64
# Signed values use two's complement
struct Int128 {
    lo @0 :UInt64;
    hi @1 :UInt64;  # Sign bit in MSB for two's complement
}

struct UInt128 {
    lo @0 :UInt64;
    hi @1 :UInt64;
}

# Rust Decimal representation (rust_decimal crate)
# Used for arbitrary precision decimal values in orders and positions
struct Decimal {
    lo @0 :UInt64;    # Low 64 bits of coefficient
    mid @1 :UInt64;   # Middle 64 bits of coefficient
    hi @2 :UInt64;    # High 64 bits of coefficient
    flags @3 :UInt32; # Scale and sign information
}

# Fixed-point price representation
# Precision varies by instrument (e.g., FX: 5, crypto: 8, equities: 2)
# Supports both standard (i64) and high-precision (i128) modes via Int128
struct Price {
    raw @0 :Int128;
    precision @1 :UInt8;  # 0-9 standard mode, 0-16 high-precision mode
}

# Fixed-point quantity representation
# Precision varies by instrument and exchange
# Supports both standard (u64) and high-precision (u128) modes via UInt128
struct Quantity {
    raw @0 :UInt128;
    precision @1 :UInt8;  # 0-9 standard mode, 0-16 high-precision mode
}

struct Money {
    raw @0 :Int128;
    currency @1 :Currency;
}

# Currency denomination with precision and metadata
# ISO 4217 for fiat, crypto symbols for digital assets
struct Currency {
    code @0 :Text;                        # Alpha-3 (e.g., "USD", "BTC", "ETH")
    precision @1 :UInt8;                  # Decimal places (USD: 2, BTC: 8, JPY: 0)
    iso4217 @2 :UInt16;                   # ISO 4217 numeric code (0 for crypto)
    name @3 :Text;                        # Full name (e.g., "US Dollar", "Bitcoin")
    currencyType @4 :Enums.CurrencyType;
}

struct AccountBalance {
    total @0 :Money;
    locked @1 :Money;
    free @2 :Money;
}

struct MarginBalance {
    initial @0 :Money;
    maintenance @1 :Money;
    instrument @2 :Identifiers.InstrumentId;
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 42


**Identifiers**: `AccountBalance`, `Alpha`, `BTC`, `Bitcoin`, `Cap`, `Currency`, `CurrencyType`, `Decimal`, `Dollar`, `ETH`, `Enums`, `Fixed`, `Full`, `High`, `ISO`, `Identifiers`, `InstrumentId`, `Int128`, `JPY`, `Low`, `MSB`, `MarginBalance`, `Middle`, `Money`, `Nautilus`, `Precision`, `Price`, `Proto`, `Quantity`, `Rust` *(+12 more)*

## Related Files

This file is located in `crates/serialization/schemas/capnp/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.063823Z*
