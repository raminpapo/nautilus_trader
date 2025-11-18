# Documentation: datetime.pxd

## File Metadata

- **Path**: `nautilus_trader/core/datetime.pxd`
- **Size**: 1,581 bytes
- **Lines**: 35
- **Language**: Unknown

## Original Source

```
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 23


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `See`, `Systems`, `Timestamp`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/core/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.283425Z*
