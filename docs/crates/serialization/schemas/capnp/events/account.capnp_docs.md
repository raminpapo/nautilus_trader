# Documentation: `crates/serialization/schemas/capnp/events/account.capnp`
**Generated:** 2025-11-15T19:40:03.696534Z
**File Size:** 742 bytes
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

- **Path:** `crates/serialization/schemas/capnp/events/account.capnp`
- **Size:** 742 bytes
- **Lines:** 20
- **Extension:** `.capnp`
- **Type:** text

---

## Source Code

```
@0xfec455d315607b3f;
# Cap'n Proto schema for Nautilus account events

using Identifiers = import "../common/identifiers.capnp";
using Types = import "../common/types.capnp";
using Enums = import "../common/enums.capnp";
using Base = import "../common/base.capnp";

# AccountState - represents the state of an account including balances and margins
struct AccountState {
    accountId @0 :Identifiers.AccountId;
    accountType @1 :Enums.AccountType;
    baseCurrency @2 :Types.Currency;
    balances @3 :List(Types.AccountBalance);
    margins @4 :List(Types.MarginBalance);
    isReported @5 :Bool;  # If reported by exchange vs system-calculated
    eventId @6 :Base.UUID4;
    tsEvent @7 :Base.UnixNanos;
    tsInit @8 :Base.UnixNanos;
}
```


---

## Overview

This file is located at `crates/serialization/schemas/capnp/events/account.capnp` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/serialization/schemas/capnp/events`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


