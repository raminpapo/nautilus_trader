# Documentation: test_perf_xrate_calculator.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_xrate_calculator.py`
- **Size**: 1,447 bytes
- **Lines**: 42
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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.currencies import ETH
from nautilus_trader.model.currencies import USDT


def test_get_rate(benchmark):
    bid_quotes = {
        "BTC/USD": 11291.38,
        "ETH/USDT": 371.90,
        "XBT/USD": 11285.50,
    }

    ask_quotes = {
        "BTC/USD": 11292.58,
        "ETH/USDT": 372.11,
        "XBT/USD": 11286.0,
    }

    benchmark(
        nautilus_pyo3.get_exchange_rate,
        ETH.code,
        USDT.code,
        nautilus_pyo3.PriceType.MID,
        bid_quotes,
        ask_quotes,
    )

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_get_rate()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `test_get_rate`
**Imports**: `nautilus_trader.core`, `nautilus_trader.model.currencies`

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
pytest tests/performance_tests/test_perf_xrate_calculator.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.324758Z*
