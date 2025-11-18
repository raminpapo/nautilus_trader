# Documentation: test_volatility_ratio.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_volatility_ratio.py`
- **Size**: 4,616 bytes
- **Lines**: 147
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

from nautilus_trader.indicators import VolatilityRatio
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestVolatilityCompressionRatio:
    def setup(self):
        # Fixture Setup
        self.vcr = VolatilityRatio(10, 100)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.vcr.name == "VolatilityRatio"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.vcr) == "VolatilityRatio(10, 100, SIMPLE, True, 0.0)"
        assert repr(self.vcr) == "VolatilityRatio(10, 100, SIMPLE, True, 0.0)"

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.vcr.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange, Act
        for _ in range(100):
            self.vcr.update_raw(1.00000, 1.00000, 1.00000)

        # Assert
        assert self.vcr.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = VolatilityRatio(10, 100)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_value_with_no_inputs_returns_none(self):
        # Arrange, Act, Assert
        assert self.vcr.value == 0

    def test_value_with_epsilon_inputs_returns_expected_value(self):
        # Arrange
        epsilon = sys.float_info.epsilon
        self.vcr.update_raw(epsilon, epsilon, epsilon)

        # Act, Assert
        assert self.vcr.value == 0

    def test_value_with_one_ones_input_returns_expected_value(self):
        # Arrange
        self.vcr.update_raw(1.00000, 1.00000, 1.00000)

        # Act, Assert
        assert self.vcr.value == 0

    def test_value_with_one_input_returns_expected_value(self):
        # Arrange
        self.vcr.update_raw(1.00020, 1.00000, 1.00010)

        # Act, Assert
        assert self.vcr.value == 1.0

    def test_value_with_three_inputs_returns_expected_value(self):
        # Arrange
        self.vcr.update_raw(1.00020, 1.00000, 1.00010)
        self.vcr.update_raw(1.00020, 1.00000, 1.00010)
        self.vcr.update_raw(1.00020, 1.00000, 1.00010)

        # Act, Assert
        assert self.vcr.value == 1.0

    def test_value_with_close_on_high_returns_expected_value(self):
        # Arrange
        high = 1.00010
        low = 1.00000
        factor = 0

        # Act
        for _ in range(1000):
            high += 0.00010 + factor
            low += 0.00010 + factor
            factor += 0.00001
            close = high
            self.vcr.update_raw(high, low, close)

        # Assert
        assert self.vcr.value == pytest.approx(0.9552015928322548, 2)

    def test_value_with_close_on_low_returns_expected_value(self):
        # Arrange
        high = 1.00010
        low = 1.00000
        factor = 0

        # Act
        for _ in range(1000):
            high -= 0.00010 + factor
            low -= 0.00010 + factor
            factor -= 0.00002
            close = low
            self.vcr.update_raw(high, low, close)

        # Assert
        assert self.vcr.value == 0.9547511312217188

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        for _ in range(1000):
            self.vcr.update_raw(1.00010, 1.00000, 1.00005)

        # Act
        self.vcr.reset()

        # Assert
        assert not self.vcr.initialized
        assert self.vcr.value == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestVolatilityCompressionRatio`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `TestVolatilityCompressionRatio`
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
pytest tests/unit_tests/indicators/test_volatility_ratio.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.456385Z*
