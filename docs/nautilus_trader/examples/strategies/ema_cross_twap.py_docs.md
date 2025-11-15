# Documentation: `nautilus_trader/examples/strategies/ema_cross_twap.py`
**Generated:** 2025-11-15T19:40:04.875300Z
**File Size:** 12057 bytes
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

- **Path:** `nautilus_trader/examples/strategies/ema_cross_twap.py`
- **Size:** 12,057 bytes
- **Lines:** 363
- **Extension:** `.py`
- **Type:** text
- **Imports:** 24
- **Classes:** 2
- **Functions:** 17

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

from decimal import Decimal
from typing import Any

import pandas as pd

from nautilus_trader.common.enums import LogColor
from nautilus_trader.config import PositiveFloat
from nautilus_trader.config import PositiveInt
from nautilus_trader.config import StrategyConfig
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.core.data import Data
from nautilus_trader.core.message import Event
from nautilus_trader.indicators import ExponentialMovingAverage
from nautilus_trader.model.book import OrderBook
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarType
from nautilus_trader.model.data import OrderBookDeltas
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.identifiers import ExecAlgorithmId
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.model.orders import MarketOrder
from nautilus_trader.trading.strategy import Strategy


# *** THIS IS A TEST STRATEGY WITH NO ALPHA ADVANTAGE WHATSOEVER. ***
# *** IT IS NOT INTENDED TO BE USED TO TRADE LIVE WITH REAL MONEY. ***


class EMACrossTWAPConfig(StrategyConfig, frozen=True):
    """
    Configuration for ``EMACrossTWAP`` instances.

    Parameters
    ----------
    instrument_id : InstrumentId
        The instrument ID for the strategy.
    bar_type : BarType
        The bar type for the strategy.
    trade_size : Decimal
        The position size per trade.
    fast_ema_period : PositiveInt, default 10
        The fast EMA period.
    slow_ema_period : PositiveInt, default 20
        The slow EMA period.
    twap_horizon_secs : PositiveFloat, default 30.0
        The TWAP horizon (seconds) over which the algorithm will execute.
    twap_interval_secs : PositiveFloat, default 3.0
        The TWAP interval (seconds) between orders.
    close_positions_on_stop : bool, default True
        If all open positions should be closed on strategy stop.

    """

    instrument_id: InstrumentId
    bar_type: BarType
    trade_size: Decimal
    fast_ema_period: PositiveInt = 10
    slow_ema_period: PositiveInt = 20
    twap_horizon_secs: PositiveFloat = 30.0
    twap_interval_secs: PositiveFloat = 3.0
    close_positions_on_stop: bool = True


