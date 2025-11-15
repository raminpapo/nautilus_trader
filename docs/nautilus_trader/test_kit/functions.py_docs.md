# Documentation: `nautilus_trader/test_kit/functions.py`
**Generated:** 2025-11-15T19:40:05.331477Z
**File Size:** 2652 bytes
**Extension:** .py
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

- **Path:** `nautilus_trader/test_kit/functions.py`
- **Size:** 2,652 bytes
- **Lines:** 75
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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


---

## Overview

This file is located at `nautilus_trader/test_kit/functions.py` within the repository.

**Functions defined:** ensure_all_tasks_completed

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `ensure_all_tasks_completed()`


### Imports

- `import asyncio`
- `from collections.abc import Callable`
- `from contextlib import suppress`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.functions import ensure_all_tasks_completed
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from collections.abc import Callable`
- `from contextlib import suppress`

**Directory:** `nautilus_trader/test_kit`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


