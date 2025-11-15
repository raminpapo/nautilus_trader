# Documentation: `tests/unit_tests/common/test_generators.py`
**Generated:** 2025-11-15T19:40:09.055357Z
**File Size:** 5738 bytes
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

- **Path:** `tests/unit_tests/common/test_generators.py`
- **Size:** 5,738 bytes
- **Lines:** 165
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9
- **Classes:** 3
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

from nautilus_trader.common.component import TestClock
from nautilus_trader.common.generators import ClientOrderIdGenerator
from nautilus_trader.common.generators import OrderListIdGenerator
from nautilus_trader.common.generators import PositionIdGenerator
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import OrderListId
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import TraderId


class TestOrderIdGenerator:
    def setup(self):
        # Fixture Setup
        self.generator = ClientOrderIdGenerator(
            trader_id=TraderId("TRADER-001"),
            strategy_id=StrategyId("SCALPER-001"),
            clock=TestClock(),
        )

    def test_generate_order_id(self):
        # Arrange, Act
        result1 = self.generator.generate()
        result2 = self.generator.generate()
        result3 = self.generator.generate()

        # Assert
        assert result1 == ClientOrderId("O-19700101-000000-001-001-1")
        assert result2 == ClientOrderId("O-19700101-000000-001-001-2")
        assert result3 == ClientOrderId("O-19700101-000000-001-001-3")

    def test_reset_id_generator(self):
        # Arrange
        self.generator.generate()
        self.generator.generate()
        self.generator.generate()

        # Act
        self.generator.reset()
        result1 = self.generator.generate()

        # Assert
        assert result1 == ClientOrderId("O-19700101-000000-001-001-1")


class TestOrderListIdGenerator:
    def setup(self):
        # Fixture Setup
        self.generator = OrderListIdGenerator(
            trader_id=TraderId("TRADER-001"),
            strategy_id=StrategyId("SCALPER-001"),
            clock=TestClock(),
        )

    def test_initial_count(self):
        # Arrange, Act, Assert
        assert self.generator.count == 0

    def test_set_count(self):
        self.generator.set_count(5)

        assert self.generator.count == 5

    def test_generate(self):
        # Arrange
        self.generator.set_count(5)

        # Act
        order_list_id1 = self.generator.generate()
        order_list_id2 = self.generator.generate()
        order_list_id3 = self.generator.generate()

        # Assert
        assert order_list_id1 == OrderListId("OL-19700101-000000-001-001-6")
        assert order_list_id2 == OrderListId("OL-19700101-000000-001-001-7")
        assert order_list_id3 == OrderListId("OL-19700101-000000-001-001-8")

    def test_reset(self):
        # Arrange
        self.generator.set_count(5)

        # Act
        self.generator.reset()

        # Assert
        assert self.generator.count == 0


class TestPositionIdGenerator:
    def setup(self):
        # Fixture Setup
        self.generator = PositionIdGenerator(
            trader_id=TraderId("TRADER-001"),
            clock=TestClock(),
        )

    def test_generate_position_id(self):
        # Arrange, Act
        result1 = self.generator.generate(StrategyId("S-002"))
        result2 = self.generator.generate(StrategyId("S-002"))
        result3 = self.generator.generate(StrategyId("S-002"))

        # Assert
        assert result1 == PositionId("P-19700101-000000-001-002-1")
        assert result2 == PositionId("P-19700101-000000-001-002-2")
        assert result3 == PositionId("P-19700101-000000-001-002-3")

    def test_generate_position_id_with_flip_appends_correctly(self):
        # Arrange, Act
        result1 = self.generator.generate(StrategyId("S-001"))
        result2 = self.generator.generate(StrategyId("S-002"), flipped=True)
        result3 = self.generator.generate(StrategyId("S-001"), flipped=True)

        # Assert
        assert result1 == PositionId("P-19700101-000000-001-001-1")
        assert result2 == PositionId("P-19700101-000000-001-002-1F")
        assert result3 == PositionId("P-19700101-000000-001-001-2F")

    def test_set_count_with_valid_strategy_identifier(self):
        # Arrange
        strategy_id = StrategyId("S-001")

        # Act
        self.generator.set_count(strategy_id, 5)

        # Assert
        assert self.generator.get_count(strategy_id) == 5

    def test_get_count_when_strategy_id_has_no_count_returns_zero(self):
        # Arrange
        strategy_id = StrategyId("S-001")

        # Act
        result = self.generator.get_count(strategy_id)

        # Assert
        assert result == 0

    def test_reset(self):
        # Arrange
        self.generator.generate(StrategyId("S-002"))
        self.generator.generate(StrategyId("S-002"))
        self.generator.generate(StrategyId("S-002"))

        # Act
        self.generator.reset()
        result1 = self.generator.generate(StrategyId("S-002"))

        # Assert
        assert result1 == PositionId("P-19700101-000000-001-002-1")
```


---

## Overview

This file is located at `tests/unit_tests/common/test_generators.py` within the repository.

**Classes defined:** TestOrderIdGenerator, TestOrderListIdGenerator, TestPositionIdGenerator

**Functions defined:** setup, test_generate_order_id, test_reset_id_generator, setup, test_initial_count, test_set_count, test_generate, test_reset, setup, test_generate_position_id and 4 more

**Import statements:** 9


---

## Detailed Analysis

### Classes

#### `TestOrderIdGenerator`


#### `TestOrderListIdGenerator`


#### `TestPositionIdGenerator`


### Functions

#### `setup(self)`


#### `test_generate_order_id(self)`


#### `test_reset_id_generator(self)`


#### `setup(self)`


#### `test_initial_count(self)`


#### `test_set_count(self)`


#### `test_generate(self)`


#### `test_reset(self)`


#### `setup(self)`


#### `test_generate_position_id(self)`


#### `test_generate_position_id_with_flip_appends_correctly(self)`


#### `test_set_count_with_valid_strategy_identifier(self)`


#### `test_get_count_when_strategy_id_has_no_count_returns_zero(self)`


#### `test_reset(self)`


### Imports

- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.common.generators import ClientOrderIdGenerator`
- `from nautilus_trader.common.generators import OrderListIdGenerator`
- `from nautilus_trader.common.generators import PositionIdGenerator`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import OrderListId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import TraderId`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_generators import TestOrderIdGenerator
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.common.generators import ClientOrderIdGenerator`
- `from nautilus_trader.common.generators import OrderListIdGenerator`
- `from nautilus_trader.common.generators import PositionIdGenerator`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import OrderListId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import TraderId`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


