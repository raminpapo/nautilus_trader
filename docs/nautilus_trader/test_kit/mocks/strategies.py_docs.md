# Documentation: `nautilus_trader/test_kit/mocks/strategies.py`
**Generated:** 2025-11-15T19:40:05.344236Z
**File Size:** 7596 bytes
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

- **Path:** `nautilus_trader/test_kit/mocks/strategies.py`
- **Size:** 7,596 bytes
- **Lines:** 224
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 2
- **Functions:** 34

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

import inspect

from nautilus_trader.indicators import ExponentialMovingAverage
from nautilus_trader.model.data import BarType
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.trading.strategy import Strategy


class MockStrategy(Strategy):
    """
    Provides a mock trading strategy for testing.

    Parameters
    ----------
    bar_type : BarType
        The bar type for the strategy.

    """

    def __init__(self, bar_type: BarType) -> None:
        super().__init__()

        self.store: list[object] = []
        self.bar_type = bar_type

        self.ema1 = ExponentialMovingAverage(10)
        self.ema2 = ExponentialMovingAverage(20)

        self.position_id: PositionId | None = None

        self.calls: list[str] = []

    def on_start(self) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.register_indicator_for_bars(self.bar_type, self.ema1)
        self.register_indicator_for_bars(self.bar_type, self.ema2)

    def on_instrument(self, instrument) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(instrument)

    def on_ticker(self, ticker):
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(ticker)

    def on_quote_tick(self, tick):
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(tick)

    def on_trade_tick(self, tick) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(tick)

    def on_bar(self, bar) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(bar)

        if bar.bar_type != self.bar_type:
            return

        if self.ema1.value > self.ema2.value:
            buy_order = self.order_factory.market(
                self.bar_type.instrument_id,
                OrderSide.BUY,
                100000,
            )

            self.submit_order(buy_order)
            self.position_id = buy_order.client_order_id
        elif self.ema1.value < self.ema2.value:
            sell_order = self.order_factory.market(
                self.bar_type.instrument_id,
                OrderSide.SELL,
                100000,
            )

            self.submit_order(sell_order)
            self.position_id = sell_order.client_order_id

    def on_data(self, data) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(data)

    def on_signal(self, signal) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(signal)

    def on_strategy_data(self, data) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(data)

    def on_event(self, event) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(event)

    def on_stop(self) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)

    def on_resume(self) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)

    def on_reset(self) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)

    def on_save(self) -> dict[str, bytes]:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        return {"UserState": b"1"}

    def on_load(self, state: dict[str, bytes]) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)
        self.store.append(state)

    def on_dispose(self) -> None:
        current_frame = inspect.currentframe()
        assert current_frame  # Type checking
        self.calls.append(current_frame.f_code.co_name)


class KaboomStrategy(Strategy):
    """
    Provides a mock trading strategy where every called method blows up.
    """

    def __init__(self) -> None:
        super().__init__()

        self._explode_on_start = True
        self._explode_on_stop = True

    def set_explode_on_start(self, setting) -> None:
        self._explode_on_start = setting

    def set_explode_on_stop(self, setting) -> None:
        self._explode_on_stop = setting

    def on_start(self) -> None:
        if self._explode_on_start:
            raise RuntimeError(f"{self} BOOM!")

    def on_stop(self) -> None:
        if self._explode_on_stop:
            raise RuntimeError(f"{self} BOOM!")

    def on_resume(self) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_reset(self) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_save(self) -> dict[str, bytes]:
        raise RuntimeError(f"{self} BOOM!")

    def on_load(self, state: dict[str, bytes]) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_dispose(self) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_instrument(self, instrument) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_quote_tick(self, tick) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_trade_tick(self, tick) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_bar(self, bar) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_data(self, data) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_signal(self, data) -> None:
        raise RuntimeError(f"{self} BOOM!")

    def on_event(self, event) -> None:
        raise RuntimeError(f"{self} BOOM!")
```


---

## Overview

This file is located at `nautilus_trader/test_kit/mocks/strategies.py` within the repository.

**Classes defined:** MockStrategy, KaboomStrategy

**Functions defined:** __init__, on_start, on_instrument, on_ticker, on_quote_tick, on_trade_tick, on_bar, on_data, on_signal, on_strategy_data and 24 more

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `MockStrategy`

**Inherits from:** Strategy


#### `KaboomStrategy`

**Inherits from:** Strategy


### Functions

#### `__init__(self, bar_type: BarType)`


#### `on_start(self)`


#### `on_instrument(self, instrument)`


#### `on_ticker(self, ticker)`


#### `on_quote_tick(self, tick)`


#### `on_trade_tick(self, tick)`


#### `on_bar(self, bar)`


#### `on_data(self, data)`


#### `on_signal(self, signal)`


#### `on_strategy_data(self, data)`


#### `on_event(self, event)`


#### `on_stop(self)`


#### `on_resume(self)`


#### `on_reset(self)`


#### `on_save(self)`


#### `on_load(self, state: dict[str, bytes])`


#### `on_dispose(self)`


#### `__init__(self)`


#### `set_explode_on_start(self, setting)`


#### `set_explode_on_stop(self, setting)`


#### `on_start(self)`


#### `on_stop(self)`


#### `on_resume(self)`


#### `on_reset(self)`


#### `on_save(self)`


#### `on_load(self, state: dict[str, bytes])`


#### `on_dispose(self)`


#### `on_instrument(self, instrument)`


#### `on_quote_tick(self, tick)`


#### `on_trade_tick(self, tick)`


#### `on_bar(self, bar)`


#### `on_data(self, data)`


#### `on_signal(self, data)`


#### `on_event(self, event)`


### Imports

- `import inspect`
- `from nautilus_trader.indicators import ExponentialMovingAverage`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.mocks.strategies import MockStrategy
```


---

## Related Files

This file imports from the following modules:

- `import inspect`
- `from nautilus_trader.indicators import ExponentialMovingAverage`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.trading.strategy import Strategy`

**Directory:** `nautilus_trader/test_kit/mocks`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


