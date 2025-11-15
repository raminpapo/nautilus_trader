# Documentation: `tests/unit_tests/indicators/test_wma.py`
**Generated:** 2025-11-15T19:40:09.221952Z
**File Size:** 5425 bytes
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

- **Path:** `tests/unit_tests/indicators/test_wma.py`
- **Size:** 5,425 bytes
- **Lines:** 172
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Classes:** 1
- **Functions:** 14

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

import pytest

from nautilus_trader.indicators import MovingAverageFactory
from nautilus_trader.indicators import MovingAverageType
from nautilus_trader.indicators import WeightedMovingAverage
from nautilus_trader.model.enums import PriceType
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestWeightedMovingAverage:
    def setup(self):
        # Fixture Setup
        self.w = [round(i * 0.1, 2) for i in range(1, 11)]
        self.wma = WeightedMovingAverage(10, self.w)
        self.wma_noweights = WeightedMovingAverage(10)
        self.wma_factory = MovingAverageFactory.create(
            10,
            MovingAverageType.WEIGHTED,
            weights=self.w,
        )

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.wma.name == "WeightedMovingAverage"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        weights_repr = repr(self.wma.weights)
        assert str(self.wma) == f"WeightedMovingAverage(10, {weights_repr})"
        assert repr(self.wma) == f"WeightedMovingAverage(10, {weights_repr})"

    def test_weights_returns_expected_weights(self):
        # Arrange, Act, Assert
        assert list(self.wma.weights) == self.w

    def test_wma_factory_update_raw(self):
        # Arrange, Act
        for i in range(1, 12):
            self.wma_factory.update_raw(float(i))

        # Assert
        assert self.wma_factory.value == 8.0
        assert list(self.wma_factory.weights) == list(self.w)

    def test_handle_quote_tick_updates_indicator(self):
        # Arrange
        indicator = WeightedMovingAverage(10, self.w, PriceType.MID)

        tick = TestDataStubs.quote_tick()

        # Act
        indicator.handle_quote_tick(tick)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_handle_trade_tick_updates_indicator(self):
        # Arrange
        indicator = WeightedMovingAverage(10, self.w)

        tick = TestDataStubs.trade_tick()

        # Act
        indicator.handle_trade_tick(tick)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = WeightedMovingAverage(10, self.w)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.00003

    def test_value_with_one_input_returns_expected_value(self):
        # Arrange
        self.wma.update_raw(1.0)

        # Act, Assert
        assert self.wma.value == 1.0

    def test_value_with_two_input_returns_expected_value(self):
        # Arrange
        self.wma.update_raw(1.0)
        self.wma.update_raw(10.0)

        # 10 * 1.0, 1 * 0.9

        # Act, Assert
        assert self.wma.value == (10 * 1.0 + 1 * 0.9) / 1.9

    def test_value_with_no_weights(self):
        # Arrange
        self.wma_noweights.update_raw(1.0)
        self.wma_noweights.update_raw(2.0)

        # Act, Assert
        assert self.wma_noweights.value == 1.5

    def test_value_with_ten_inputs_returns_expected_value(self):
        # Arrange
        self.wma.update_raw(1.0)
        self.wma.update_raw(2.0)
        self.wma.update_raw(3.0)
        self.wma.update_raw(4.0)
        self.wma.update_raw(5.0)
        self.wma.update_raw(6.0)
        self.wma.update_raw(7.0)
        self.wma.update_raw(8.0)
        self.wma.update_raw(9.0)
        self.wma.update_raw(10.0)

        # Act, Assert
        assert self.wma.value == pytest.approx(7.00, 2)

    def test_value_at_returns_expected_value(self):
        # Arrange
        self.wma.update_raw(1.0)
        self.wma.update_raw(2.0)
        self.wma.update_raw(3.0)
        self.wma.update_raw(4.0)
        self.wma.update_raw(5.0)
        self.wma.update_raw(6.0)
        self.wma.update_raw(7.0)
        self.wma.update_raw(8.0)
        self.wma.update_raw(9.0)
        self.wma.update_raw(10.0)
        self.wma.update_raw(11.0)

        # Act, Assert
        assert self.wma.value == 8.0

    def test_reset(self):
        # Arrange
        self.wma.update_raw(1.0)
        self.wma.update_raw(2.0)
        self.wma.update_raw(3.0)

        # Act
        self.wma.reset()

        # Assert
        assert not self.wma.initialized
        assert self.wma.value == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_wma.py` within the repository.

**Classes defined:** TestWeightedMovingAverage

**Functions defined:** setup, test_name_returns_expected_string, test_str_repr_returns_expected_string, test_weights_returns_expected_weights, test_wma_factory_update_raw, test_handle_quote_tick_updates_indicator, test_handle_trade_tick_updates_indicator, test_handle_bar_updates_indicator, test_value_with_one_input_returns_expected_value, test_value_with_two_input_returns_expected_value and 4 more

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `TestWeightedMovingAverage`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_weights_returns_expected_weights(self)`


#### `test_wma_factory_update_raw(self)`


#### `test_handle_quote_tick_updates_indicator(self)`


#### `test_handle_trade_tick_updates_indicator(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input_returns_expected_value(self)`


#### `test_value_with_two_input_returns_expected_value(self)`


#### `test_value_with_no_weights(self)`


#### `test_value_with_ten_inputs_returns_expected_value(self)`


#### `test_value_at_returns_expected_value(self)`


#### `test_reset(self)`


### Imports

- `import pytest`
- `from nautilus_trader.indicators import MovingAverageFactory`
- `from nautilus_trader.indicators import MovingAverageType`
- `from nautilus_trader.indicators import WeightedMovingAverage`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_wma import TestWeightedMovingAverage
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.indicators import MovingAverageFactory`
- `from nautilus_trader.indicators import MovingAverageType`
- `from nautilus_trader.indicators import WeightedMovingAverage`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


