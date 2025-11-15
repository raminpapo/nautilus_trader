# Documentation: `tests/unit_tests/backtest/test_enhanced_fill_models.py`
**Generated:** 2025-11-15T19:40:08.962264Z
**File Size:** 10303 bytes
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

- **Path:** `tests/unit_tests/backtest/test_enhanced_fill_models.py`
- **Size:** 10,303 bytes
- **Lines:** 298
- **Extension:** `.py`
- **Type:** text
- **Imports:** 13
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
"""
Tests for the enhanced FillModel functionality with order book simulation.
"""

from nautilus_trader.backtest.models import BestPriceFillModel
from nautilus_trader.backtest.models import FillModel
from nautilus_trader.backtest.models import OneTickSlippageFillModel
from nautilus_trader.backtest.models import SizeAwareFillModel
from nautilus_trader.backtest.models import TwoTierFillModel
from nautilus_trader.common.component import TestClock
from nautilus_trader.core.rust.model import BookType
from nautilus_trader.model.book import OrderBook
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.execution import TestExecStubs


class TestEnhancedFillModels:
    def setup_method(self):
        # Common test setup
        self.clock = TestClock()
        self.instrument = TestInstrumentProvider.default_fx_ccy("AUD/USD")
        self.venue = Venue("SIM")

    def test_default_fill_model_returns_none(self):
        """
        Test that default FillModel returns None for simulation.
        """
        # Arrange
        fill_model = FillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        order = TestExecStubs.market_order(instrument=self.instrument)

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is None

    def test_best_price_fill_model_creates_unlimited_liquidity(self):
        """
        Test BestPriceFillModel creates OrderBook with unlimited liquidity at best
        prices.
        """
        # Arrange
        fill_model = BestPriceFillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        order = TestExecStubs.market_order(instrument=self.instrument)

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is not None
        assert isinstance(result, OrderBook)
        assert result.instrument_id == self.instrument.id
        assert result.book_type == BookType.L2_MBP

        # Check that there's liquidity at best prices
        bids = list(result.bids())
        asks = list(result.asks())

        assert len(bids) >= 1
        assert len(asks) >= 1
        assert bids[0].price == best_bid
        assert asks[0].price == best_ask
        assert bids[0].size() == 1_000_000  # UNLIMITED
        assert asks[0].size() == 1_000_000  # UNLIMITED

    def test_one_tick_slippage_model_creates_slippage(self):
        """
        Test OneTickSlippageFillModel creates OrderBook with guaranteed slippage.
        """
        # Arrange
        fill_model = OneTickSlippageFillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        order = TestExecStubs.market_order(instrument=self.instrument)

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is not None
        assert isinstance(result, OrderBook)

        bids = list(result.bids())
        asks = list(result.asks())

        # Should have exactly 1 level per side (one tick away from best)
        # No liquidity at best price guarantees slippage
        assert len(bids) == 1
        assert len(asks) == 1

        # Only level should be one tick away from best price with unlimited volume
        tick = self.instrument.price_increment
        assert bids[0].price == best_bid - tick
        assert asks[0].price == best_ask + tick
        assert bids[0].size() == 1_000_000
        assert asks[0].size() == 1_000_000

    def test_two_tier_fill_model_creates_tiered_liquidity(self):
        """
        Test TwoTierFillModel creates OrderBook with two-tier liquidity.
        """
        # Arrange
        fill_model = TwoTierFillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        order = TestExecStubs.market_order(instrument=self.instrument)

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is not None
        bids = list(result.bids())
        asks = list(result.asks())

        assert len(bids) >= 2
        assert len(asks) >= 2

        # First tier: 10 contracts at best price
        assert bids[0].price == best_bid
        assert asks[0].price == best_ask
        assert bids[0].size() == 10
        assert asks[0].size() == 10

        # Second tier: unlimited contracts one tick worse
        tick = self.instrument.price_increment
        assert bids[1].price == best_bid - tick
        assert asks[1].price == best_ask + tick
        assert bids[1].size() == 1_000_000
        assert asks[1].size() == 1_000_000

    def test_size_aware_fill_model_small_order(self):
        """
        Test SizeAwareFillModel handles small orders differently.
        """
        # Arrange
        fill_model = SizeAwareFillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        small_order = TestExecStubs.market_order(
            instrument=self.instrument,
            quantity=Quantity.from_int(5),
        )  # Small order

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            small_order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is not None
        bids = list(result.bids())
        asks = list(result.asks())

        # Small orders should get good liquidity at best prices
        assert len(bids) == 1
        assert len(asks) == 1
        assert bids[0].price == best_bid
        assert asks[0].price == best_ask
        assert bids[0].size() == 50
        assert asks[0].size() == 50

    def test_size_aware_fill_model_large_order(self):
        """
        Test SizeAwareFillModel handles large orders with price impact.
        """
        # Arrange
        fill_model = SizeAwareFillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        large_order = TestExecStubs.market_order(
            instrument=self.instrument,
            quantity=Quantity.from_int(50),
        )  # Large order

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            large_order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is not None
        bids = list(result.bids())
        asks = list(result.asks())

        # Large orders should experience price impact
        assert len(bids) >= 2
        assert len(asks) >= 2

        # First level: 10 contracts at best price
        assert bids[0].price == best_bid
        assert asks[0].price == best_ask
        assert bids[0].size() == 10
        assert asks[0].size() == 10

        # Second level: remainder at worse price
        tick = self.instrument.price_increment
        remaining_qty = large_order.quantity.as_double() - 10
        assert bids[1].price == best_bid - tick
        assert asks[1].price == best_ask + tick
        assert bids[1].size() == remaining_qty
        assert asks[1].size() == remaining_qty

    def test_backward_compatibility_with_existing_fill_model(self):
        """
        Test that existing FillModel behavior is preserved when simulation returns None.
        """
        # This test would require integration with the matching engine
        # For now, we just verify the method exists and returns None by default
        fill_model = FillModel()
        best_bid = Price.from_str("1.0000")
        best_ask = Price.from_str("1.0001")
        order = TestExecStubs.market_order(instrument=self.instrument)

        result = fill_model.get_orderbook_for_fill_simulation(
            self.instrument,
            order,
            best_bid,
            best_ask,
        )

        assert result is None  # Default behavior should return None

    def test_fill_model_with_different_instruments(self):
        """
        Test that fill models work with different instrument types.
        """
        # Arrange
        crypto_instrument = TestInstrumentProvider.btcusdt_binance()
        fill_model = BestPriceFillModel()
        best_bid = Price.from_str("50000.00")
        best_ask = Price.from_str("50001.00")
        order = TestExecStubs.market_order(instrument=crypto_instrument)

        # Act
        result = fill_model.get_orderbook_for_fill_simulation(
            crypto_instrument,
            order,
            best_bid,
            best_ask,
        )

        # Assert
        assert result is not None
        assert result.instrument_id == crypto_instrument.id

        bids = list(result.bids())
        asks = list(result.asks())
        assert bids[0].price == best_bid
        assert asks[0].price == best_ask
