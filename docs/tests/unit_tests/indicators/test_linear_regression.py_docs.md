# Documentation: test_linear_regression.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_linear_regression.py`
- **Size**: 4,387 bytes
- **Lines**: 102
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

import math

import pytest

from nautilus_trader.indicators import LinearRegression
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestLinearRegression:
    def setup(self):
        # Fixture Setup
        self.period = 4
        self.linear_regression = LinearRegression(period=self.period)

    def test_init(self):
        assert not self.linear_regression.initialized
        assert not self.linear_regression.has_inputs
        assert self.linear_regression.period == self.period
        assert self.linear_regression.value == 0
        assert self.linear_regression.slope == 0
        assert self.linear_regression.intercept == 0
        assert self.linear_regression.degree == 0
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 0

    def test_name_returns_expected_string(self):
        assert self.linear_regression.name == "LinearRegression"

    def test_handle_bar_updates_indicator(self):
        for _ in range(self.period):
            self.linear_regression.handle_bar(TestDataStubs.bar_5decimal())

        assert self.linear_regression.has_inputs
        assert self.linear_regression.value == pytest.approx(1.0000300000000002, rel=1e-9)
        assert self.linear_regression.slope == 0.0
        assert self.linear_regression.intercept == pytest.approx(1.0000300000000002, rel=1e-9)
        assert self.linear_regression.degree == 0.0
        assert self.linear_regression.cfo == pytest.approx(2.220379437867177e-14, rel=1e-9)
        assert -math.inf == self.linear_regression.R2

    def test_value_with_one_input(self):
        self.linear_regression.update_raw(1.00000)
        assert self.linear_regression.value == 0
        assert self.linear_regression.slope == 0
        assert self.linear_regression.intercept == 0
        assert self.linear_regression.degree == 0
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 0

    def test_value_with_ten_inputs(self):
        self.linear_regression.update_raw(1.00000)
        self.linear_regression.update_raw(2.00000)
        self.linear_regression.update_raw(3.00000)
        self.linear_regression.update_raw(4.00000)
        self.linear_regression.update_raw(5.00000)
        self.linear_regression.update_raw(6.00000)
        self.linear_regression.update_raw(7.00000)
        self.linear_regression.update_raw(8.00000)
        self.linear_regression.update_raw(9.00000)
        self.linear_regression.update_raw(10.00000)

        assert self.linear_regression.value == 10
        assert self.linear_regression.slope == 1
        assert self.linear_regression.intercept == 6
        assert self.linear_regression.degree == 45
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 1

    def test_reset(self):
        self.linear_regression.update_raw(1.00000)

        self.linear_regression.reset()

        assert not self.linear_regression.initialized
        assert not self.linear_regression.has_inputs
        assert self.linear_regression.period == self.period
        assert self.linear_regression.value == 0
        assert self.linear_regression.slope == 0
        assert self.linear_regression.intercept == 0
        assert self.linear_regression.degree == 0
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestLinearRegression`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `TestLinearRegression`
**Imports**: `math`, `nautilus_trader.indicators`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.data`, `pytest`

## Related Files

This file is located in `tests/unit_tests/indicators/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/indicators/test_linear_regression.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.434741Z*
