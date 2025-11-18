# Documentation: providers.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/providers.py`
- **Size**: 6,404 bytes
- **Lines**: 163
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
"""
Instrument provider for the dYdX venue.
"""

from decimal import Decimal
from typing import Any

from grpc.aio._call import AioRpcError
from v4_proto.dydxprotocol.feetiers import query_pb2 as fee_tier_query

from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE
from nautilus_trader.adapters.dydx.common.constants import FEE_SCALING
from nautilus_trader.adapters.dydx.common.credentials import get_wallet_address
from nautilus_trader.adapters.dydx.grpc.account import DYDXAccountGRPCAPI
from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient
from nautilus_trader.adapters.dydx.http.market import DYDXMarketHttpAPI
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.providers import InstrumentProvider
from nautilus_trader.config import InstrumentProviderConfig
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Venue


class DYDXInstrumentProvider(InstrumentProvider):
    """
    Provides Nautilus instrument definitions from dYdX.

    Parameters
    ----------
    client : DYDXHttpClient
        The dYdX HTTP client.
    clock : LiveClock
        The clock instance.

    """

    def __init__(
        self,
        client: DYDXHttpClient,
        grpc_account_client: DYDXAccountGRPCAPI,
        clock: LiveClock,
        config: InstrumentProviderConfig | None = None,
        wallet_address: str | None = None,
        is_testnet: bool = False,
        venue: Venue = DYDX_VENUE,
    ) -> None:
        """
        Provide a way to load instruments from dYdX.
        """
        super().__init__(config=config)
        self._clock = clock
        self._client = client
        self._venue = venue
        self._wallet_address = wallet_address or get_wallet_address(is_testnet=is_testnet)

        # GRPC API
        self._grpc_account = grpc_account_client

        # Http API
        self._http_market = DYDXMarketHttpAPI(client=client, clock=clock)

        self._log_warnings = config.log_warnings if config else True

    async def load_all_async(self, filters: dict[str, Any] | None = None) -> None:
        filters_str = "..." if not filters else f" with filters {filters}..."
        self._log.info(f"Loading all instruments{filters_str}")

        await self._load_instruments()

    async def load_ids_async(
        self,
        instrument_ids: list[InstrumentId],
        filters: dict | None = None,
    ) -> None:
        if not instrument_ids:
            self._log.info("No instrument IDs given for loading.")
            return

        # Check all instrument IDs
        for instrument_id in instrument_ids:
            PyCondition.equal(instrument_id.venue, self._venue, "instrument_id.venue", "DYDX")

        fee_tier: fee_tier_query.QueryUserFeeTierResponse | None = None

        try:
            fee_tier = await self._grpc_account.get_user_fee_tier(address=self._wallet_address)
        except AioRpcError as e:
            self._log.warning(f"Failed to get the user fee tier: {e}")

        for instrument_id in instrument_ids:
            await self._load_instruments(
                symbol=instrument_id.symbol.value.removesuffix("-PERP"),
                fee_tier=fee_tier,
            )

    async def load_async(self, instrument_id: InstrumentId, filters: dict | None = None) -> None:
        PyCondition.not_none(instrument_id, "instrument_id")
        PyCondition.equal(instrument_id.venue, self._venue, "instrument_id.venue", "BINANCE")

        filters_str = "..." if not filters else f" with filters {filters}..."
        self._log.debug(f"Loading instrument {instrument_id}{filters_str}.")

        await self._load_instruments(symbol=instrument_id.symbol.value.removesuffix("-PERP"))

    async def _load_instruments(
        self,
        symbol: str | None = None,
        fee_tier: fee_tier_query.QueryUserFeeTierResponse | None = None,
    ) -> None:
        markets = await self._http_market.fetch_instruments(symbol=symbol)

        if markets is None:
            self._log.error("Failed to fetch the instruments")
            return

        maker_fee = Decimal(0)
        taker_fee = Decimal(0)

        if fee_tier is None:
            try:
                fee_tier = await self._grpc_account.get_user_fee_tier(address=self._wallet_address)
                maker_fee = Decimal(fee_tier.tier.maker_fee_ppm) / FEE_SCALING
                taker_fee = Decimal(fee_tier.tier.taker_fee_ppm) / FEE_SCALING
            except AioRpcError as e:
                self._log.error(f"Failed to get the user fee tier: {e}. Set fees to zero.")

        ts_init = self._clock.timestamp_ns()

        for market in markets.markets.values():
            try:
                base_currency = market.parse_base_currency()
                quote_currency = market.parse_quote_currency()

                instrument = market.parse_to_instrument(
                    base_currency=base_currency,
                    quote_currency=quote_currency,
                    maker_fee=maker_fee,
                    taker_fee=taker_fee,
                    ts_event=ts_init,
                    ts_init=ts_init,
                )
                self.add_currency(base_currency)
                self.add_currency(quote_currency)
                self.add(instrument)
            except ValueError as e:
                if self._log_warnings:
                    self._log.warning(f"Unable to parse instrument {market.ticker}: {e}")

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXInstrumentProvider`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Classs**: `DYDXInstrumentProvider`
**Imports**: `decimal`, `grpc.aio._call`, `nautilus_trader.adapters.dydx.common.constants`, `nautilus_trader.adapters.dydx.common.credentials`, `nautilus_trader.adapters.dydx.grpc.account`, `nautilus_trader.adapters.dydx.http.client`, `nautilus_trader.adapters.dydx.http.market`, `nautilus_trader.common.component`, `nautilus_trader.common.providers`, `nautilus_trader.config`, `nautilus_trader.core.correctness`, `nautilus_trader.model.identifiers`, `typing`, `v4_proto.dydxprotocol.feetiers`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.771951Z*
