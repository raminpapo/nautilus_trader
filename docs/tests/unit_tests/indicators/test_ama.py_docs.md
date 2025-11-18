# Documentation: test_ama.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_ama.py`
- **Size**: 3,780 bytes
- **Lines**: 122
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

from nautilus_trader.indicators import AdaptiveMovingAverage
from nautilus_trader.model.enums import PriceType
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestAdaptiveMovingAverage:
    def setup(self):
        # Fixture Setup
        self.ama = AdaptiveMovingAverage(10, 2, 30)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.ama.name == "AdaptiveMovingAverage"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.ama) == "AdaptiveMovingAverage(10, 2, 30)"
        assert repr(self.ama) == "AdaptiveMovingAverage(10, 2, 30)"

    def test_period(self):
        # Arrange, Act, Assert
        assert self.ama.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.ama.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange
        # Arrange, Act
        for _ in range(10):
            self.ama.update_raw(1.0)

        # Assert
        assert self.ama.initialized is True

    def test_handle_quote_tick_updates_indicator(self):
        # Arrange
        indicator = AdaptiveMovingAverage(10, 2, 30, PriceType.MID)

        tick = TestDataStubs.quote_tick()

        # Act
        indicator.handle_quote_tick(tick)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_handle_trade_tick_updates_indicator(self):
        # Arrange
        indicator = AdaptiveMovingAverage(10, 2, 30)

        tick = TestDataStubs.trade_tick()

        # Act
        indicator.handle_trade_tick(tick)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = AdaptiveMovingAverage(10, 2, 30)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.00003

    def test_value_with_one_input(self):
        # Arrange
        self.ama.update_raw(1.0)

        # Act, Assert
        assert self.ama.value == 1.0

    def test_value_with_three_inputs(self):
        # Arrange
        self.ama.update_raw(1.0)
        self.ama.update_raw(2.0)
        self.ama.update_raw(3.0)

        # Act, Assert
        assert self.ama.value == 2.135802469135802

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        for _ in range(1000):
            self.ama.update_raw(1.0)

        # Act
        self.ama.reset()

        # Assert
        assert not self.ama.initialized
        assert self.ama.value == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestAdaptiveMovingAverage`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `TestAdaptiveMovingAverage`
**Imports**: `nautilus_trader.indicators`, `nautilus_trader.model.enums`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.data`

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
pytest tests/unit_tests/indicators/test_ama.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.406978Z*
