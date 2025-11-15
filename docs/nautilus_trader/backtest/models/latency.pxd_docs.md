# Documentation: `nautilus_trader/backtest/models/latency.pxd`
**Generated:** 2025-11-15T19:40:04.590956Z
**File Size:** 1499 bytes
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

- **Path:** `nautilus_trader/backtest/models/latency.pxd`
- **Size:** 1,499 bytes
- **Lines:** 27
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


cdef class LatencyModel:
    cdef readonly uint64_t base_latency_nanos
    """The default latency to the exchange.\n\n:returns: `int`"""
    cdef readonly uint64_t insert_latency_nanos
    """The latency (nanoseconds) for order insert messages to reach the exchange.\n\n:returns: `int`"""
    cdef readonly uint64_t update_latency_nanos
    """The latency (nanoseconds) for order update messages to reach the exchange.\n\n:returns: `int`"""
    cdef readonly uint64_t cancel_latency_nanos
    """The latency (nanoseconds) for order cancel messages to reach the exchange.\n\n:returns: `int`"""
```


---

## Overview

This file is located at `nautilus_trader/backtest/models/latency.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/backtest/models`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


