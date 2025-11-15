# Documentation: `nautilus_trader/test_kit/mocks/cache_database.py`
**Generated:** 2025-11-15T19:40:05.336235Z
**File Size:** 7164 bytes
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

- **Path:** `nautilus_trader/test_kit/mocks/cache_database.py`
- **Size:** 7,164 bytes
- **Lines:** 192
- **Extension:** `.py`
- **Type:** text
- **Imports:** 17
- **Classes:** 1
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

from typing import Any

import pandas as pd

from nautilus_trader.accounting.accounts.base import Account
from nautilus_trader.cache.facade import CacheDatabaseFacade
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.model.instruments import SyntheticInstrument
from nautilus_trader.model.objects import Currency
from nautilus_trader.model.objects import Money
from nautilus_trader.model.orders import Order
from nautilus_trader.model.position import Position
from nautilus_trader.trading.strategy import Strategy


class MockCacheDatabase(CacheDatabaseFacade):
    """
    Provides a mock cache database for testing.
    """

    def __init__(self) -> None:
        super().__init__()

        self.general: dict[str, bytes] = {}
        self.currencies: dict[str, Currency] = {}
        self.instruments: dict[InstrumentId, Instrument] = {}
        self.synthetics: dict[InstrumentId, SyntheticInstrument] = {}
        self.accounts: dict[AccountId, Account] = {}
        self.orders: dict[ClientOrderId, Order] = {}
        self.positions: dict[PositionId, Position] = {}
        self.order_states: dict[ClientOrderId, dict[str, Any]] = {}
        self.position_states: dict[PositionId, dict[str, Any]] = {}
        self.last_heartbeat: int = 0
        self._index_order_position: dict[ClientOrderId, PositionId] = {}
        self._index_order_client: dict[ClientOrderId, ClientId] = {}

    def flush(self) -> None:
        self.general.clear()
        self.currencies.clear()
        self.instruments.clear()
        self.synthetics.clear()
        self.accounts.clear()
        self.orders.clear()
        self.positions.clear()
        self.order_states.clear()
        self.position_states.clear()
        self.last_heartbeat = 0
        self._index_order_position.clear()
        self._index_order_client.clear()

    def load_all(self) -> dict:
        return {
            "currencies": self.currencies.copy(),
            "instruments": self.instruments.copy(),
            "synthetics": self.synthetics.copy(),
            "accounts": self.accounts.copy(),
            "orders": self.orders.copy(),
            "positions": self.positions.copy(),
        }

    def load(self) -> dict:
        return self.general.copy()

    def load_currencies(self) -> dict:
        return self.currencies.copy()

    def load_instruments(self) -> dict:
        return self.instruments.copy()

    def load_synthetics(self) -> dict:
        return self.synthetics.copy()

    def load_accounts(self) -> dict:
        return self.accounts.copy()

    def load_orders(self) -> dict:
        return self.orders.copy()

    def load_positions(self) -> dict:
        return self.positions.copy()

    def load_currency(self, code: str) -> Currency:
        return self.currencies.get(code)

    def load_instrument(self, instrument_id: InstrumentId) -> Instrument | None:
        return self.instruments.get(instrument_id)

    def load_synthetic(self, instrument_id: InstrumentId) -> SyntheticInstrument | None:
        return self.synthetics.get(instrument_id)

    def load_account(self, account_id: AccountId) -> Account | None:
        return self.accounts.get(account_id)

    def load_order(self, client_order_id: ClientOrderId) -> Order | None:
        return self.orders.get(client_order_id)

    def load_index_order_position(self) -> dict[ClientOrderId, PositionId]:
        return self._index_order_position

    def load_index_order_client(self) -> dict[ClientOrderId, ClientId]:
        return self._index_order_client

    def load_position(self, position_id: PositionId) -> Position | None:
        return self.positions.get(position_id)

    def load_strategy(self, strategy_id: StrategyId) -> dict:
        return {}

    def delete_strategy(self, strategy_id: StrategyId) -> None:
        pass

    def add_currency(self, currency: Currency) -> None:
        self.currencies[currency.code] = currency

    def add_instrument(self, instrument: Instrument) -> None:
        self.instruments[instrument.id] = instrument

    def add_synthetic(self, synthetic: SyntheticInstrument) -> None:
        self.synthetics[synthetic.id] = synthetic

    def add_account(self, account: Account) -> None:
        self.accounts[account.id] = account

    def add_order(
        self,
        order: Order,
        position_id: PositionId | None = None,
        client_id: ClientId | None = None,
    ) -> None:
        self.orders[order.client_order_id] = order
        self._index_order_position[order.client_order_id] = position_id
        self._index_order_client[order.client_order_id] = client_id

    def add_position(self, position: Position) -> None:
        self.positions[position.id] = position

    def index_order_position(self, client_order_id: ClientOrderId, position_id: PositionId) -> None:
        self._index_order_position[client_order_id] = position_id

    def update_account(self, event: Account) -> None:
        pass  # Would persist the event

    def update_order(self, order: Order) -> None:
        pass  # Would persist the event

    def update_position(self, position: Position) -> None:
        pass  # Would persist the event

    def update_strategy(self, strategy: Strategy) -> None:
        pass  # Would persist the user state dict

    def snapshot_order_state(self, order: Order) -> None:
        self.order_states[order.client_order_id] = order.to_dict()

    def snapshot_position_state(
        self,
        position: Position,
        ts_snapshot: int,
        unrealized_pnl: Money | None = None,
    ) -> None:
        position_state = position.to_dict()

        if unrealized_pnl is not None:
            position_state["unrealized_pnl"] = str(unrealized_pnl)

        position_state["ts_snapshot"] = ts_snapshot

        self.order_states[position.id] = position_state

    def heartbeat(self, timestamp: pd.Timestamp) -> None:
        self.last_heartbeat = timestamp.value
