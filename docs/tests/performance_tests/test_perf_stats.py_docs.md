# Documentation: test_perf_stats.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_stats.py`
- **Size**: 1,386 bytes
- **Lines**: 39
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

import numpy as np

from nautilus_trader.core.stats import fast_mean
from nautilus_trader.core.stats import fast_std


def test_np_mean(benchmark):
    benchmark(
        np.mean,
        np.random.default_rng(10).random(100),
    )


def test_np_std(benchmark):
    benchmark(np.std, np.random.default_rng(10).random(100))


def test_fast_mean(benchmark):
    benchmark(fast_mean, np.random.default_rng(10).random(100))


def test_fast_std(benchmark):
    benchmark(fast_std, np.random.default_rng(10).random(100))

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`test_np_mean()`**: Function defined in this file
- **`test_np_std()`**: Function defined in this file
- **`test_fast_mean()`**: Function defined in this file
- **`test_fast_std()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `test_fast_mean`, `test_fast_std`, `test_np_mean`, `test_np_std`
**Imports**: `nautilus_trader.core.stats`, `numpy`

## Related Files

This file is located in `tests/performance_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/performance_tests/test_perf_stats.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.320557Z*
