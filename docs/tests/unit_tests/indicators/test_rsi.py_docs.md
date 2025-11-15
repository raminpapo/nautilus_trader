# Documentation: `tests/unit_tests/indicators/test_rsi.py`
**Generated:** 2025-11-15T19:40:09.207400Z
**File Size:** 5063 bytes
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

- **Path:** `tests/unit_tests/indicators/test_rsi.py`
- **Size:** 5,063 bytes
- **Lines:** 153
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

from nautilus_trader.indicators import RelativeStrengthIndex
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestRelativeStrengthIndex:
    def setup(self):
        # Fixture Setup
        self.rsi = RelativeStrengthIndex(10)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.rsi.name == "RelativeStrengthIndex"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.rsi) == "RelativeStrengthIndex(10, EXPONENTIAL)"
        assert repr(self.rsi) == "RelativeStrengthIndex(10, EXPONENTIAL)"

    def test_period_returns_expected_value(self):
        # Arrange, Act, Assert
        assert self.rsi.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.rsi.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(4.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(8.00000)
        self.rsi.update_raw(9.00000)
        self.rsi.update_raw(10.00000)

        # Act, Assert
        assert self.rsi.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = RelativeStrengthIndex(10)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 1.0

    def test_value_with_one_input_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(1.00000)

        # Act, Assert
        assert self.rsi.value == 1

    def test_value_with_all_higher_inputs_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(4.00000)

        # Act, Assert
        assert self.rsi.value == 1

    def test_value_with_all_lower_inputs_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(0.50000)

        # Act, Assert
        assert self.rsi.value == 0

    def test_value_with_various_inputs_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(6.00000)

        # Act, Assert
        assert self.rsi.value == 0.6837363325825265

    def test_value_at_returns_expected_value(self):
        # Arrange
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)

        # Act, Assert
        assert self.rsi.value == 0.7615344667662725

    def test_min_value_as_first(self):
        # Arrange
        self.rsi.update_raw(1.00000)
        self.rsi.update_raw(2.00000)
        self.rsi.update_raw(3.00000)
        self.rsi.update_raw(4.00000)
        self.rsi.update_raw(5.00000)
        self.rsi.update_raw(6.00000)
        self.rsi.update_raw(7.00000)
        self.rsi.update_raw(2.00000)

        # Act, Assert
        assert self.rsi.value == 0.38650828748031707

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        self.rsi.update_raw(1.00020)
        self.rsi.update_raw(1.00030)
        self.rsi.update_raw(1.00050)

        # Act
        self.rsi.reset()

        # Assert
        assert not self.rsi.initialized
        assert self.rsi.value == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_rsi.py` within the repository.

**Classes defined:** TestRelativeStrengthIndex

**Functions defined:** setup, test_name_returns_expected_string, test_str_repr_returns_expected_string, test_period_returns_expected_value, test_initialized_without_inputs_returns_false, test_initialized_with_required_inputs_returns_true, test_handle_bar_updates_indicator, test_value_with_one_input_returns_expected_value, test_value_with_all_higher_inputs_returns_expected_value, test_value_with_all_lower_inputs_returns_expected_value and 4 more

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `TestRelativeStrengthIndex`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_period_returns_expected_value(self)`


#### `test_initialized_without_inputs_returns_false(self)`


#### `test_initialized_with_required_inputs_returns_true(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input_returns_expected_value(self)`


#### `test_value_with_all_higher_inputs_returns_expected_value(self)`


#### `test_value_with_all_lower_inputs_returns_expected_value(self)`


#### `test_value_with_various_inputs_returns_expected_value(self)`


#### `test_value_at_returns_expected_value(self)`


#### `test_min_value_as_first(self)`


#### `test_reset_successfully_returns_indicator_to_fresh_state(self)`


### Imports

- `from nautilus_trader.indicators import RelativeStrengthIndex`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_rsi import TestRelativeStrengthIndex
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.indicators import RelativeStrengthIndex`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


