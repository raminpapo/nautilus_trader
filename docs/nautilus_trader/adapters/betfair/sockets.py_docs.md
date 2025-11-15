# Documentation: `nautilus_trader/adapters/betfair/sockets.py`
**Generated:** 2025-11-15T19:40:04.049317Z
**File Size:** 12163 bytes
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

- **Path:** `nautilus_trader/adapters/betfair/sockets.py`
- **Size:** 12,163 bytes
- **Lines:** 383
- **Extension:** `.py`
- **Type:** text
- **Imports:** 10
- **Classes:** 3
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

import asyncio
import itertools
import os
from collections.abc import Callable

import msgspec

from nautilus_trader.adapters.betfair.client import BetfairHttpClient
from nautilus_trader.common.component import Logger
from nautilus_trader.common.functions import get_event_loop
from nautilus_trader.core.nautilus_pyo3 import SocketClient
from nautilus_trader.core.nautilus_pyo3 import SocketConfig


HOST = "stream-api.betfair.com"
PORT = 443
CRLF = b"\r\n"
ENCODING = "utf-8"
UNIQUE_ID = itertools.count()


class BetfairStreamClient:
    """
    Provides a streaming client for Betfair.
    """

    def __init__(
        self,
        http_client: BetfairHttpClient,
        message_handler: Callable[[bytes], None],
        host: str | None = HOST,
        port: int | None = None,
        crlf: bytes | None = None,
        encoding: str | None = None,
        certs_dir: str | None = None,
    ) -> None:
        self.handler = message_handler
        self.host = host or HOST
        self.port = port or PORT
        self.crlf = crlf or CRLF
        self.encoding = encoding or ENCODING
        self.use_ssl = True
        self.certs_dir = certs_dir or os.environ.get("BETFAIR_CERTS_DIR")

        self._loop = get_event_loop()
        self._http_client = http_client
        self._client: SocketClient | None = None
        self._log = Logger(type(self).__name__)

        self.unique_id = next(UNIQUE_ID)

    async def connect(self):
        if not self._http_client.session_token:
            await self._http_client.connect()

        if self._client is not None and self._client.is_active():
            self._log.info("Socket already connected")
            return

        self._log.info("Connecting Betfair socket client...")
        config = SocketConfig(
            url=f"{self.host}:{self.port}",
            ssl=self.use_ssl,
            suffix=self.crlf,
            handler=self.handler,
            heartbeat=(10, msgspec.json.encode({"op": "heartbeat"})),
            certs_dir=self.certs_dir,
        )
        self._client = await SocketClient.connect(
            config,
            post_connection=None,  # this method itself needs the `self._client` reference
            post_reconnection=self.post_reconnection,
        )

        await self._post_connection()

        self._log.info("Connected")

    async def reconnect(self):
        try:
            if self._client is None:
                self._log.warning("Cannot reconnect: not connected")
                return

            if not self._client.is_active():
                self._log.warning(f"Cannot reconnect: client in {self._client.mode()} mode")
                return

            self._log.info("Reconnecting...")

            await self._client.reconnect()
            await asyncio.sleep(0.1)

            self._log.info("Reconnected")
        except asyncio.CancelledError:
            self._log.warning("Canceled task 'reconnect'")

    async def disconnect(self):
        try:
            if self._client is None:
                self._log.warning("Cannot disconnect: not connected")
                return

            self._log.info(f"Disconnecting from {self._client.mode()} mode...")

            await self._client.close()

            self._log.info("Disconnected")
        except asyncio.CancelledError:
            self._log.warning("Canceled task 'disconnect'")

    def is_active(self) -> bool:
        """
        Check whether the client connection is active.

        Returns
        -------
        bool

        """
        if self._client is None:
            return False
        return self._client.is_active()

    def is_reconnecting(self) -> bool:
        """
        Check whether the client is reconnecting.

        Returns
        -------
        bool

        """
        if self._client is None:
            return False
        return self._client.is_reconnecting()

    def is_disconnecting(self) -> bool:
        """
        Check whether the client is disconnecting.

        Returns
        -------
        bool

        """
        if self._client is None:
            return False
        return self._client.is_disconnecting()

    def is_closed(self) -> bool:
        """
        Check whether the client is closed.

        Returns
        -------
        bool

        """
        if self._client is None:
            return True
        return self._client.is_closed()

    async def _post_connection(self) -> None:
        pass

    def post_connection(self) -> None:
        """
        Actions to be performed post connection.
        """

    def post_reconnection(self) -> None:
        """
        Actions to be performed post connection.
        """

    def post_disconnection(self) -> None:
        """
        Actions to be performed post disconnection.
        """

    async def send(self, message: bytes) -> None:
        try:
            if self._client is None:
                raise RuntimeError("Cannot send message: no client")

            await self._client.send(message)
        except asyncio.CancelledError:
            self._log.warning("Canceled task 'send'")

    def auth_message(self):
        return {
            "op": "authentication",
            "id": self.unique_id,
            "appKey": self._http_client.app_key,
            "session": self._http_client.session_token,
        }


