# Documentation: `nautilus_trader/adapters/binance/futures/http/market.py`
**Generated:** 2025-11-15T19:40:04.098681Z
**File Size:** 3630 bytes
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

- **Path:** `nautilus_trader/adapters/binance/futures/http/market.py`
- **Size:** 3,630 bytes
- **Lines:** 100
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 2
- **Functions:** 2

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

import msgspec

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.common.enums import BinanceSecurityType
from nautilus_trader.adapters.binance.futures.schemas.market import BinanceFuturesExchangeInfo
from nautilus_trader.adapters.binance.http.client import BinanceHttpClient
from nautilus_trader.adapters.binance.http.endpoint import BinanceHttpEndpoint
from nautilus_trader.adapters.binance.http.market import BinanceMarketHttpAPI
from nautilus_trader.core.nautilus_pyo3 import HttpMethod


class BinanceFuturesExchangeInfoHttp(BinanceHttpEndpoint):
    """
    Endpoint of FUTURES exchange trading rules and symbol information.

    `GET /fapi/v1/exchangeInfo`
    `GET /dapi/v1/exchangeInfo`

    References
    ----------
    https://binance-docs.github.io/apidocs/futures/en/#exchange-information
    https://binance-docs.github.io/apidocs/delivery/en/#exchange-information

    """

    def __init__(
        self,
        client: BinanceHttpClient,
        base_endpoint: str,
    ):
        methods = {
            HttpMethod.GET: BinanceSecurityType.NONE,
        }
        url_path = base_endpoint + "exchangeInfo"
        super().__init__(
            client,
            methods,
            url_path,
        )
        self._get_resp_decoder = msgspec.json.Decoder(BinanceFuturesExchangeInfo)

    async def get(self) -> BinanceFuturesExchangeInfo:
        method_type = HttpMethod.GET
        raw = await self._method(method_type, None)
        return self._get_resp_decoder.decode(raw)


class BinanceFuturesMarketHttpAPI(BinanceMarketHttpAPI):
    """
    Provides access to the Binance Futures HTTP REST API.

    Parameters
    ----------
    client : BinanceHttpClient
        The Binance REST API client.
    account_type : BinanceAccountType
        The Binance account type, used to select the endpoint.

    """

    def __init__(
        self,
        client: BinanceHttpClient,
        account_type: BinanceAccountType = BinanceAccountType.USDT_FUTURES,
    ):
        super().__init__(
            client=client,
            account_type=account_type,
        )

        if not account_type.is_futures:
            raise RuntimeError(  # pragma: no cover (design-time error)
                f"`BinanceAccountType` not USDT_FUTURES or COIN_FUTURES, was {account_type}",  # pragma: no cover
            )

        self._endpoint_futures_exchange_info = BinanceFuturesExchangeInfoHttp(
            client,
            self.base_endpoint,
        )

    async def query_futures_exchange_info(self) -> BinanceFuturesExchangeInfo:
        """
        Retrieve Binance Futures exchange information.
        """
        return await self._endpoint_futures_exchange_info.get()
```


---

## Overview

This file is located at `nautilus_trader/adapters/binance/futures/http/market.py` within the repository.

**Classes defined:** BinanceFuturesExchangeInfoHttp, BinanceFuturesMarketHttpAPI

**Functions defined:** __init__, __init__

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `BinanceFuturesExchangeInfoHttp`

**Inherits from:** BinanceHttpEndpoint


#### `BinanceFuturesMarketHttpAPI`

**Inherits from:** BinanceMarketHttpAPI


### Functions

#### `__init__(
        self,
        client: BinanceHttpClient,
        base_endpoint: str,
    )`


#### `__init__(
        self,
        client: BinanceHttpClient,
        account_type: BinanceAccountType = BinanceAccountType.USDT_FUTURES,
    )`


### Imports

- `import msgspec`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.common.enums import BinanceSecurityType`
- `from nautilus_trader.adapters.binance.futures.schemas.market import BinanceFuturesExchangeInfo`
- `from nautilus_trader.adapters.binance.http.client import BinanceHttpClient`
- `from nautilus_trader.adapters.binance.http.endpoint import BinanceHttpEndpoint`
- `from nautilus_trader.adapters.binance.http.market import BinanceMarketHttpAPI`
- `from nautilus_trader.core.nautilus_pyo3 import HttpMethod`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.binance.futures.http.market import BinanceFuturesExchangeInfoHttp
```


---

## Related Files

This file imports from the following modules:

- `import msgspec`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.common.enums import BinanceSecurityType`
- `from nautilus_trader.adapters.binance.futures.schemas.market import BinanceFuturesExchangeInfo`
- `from nautilus_trader.adapters.binance.http.client import BinanceHttpClient`
- `from nautilus_trader.adapters.binance.http.endpoint import BinanceHttpEndpoint`
- `from nautilus_trader.adapters.binance.http.market import BinanceMarketHttpAPI`
- `from nautilus_trader.core.nautilus_pyo3 import HttpMethod`

**Directory:** `nautilus_trader/adapters/binance/futures/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


