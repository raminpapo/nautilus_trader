# Documentation: conftest.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/kraken/conftest.py`
- **Size**: 6,194 bytes
- **Lines**: 192
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

from decimal import Decimal
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

import pytest

from nautilus_trader.adapters.kraken.constants import KRAKEN_VENUE
from nautilus_trader.adapters.kraken.providers import KrakenInstrumentProvider
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import Logger
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.currencies import BTC
from nautilus_trader.model.currencies import USDT
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.events import AccountState
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.instruments import CurrencyPair
from nautilus_trader.model.objects import AccountBalance
from nautilus_trader.model.objects import Money
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


@pytest.fixture(scope="session")
def live_clock():
    return LiveClock()


@pytest.fixture(scope="session")
def live_logger():
    return Logger("TEST_LOGGER")


@pytest.fixture
def venue() -> Venue:
    return KRAKEN_VENUE


@pytest.fixture
def account_id(venue) -> AccountId:
    return AccountId(f"{venue.value}-123")


@pytest.fixture
def instrument() -> CurrencyPair:
    return CurrencyPair(
        instrument_id=InstrumentId(Symbol("XBT/USDT"), KRAKEN_VENUE),
        raw_symbol=Symbol("XBTUSDT"),
        base_currency=BTC,
        quote_currency=USDT,
        price_precision=1,
        size_precision=8,
        price_increment=Price.from_str("0.1"),
        size_increment=Quantity.from_str("0.00000001"),
        ts_event=0,
        ts_init=0,
        maker_fee=Decimal("0.0016"),
        taker_fee=Decimal("0.0026"),
    )


@pytest.fixture
def account_state(account_id) -> AccountState:
    return AccountState(
        account_id=account_id,
        account_type=AccountType.CASH,
        base_currency=USDT,
        reported=True,
        balances=[
            AccountBalance(
                total=Money(100_000, USDT),
                locked=Money(0, USDT),
                free=Money(100_000, USDT),
            ),
        ],
        margins=[],
        info={},
        event_id=TestIdStubs.uuid(),
        ts_event=0,
        ts_init=0,
    )


@pytest.fixture
def mock_http_client():
    mock = MagicMock(spec=nautilus_pyo3.KrakenHttpClient)
    mock.api_key = "test_api_key"
    mock.api_secret = "test_api_secret"

    mock.request_instruments = AsyncMock(return_value=[])
    mock.cache_instrument = MagicMock()
    mock.cancel_all_requests = MagicMock()
    mock.is_initialized = MagicMock(return_value=True)

    return mock


def _create_ws_mock() -> MagicMock:
    mock = MagicMock(spec=nautilus_pyo3.KrakenWebSocketClient)
    mock.url = "wss://ws.kraken.com/v2"
    mock.is_closed = MagicMock(return_value=False)
    mock.is_active = AsyncMock(return_value=True)
    mock.connect = AsyncMock()
    mock.wait_until_active = AsyncMock()
    mock.close = AsyncMock()
    mock.subscribe_quotes = AsyncMock()
    mock.subscribe_trades = AsyncMock()
    mock.subscribe_book = AsyncMock()
    mock.subscribe_bars = AsyncMock()
    mock.unsubscribe_quotes = AsyncMock()
    mock.unsubscribe_trades = AsyncMock()
    mock.unsubscribe_book = AsyncMock()
    mock.unsubscribe_bars = AsyncMock()
    mock.cache_instrument = MagicMock()
    return mock


@pytest.fixture
def mock_ws_clients():
    return _create_ws_mock(), _create_ws_mock()


@pytest.fixture
def mock_instrument_provider(instrument):
    provider = MagicMock(spec=KrakenInstrumentProvider)
    provider.initialize = AsyncMock()
    provider.instruments_pyo3 = MagicMock(return_value=[MagicMock(name="py_instrument")])
    provider.get_all = MagicMock(return_value={instrument.id: instrument})
    provider.currencies = MagicMock(return_value={})
    provider.find = MagicMock(return_value=instrument)
    return provider


@pytest.fixture
def data_client():
    pass


@pytest.fixture
def exec_client():
    pass


def create_kraken_spot_instrument(base_currency, quote_currency):
    """
    Create a spot instrument for testing.
    """
    return CurrencyPair(
        instrument_id=InstrumentId.from_str(
            f"{base_currency.code}/{quote_currency.code}.KRAKEN",
        ),
        raw_symbol=Symbol(f"{base_currency.code}{quote_currency.code}"),
        base_currency=base_currency,
        quote_currency=quote_currency,
        price_precision=1,
        size_precision=8,
        price_increment=Price.from_str("0.1"),
        size_increment=Quantity.from_str("0.00000001"),
        lot_size=None,
        max_quantity=Quantity.from_str("100000"),
        min_quantity=Quantity.from_str("0.00000001"),
        max_notional=None,
        min_notional=Money(1, quote_currency),
        max_price=Price.from_str("1000000"),
        min_price=Price.from_str("0.1"),
        margin_init=Decimal(0),
        margin_maint=Decimal(0),
        maker_fee=Decimal("0.0016"),
        taker_fee=Decimal("0.0026"),
        ts_event=0,
        ts_init=0,
    )

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 13 function(s).

## Detailed Walkthrough

### Functions
- **`live_clock()`**: Function defined in this file
- **`live_logger()`**: Function defined in this file
- **`venue()`**: Function defined in this file
- **`account_id()`**: Function defined in this file
- **`instrument()`**: Function defined in this file
- **`account_state()`**: Function defined in this file
- **`mock_http_client()`**: Function defined in this file
- **`_create_ws_mock()`**: Function defined in this file
- **`mock_ws_clients()`**: Function defined in this file
- **`mock_instrument_provider()`**: Function defined in this file
- **`data_client()`**: Function defined in this file
- **`exec_client()`**: Function defined in this file
- **`create_kraken_spot_instrument()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 27


**Functions**: `_create_ws_mock`, `account_id`, `account_state`, `create_kraken_spot_instrument`, `data_client`, `exec_client`, `instrument`, `live_clock`, `live_logger`, `mock_http_client`, `mock_instrument_provider`, `mock_ws_clients`, `venue`
**Imports**: `decimal`, `nautilus_trader.adapters.kraken.constants`, `nautilus_trader.adapters.kraken.providers`, `nautilus_trader.common.component`, `nautilus_trader.core`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.events`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.instruments`, `nautilus_trader.model.objects`, `nautilus_trader.test_kit.stubs.identifiers`, `pytest`, `unittest.mock`

## Related Files

This file is located in `tests/integration_tests/adapters/kraken/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/kraken/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:07.041975Z*