class BetfairOrderStreamClient(BetfairStreamClient):
    """
    Provides an order stream client for Betfair.
    """

    def __init__(
        self,
        http_client: BetfairHttpClient,
        message_handler: Callable[[bytes], None],
        certs_dir: str | None = None,
        partition_matched_by_strategy_ref: bool = True,
        include_overall_position: str | None = None,
        customer_strategy_refs: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            http_client=http_client,
            message_handler=message_handler,
            certs_dir=certs_dir,
            **kwargs,
        )
        self.order_filter = {
            "includeOverallPosition": include_overall_position,
            "customerStrategyRefs": customer_strategy_refs,
            "partitionMatchedByStrategyRef": partition_matched_by_strategy_ref,
        }

    def post_connection(self):
        self._loop.create_task(self._post_connection())

    def post_reconnection(self):
        self._loop.create_task(self._post_connection())

    async def _post_connection(self):
        retries = 5
        for i in range(retries):
            try:
                subscribe_msg = {
                    "op": "orderSubscription",
                    "id": self.unique_id,
                    "orderFilter": self.order_filter,
                    "initialClk": None,
                    "clk": None,
                }
                await self.send(msgspec.json.encode(self.auth_message()))
                await self.send(msgspec.json.encode(subscribe_msg))
                return
            except Exception as e:
                self._log.error(f"Failed to send auth message({e}), retrying {i + 1}/{retries}...")
                await asyncio.sleep(1.0)


class BetfairMarketStreamClient(BetfairStreamClient):
    """
    Provides a Betfair market stream client.
    """

    def __init__(
        self,
        http_client: BetfairHttpClient,
        message_handler: Callable,
        certs_dir: str | None = None,
        **kwargs,
    ):
        super().__init__(
            http_client=http_client,
            message_handler=message_handler,
            certs_dir=certs_dir,
            **kwargs,
        )

    # TODO - Add support for initial_clk/clk reconnection
    async def send_subscription_message(
        self,
        market_ids: list | None = None,
        betting_types: list | None = None,
        event_type_ids: list | None = None,
        event_ids: list | None = None,
        turn_in_play_enabled: bool | None = None,
        market_types: list | None = None,
        venues: list | None = None,
        country_codes: list | None = None,
        race_types: list | None = None,
        initial_clk: str | None = None,
        clk: str | None = None,
        conflate_ms: int | None = None,
        heartbeat_ms: int | None = None,
        segmentation_enabled: bool = True,
        subscribe_book_updates=True,
        subscribe_trade_updates=True,
        subscribe_market_definitions=True,
        subscribe_ticker=True,
        subscribe_bsp_updates=True,
        subscribe_bsp_projected=True,
    ) -> None:
        filters = (
            market_ids,
            betting_types,
            event_type_ids,
            event_ids,
            turn_in_play_enabled,
            market_types,
            venues,
            country_codes,
            race_types,
        )
        assert any(filters), "Must pass at least one filter"
        assert any(
            (subscribe_book_updates, subscribe_trade_updates),
        ), "Must subscribe to either book updates or trades"
        if market_ids is not None:
            # TODO - Log a warning about inefficiencies of specific market ids - Won't receive any updates for new
            #  markets that fit criteria like when using event type / market type etc
            # logging.warning()
            pass
        market_filter = {
            "marketIds": market_ids,
            "bettingTypes": betting_types,
            "eventTypeIds": event_type_ids,
            "eventIds": event_ids,
            "turnInPlayEnabled": turn_in_play_enabled,
            "marketTypes": market_types,
            "venues": venues,
            "countryCodes": country_codes,
            "raceTypes": race_types,
        }
        data_fields = []
        if subscribe_book_updates:
            data_fields.append("EX_ALL_OFFERS")
        if subscribe_trade_updates:
            data_fields.append("EX_TRADED")
        if subscribe_ticker:
            data_fields.extend(["EX_TRADED_VOL", "EX_LTP"])
        if subscribe_market_definitions:
            data_fields.append("EX_MARKET_DEF")
        if subscribe_bsp_updates:
            data_fields.append("SP_TRADED")
        if subscribe_bsp_projected:
            data_fields.append("SP_PROJECTED")

        message = {
            "op": "marketSubscription",
            "id": self.unique_id,
            "marketFilter": market_filter,
            "marketDataFilter": {"fields": data_fields},
            "initialClk": initial_clk,
            "clk": clk,
            "conflateMs": conflate_ms,
            "heartbeatMs": heartbeat_ms,
            "segmentationEnabled": segmentation_enabled,
        }
        await self.send(msgspec.json.encode(message))

    def post_connection(self) -> None:
        self._loop.create_task(self._post_connection())

    def post_reconnection(self) -> None:
        super().post_reconnection()
        self._loop.create_task(self._post_connection())

    async def _post_connection(self) -> None:
        retries = 5
        for i in range(retries):
            try:
                await self.send(msgspec.json.encode(self.auth_message()))
                return
            except Exception as e:
                self._log.error(f"Failed to send auth message({e}), retrying {i + 1}/{retries}...")
                await asyncio.sleep(1.0)
