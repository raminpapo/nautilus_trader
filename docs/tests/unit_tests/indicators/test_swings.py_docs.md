# Documentation: `tests/unit_tests/indicators/test_swings.py`
**Generated:** 2025-11-15T19:40:09.214159Z
**File Size:** 6761 bytes
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

- **Path:** `tests/unit_tests/indicators/test_swings.py`
- **Size:** 6,761 bytes
- **Lines:** 169
- **Extension:** `.py`
- **Type:** text
- **Imports:** 10
- **Classes:** 1
- **Functions:** 11

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

from nautilus_trader.indicators import Swings
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarSpecification
from nautilus_trader.model.data import BarType
from nautilus_trader.model.enums import BarAggregation
from nautilus_trader.model.enums import PriceType
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.test_kit.stubs.data import UNIX_EPOCH
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


AUDUSD_SIM = TestIdStubs.audusd_id()
ONE_MIN_BID = BarSpecification(1, BarAggregation.MINUTE, PriceType.BID)
AUDUSD_1_MIN_BID = BarType(AUDUSD_SIM, ONE_MIN_BID)


class TestSwings:
    def setup(self):
        # Fixture Setup
        self.swings = Swings(3)

    def test_name_returns_expected_name(self):
        # Arrange, Act, Assert
        assert self.swings.name == "Swings"

    def test_str_repr_returns_expected_string(self):
        # Arrange, Act, Assert
        assert str(self.swings) == "Swings(3)"
        assert repr(self.swings) == "Swings(3)"

    def test_instantiate_returns_expected_property_values(self):
        # Arrange, Act, Assert
        assert self.swings.period == 3
        assert self.swings.initialized is False
        assert self.swings.direction == 0
        assert self.swings.changed is False
        assert self.swings.since_high == 0
        assert self.swings.since_low == 0

    def test_handle_bar(self):
        # Arrange
        bar = Bar(
            AUDUSD_1_MIN_BID,
            Price.from_str("1.00001"),
            Price.from_str("1.00004"),
            Price.from_str("1.00000"),
            Price.from_str("1.00003"),
            Quantity.from_int(100_000),
            0,
            0,
        )

        # Act
        self.swings.handle_bar(bar)

        # Assert
        assert self.swings.has_inputs

    def test_determine_swing_high(self):
        # Arrange
        self.swings.update_raw(1.00010, 1.00000, UNIX_EPOCH)
        self.swings.update_raw(1.00030, 1.00010, UNIX_EPOCH)
        self.swings.update_raw(1.00040, 1.00020, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00030, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00040, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00040, UNIX_EPOCH)

        # Act, Assert
        assert self.swings.direction == 1
        assert self.swings.high_price == 1.0006

    def test_determine_swing_low(self):
        # Arrange
        self.swings.update_raw(1.00100, 1.00080, UNIX_EPOCH)
        self.swings.update_raw(1.00080, 1.00060, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00040, UNIX_EPOCH)
        self.swings.update_raw(1.00040, 1.00030, UNIX_EPOCH)
        self.swings.update_raw(1.00020, 1.00010, UNIX_EPOCH)
        self.swings.update_raw(1.00020, 1.00020, UNIX_EPOCH)

        # Act, Assert
        assert self.swings.direction == -1
        assert self.swings.low_price == 1.0001

    def test_swing_change_high_to_low(self):
        # Arrange
        self.swings.update_raw(1.00010, 1.00000, UNIX_EPOCH)
        self.swings.update_raw(1.00020, 1.00010, UNIX_EPOCH)
        self.swings.update_raw(1.00030, 1.00020, UNIX_EPOCH)
        self.swings.update_raw(1.00040, 1.00030, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00040, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00050, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00040, UNIX_EPOCH)

        # Act, Assert
        assert self.swings.direction == -1
        assert self.swings.changed
        assert self.swings.since_low == 0
        assert self.swings.since_high == 1
        assert self.swings.length == 0  # Just changed

    def test_swing_change_low_to_high(self):
        # Arrange
        self.swings.update_raw(1.00090, 1.00080, UNIX_EPOCH)
        self.swings.update_raw(1.00080, 1.00070, UNIX_EPOCH)
        self.swings.update_raw(1.00070, 1.00060, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00050, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00040, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00050, UNIX_EPOCH)

        # Act, Assert
        assert self.swings.direction == 1
        assert self.swings.changed
        assert self.swings.since_high == 0
        assert self.swings.since_low == 1
        assert self.swings.length == 0  # Just changed

    def test_swing_changes(self):
        # Arrange
        self.swings.update_raw(1.00010, 1.00000, UNIX_EPOCH)
        self.swings.update_raw(1.00020, 1.00010, UNIX_EPOCH)
        self.swings.update_raw(1.00030, 1.00020, UNIX_EPOCH)
        self.swings.update_raw(1.00040, 1.00030, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00040, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00050, UNIX_EPOCH)
        self.swings.update_raw(1.00050, 1.00040, UNIX_EPOCH)
        self.swings.update_raw(1.00040, 1.00030, UNIX_EPOCH)
        self.swings.update_raw(1.00030, 1.00020, UNIX_EPOCH)
        self.swings.update_raw(1.00020, 1.00010, UNIX_EPOCH)
        self.swings.update_raw(1.00010, 1.00000, UNIX_EPOCH)
        self.swings.update_raw(1.00020, 1.00010, UNIX_EPOCH)
        self.swings.update_raw(1.00030, 1.00020, UNIX_EPOCH)
        self.swings.update_raw(1.00040, 1.00030, UNIX_EPOCH)

        # Act, Assert
        assert self.swings.direction == 1
        assert self.swings.since_low == 3
        assert self.swings.since_high == 0
        assert self.swings.length == 0.00039999999999995595
        assert self.swings.initialized

    def test_reset(self):
        # Arrange
        self.swings.update_raw(1.00100, 1.00080, UNIX_EPOCH)
        self.swings.update_raw(1.00080, 1.00060, UNIX_EPOCH)
        self.swings.update_raw(1.00060, 1.00040, UNIX_EPOCH)

        # Act
        self.swings.reset()

        # Assert
        assert self.swings.has_inputs == 0
        assert self.swings.direction == 0
```


---

## Overview

This file is located at `tests/unit_tests/indicators/test_swings.py` within the repository.

**Classes defined:** TestSwings

**Functions defined:** setup, test_name_returns_expected_name, test_str_repr_returns_expected_string, test_instantiate_returns_expected_property_values, test_handle_bar, test_determine_swing_high, test_determine_swing_low, test_swing_change_high_to_low, test_swing_change_low_to_high, test_swing_changes and 1 more

**Import statements:** 10


---

## Detailed Analysis

### Classes

#### `TestSwings`


### Functions

#### `setup(self)`


#### `test_name_returns_expected_name(self)`


#### `test_str_repr_returns_expected_string(self)`


#### `test_instantiate_returns_expected_property_values(self)`


#### `test_handle_bar(self)`


#### `test_determine_swing_high(self)`


#### `test_determine_swing_low(self)`


#### `test_swing_change_high_to_low(self)`


#### `test_swing_change_low_to_high(self)`


#### `test_swing_changes(self)`


#### `test_reset(self)`


### Imports

- `from nautilus_trader.indicators import Swings`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarSpecification`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.enums import BarAggregation`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.test_kit.stubs.data import UNIX_EPOCH`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.indicators.test_swings import TestSwings
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.indicators import Swings`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarSpecification`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.enums import BarAggregation`
- `from nautilus_trader.model.enums import PriceType`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.test_kit.stubs.data import UNIX_EPOCH`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`

**Directory:** `tests/unit_tests/indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


