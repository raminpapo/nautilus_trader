# Documentation: datetime.pyi

## File Metadata

- **Path**: `nautilus_trader/core/datetime.pyi`
- **Size**: 2,873 bytes
- **Lines**: 56
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

import datetime as dt
from typing import Final

import pandas as pd

# Re-exports
from nautilus_trader.core.nautilus_pyo3 import micros_to_nanos as micros_to_nanos
from nautilus_trader.core.nautilus_pyo3 import millis_to_nanos as millis_to_nanos
from nautilus_trader.core.nautilus_pyo3 import nanos_to_micros as nanos_to_micros
from nautilus_trader.core.nautilus_pyo3 import nanos_to_millis as nanos_to_millis
from nautilus_trader.core.nautilus_pyo3 import nanos_to_secs as nanos_to_secs
from nautilus_trader.core.nautilus_pyo3 import secs_to_millis as secs_to_millis
from nautilus_trader.core.nautilus_pyo3 import secs_to_nanos as secs_to_nanos


# UNIX epoch is the UTC time at midnight on 1970-01-01
UNIX_EPOCH: Final[pd.Timestamp]

def unix_nanos_to_dt(nanos: int) -> pd.Timestamp: ...
def dt_to_unix_nanos(dt: pd.Timestamp | str | int) -> int: ...
def unix_nanos_to_iso8601(unix_nanos: int, nanos_precision: bool = True) -> str: ...
def format_iso8601(dt: dt.datetime, nanos_precision: bool = True) -> str: ...
def format_optional_iso8601(dt: dt.datetime | None, nanos_precision: bool = True) -> str: ...
def maybe_unix_nanos_to_dt(nanos: int | None) -> pd.Timestamp | None: ...
def maybe_dt_to_unix_nanos(dt: pd.Timestamp | None) -> int | None: ...
def is_datetime_utc(dt: dt.datetime) -> bool: ...
def is_tz_aware(time_object: dt.datetime | pd.DataFrame) -> bool: ...
def is_tz_naive(time_object: dt.datetime | pd.DataFrame) -> bool: ...
def as_utc_timestamp(dt: dt.datetime) -> dt.datetime: ...
def as_utc_index(data: pd.DataFrame) -> pd.DataFrame: ...
def time_object_to_dt(time_object: pd.Timestamp | str | int | None) -> dt.datetime | None: ...
def max_date(
    date1: pd.Timestamp | str | int | None = None,
    date2: str | int | None = None,
) -> pd.Timestamp | None: ...
def min_date(
    date1: pd.Timestamp | str | int | None = None,
    date2: str | int | None = None,
) -> pd.Timestamp | None: ...
def ensure_pydatetime_utc(timestamp: pd.Timestamp | None) -> dt.datetime | None: ...

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 30


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `DataFrame`, `Final`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `None`, `Pty`, `Public`, `See`, `Systems`, `Timestamp`, `True`, `UNIX`, `UNIX_EPOCH`, `UTC`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

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
*Generated on 2025-11-18T21:55:05.284639Z*
