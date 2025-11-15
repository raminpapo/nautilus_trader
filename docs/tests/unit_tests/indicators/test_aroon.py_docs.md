# Documentation: `tests/unit_tests/indicators/test_aroon.py`
**Generated:** 2025-11-15T19:40:09.173815Z
**File Size:** 4035 bytes
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

- **Path:** `tests/unit_tests/indicators/test_aroon.py`
- **Size:** 4,035 bytes
- **Lines:** 112
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 1
- **Functions:** 9

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

from nautilus_trader.indicators import AroonOscillator
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestAroonOscillator:
    def setup(self):
        # Fixture Setup
        self.aroon = AroonOscillator(10)

    def test_name_returns_expected_string(self):
        # Arrange, Act, Assert
        assert self.aroon.name == "AroonOscillator"

    def test_period(self):
        # Arrange, Act, Assert
        assert self.aroon.period == 10

    def test_initialized_without_inputs_returns_false(self):
        # Arrange, Act, Assert
        assert self.aroon.initialized is False

    def test_initialized_with_required_inputs_returns_true(self):
        # Arrange, Act
        for _ in range(20):
            self.aroon.update_raw(110.08, 109.61)

        # Assert
        assert self.aroon.initialized is True

    def test_handle_bar_updates_indicator(self):
        # Arrange
        indicator = AroonOscillator(10)
        bar = TestDataStubs.bar_5decimal()

        # Act
        indicator.handle_bar(bar)

        # Assert
        assert indicator.has_inputs
        assert indicator.aroon_up == 100.0
        assert indicator.aroon_down == 100.0
        assert indicator.value == 0

    def test_value_with_one_input(self):
        # Arrange, Act
        self.aroon.update_raw(110.08, 109.61)

        # Assert
        assert self.aroon.aroon_up == 100.0
        assert self.aroon.aroon_down == 100.0
        assert self.aroon.value == 0

    def test_value_with_twenty_inputs(self):
        # Arrange, Act
        self.aroon.update_raw(110.08, 109.61)
        self.aroon.update_raw(110.15, 109.91)
        self.aroon.update_raw(110.1, 109.73)
        self.aroon.update_raw(110.06, 109.77)
        self.aroon.update_raw(110.29, 109.88)
        self.aroon.update_raw(110.53, 110.29)
        self.aroon.update_raw(110.61, 110.26)
        self.aroon.update_raw(110.28, 110.17)
        self.aroon.update_raw(110.3, 110.0)
        self.aroon.update_raw(110.25, 110.01)
        self.aroon.update_raw(110.25, 109.81)
        self.aroon.update_raw(109.92, 109.71)
        self.aroon.update_raw(110.21, 109.84)
        self.aroon.update_raw(110.08, 109.95)
        self.aroon.update_raw(110.2, 109.96)
        self.aroon.update_raw(110.16, 109.95)
        self.aroon.update_raw(109.99, 109.75)
        self.aroon.update_raw(110.2, 109.73)
        self.aroon.update_raw(110.1, 109.81)
        self.aroon.update_raw(110.04, 109.96)

        # Assert
        assert self.aroon.aroon_up == 9.999999999999998
        assert self.aroon.aroon_down == 19.999999999999996
        assert self.aroon.value == -9.999999999999998

    def test_reset_successfully_returns_indicator_to_fresh_state(self):
        # Arrange
        for _ in range(1000):
            self.aroon.update_raw(110.08, 109.61)

        # Act
        self.aroon.reset()

        # Assert
        assert not self.aroon.initialized
        assert self.aroon.aroon_up == 0
        assert self.aroon.aroon_down == 0
        assert self.aroon.value == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_aroon.py` within the repository.

**Classes defined:** TestAroonOscillator

**Functions defined:** setup, test_name_returns_expected_string, test_period, test_initialized_without_inputs_returns_false, test_initialized_with_required_inputs_returns_true, test_handle_bar_updates_indicator, test_value_with_one_input, test_value_with_twenty_inputs, test_reset_successfully_returns_indicator_to_fresh_state

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `TestAroonOscillator`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_string(self)`


#### `test_period(self)`


#### `test_initialized_without_inputs_returns_false(self)`


#### `test_initialized_with_required_inputs_returns_true(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input(self)`


#### `test_value_with_twenty_inputs(self)`


#### `test_reset_successfully_returns_indicator_to_fresh_state(self)`


### Imports

- `from nautilus_trader.indicators import AroonOscillator`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_aroon import TestAroonOscillator
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.indicators import AroonOscillator`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


