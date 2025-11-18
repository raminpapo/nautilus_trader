# Documentation: functions.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/functions.py`
- **Size**: 2,652 bytes
- **Lines**: 76
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
from collections.abc import Callable
from contextlib import suppress


async def eventually(condition: Callable, timeout: float = 2.0) -> None:
    """
    Await the given condition to eventually evaluate True.

    The intention is to pass an anonymous function as the `condition` which will
    be continually evaluated until either returning True, or the timeout expiring.

    Parameters
    ----------
    condition : Callable
        The condition to evaluate.
    timeout: float, default 2.0
        The amount of time (seconds) to wait for the condition to become True.

    Raises
    ------
    asyncio.TimeoutError
        If `condition` does not become True prior to `timeout` expiring.

    """

    async def await_condition(c):
        while not c():
            await asyncio.sleep(0)

    await asyncio.wait_for(await_condition(condition), timeout=timeout)


def ensure_all_tasks_completed() -> None:
    """
    Gather all remaining tasks from the running event loop, cancel then run until
    complete.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No loop is running, attempt to retrieve any preconfigured loop
        try:
            policy = asyncio.get_event_loop_policy()
            loop = policy.get_event_loop()
        except RuntimeError:
            return  # Nothing to clean up
        if loop.is_closed():
            return  # Loop is already closed

    # Cancel ALL tasks in the event loop
    all_tasks = asyncio.tasks.all_tasks(loop)
    for task in all_tasks:
        task.cancel()

    gather_all = asyncio.gather(*all_tasks, return_exceptions=True)

    # Expected due to task cancellation
    with suppress(asyncio.CancelledError):
        loop.run_until_complete(gather_all)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`ensure_all_tasks_completed()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `ensure_all_tasks_completed`
**Imports**: `asyncio`, `collections.abc`, `contextlib`

## Related Files

This file is located in `nautilus_trader/test_kit/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/functions.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.948315Z*
