# Documentation: identifiers.capnp

## File Metadata

- **Path**: `crates/serialization/schemas/capnp/common/identifiers.capnp`
- **Size**: 824 bytes
- **Lines**: 66
- **Language**: Unknown

## Original Source

```
@0xf0a1b2c3d4e5f607;
# Cap'n Proto schema for Nautilus identifier types

# Base identifier types - all are interned strings (Ustr) in Rust
struct TraderId {
    value @0 :Text;
}

struct StrategyId {
    value @0 :Text;
}

struct ActorId {
    value @0 :Text;
}

struct AccountId {
    value @0 :Text;
}

struct ClientId {
    value @0 :Text;
}

struct ClientOrderId {
    value @0 :Text;
}

struct VenueOrderId {
    value @0 :Text;
}

struct TradeId {
    value @0 :Text;
}

struct PositionId {
    value @0 :Text;
}

struct ExecAlgorithmId {
    value @0 :Text;
}

struct ComponentId {
    value @0 :Text;
}

struct OrderListId {
    value @0 :Text;
}

struct Symbol {
    value @0 :Text;
}

struct Venue {
    value @0 :Text;
}

# Composite identifier
struct InstrumentId {
    symbol @0 :Symbol;
    venue @1 :Venue;
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 23


**Identifiers**: `AccountId`, `ActorId`, `Base`, `Cap`, `ClientId`, `ClientOrderId`, `ComponentId`, `Composite`, `ExecAlgorithmId`, `InstrumentId`, `Nautilus`, `OrderListId`, `PositionId`, `Proto`, `Rust`, `StrategyId`, `Symbol`, `Text`, `TradeId`, `TraderId`, `Ustr`, `Venue`, `VenueOrderId`

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
*Generated on 2025-11-18T21:55:04.062189Z*
