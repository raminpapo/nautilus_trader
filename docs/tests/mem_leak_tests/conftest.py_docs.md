# Documentation: conftest.py

## File Metadata

- **Path**: `tests/mem_leak_tests/conftest.py`
- **Size**: 3,100 bytes
- **Lines**: 84
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`snapshot_memory()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `snapshot_memory`
**Imports**: `gc`, `tracemalloc`

## Related Files

This file is located in `tests/mem_leak_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/mem_leak_tests/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.264078Z*
