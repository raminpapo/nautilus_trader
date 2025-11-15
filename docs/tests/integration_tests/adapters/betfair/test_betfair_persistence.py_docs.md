# Documentation: `tests/integration_tests/adapters/betfair/test_betfair_persistence.py`
**Generated:** 2025-11-15T19:40:07.566616Z
**File Size:** 4076 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/test_betfair_persistence.py`
- **Size:** 4,076 bytes
- **Lines:** 111
- **Extension:** `.py`
- **Type:** text
- **Imports:** 13
- **Classes:** 1
- **Functions:** 5

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

from nautilus_trader.adapters.betfair.data_types import BetfairStartingPrice
from nautilus_trader.adapters.betfair.data_types import BetfairTicker
from nautilus_trader.adapters.betfair.data_types import BSPOrderBookDelta
from nautilus_trader.core.rust.model import BookAction
from nautilus_trader.core.rust.model import OrderSide
from nautilus_trader.model.data import BookOrder
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.serialization.arrow.serializer import ArrowSerializer
from nautilus_trader.test_kit.mocks.data import setup_catalog
from tests.integration_tests.adapters.betfair.test_kit import betting_instrument
from tests.integration_tests.adapters.betfair.test_kit import load_betfair_data


class TestBetfairPersistence:
    @pytest.fixture(autouse=True)
    def setup_method(self, tmp_path):
        self.catalog = setup_catalog(protocol="memory", path=tmp_path / "catalog")
        self.fs = self.catalog.fs
        self.instrument = betting_instrument()

    def test_bsp_delta_serialize(self):
        # Arrange
        bsp_delta = BSPOrderBookDelta(
            instrument_id=self.instrument.id,
            action=BookAction.UPDATE,
            order=BookOrder(
                price=Price.from_str("0.990099"),
                size=Quantity.from_str("60.07"),
                side=OrderSide.BUY,
                order_id=1,
            ),
            flags=0,
            sequence=0,
            ts_event=1635313844283000000,
            ts_init=1635313844283000000,
        )

        # Act
        self.catalog.write_data([bsp_delta, bsp_delta])
        values = self.catalog.custom_data(BSPOrderBookDelta)

        # Assert
        assert len(values) == 2
        assert values[1] == bsp_delta

    def test_betfair_starting_price_to_from_dict(self):
        # Arrange
        bsp = BetfairStartingPrice.from_dict(
            {
                "type": "BetfairStartingPrice",
                "instrument_id": self.instrument.id.value,
                "bsp": 1.20,
                "ts_event": 1635313844283000000,
                "ts_init": 1635313844283000000,
            },
        )

        # Act
        values = bsp.to_dict(bsp)
        result = bsp.from_dict(values)

        # Assert
        assert values["type"] == "BetfairStartingPrice"
        assert result.bsp == bsp.bsp

    def test_betfair_starting_price_serialization(self):
        # Arrange
        bsp = BetfairStartingPrice.from_dict(
            {
                "type": "BetfairStartingPrice",
                "instrument_id": self.instrument.id.value,
                "bsp": 1.20,
                "ts_event": 1635313844283000000,
                "ts_init": 1635313844283000000,
            },
        )

        # Act
        serialized = ArrowSerializer.serialize(bsp)
        [result] = ArrowSerializer.deserialize(BetfairStartingPrice, serialized)

        # Assert
        assert result.bsp == bsp.bsp

    def test_query_custom_type(self):
        # Arrange
        load_betfair_data(self.catalog)

        # Act
        data = self.catalog.query(BetfairTicker)

        # Assert
        assert len(data) == 210
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/test_betfair_persistence.py` within the repository.

**Classes defined:** TestBetfairPersistence

**Functions defined:** setup_method, test_bsp_delta_serialize, test_betfair_starting_price_to_from_dict, test_betfair_starting_price_serialization, test_query_custom_type

**Import statements:** 13


---

## Detailed Analysis

### Classes

#### `TestBetfairPersistence`


### Functions

#### `setup_method(self, tmp_path)`


#### `test_bsp_delta_serialize(self)`


#### `test_betfair_starting_price_to_from_dict(self)`


#### `test_betfair_starting_price_serialization(self)`


#### `test_query_custom_type(self)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.betfair.data_types import BetfairStartingPrice`
- `from nautilus_trader.adapters.betfair.data_types import BetfairTicker`
- `from nautilus_trader.adapters.betfair.data_types import BSPOrderBookDelta`
- `from nautilus_trader.core.rust.model import BookAction`
- `from nautilus_trader.core.rust.model import OrderSide`
- `from nautilus_trader.model.data import BookOrder`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.serialization.arrow.serializer import ArrowSerializer`
- `from nautilus_trader.test_kit.mocks.data import setup_catalog`
- `from tests.integration_tests.adapters.betfair.test_kit import betting_instrument`
- `from tests.integration_tests.adapters.betfair.test_kit import load_betfair_data`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.betfair.test_betfair_persistence import TestBetfairPersistence
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.betfair.data_types import BetfairStartingPrice`
- `from nautilus_trader.adapters.betfair.data_types import BetfairTicker`
- `from nautilus_trader.adapters.betfair.data_types import BSPOrderBookDelta`
- `from nautilus_trader.core.rust.model import BookAction`
- `from nautilus_trader.core.rust.model import OrderSide`
- `from nautilus_trader.model.data import BookOrder`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.serialization.arrow.serializer import ArrowSerializer`

*... and 3 more*

**Directory:** `tests/integration_tests/adapters/betfair`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


