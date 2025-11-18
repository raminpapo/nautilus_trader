# Documentation: test_atr.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_atr.py`
- **Size**: 5,204 bytes
- **Lines**: 174
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

import sys

import pytest

from nautilus_trader.indicators import AverageTrueRange
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestAverageTrueRange:
    def setup(self):
        # Fixture Setup
        self.atr = AverageTrueRange(10)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.atr.name == "AverageTrueRange"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.atr) == "AverageTrueRange(10, SIMPLE, True, 0.0)"
        assert repr(self.atr) == "AverageTrueRange(10, SIMPLE, True, 0.0)"

    def test_period(self):
        # Arrange, Act, Assert
        assert self.atr.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.atr.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange, Act
        for _ in range(10):
            self.atr.update_raw(1.00000, 1.00000, 1.00000)

        # Assert
        assert self.atr.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = AverageTrueRange(10)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 2.999999999997449e-05

    def test_value_with_no_inputs_returns_zero(self):
        # Arrange, Act, Assert
        assert self.atr.value == 0.0

    def test_value_with_epsilon_input(self):
        # Arrange
        epsilon = sys.float_info.epsilon
        self.atr.update_raw(epsilon, epsilon, epsilon)

        # Act, Assert
        assert self.atr.value == 0.0

    def test_value_with_one_ones_input(self):
        # Arrange
        self.atr.update_raw(1.00000, 1.00000, 1.00000)

        # Act, Assert
        assert self.atr.value == 0.0

    def test_value_with_one_input(self):
        # Arrange
        self.atr.update_raw(1.00020, 1.00000, 1.00010)

        # Act, Assert
        assert self.atr.value == pytest.approx(0.00020)

    def test_value_with_three_inputs(self):
        # Arrange
        self.atr.update_raw(1.00020, 1.00000, 1.00010)
        self.atr.update_raw(1.00020, 1.00000, 1.00010)
        self.atr.update_raw(1.00020, 1.00000, 1.00010)

        # Act, Assert
        assert self.atr.value == pytest.approx(0.00020)

    def test_value_with_close_on_high(self):
        # Arrange
        high = 1.00010
        low = 1.00000

        # Act
        for _ in range(1000):
            high += 0.00010
            low += 0.00010
            close = high
            self.atr.update_raw(high, low, close)

        # Assert
        assert self.atr.value == pytest.approx(0.00010, 2)

    def test_value_with_close_on_low(self):
        # Arrange
        high = 1.00010
        low = 1.00000

        # Act
        for _ in range(1000):
            high -= 0.00010
            low -= 0.00010
            close = low
            self.atr.update_raw(high, low, close)

        # Assert
        assert self.atr.value == pytest.approx(0.00010)

    def test_floor_with_ten_ones_inputs(self):
        # Arrange
        floor = 0.00005
        floored_atr = AverageTrueRange(10, value_floor=floor)

        for _ in range(20):
            floored_atr.update_raw(1.00000, 1.00000, 1.00000)

        # Act, Assert
        assert floored_atr.value == 5e-05

    def test_floor_with_exponentially_decreasing_high_inputs(self):
        # Arrange
        floor = 0.00005
        floored_atr = AverageTrueRange(10, value_floor=floor)

        high = 1.00020
        low = 1.00000
        close = 1.00000

        for _ in range(20):
            high -= (high - low) / 2
            floored_atr.update_raw(high, low, close)

        # Act, Assert
        assert floored_atr.value == 5e-05

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        for _ in range(1000):
            self.atr.update_raw(1.00010, 1.00000, 1.00005)

        # Act
        self.atr.reset()

        # Assert
        assert not self.atr.initialized
        assert self.atr.value == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestAverageTrueRange`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `TestAverageTrueRange`
**Imports**: `nautilus_trader.indicators`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.data`, `pytest`, `sys`

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
pytest tests/unit_tests/indicators/test_atr.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.410998Z*
