# Documentation: `nautilus_trader/core/datetime.pxd`
**Generated:** 2025-11-15T19:40:04.723992Z
**File Size:** 1581 bytes
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

- **Path:** `nautilus_trader/core/datetime.pxd`
- **Size:** 1,581 bytes
- **Lines:** 34
- **Extension:** `.pxd`
- **Type:** text
- **Imports:** 1

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

import pandas as pd

from cpython.datetime cimport datetime
from libc.stdint cimport uint64_t


cpdef unix_nanos_to_dt(uint64_t nanos)
cpdef dt_to_unix_nanos(dt: pd.Timestamp)
cpdef str unix_nanos_to_iso8601(uint64_t unix_nanos, bint nanos_precision=*)
cpdef str format_iso8601(datetime dt, bint nanos_precision=*)
cpdef str format_optional_iso8601(datetime dt, bint nanos_precision=*)
cpdef maybe_unix_nanos_to_dt(nanos)
cpdef maybe_dt_to_unix_nanos(dt: pd.Timestamp)
cpdef bint is_datetime_utc(datetime dt)
cpdef bint is_tz_aware(time_object)
cpdef bint is_tz_naive(time_object)
cpdef datetime as_utc_timestamp(datetime dt)
cpdef object as_utc_index(time_object)
cpdef datetime time_object_to_dt(time_object)
```


---

## Overview

This file is located at `nautilus_trader/core/datetime.pxd` within the repository.

**Import statements:** 1


---

## Detailed Analysis

### Imports

- `import pandas as pd`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`

**Directory:** `nautilus_trader/core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


