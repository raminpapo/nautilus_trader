# Documentation: `nautilus_trader/serialization/base.pxd`
**Generated:** 2025-11-15T19:40:05.314390Z
**File Size:** 1096 bytes
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

- **Path:** `nautilus_trader/serialization/base.pxd`
- **Size:** 1,096 bytes
- **Lines:** 23
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

cdef dict _OBJECT_TO_DICT_MAP
cdef dict _OBJECT_FROM_DICT_MAP
cdef set[type] _EXTERNAL_PUBLISHABLE_TYPES


cdef class Serializer:
    cpdef bytes serialize(self, object obj)
    cpdef object deserialize(self, bytes obj_bytes)
```


---

## Overview

This file is located at `nautilus_trader/serialization/base.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/serialization`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