```


---

## Overview

This file is located at `nautilus_trader/test_kit/mocks/cache_database.py` within the repository.

**Classes defined:** MockCacheDatabase

**Functions defined:** __init__, flush, load_all, load, load_currencies, load_instruments, load_synthetics, load_accounts, load_orders, load_positions and 24 more

**Import statements:** 17


---

## Detailed Analysis

### Classes

#### `MockCacheDatabase`

**Inherits from:** CacheDatabaseFacade


### Functions

#### `__init__(self)`


#### `flush(self)`


#### `load_all(self)`


#### `load(self)`


#### `load_currencies(self)`


#### `load_instruments(self)`


#### `load_synthetics(self)`


#### `load_accounts(self)`


#### `load_orders(self)`


#### `load_positions(self)`


#### `load_currency(self, code: str)`


#### `load_instrument(self, instrument_id: InstrumentId)`


#### `load_synthetic(self, instrument_id: InstrumentId)`


#### `load_account(self, account_id: AccountId)`


#### `load_order(self, client_order_id: ClientOrderId)`


#### `load_index_order_position(self)`


#### `load_index_order_client(self)`


#### `load_position(self, position_id: PositionId)`


#### `load_strategy(self, strategy_id: StrategyId)`


#### `delete_strategy(self, strategy_id: StrategyId)`


#### `add_currency(self, currency: Currency)`


#### `add_instrument(self, instrument: Instrument)`


#### `add_synthetic(self, synthetic: SyntheticInstrument)`


#### `add_account(self, account: Account)`


#### `add_order(
        self,
        order: Order,
        position_id: PositionId | None = None,
        client_id: ClientId | None = None,
    )`


#### `add_position(self, position: Position)`


#### `index_order_position(self, client_order_id: ClientOrderId, position_id: PositionId)`


#### `update_account(self, event: Account)`


#### `update_order(self, order: Order)`


#### `update_position(self, position: Position)`


#### `update_strategy(self, strategy: Strategy)`


#### `snapshot_order_state(self, order: Order)`


#### `snapshot_position_state(
        self,
        position: Position,
        ts_snapshot: int,
        unrealized_pnl: Money | None = None,
    )`


#### `heartbeat(self, timestamp: pd.Timestamp)`


### Imports

- `from typing import Any`
- `import pandas as pd`
- `from nautilus_trader.accounting.accounts.base import Account`
- `from nautilus_trader.cache.facade import CacheDatabaseFacade`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.instruments import Instrument`
- `from nautilus_trader.model.instruments import SyntheticInstrument`
- `from nautilus_trader.model.objects import Currency`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.model.orders import Order`
- `from nautilus_trader.model.position import Position`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.mocks.cache_database import MockCacheDatabase
```


---

## Related Files

This file imports from the following modules:

- `from typing import Any`
- `import pandas as pd`
- `from nautilus_trader.accounting.accounts.base import Account`
- `from nautilus_trader.cache.facade import CacheDatabaseFacade`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`

*... and 7 more*

**Directory:** `nautilus_trader/test_kit/mocks`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


