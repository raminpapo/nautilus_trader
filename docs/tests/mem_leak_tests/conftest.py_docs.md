# Documentation: `tests/mem_leak_tests/conftest.py`
**Generated:** 2025-11-15T19:40:08.017285Z
**File Size:** 3100 bytes
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

- **Path:** `tests/mem_leak_tests/conftest.py`
- **Size:** 3,100 bytes
- **Lines:** 83
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 3

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

import gc
import tracemalloc


# Number of runs
def snapshot_memory(runs):
    # Snapshot memory for func
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Start tracing memory allocations
            tracemalloc.start()

            # Initialize variables to track max memory usage and continuously increasing memory allocations
            max_peak_memory = 0
            snapshot = None
            initial_snapshot = None

            # Run the function n times and measure memory usage each time
            for i in range(runs):
                # Print the max heap memory usage
                print(f"Run {i}...")

                # Run func
                func(args, kwargs)

                # Register snapshots and measure memory
                snapshot = tracemalloc.take_snapshot()
                if i == 0:
                    initial_snapshot = snapshot

                (current_memory, peak) = tracemalloc.get_traced_memory()
                current_memory = current_memory / (1024 * 1024)
                peak = peak / (1024 * 1024)

                # Update max_memory if current_memory is greater
                if peak > max_peak_memory:
                    max_peak_memory = current_memory

                # Print the difference in memory usage between runs
                print(
                    f"Memory allocated after run {i+1}: {current_memory} MB",
                )
                print(
                    f"Max peak memory recorded: {max_peak_memory} MB",
                )
                print()

                # reset
                gc.collect()
                tracemalloc.reset_peak()

            # Stop tracing memory allocations
            tracemalloc.stop()

            # Find and display largest memory blocks, since initial run
            top_stats = snapshot.compare_to(initial_snapshot, "lineno")
            print("[ Top 10 differences ]")
            for stat in top_stats[:10]:
                print(stat)

            stat = top_stats[0]
            print(f"{stat.count} memory blocks: {stat.size / 1024:.1f} KiB")
            for line in stat.traceback.format():
                print(line)

        return wrapper

    return decorator
```


---

## Overview

This file is located at `tests/mem_leak_tests/conftest.py` within the repository.

**Functions defined:** snapshot_memory, decorator, wrapper

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `snapshot_memory(runs)`


#### `decorator(func)`


#### `wrapper(*args, **kwargs)`


### Imports

- `import gc`
- `import tracemalloc`


---

## Usage Examples

### Importing

```python
from tests.mem_leak_tests.conftest import snapshot_memory
```


---

## Related Files

This file imports from the following modules:

- `import gc`
- `import tracemalloc`

**Directory:** `tests/mem_leak_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


