# Documentation: test_perf_throttler.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_throttler.py`
- **Size**: 1,458 bytes
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

import pandas as pd
import pytest

from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import Throttler


def buffering_throttler(name: str, limit: int) -> Throttler:
    handler: list[str] = []
    return Throttler(
        name=name,
        limit=limit,
        interval=pd.Timedelta(seconds=1),
        output_send=handler.append,
        output_drop=None,
        clock=LiveClock(),
    )


@pytest.mark.skip
def test_send_unlimited(benchmark):
    throttler = buffering_throttler("buffer-1", 10_000)
    benchmark(throttler.send, "MESSAGE")

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`buffering_throttler()`**: Function defined in this file
- **`test_send_unlimited()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `buffering_throttler`, `test_send_unlimited`
**Imports**: `nautilus_trader.common.component`, `pandas`, `pytest`

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
pytest tests/performance_tests/test_perf_throttler.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.321574Z*
