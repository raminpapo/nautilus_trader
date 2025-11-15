# Documentation: `nautilus_trader/examples/strategies/signal_strategy.py`
**Generated:** 2025-11-15T19:40:04.882660Z
**File Size:** 2805 bytes
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

- **Path:** `nautilus_trader/examples/strategies/signal_strategy.py`
- **Size:** 2,805 bytes
- **Lines:** 78
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 2
- **Functions:** 4

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


from nautilus_trader.config import StrategyConfig
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.trading.strategy import Strategy


# *** THIS IS A TEST STRATEGY ***


class SignalStrategyConfig(StrategyConfig, frozen=True):
    """
    Configuration for ``SignalStrategy`` instances.

    Parameters
    ----------
    instrument_id : InstrumentId
        The instrument ID for the strategy.

    """

    instrument_id: InstrumentId


class SignalStrategy(Strategy):
    """
    A strategy that simply emits a signal counter (FOR TESTING PURPOSES ONLY).

    Parameters
    ----------
    config : OrderbookImbalanceConfig
        The configuration for the instance.

    """

    def __init__(self, config: SignalStrategyConfig) -> None:
        super().__init__(config)
        self.instrument: Instrument | None = None
        self.counter = 0

    def on_start(self) -> None:
        """
        Actions to be performed on strategy start.
        """
        self.instrument = self.cache.instrument(self.config.instrument_id)
        self.subscribe_trade_ticks(instrument_id=self.config.instrument_id)
        self.subscribe_quote_ticks(instrument_id=self.config.instrument_id)

    def on_quote_tick(self, tick: QuoteTick) -> None:
        """
        Actions to be performed when the strategy is running and receives a quote tick.
        """
        self.counter += 1
        self.publish_signal(name="counter", value=self.counter, ts_event=tick.ts_event)

    def on_trade_tick(self, tick: TradeTick) -> None:
        """
        Actions to be performed when the strategy is running and receives a trade tick.
        """
        self.counter += 1
        self.publish_signal(name="counter", value=self.counter, ts_event=tick.ts_event)
```


---

## Overview

This file is located at `nautilus_trader/examples/strategies/signal_strategy.py` within the repository.

**Classes defined:** SignalStrategyConfig, SignalStrategy

**Functions defined:** __init__, on_start, on_quote_tick, on_trade_tick

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `SignalStrategyConfig`

**Inherits from:** StrategyConfig, frozen=True


#### `SignalStrategy`

**Inherits from:** Strategy


### Functions

#### `__init__(self, config: SignalStrategyConfig)`


#### `on_start(self)`


#### `on_quote_tick(self, tick: QuoteTick)`


#### `on_trade_tick(self, tick: TradeTick)`


### Imports

- `from nautilus_trader.config import StrategyConfig`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from nautilus_trader.examples.strategies.signal_strategy import SignalStrategyConfig
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.config import StrategyConfig`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.trading.strategy import Strategy`

**Directory:** `nautilus_trader/examples/strategies`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


