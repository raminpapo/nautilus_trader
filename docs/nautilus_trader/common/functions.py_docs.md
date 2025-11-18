# Documentation: functions.py

## File Metadata

- **Path**: `nautilus_trader/common/functions.py`
- **Size**: 4,205 bytes
- **Lines**: 125
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

import asyncio
import sys

import pandas as pd

from nautilus_trader.core.datetime import format_iso8601


def get_event_loop() -> asyncio.AbstractEventLoop:
    """
    Get or create an event loop compatible with uvloop and Python 3.11+.

    This function provides a safe way to obtain an event loop that works with
    uvloop 0.22+ which no longer auto-creates loops in `asyncio.get_event_loop()`.

    The function will:
    1. Return the running event loop if one exists.
    2. Return any preconfigured loop set via asyncio.set_event_loop().
    3. Create and set a new event loop only if none exists (production mode).

    In test environments (when pytest is running), this function will not create
    new event loops to prevent resource leaks. Instead, it will raise a clear error
    instructing the caller to use pytest-asyncio's event_loop fixture.

    Returns
    -------
    asyncio.AbstractEventLoop
        The running event loop, preconfigured loop, or a newly created loop.

    Raises
    ------
    RuntimeError
        If no event loop is available in a test environment.

    """
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        pass  # No running loop active

    # Try the legacy semantics which respect preconfigured loops
    loop: asyncio.AbstractEventLoop | None = None

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = None
    except Exception:
        # Compatibility: some policies raise non-RuntimeError exceptions
        loop = None

    if loop is not None and not loop.is_closed():
        return loop

    # Fall back to the policy directly (uvloop 0.22+ requires this path)
    try:
        policy = asyncio.get_event_loop_policy()
    except RuntimeError:
        policy = None

    if policy is not None:
        try:
            loop = policy.get_event_loop()
        except Exception:
            loop = None
        if loop is not None and not loop.is_closed():
            return loop

    # In test environments, do not create new loops to prevent resource leaks
    # Instead, raise an error instructing the caller to use pytest fixtures
    if "pytest" in sys.modules:
        msg = (
            "No event loop available in test environment. "
            "Use pytest-asyncio's 'event_loop' fixture parameter instead of calling get_event_loop(). "
            "Example: def test_example(event_loop): ..."
        )
        raise RuntimeError(msg)

    # No preconfigured loop is available, create and register a new one (production mode only)
    policy = policy or asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    policy.set_event_loop(loop)
    return loop


def format_utc_timerange(start: pd.Timestamp | None, end: pd.Timestamp | None) -> str:
    """
    Return a formatted time range string based on start and end timestamps (UTC).

    Parameters
    ----------
    start : pd.Timestamp | None
        The start timestamp (UTC).
    end : pd.Timestamp | None
        The end timestamp (UTC).

    Returns
    -------
    str

    """
    if start and end:
        return f" from {format_iso8601(start)} to {format_iso8601(end)}"
    elif start:
        return f" from {format_iso8601(start)}"
    elif end:
        return f" to {format_iso8601(end)}"
    else:
        return ""

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`get_event_loop()`**: Function defined in this file
- **`format_utc_timerange()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `format_utc_timerange`, `get_event_loop`
**Imports**: `asyncio`, `nautilus_trader.core.datetime`, `pandas`, `sys`

## Related Files

This file is located in `nautilus_trader/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.253536Z*
