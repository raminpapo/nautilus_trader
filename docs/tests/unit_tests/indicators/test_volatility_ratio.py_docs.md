# Documentation: `tests/unit_tests/indicators/test_volatility_ratio.py`
**Generated:** 2025-11-15T19:40:09.218730Z
**File Size:** 4616 bytes
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

- **Path:** `tests/unit_tests/indicators/test_volatility_ratio.py`
- **Size:** 4,616 bytes
- **Lines:** 146
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
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


---

## Overview

This file is located at `tests/unit_tests/indicators/test_volatility_ratio.py` within the repository.

**Classes defined:** TestVolatilityCompressionRatio

**Functions defined:** setup, test_name_returns_expected_string, test_str_repr_returns_expected_string, test_initialized_without_inputs_returns_false, test_initialized_with_required_inputs_returns_true, test_handle_bar_updates_indicator, test_value_with_no_inputs_returns_none, test_value_with_epsilon_inputs_returns_expected_value, test_value_with_one_ones_input_returns_expected_value, test_value_with_one_input_returns_expected_value and 4 more

**Import statements:** 5


---

## Detailed Analysis

### Classes

#### `TestVolatilityCompressionRatio`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_initialized_without_inputs_returns_false(self)`


#### `test_initialized_with_required_inputs_returns_true(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_no_inputs_returns_none(self)`


#### `test_value_with_epsilon_inputs_returns_expected_value(self)`


#### `test_value_with_one_ones_input_returns_expected_value(self)`


#### `test_value_with_one_input_returns_expected_value(self)`


#### `test_value_with_three_inputs_returns_expected_value(self)`


#### `test_value_with_close_on_high_returns_expected_value(self)`


#### `test_value_with_close_on_low_returns_expected_value(self)`


#### `test_reset_successfully_returns_indicator_to_fresh_state(self)`


### Imports

- `import sys`
- `import pytest`
- `from nautilus_trader.indicators import VolatilityRatio`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_volatility_ratio import TestVolatilityCompressionRatio
```


---

## Related Files

This file imports from the following modules:

- `import sys`
- `import pytest`
- `from nautilus_trader.indicators import VolatilityRatio`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


