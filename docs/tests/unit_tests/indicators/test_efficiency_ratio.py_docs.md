# Documentation: `tests/unit_tests/indicators/test_efficiency_ratio.py`
**Generated:** 2025-11-15T19:40:09.186410Z
**File Size:** 4328 bytes
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

- **Path:** `tests/unit_tests/indicators/test_efficiency_ratio.py`
- **Size:** 4,328 bytes
- **Lines:** 143
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
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

from nautilus_trader.indicators import EfficiencyRatio
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestEfficiencyRatio:
    def setup(self):
        # Fixture Setup
        self.er = EfficiencyRatio(10)

    def test_name_returns_expected_string(self):
        # Act, Assert
        assert self.er.name == "EfficiencyRatio"

    def test_str_repr_returns_expected_string(self):
        # Act, Assert
        assert str(self.er) == "EfficiencyRatio(10)"
        assert repr(self.er) == "EfficiencyRatio(10)"

    def test_period(self):
        # Act, Assert
        assert self.er.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Act, Assert
        assert self.er.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange, Act
        for _ in range(10):
            self.er.update_raw(1.00000)

        # Assert
        assert self.er.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = EfficiencyRatio(10)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 0

    def test_value_with_one_input(self):
        # Arrange
        self.er.update_raw(1.00000)

        # Act, Assert
        assert self.er.value == 0.0

    def test_value_with_efficient_higher_inputs(self):
        # Arrange
        initial_price = 1.00000

        # Act
        for _ in range(10):
            initial_price += 0.00001
            self.er.update_raw(initial_price)

        # Assert
        assert self.er.value == 1.0

    def test_value_with_efficient_lower_inputs(self):
        # Arrange
        initial_price = 1.00000

        # Act
        for _ in range(10):
            initial_price -= 0.00001
            self.er.update_raw(initial_price)

        # Assert
        assert self.er.value == 1.0

    def test_value_with_oscillating_inputs_returns_zero(self):
        # Arrange
        self.er.update_raw(1.00000)
        self.er.update_raw(1.00010)
        self.er.update_raw(1.00000)
        self.er.update_raw(0.99990)
        self.er.update_raw(1.00000)

        # Act, Assert
        assert self.er.value == 0.0

    def test_value_with_half_oscillating_inputs_returns_zero(self):
        # Arrange
        self.er.update_raw(1.00000)
        self.er.update_raw(1.00020)
        self.er.update_raw(1.00010)
        self.er.update_raw(1.00030)
        self.er.update_raw(1.00020)

        # Act, Assert
        assert self.er.value == 0.3333333333333333

    def test_value_with_noisy_inputs(self):
        # Arrange
        self.er.update_raw(1.00000)
        self.er.update_raw(1.00010)
        self.er.update_raw(1.00008)
        self.er.update_raw(1.00007)
        self.er.update_raw(1.00012)
        self.er.update_raw(1.00005)
        self.er.update_raw(1.00015)

        # Act, Assert
        assert self.er.value == 0.42857142857215363

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        for _ in range(10):
            self.er.update_raw(1.00000)

        # Act
        self.er.reset()

        # Assert
        assert not self.er.initialized
        assert self.er.value == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_efficiency_ratio.py` within the repository.

**Classes defined:** TestEfficiencyRatio

**Functions defined:** setup, test_name_returns_expected_string, test_str_repr_returns_expected_string, test_period, test_initialized_without_inputs_returns_false, test_initialized_with_required_inputs_returns_true, test_handle_bar_updates_indicator, test_value_with_one_input, test_value_with_efficient_higher_inputs, test_value_with_efficient_lower_inputs and 4 more

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `TestEfficiencyRatio`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_period(self)`


#### `test_initialized_without_inputs_returns_false(self)`


#### `test_initialized_with_required_inputs_returns_true(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input(self)`


#### `test_value_with_efficient_higher_inputs(self)`


#### `test_value_with_efficient_lower_inputs(self)`


#### `test_value_with_oscillating_inputs_returns_zero(self)`


#### `test_value_with_half_oscillating_inputs_returns_zero(self)`


#### `test_value_with_noisy_inputs(self)`


#### `test_reset_successfully_returns_indicator_to_fresh_state(self)`


### Imports

- `from nautilus_trader.indicators import EfficiencyRatio`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_efficiency_ratio import TestEfficiencyRatio
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.indicators import EfficiencyRatio`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


