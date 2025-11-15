# Documentation: `tests/unit_tests/indicators/test_keltner_position.py`
**Generated:** 2025-11-15T19:40:09.195371Z
**File Size:** 5134 bytes
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

- **Path:** `tests/unit_tests/indicators/test_keltner_position.py`
- **Size:** 5,134 bytes
- **Lines:** 151
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Classes:** 1
- **Functions:** 15

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

from nautilus_trader.indicators import KeltnerPosition
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestKeltnerPosition:
    def setup(self):
        # Fixture Setup
        self.kp = KeltnerPosition(10, 2.5)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.kp.name == "KeltnerPosition"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.kp) == "KeltnerPosition(10, 2.5, EXPONENTIAL, SIMPLE, True, 0.0)"
        assert repr(self.kp) == "KeltnerPosition(10, 2.5, EXPONENTIAL, SIMPLE, True, 0.0)"

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.kp.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange
        for _ in range(10):
            self.kp.update_raw(1.00000, 1.00000, 1.00000)

        # Act, Assert
        assert self.kp.initialized is True

    def test_period_returns_expected_value(self):
        # Arrange, Act, Assert
        assert self.kp.period == 10

    def test_k_multiple_returns_expected_value(self):
        # Arrange, Act, Assert
        assert self.kp.k_multiplier == 2.5

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = KeltnerPosition(10, 2.5)

        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.value == 0.0444444444447405

    def test_value_with_one_input_returns_zero(self):
        # Arrange
        self.kp.update_raw(1.00020, 1.00000, 1.00010)

        # Act, Assert
        assert self.kp.value == 0

    def test_value_with_zero_width_input_returns_zero(self):
        # Arrange
        for _ in range(10):
            self.kp.update_raw(1.00000, 1.00000, 1.00000)

        # Act, Assert
        assert self.kp.value == 0

    def test_value_with_three_inputs_returns_expected_value(self):
        # Arrange
        self.kp.update_raw(1.00020, 1.00000, 1.00010)
        self.kp.update_raw(1.00030, 1.00010, 1.00020)
        self.kp.update_raw(1.00040, 1.00020, 1.00030)

        # Act, Assert
        assert self.kp.value == 0.29752066115754594

    def test_value_with_close_on_high_returns_positive_value(self):
        # Arrange
        high = 1.00010
        low = 1.00000

        for _ in range(10):
            high += 0.00010
            low += 0.00010
            close = high
            self.kp.update_raw(high, low, close)

        # Act, Assert
        assert self.kp.value == 1.637585941284833

    def test_value_with_close_on_low_returns_lower_value(self):
        # Arrange
        high = 1.00010
        low = 1.00000

        for _ in range(10):
            high -= 0.00010
            low -= 0.00010
            close = low
            self.kp.update_raw(high, low, close)

        # Act, Assert
        assert self.kp.value == pytest.approx(-1.637585941284833, rel=1e-9)

    def test_value_with_ten_inputs_returns_expected_value(self):
        # Arrange
        self.kp.update_raw(1.00020, 1.00000, 1.00010)
        self.kp.update_raw(1.00030, 1.00010, 1.00020)
        self.kp.update_raw(1.00050, 1.00020, 1.00030)
        self.kp.update_raw(1.00030, 1.00000, 1.00010)
        self.kp.update_raw(1.00030, 1.00010, 1.00020)
        self.kp.update_raw(1.00040, 1.00020, 1.00030)
        self.kp.update_raw(1.00010, 1.00000, 1.00010)
        self.kp.update_raw(1.00030, 1.00010, 1.00020)
        self.kp.update_raw(1.00030, 1.00020, 1.00030)
        self.kp.update_raw(1.00020, 1.00010, 1.00010)

        # Act, Assert
        assert self.kp.value == pytest.approx(-0.14281747514671334, rel=1e-9)

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        self.kp.update_raw(1.00020, 1.00000, 1.00010)
        self.kp.update_raw(1.00030, 1.00010, 1.00020)
        self.kp.update_raw(1.00040, 1.00020, 1.00030)

        # Act
        self.kp.reset()

        # Assert
        assert not self.kp.initialized
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_keltner_position.py` within the repository.

**Classes defined:** TestKeltnerPosition

**Functions defined:** setup, test_name_returns_expected_string, test_str_repr_returns_expected_string, test_initialized_without_inputs_returns_false, test_initialized_with_required_inputs_returns_true, test_period_returns_expected_value, test_k_multiple_returns_expected_value, test_handle_bar_updates_indicator, test_value_with_one_input_returns_zero, test_value_with_zero_width_input_returns_zero and 5 more

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `TestKeltnerPosition`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_initialized_without_inputs_returns_false(self)`


#### `test_initialized_with_required_inputs_returns_true(self)`


#### `test_period_returns_expected_value(self)`


#### `test_k_multiple_returns_expected_value(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input_returns_zero(self)`


#### `test_value_with_zero_width_input_returns_zero(self)`


#### `test_value_with_three_inputs_returns_expected_value(self)`


#### `test_value_with_close_on_high_returns_positive_value(self)`


#### `test_value_with_close_on_low_returns_lower_value(self)`


#### `test_value_with_ten_inputs_returns_expected_value(self)`


#### `test_reset_successfully_returns_indicator_to_fresh_state(self)`


### Imports

- `import pytest`
- `from nautilus_trader.indicators import KeltnerPosition`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_keltner_position import TestKeltnerPosition
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.indicators import KeltnerPosition`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


