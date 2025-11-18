# Documentation: test_perf_fill_model.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_fill_model.py`
- **Size**: 1,191 bytes
- **Lines**: 32
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

from nautilus_trader.backtest.models import FillModel


_FILL_MODEL = FillModel(
    prob_fill_on_stop=0.95,
    prob_fill_on_limit=0.5,
    random_seed=42,
)


def test_is_limit_filled(benchmark):
    benchmark(_FILL_MODEL.is_limit_filled)


def test_is_stop_filled(benchmark):
    benchmark(_FILL_MODEL.is_stop_filled)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`test_is_limit_filled()`**: Function defined in this file
- **`test_is_stop_filled()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `test_is_limit_filled`, `test_is_stop_filled`
**Imports**: `nautilus_trader.backtest.models`

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
pytest tests/performance_tests/test_perf_fill_model.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.307043Z*