```


---

## Overview

This file is located at `tests/unit_tests/backtest/test_enhanced_fill_models.py` within the repository.

**Classes defined:** TestEnhancedFillModels

**Functions defined:** setup_method, test_default_fill_model_returns_none, test_best_price_fill_model_creates_unlimited_liquidity, test_one_tick_slippage_model_creates_slippage, test_two_tier_fill_model_creates_tiered_liquidity, test_size_aware_fill_model_small_order, test_size_aware_fill_model_large_order, test_backward_compatibility_with_existing_fill_model, test_fill_model_with_different_instruments

**Import statements:** 13


---

## Detailed Analysis

### Classes

#### `TestEnhancedFillModels`


### Functions

#### `setup_method(self)`


#### `test_default_fill_model_returns_none(self)`


#### `test_best_price_fill_model_creates_unlimited_liquidity(self)`


#### `test_one_tick_slippage_model_creates_slippage(self)`


#### `test_two_tier_fill_model_creates_tiered_liquidity(self)`


#### `test_size_aware_fill_model_small_order(self)`


#### `test_size_aware_fill_model_large_order(self)`


#### `test_backward_compatibility_with_existing_fill_model(self)`


#### `test_fill_model_with_different_instruments(self)`


### Imports

- `from nautilus_trader.backtest.models import BestPriceFillModel`
- `from nautilus_trader.backtest.models import FillModel`
- `from nautilus_trader.backtest.models import OneTickSlippageFillModel`
- `from nautilus_trader.backtest.models import SizeAwareFillModel`
- `from nautilus_trader.backtest.models import TwoTierFillModel`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.core.rust.model import BookType`
- `from nautilus_trader.model.book import OrderBook`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.execution import TestExecStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.backtest.test_enhanced_fill_models import TestEnhancedFillModels
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.backtest.models import BestPriceFillModel`
- `from nautilus_trader.backtest.models import FillModel`
- `from nautilus_trader.backtest.models import OneTickSlippageFillModel`
- `from nautilus_trader.backtest.models import SizeAwareFillModel`
- `from nautilus_trader.backtest.models import TwoTierFillModel`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.core.rust.model import BookType`
- `from nautilus_trader.model.book import OrderBook`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Price`

*... and 3 more*

**Directory:** `tests/unit_tests/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


