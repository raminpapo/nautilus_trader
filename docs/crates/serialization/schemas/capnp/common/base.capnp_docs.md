# Documentation: `crates/serialization/schemas/capnp/common/base.capnp`
**Generated:** 2025-11-15T19:40:03.690871Z
**File Size:** 464 bytes
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

- **Path:** `crates/serialization/schemas/capnp/common/base.capnp`
- **Size:** 464 bytes
- **Lines:** 23
- **Extension:** `.capnp`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/serialization/schemas/capnp/common/base.capnp` within the repository.


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


