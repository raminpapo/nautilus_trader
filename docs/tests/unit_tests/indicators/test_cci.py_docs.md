# Documentation: `tests/unit_tests/indicators/test_cci.py`
**Generated:** 2025-11-15T19:40:09.179621Z
**File Size:** 3250 bytes
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

- **Path:** `tests/unit_tests/indicators/test_cci.py`
- **Size:** 3,250 bytes
- **Lines:** 85
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
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

import numpy as np

from nautilus_trader.indicators import CommodityChannelIndex
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestCommodityChannelIndex:
    def setup(self):
        # Fixture Setup
        self.period = 10
        self.cci = CommodityChannelIndex(period=self.period)

    def test_init(self):
        assert not self.cci.initialized
        assert not self.cci.has_inputs
        assert self.cci.period == self.period
        assert self.cci.scalar == 0.015
        assert self.cci._mad == 0
        assert self.cci.value == 0

    def test_name_returns_expected_string(self):
        assert self.cci.name == "CommodityChannelIndex"

    def test_handle_bar_updates_indicator(self):
        for _ in range(self.period):
            self.cci.handle_bar(TestDataStubs.bar_5decimal())

        assert self.cci.has_inputs
        assert self.cci.scalar == 0.015
        assert self.cci._mad == 0
        assert np.isnan(self.cci.value)

    def test_value_with_one_input(self):
        self.cci.update_raw(0.18000, 0.01001, 0.13810)

        assert self.cci.scalar == 0.015
        assert self.cci._mad == 0
        assert self.cci.value == 0

    def test_value_with_ten_inputs(self):
        self.cci.update_raw(0.18000, 0.01001, 0.13810)
        self.cci.update_raw(0.14499, 0.136, 0.14131)
        self.cci.update_raw(0.155, 0.13945, 0.15)
        self.cci.update_raw(0.17, 0.1468, 0.15829)
        self.cci.update_raw(0.172, 0.15712, 0.15938)
        self.cci.update_raw(0.15937, 0.14352, 0.14564)
        self.cci.update_raw(0.15171, 0.14571, 0.148)
        self.cci.update_raw(0.15699, 0.148, 0.15456)
        self.cci.update_raw(0.15547, 0.14894, 0.15029)
        self.cci.update_raw(0.15199, 0.14908, 0.15181)

        assert self.cci.scalar == 0.015
        assert self.cci._mad == 0.008899733333333352
        assert self.cci.value == 27.284213259823147

    def test_reset(self):
        self.cci.update_raw(0.18000, 0.01001, 0.13810)

        self.cci.reset()

        assert not self.cci.initialized
        assert not self.cci.has_inputs
        assert self.cci.period == self.period
        assert self.cci.scalar == 0.015
        assert self.cci._mad == 0
        assert self.cci.value == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_cci.py` within the repository.

**Classes defined:** TestCommodityChannelIndex

**Functions defined:** setup, test_init, test_name_returns_expected_string, test_handle_bar_updates_indicator, test_value_with_one_input, test_value_with_ten_inputs, test_reset

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `TestCommodityChannelIndex`


### Functions

#### `setup(self)`


#### `test_init(self)`


#### `test_name_returns_expected_string(self)`


#### `test_handle_bar_updates_indicator(self)`


#### `test_value_with_one_input(self)`


#### `test_value_with_ten_inputs(self)`


#### `test_reset(self)`


### Imports

- `import numpy as np`
- `from nautilus_trader.indicators import CommodityChannelIndex`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_cci import TestCommodityChannelIndex
```


---

## Related Files

This file imports from the following modules:

- `import numpy as np`
- `from nautilus_trader.indicators import CommodityChannelIndex`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


