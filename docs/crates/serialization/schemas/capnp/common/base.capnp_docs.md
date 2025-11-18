# Documentation: base.capnp

## File Metadata

- **Path**: `crates/serialization/schemas/capnp/common/base.capnp`
- **Size**: 464 bytes
- **Lines**: 24
- **Language**: Unknown

## Original Source

```
@0xddc8dbb7e478d532;
# Cap'n Proto schema for Nautilus base types
# These types are used across all schemas to ensure consistency

# UUID version 4 (RFC 4122)
struct UUID4 {
    value @0 :Data;  # 16 bytes
}

# Unix timestamp in nanoseconds since epoch
struct UnixNanos {
    value @0 :UInt64;
}

# String-to-string map for metadata and tags
struct StringMap {
    entries @0 :List(Entry);

    struct Entry {
        key @0 :Text;
        value @1 :Text;
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 16


**Identifiers**: `Cap`, `Data`, `Entry`, `List`, `Nautilus`, `Proto`, `RFC`, `String`, `StringMap`, `Text`, `These`, `UInt64`, `UUID`, `UUID4`, `Unix`, `UnixNanos`

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
*Generated on 2025-11-18T21:55:04.059520Z*
