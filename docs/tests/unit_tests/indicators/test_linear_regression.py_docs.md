# Documentation: `tests/unit_tests/indicators/test_linear_regression.py`
**Generated:** 2025-11-15T19:40:09.197978Z
**File Size:** 4387 bytes
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

- **Path:** `tests/unit_tests/indicators/test_linear_regression.py`
- **Size:** 4,387 bytes
- **Lines:** 101
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Classes:** 1
- **Functions:** 7

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

import math

import pytest

from nautilus_trader.indicators import LinearRegression
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestLinearRegression:
    def setup(self):
        # Fixture Setup
        self.period = 4
        self.linear_regression = LinearRegression(period=self.period)

    def test_init(self):
        assert not self.linear_regression.initialized
        assert not self.linear_regression.has_inputs
        assert self.linear_regression.period == self.period
        assert self.linear_regression.value == 0
        assert self.linear_regression.slope == 0
        assert self.linear_regression.intercept == 0
        assert self.linear_regression.degree == 0
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 0

    def test_name_returns_expected_string(self):
        assert self.linear_regression.name == "LinearRegression"

    def test_handle_bar_updates_indicator(self):
        for _ in range(self.period):
            self.linear_regression.handle_bar(TestDataStubs.bar_5decimal())

        assert self.linear_regression.has_inputs
        assert self.linear_regression.value == pytest.approx(1.0000300000000002, rel=1e-9)
        assert self.linear_regression.slope == 0.0
        assert self.linear_regression.intercept == pytest.approx(1.0000300000000002, rel=1e-9)
        assert self.linear_regression.degree == 0.0
        assert self.linear_regression.cfo == pytest.approx(2.220379437867177e-14, rel=1e-9)
        assert -math.inf == self.linear_regression.R2

    def test_value_with_one_input(self):
        self.linear_regression.update_raw(1.00000)
        assert self.linear_regression.value == 0
        assert self.linear_regression.slope == 0
        assert self.linear_regression.intercept == 0
        assert self.linear_regression.degree == 0
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 0

    def test_value_with_ten_inputs(self):
        self.linear_regression.update_raw(1.00000)
        self.linear_regression.update_raw(2.00000)
        self.linear_regression.update_raw(3.00000)
        self.linear_regression.update_raw(4.00000)
        self.linear_regression.update_raw(5.00000)
        self.linear_regression.update_raw(6.00000)
        self.linear_regression.update_raw(7.00000)
        self.linear_regression.update_raw(8.00000)
        self.linear_regression.update_raw(9.00000)
        self.linear_regression.update_raw(10.00000)

        assert self.linear_regression.value == 10
        assert self.linear_regression.slope == 1
        assert self.linear_regression.intercept == 6
        assert self.linear_regression.degree == 45
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 1

    def test_reset(self):
        self.linear_regression.update_raw(1.00000)

        self.linear_regression.reset()

        assert not self.linear_regression.initialized
        assert not self.linear_regression.has_inputs
        assert self.linear_regression.period == self.period
        assert self.linear_regression.value == 0
        assert self.linear_regression.slope == 0
        assert self.linear_regression.intercept == 0
        assert self.linear_regression.degree == 0
        assert self.linear_regression.cfo == 0
        assert self.linear_regression.R2 == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_linear_regression.py` within the repository.

**Classes defined:** TestLinearRegression

**Functions defined:** setup, test_init, test_name_returns_expected_string, test_handle_bar_updates_indicator, test_value_with_one_input, test_value_with_ten_inputs, test_reset

**Import statements:** 5


---

## Detailed Analysis

### Classes

#### `TestLinearRegression`


### Functions

#### `setup(self)`


#### `test_init(self)`


#### `test_name_returns_expected_string(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input(self)`


#### `test_value_with_ten_inputs(self)`


#### `test_reset(self)`


### Imports

- `import math`
- `import pytest`
- `from nautilus_trader.indicators import LinearRegression`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_linear_regression import TestLinearRegression
```


---

## Related Files

This file imports from the following modules:

- `import math`
- `import pytest`
- `from nautilus_trader.indicators import LinearRegression`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