```


---

## Overview

This file is located at `nautilus_trader/adapters/betfair/sockets.py` within the repository.

**Classes defined:** BetfairStreamClient, BetfairOrderStreamClient, BetfairMarketStreamClient

**Functions defined:** __init__, is_active, is_reconnecting, is_disconnecting, is_closed, post_connection, post_reconnection, post_disconnection, auth_message, __init__ and 5 more

**Import statements:** 10


---

## Detailed Analysis

### Classes

#### `BetfairStreamClient`


#### `BetfairOrderStreamClient`

**Inherits from:** BetfairStreamClient


#### `BetfairMarketStreamClient`

**Inherits from:** BetfairStreamClient


### Functions

#### `__init__(
        self,
        http_client: BetfairHttpClient,
        message_handler: Callable[[bytes], None],
        host: str | None = HOST,
        port: int | None = None,
        crlf: bytes | None = None,
        encoding: str | None = None,
        certs_dir: str | None = None,
    )`


#### `is_active(self)`


#### `is_reconnecting(self)`


#### `is_disconnecting(self)`


#### `is_closed(self)`


#### `post_connection(self)`


#### `post_reconnection(self)`


#### `post_disconnection(self)`


#### `auth_message(self)`


#### `__init__(
        self,
        http_client: BetfairHttpClient,
        message_handler: Callable[[bytes], None],
        certs_dir: str | None = None,
        partition_matched_by_strategy_ref: bool = True,
        include_overall_position: str | None = None,
        customer_strategy_refs: str | None = None,
        **kwargs,
    )`


#### `post_connection(self)`


#### `post_reconnection(self)`


#### `__init__(
        self,
        http_client: BetfairHttpClient,
        message_handler: Callable,
        certs_dir: str | None = None,
        **kwargs,
    )`


#### `post_connection(self)`


#### `post_reconnection(self)`


### Imports

- `import asyncio`
- `import itertools`
- `import os`
- `from collections.abc import Callable`
- `import msgspec`
- `from nautilus_trader.adapters.betfair.client import BetfairHttpClient`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.functions import get_event_loop`
- `from nautilus_trader.core.nautilus_pyo3 import SocketClient`
- `from nautilus_trader.core.nautilus_pyo3 import SocketConfig`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.betfair.sockets import BetfairStreamClient
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import itertools`
- `import os`
- `from collections.abc import Callable`
- `import msgspec`
- `from nautilus_trader.adapters.betfair.client import BetfairHttpClient`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.functions import get_event_loop`
- `from nautilus_trader.core.nautilus_pyo3 import SocketClient`
- `from nautilus_trader.core.nautilus_pyo3 import SocketConfig`

**Directory:** `nautilus_trader/adapters/betfair`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token, auth, session. Ensure proper handling of secrets.


