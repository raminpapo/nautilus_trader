# Documentation: `tests/unit_tests/indicators/test_ama.py`
**Generated:** 2025-11-15T19:40:09.170467Z
**File Size:** 3780 bytes
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

- **Path:** `tests/unit_tests/indicators/test_ama.py`
- **Size:** 3,780 bytes
- **Lines:** 121
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Classes:** 1
- **Functions:** 12

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


---

## Overview

This file is located at `tests/unit_tests/indicators/test_ama.py` within the repository.

**Classes defined:** TestAdaptiveMovingAverage

**Functions defined:** setup, test_name_returns_expected_string, test_str_repr_returns_expected_string, test_period, test_initialized_without_inputs_returns_false, test_initialized_with_required_inputs_returns_true, test_handle_quote_tick_updates_indicator, test_handle_trade_tick_updates_indicator, test_handle_bar_updates_indicator, test_value_with_one_input and 2 more

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `TestAdaptiveMovingAverage`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_period(self)`


#### `test_initialized_without_inputs_returns_false(self)`


#### `test_initialized_with_required_inputs_returns_true(self)`


#### `test_handle_quote_tick_updates_indicator(self)`


#### `test_handle_trade_tick_updates_indicator(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input(self)`


#### `test_value_with_three_inputs(self)`


#### `test_reset_successfully_returns_indicator_to_fresh_state(self)`


### Imports

- `from nautilus_trader.indicators import AdaptiveMovingAverage`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_ama import TestAdaptiveMovingAverage
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.indicators import AdaptiveMovingAverage`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


