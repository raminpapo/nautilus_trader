# Documentation: blank.py

## File Metadata

- **Path**: `nautilus_trader/examples/strategies/blank.py`
- **Size**: 5,194 bytes
- **Lines**: 193
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

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`MyStrategyConfig`**: Class defined in this file
- **`MyStrategy`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Classs**: `MyStrategy`, `MyStrategyConfig`
**Imports**: `nautilus_trader.config`, `nautilus_trader.core.data`, `nautilus_trader.core.message`, `nautilus_trader.model.data`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.instruments`, `nautilus_trader.trading.strategy`

## Related Files

This file is located in `nautilus_trader/examples/strategies/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.428498Z*
