# Documentation: `crates/serialization/schemas/capnp/common/identifiers.capnp`
**Generated:** 2025-11-15T19:40:03.693214Z
**File Size:** 824 bytes
**Extension:** .capnp
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

- **Path:** `crates/serialization/schemas/capnp/common/identifiers.capnp`
- **Size:** 824 bytes
- **Lines:** 65
- **Extension:** `.capnp`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/serialization/schemas/capnp/common/identifiers.capnp` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/serialization/schemas/capnp/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