class EMACrossTWAP(Strategy):
    """
    A simple moving average cross example strategy.

    When the fast EMA crosses the slow EMA then enter a position at the market
    in that direction.

    Cancels all orders and closes all positions on stop.

    Parameters
    ----------
    config : EMACrossConfig
        The configuration for the instance.

    Raises
    ------
    ValueError
        If `config.fast_ema_period` is not less than `config.slow_ema_period`.
    ValueError
        If `config.twap_interval_secs` is not less than or equal to `config.twap_horizon_secs`.

    """

    def __init__(self, config: EMACrossTWAPConfig) -> None:
        PyCondition.is_true(
            config.fast_ema_period < config.slow_ema_period,
            "{config.fast_ema_period=} must be less than {config.slow_ema_period=}",
        )
        PyCondition.is_true(
            config.twap_interval_secs <= config.twap_horizon_secs,
            "{config.twap_interval_secs=} must be less than or equal to {config.twap_horizon_secs=}",
        )
        super().__init__(config)

        self.instrument: Instrument = None  # Initialized in on_start

        # Create the indicators for the strategy
        self.fast_ema = ExponentialMovingAverage(config.fast_ema_period)
        self.slow_ema = ExponentialMovingAverage(config.slow_ema_period)

        # Order management
        self.twap_exec_algorithm_id = ExecAlgorithmId("TWAP")
        self.twap_exec_algorithm_params: dict[str, Any] = {
            "horizon_secs": config.twap_horizon_secs,
            "interval_secs": config.twap_interval_secs,
        }

    def on_start(self) -> None:
        """
        Actions to be performed on strategy start.
        """
        self.instrument = self.cache.instrument(self.config.instrument_id)
        if self.instrument is None:
            self.log.error(f"Could not find instrument for {self.config.instrument_id}")
            self.stop()
            return

        # Register the indicators for updating
        self.register_indicator_for_bars(self.config.bar_type, self.fast_ema)
        self.register_indicator_for_bars(self.config.bar_type, self.slow_ema)

        # Get historical data
        self.request_bars(
            self.config.bar_type,
            start=self._clock.utc_now() - pd.Timedelta(days=1),
        )

        # Subscribe to live data
        self.subscribe_bars(self.config.bar_type)
        self.subscribe_quote_ticks(self.config.instrument_id)

    def on_instrument(self, instrument: Instrument) -> None:
        """
        Actions to be performed when the strategy is running and receives an instrument.

        Parameters
        ----------
        instrument : Instrument
            The instrument received.

        """
        # For debugging (must add a subscription)
        # self.log.info(repr(instrument), LogColor.CYAN)

    def on_order_book_deltas(self, deltas: OrderBookDeltas) -> None:
        """
        Actions to be performed when the strategy is running and receives order book
        deltas.

        Parameters
        ----------
        deltas : OrderBookDeltas
            The order book deltas received.

        """
        # For debugging (must add a subscription)
        # self.log.info(repr(deltas), LogColor.CYAN)

    def on_order_book(self, order_book: OrderBook) -> None:
        """
        Actions to be performed when the strategy is running and receives an order book.

        Parameters
        ----------
        order_book : OrderBook
            The order book received.

        """
        # For debugging (must add a subscription)
        # self.log.info(repr(order_book), LogColor.CYAN)

    def on_quote_tick(self, tick: QuoteTick) -> None:
        """
        Actions to be performed when the strategy is running and receives a quote tick.

        Parameters
        ----------
        tick : QuoteTick
            The tick received.

        """
        # For debugging (must add a subscription)
        # self.log.info(repr(tick), LogColor.CYAN)

    def on_trade_tick(self, tick: TradeTick) -> None:
        """
        Actions to be performed when the strategy is running and receives a trade tick.

        Parameters
        ----------
        tick : TradeTick
            The tick received.

        """
        # For debugging (must add a subscription)
        # self.log.info(repr(tick), LogColor.CYAN)

    def on_bar(self, bar: Bar) -> None:
        """
        Actions to be performed when the strategy is running and receives a bar.

        Parameters
        ----------
        bar : Bar
            The bar received.

        """
        self.log.info(repr(bar), LogColor.CYAN)

        # Check if indicators ready
        if not self.indicators_initialized():
            self.log.info(
                f"Waiting for indicators to warm up [{self.cache.bar_count(self.config.bar_type)}]",
                color=LogColor.BLUE,
            )
            return  # Wait for indicators to warm up...

        if bar.is_single_price():
            # Implies no market information for this bar
            return

        # BUY LOGIC
        if self.fast_ema.value >= self.slow_ema.value:
            if self.portfolio.is_flat(self.config.instrument_id):
                self.buy()
            elif self.portfolio.is_net_short(self.config.instrument_id):
                self.close_all_positions(self.config.instrument_id)
                self.buy()
        # SELL LOGIC
        elif self.fast_ema.value < self.slow_ema.value:
            if self.portfolio.is_flat(self.config.instrument_id):
                self.sell()
            elif self.portfolio.is_net_long(self.config.instrument_id):
                self.close_all_positions(self.config.instrument_id)
                self.sell()

    def buy(self) -> None:
        """
        Users simple buy method (example).
        """
        order: MarketOrder = self.order_factory.market(
            instrument_id=self.config.instrument_id,
            order_side=OrderSide.BUY,
            quantity=self.instrument.make_qty(self.config.trade_size),
            time_in_force=TimeInForce.FOK,
            exec_algorithm_id=self.twap_exec_algorithm_id,
            exec_algorithm_params=self.twap_exec_algorithm_params,
        )

        self.submit_order(order)

    def sell(self) -> None:
        """
        Users simple sell method (example).
        """
        order: MarketOrder = self.order_factory.market(
            instrument_id=self.config.instrument_id,
            order_side=OrderSide.SELL,
            quantity=self.instrument.make_qty(self.config.trade_size),
            time_in_force=TimeInForce.FOK,
            exec_algorithm_id=self.twap_exec_algorithm_id,
            exec_algorithm_params=self.twap_exec_algorithm_params,
        )

        self.submit_order(order)

    def on_data(self, data: Data) -> None:
        """
        Actions to be performed when the strategy is running and receives data.

        Parameters
        ----------
        data : Data
            The data received.

        """

    def on_event(self, event: Event) -> None:
        """
        Actions to be performed when the strategy is running and receives an event.

        Parameters
        ----------
        event : Event
            The event received.

        """

    def on_stop(self) -> None:
        """
        Actions to be performed when the strategy is stopped.
        """
        self.cancel_all_orders(self.config.instrument_id)
        if self.config.close_positions_on_stop:
            self.close_all_positions(self.config.instrument_id)

        # Unsubscribe from data
        self.unsubscribe_bars(self.config.bar_type)

    def on_reset(self) -> None:
        """
        Actions to be performed when the strategy is reset.
        """
        # Reset indicators here
        self.fast_ema.reset()
        self.slow_ema.reset()

    def on_save(self) -> dict[str, bytes]:
        """
        Actions to be performed when the strategy is saved.

        Create and return a state dictionary of values to be saved.

        Returns
        -------
        dict[str, bytes]
            The strategy state dictionary.

        """
        return {}

    def on_load(self, state: dict[str, bytes]) -> None:
        """
        Actions to be performed when the strategy is loaded.

        Saved state values will be contained in the give state dictionary.

        Parameters
        ----------
        state : dict[str, bytes]
            The strategy state dictionary.

        """

    def on_dispose(self) -> None:
        """
        Actions to be performed when the strategy is disposed.

        Cleanup any resources used by the strategy here.

        """
