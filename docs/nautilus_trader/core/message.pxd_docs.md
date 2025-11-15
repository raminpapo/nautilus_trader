# Documentation: `nautilus_trader/core/message.pxd`
**Generated:** 2025-11-15T19:40:04.765108Z
**File Size:** 2341 bytes
**Extension:** .pxd
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

- **Path:** `nautilus_trader/core/message.pxd`
- **Size:** 2,341 bytes
- **Lines:** 58
- **Extension:** `.pxd`
- **Type:** text

---

## Source Code

```python
# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from libc.stdint cimport uint64_t

from nautilus_trader.core.uuid cimport UUID4


cdef class Command:
    cdef readonly UUID4 id
    """The command message ID.\n\n:returns: `UUID4`"""
    cdef readonly uint64_t ts_init
    """UNIX timestamp (nanoseconds) when the object was initialized.\n\n:returns: `uint64_t`"""
    cdef readonly UUID4 correlation_id
    """The command correlation ID.\n\n:returns: `UUID4` or ``None``"""


cdef class Document:
    cdef readonly UUID4 id
    """The document message ID.\n\n:returns: `UUID4`"""
    cdef readonly uint64_t ts_init
    """UNIX timestamp (nanoseconds) when the object was initialized.\n\n:returns: `uint64_t`"""


cdef class Event:
    pass


cdef class Request:
    cdef readonly UUID4 id
    """The request message ID.\n\n:returns: `UUID4`"""
    cdef readonly uint64_t ts_init
    """UNIX timestamp (nanoseconds) when the object was initialized.\n\n:returns: `uint64_t`"""
    cdef readonly object callback
    """The callback for the response.\n\n:returns: `Callable`"""
    cdef readonly UUID4 correlation_id
    """The request correlation ID.\n\n:returns: `UUID4` or ``None``"""


cdef class Response:
    cdef readonly UUID4 id
    """The response message ID.\n\n:returns: `UUID4`"""
    cdef readonly uint64_t ts_init
    """UNIX timestamp (nanoseconds) when the object was initialized.\n\n:returns: `uint64_t`"""
    cdef readonly UUID4 correlation_id
    """The response correlation ID.\n\n:returns: `UUID4`"""
```


---

## Overview

This file is located at `nautilus_trader/core/message.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


