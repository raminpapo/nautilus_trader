# Documentation: config.py

## File Metadata

- **Path**: `nautilus_trader/cache/config.py`
- **Size**: 3,116 bytes
- **Lines**: 69
- **Language**: Python

## Original Source

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

from __future__ import annotations

from nautilus_trader.common.config import DatabaseConfig
from nautilus_trader.common.config import NautilusConfig
from nautilus_trader.common.config import PositiveInt


class CacheConfig(NautilusConfig, frozen=True):
    """
    Configuration for ``Cache`` instances.

    Parameters
    ----------
    database : DatabaseConfig, optional
        The configuration for the cache backing database.
    encoding : str, {'msgpack', 'json'}, default 'msgpack'
        The encoding for database operations, controls the type of serializer used.
    timestamps_as_iso8601 : bool, default False
        If timestamps should be persisted as ISO 8601 strings.
        If `False` then will persist as UNIX nanoseconds.
    persist_account_events : bool, default True
        If account state events are written to the backing database.
        Set to `False` in place of purging account state events.
    buffer_interval_ms : PositiveInt, optional
        The buffer interval (milliseconds) between pipelined/batched transactions.
        The recommended range if using buffered pipelining is [10, 1000] milliseconds,
        with a good compromise being 100 milliseconds.
    use_trader_prefix : bool, default True
        If a 'trader-' prefix is used for keys.
    use_instance_id : bool, default False
        If the traders instance ID is used for keys.
    flush_on_start : bool, default False
        If database should be flushed on start.
    drop_instruments_on_reset : bool, default True
        If instruments data should be dropped from the caches memory on reset.
    tick_capacity : PositiveInt, default 10_000
        The maximum length for internal tick dequeues.
    bar_capacity : PositiveInt, default 10_000
        The maximum length for internal bar dequeues.

    """

    database: DatabaseConfig | None = None
    encoding: str = "msgpack"
    timestamps_as_iso8601: bool = False
    persist_account_events: bool = True
    buffer_interval_ms: PositiveInt | None = None
    use_trader_prefix: bool = True
    use_instance_id: bool = False
    flush_on_start: bool = False
    drop_instruments_on_reset: bool = True
    tick_capacity: PositiveInt = 10_000
    bar_capacity: PositiveInt = 10_000

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`CacheConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `CacheConfig`
**Imports**: `__future__`, `nautilus_trader.common.config`

## Related Files

This file is located in `nautilus_trader/cache/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.168384Z*