```


---

## Overview

This file is located at `nautilus_trader/examples/strategies/ema_cross_twap.py` within the repository.

**Classes defined:** EMACrossTWAPConfig, EMACrossTWAP

**Functions defined:** __init__, on_start, on_instrument, on_order_book_deltas, on_order_book, on_quote_tick, on_trade_tick, on_bar, buy, sell and 7 more

**Import statements:** 24


---

## Detailed Analysis

### Classes

#### `EMACrossTWAPConfig`

**Inherits from:** StrategyConfig, frozen=True


#### `EMACrossTWAP`

**Inherits from:** Strategy


### Functions

#### `__init__(self, config: EMACrossTWAPConfig)`


#### `on_start(self)`


#### `on_instrument(self, instrument: Instrument)`


#### `on_order_book_deltas(self, deltas: OrderBookDeltas)`


#### `on_order_book(self, order_book: OrderBook)`


#### `on_quote_tick(self, tick: QuoteTick)`


#### `on_trade_tick(self, tick: TradeTick)`


#### `on_bar(self, bar: Bar)`


#### `buy(self)`


#### `sell(self)`


#### `on_data(self, data: Data)`


#### `on_event(self, event: Event)`


#### `on_stop(self)`


#### `on_reset(self)`


#### `on_save(self)`


#### `on_load(self, state: dict[str, bytes])`


#### `on_dispose(self)`


### Imports

- `from decimal import Decimal`
- `from typing import Any`
- `import pandas as pd`
- `from nautilus_trader.common.enums import LogColor`
- `from nautilus_trader.config import PositiveFloat`
- `from nautilus_trader.config import PositiveInt`
- `from nautilus_trader.config import StrategyConfig`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.core.message import Event`
- `from nautilus_trader.indicators import ExponentialMovingAverage`
- `from nautilus_trader.model.book import OrderBook`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.data import OrderBookDeltas`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.identifiers import ExecAlgorithmId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.model.orders import MarketOrder`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from nautilus_trader.examples.strategies.ema_cross_twap import EMACrossTWAPConfig
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from typing import Any`
- `import pandas as pd`
- `from nautilus_trader.common.enums import LogColor`
- `from nautilus_trader.config import PositiveFloat`
- `from nautilus_trader.config import PositiveInt`
- `from nautilus_trader.config import StrategyConfig`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.core.message import Event`

*... and 14 more*

**Directory:** `nautilus_trader/examples/strategies`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


