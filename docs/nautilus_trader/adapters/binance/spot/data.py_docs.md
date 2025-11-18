# Documentation: data.py

## File Metadata

- **Path**: `nautilus_trader/adapters/binance/spot/data.py`
- **Size**: 5,584 bytes
- **Lines**: 141
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

import asyncio

import msgspec

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.config import BinanceDataClientConfig
from nautilus_trader.adapters.binance.data import BinanceCommonDataClient
from nautilus_trader.adapters.binance.http.client import BinanceHttpClient
from nautilus_trader.adapters.binance.spot.enums import BinanceSpotEnumParser
from nautilus_trader.adapters.binance.spot.http.market import BinanceSpotMarketHttpAPI
from nautilus_trader.adapters.binance.spot.schemas.market import BinanceSpotOrderBookPartialDepthMsg
from nautilus_trader.adapters.binance.spot.schemas.market import BinanceSpotTradeMsg
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.common.providers import InstrumentProvider
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import OrderBookDeltas
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.identifiers import InstrumentId


class BinanceSpotDataClient(BinanceCommonDataClient):
    """
    Provides a data client for the Binance Spot/Margin exchange.

    Parameters
    ----------
    loop : asyncio.AbstractEventLoop
        The event loop for the client.
    client : BinanceHttpClient
        The binance HTTP client.
    msgbus : MessageBus
        The message bus for the client.
    cache : Cache
        The cache for the client.
    clock : LiveClock
        The clock for the client.
    instrument_provider : InstrumentProvider
        The instrument provider.
    base_url_ws : str
        The base URL for the WebSocket client.
    config : BinanceDataClientConfig
        The configuration for the client.
    account_type : BinanceAccountType, default 'SPOT'
        The account type for the client.
    name : str, optional
        The custom client ID.

    """

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        client: BinanceHttpClient,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
        instrument_provider: InstrumentProvider,
        base_url_ws: str,
        config: BinanceDataClientConfig,
        account_type: BinanceAccountType = BinanceAccountType.SPOT,
        name: str | None = None,
    ) -> None:
        PyCondition.is_true(
            account_type.is_spot_or_margin,
            "account_type was not SPOT, MARGIN or ISOLATED_MARGIN",
        )

        # Spot HTTP API
        self._spot_http_market = BinanceSpotMarketHttpAPI(client, account_type)

        # Spot enum parser
        self._spot_enum_parser = BinanceSpotEnumParser()

        super().__init__(
            loop=loop,
            client=client,
            market=self._spot_http_market,
            enum_parser=self._spot_enum_parser,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            instrument_provider=instrument_provider,
            account_type=account_type,
            base_url_ws=base_url_ws,
            name=name,
            config=config,
        )

        # Websocket msgspec decoders
        self._decoder_spot_trade = msgspec.json.Decoder(BinanceSpotTradeMsg)
        self._decoder_spot_order_book_partial_depth = msgspec.json.Decoder(
            BinanceSpotOrderBookPartialDepthMsg,
        )

    # -- WEBSOCKET HANDLERS ---------------------------------------------------------------------------------

    def _handle_book_partial_update(self, raw: bytes) -> None:
        msg = self._decoder_spot_order_book_partial_depth.decode(raw)
        instrument_id: InstrumentId = self._get_cached_instrument_id(
            msg.stream.partition("@")[0],
        )
        book_snapshot: OrderBookDeltas = msg.data.parse_to_order_book_snapshot(
            instrument_id=instrument_id,
            ts_init=self._clock.timestamp_ns(),
        )
        # Check if book buffer active
        book_buffer: list[OrderBookDelta | OrderBookDeltas] | None = self._book_buffer.get(
            instrument_id,
        )
        if book_buffer is not None:
            book_buffer.append(book_snapshot)
        else:
            self._handle_data(book_snapshot)

    def _handle_trade(self, raw: bytes) -> None:
        msg = self._decoder_spot_trade.decode(raw)
        instrument_id: InstrumentId = self._get_cached_instrument_id(msg.data.s)
        trade_tick: TradeTick = msg.data.parse_to_trade_tick(
            instrument_id=instrument_id,
            ts_init=self._clock.timestamp_ns(),
        )
        self._handle_data(trade_tick)

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`BinanceSpotDataClient`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Classs**: `BinanceSpotDataClient`
**Imports**: `asyncio`, `msgspec`, `nautilus_trader.adapters.binance.common.enums`, `nautilus_trader.adapters.binance.config`, `nautilus_trader.adapters.binance.data`, `nautilus_trader.adapters.binance.http.client`, `nautilus_trader.adapters.binance.spot.enums`, `nautilus_trader.adapters.binance.spot.http.market`, `nautilus_trader.adapters.binance.spot.schemas.market`, `nautilus_trader.cache.cache`, `nautilus_trader.common.component`, `nautilus_trader.common.providers`, `nautilus_trader.core.correctness`, `nautilus_trader.model.data`, `nautilus_trader.model.identifiers`

## Related Files

This file is located in `nautilus_trader/adapters/binance/spot/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.587053Z*
