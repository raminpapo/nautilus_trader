# Documentation: account.capnp

## File Metadata

- **Path**: `crates/serialization/schemas/capnp/events/account.capnp`
- **Size**: 742 bytes
- **Lines**: 21
- **Language**: Unknown

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `AccountBalance`, `AccountId`, `AccountState`, `AccountType`, `Base`, `Bool`, `Cap`, `Currency`, `Enums`, `Identifiers`, `List`, `MarginBalance`, `Nautilus`, `Proto`, `Types`, `UUID4`, `UnixNanos`

## Related Files

This file is located in `crates/serialization/schemas/capnp/events/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.066773Z*
