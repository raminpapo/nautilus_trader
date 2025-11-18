# Documentation: test_statistics_long_ratio.py

## File Metadata

- **Path**: `tests/unit_tests/analysis/test_statistics_long_ratio.py`
- **Size**: 4,875 bytes
- **Lines**: 153
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

from nautilus_trader.analysis import LongRatio
from nautilus_trader.common.component import TestClock
from nautilus_trader.common.factories import OrderFactory
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.model.position import Position
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.events import TestEventStubs


ETHUSDT_PERP_BINANCE = TestInstrumentProvider.ethusdt_perp_binance()


class TestLongRatioPortfolioStatistics:
    def setup(self):
        # Fixture Setup
        self.order_factory = OrderFactory(
            trader_id=TraderId("TESTER-000"),
            strategy_id=StrategyId("S-001"),
            clock=TestClock(),
        )

    def test_name_returns_expected_returns_expected(self):
        # Arrange
        stat = LongRatio()

        # Act
        result = stat.name

        # Assert
        assert result == "Long Ratio"

    def test_calculate_given_empty_list_returns_none(self):
        # Arrange
        stat = LongRatio()

        # Act
        result = stat.calculate_from_positions([])

        # Assert
        assert result is None

    def test_calculate_given_two_long_returns_expected(self):
        # Arrange
        stat = LongRatio()

        order1 = self.order_factory.market(
            ETHUSDT_PERP_BINANCE.id,
            OrderSide.BUY,
            Quantity.from_int(1),
        )

        order2 = self.order_factory.market(
            ETHUSDT_PERP_BINANCE.id,
            OrderSide.SELL,
            Quantity.from_int(1),
        )

        fill1 = TestEventStubs.order_filled(
            order1,
            instrument=ETHUSDT_PERP_BINANCE,
            position_id=PositionId("P-1"),
            strategy_id=StrategyId("S-001"),
            last_px=Price.from_int(10_000),
        )

        fill2 = TestEventStubs.order_filled(
            order2,
            instrument=ETHUSDT_PERP_BINANCE,
            position_id=PositionId("P-2"),
            strategy_id=StrategyId("S-001"),
            last_px=Price.from_int(10_000),
        )

        position1 = Position(instrument=ETHUSDT_PERP_BINANCE, fill=fill1)
        position1.apply(fill2)

        position2 = Position(instrument=ETHUSDT_PERP_BINANCE, fill=fill1)
        position2.apply(fill2)

        data = [position1, position2]

        # Act
        result = stat.calculate_from_positions(data)

        # Assert
        assert result == 1.0

    def test_calculate_given_one_long_one_short_returns_expected(self):
        # Arrange
        stat = LongRatio()

        order1 = self.order_factory.market(
            ETHUSDT_PERP_BINANCE.id,
            OrderSide.BUY,
            Quantity.from_int(1),
        )

        order2 = self.order_factory.market(
            ETHUSDT_PERP_BINANCE.id,
            OrderSide.SELL,
            Quantity.from_int(1),
        )

        fill1 = TestEventStubs.order_filled(
            order1,
            instrument=ETHUSDT_PERP_BINANCE,
            position_id=PositionId("P-1"),
            strategy_id=StrategyId("S-001"),
            last_px=Price.from_int(10_000),
        )

        fill2 = TestEventStubs.order_filled(
            order2,
            instrument=ETHUSDT_PERP_BINANCE,
            position_id=PositionId("P-2"),
            strategy_id=StrategyId("S-001"),
            last_px=Price.from_int(10_000),
        )

        position1 = Position(instrument=ETHUSDT_PERP_BINANCE, fill=fill1)
        position1.apply(fill2)

        position2 = Position(instrument=ETHUSDT_PERP_BINANCE, fill=fill2)
        position2.apply(fill1)

        data = [position1, position2]

        # Act
        result = stat.calculate_from_positions(data)

        # Assert
        assert result == 0.5

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestLongRatioPortfolioStatistics`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Classs**: `TestLongRatioPortfolioStatistics`
**Imports**: `nautilus_trader.analysis`, `nautilus_trader.common.component`, `nautilus_trader.common.factories`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `nautilus_trader.model.position`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.events`

## Related Files

This file is located in `tests/unit_tests/analysis/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/analysis/test_statistics_long_ratio.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.124093Z*
