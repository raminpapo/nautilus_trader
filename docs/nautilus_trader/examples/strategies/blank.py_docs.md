# Documentation: `nautilus_trader/examples/strategies/blank.py`
**Generated:** 2025-11-15T19:40:04.855668Z
**File Size:** 5194 bytes
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

- **Path:** `nautilus_trader/examples/strategies/blank.py`
- **Size:** 5,194 bytes
- **Lines:** 192
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9
- **Classes:** 2
- **Functions:** 15

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
from nautilus_trader.core.data import Data
from nautilus_trader.core.message import Event
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.trading.strategy import Strategy


class MyStrategyConfig(StrategyConfig, frozen=True):
    """
    Configuration for ``MyStrategy`` instances.

    Parameters
    ----------
    instrument_id : InstrumentId
        The instrument ID for the strategy.

    """

    instrument_id: InstrumentId


class MyStrategy(Strategy):
    """
    A blank template strategy.

    Parameters
    ----------
    config : MyStrategyConfig
        The configuration for the instance.

    """

    def __init__(self, config: MyStrategyConfig) -> None:
        super().__init__(config)

    def on_start(self) -> None:
        """
        Actions to be performed when the strategy is started.
        """
        # Optionally implement

    def on_stop(self) -> None:
        """
        Actions to be performed when the strategy is stopped.
        """
        # Optionally implement

    def on_reset(self) -> None:
        """
        Actions to be performed when the strategy is reset.
        """
        # Optionally implement

    def on_dispose(self) -> None:
        """
        Actions to be performed when the strategy is disposed.

        Cleanup any resources used by the strategy here.

        """
        # Optionally implement

    def on_save(self) -> dict[str, bytes]:
        """
        Actions to be performed when the strategy is saved.

        Create and return a state dictionary of values to be saved.

        Returns
        -------
        dict[str, bytes]
            The strategy state dictionary.

        """
        return {}  # Optionally implement

    def on_load(self, state: dict[str, bytes]) -> None:
        """
        Actions to be performed when the strategy is loaded.

        Saved state values will be contained in the give state dictionary.

        Parameters
        ----------
        state : dict[str, bytes]
            The strategy state dictionary.

        """
        # Optionally implement

    def on_instrument(self, instrument: Instrument) -> None:
        """
        Actions to be performed when the strategy is running and receives an instrument.

        Parameters
        ----------
        instrument : Instrument
            The instrument received.

        """
        # Optionally implement

    def on_quote_tick(self, tick: QuoteTick) -> None:
        """
        Actions to be performed when the strategy is running and receives a quote tick.

        Parameters
        ----------
        tick : QuoteTick
            The tick received.

        """
        # Optionally implement

    def on_trade_tick(self, tick: TradeTick) -> None:
        """
        Actions to be performed when the strategy is running and receives a trade tick.

        Parameters
        ----------
        tick : TradeTick
            The tick received.

        """
        # Optionally implement

    def on_bar(self, bar: Bar) -> None:
        """
        Actions to be performed when the strategy is running and receives a bar.

        Parameters
        ----------
        bar : Bar
            The bar received.

        """
        # Optionally implement

    def buy(self) -> None:
        """
        Users simple buy method (example).
        """
        # Optionally implement

    def sell(self) -> None:
        """
        Users simple sell method (example).
        """
        # Optionally implement

    def on_data(self, data: Data) -> None:
        """
        Actions to be performed when the strategy is running and receives data.

        Parameters
        ----------
        data : Data
            The data received.

        """
        # Optionally implement

    def on_event(self, event: Event) -> None:
        """
        Actions to be performed when the strategy is running and receives an event.

        Parameters
        ----------
        event : Event
            The event received.

        """
        # Optionally implement
```


---

## Overview

This file is located at `nautilus_trader/examples/strategies/blank.py` within the repository.

**Classes defined:** MyStrategyConfig, MyStrategy

**Functions defined:** __init__, on_start, on_stop, on_reset, on_dispose, on_save, on_load, on_instrument, on_quote_tick, on_trade_tick and 5 more

**Import statements:** 9


---

## Detailed Analysis

### Classes

#### `MyStrategyConfig`

**Inherits from:** StrategyConfig, frozen=True


#### `MyStrategy`

**Inherits from:** Strategy


### Functions

#### `__init__(self, config: MyStrategyConfig)`


#### `on_start(self)`


#### `on_stop(self)`


#### `on_reset(self)`


#### `on_dispose(self)`


#### `on_save(self)`


#### `on_load(self, state: dict[str, bytes])`


#### `on_instrument(self, instrument: Instrument)`


#### `on_quote_tick(self, tick: QuoteTick)`


#### `on_trade_tick(self, tick: TradeTick)`


#### `on_bar(self, bar: Bar)`


#### `buy(self)`


#### `sell(self)`


#### `on_data(self, data: Data)`


#### `on_event(self, event: Event)`


### Imports

- `from nautilus_trader.config import StrategyConfig`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.core.message import Event`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from nautilus_trader.examples.strategies.blank import MyStrategyConfig
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.config import StrategyConfig`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.core.message import Event`
- `from nautilus_trader.model.data import Bar`
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


