# Documentation: test_betfair_persistence.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/test_betfair_persistence.py`
- **Size**: 4,076 bytes
- **Lines**: 112
- **Language**: Python

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestBetfairPersistence`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Classs**: `TestBetfairPersistence`
**Imports**: `nautilus_trader.adapters.betfair.data_types`, `nautilus_trader.core.rust.model`, `nautilus_trader.model.data`, `nautilus_trader.model.objects`, `nautilus_trader.serialization.arrow.serializer`, `nautilus_trader.test_kit.mocks.data`, `pytest`, `tests.integration_tests.adapters.betfair.test_kit`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/test_betfair_persistence.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:55:06.581164Z*
