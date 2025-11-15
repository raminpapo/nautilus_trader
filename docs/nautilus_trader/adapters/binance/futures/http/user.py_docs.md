# Documentation: `nautilus_trader/adapters/binance/futures/http/user.py`
**Generated:** 2025-11-15T19:40:04.100169Z
**File Size:** 1962 bytes
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

- **Path:** `nautilus_trader/adapters/binance/futures/http/user.py`
- **Size:** 1,962 bytes
- **Lines:** 47
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 1
- **Functions:** 1

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

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.http.client import BinanceHttpClient
from nautilus_trader.adapters.binance.http.user import BinanceUserDataHttpAPI


class BinanceFuturesUserDataHttpAPI(BinanceUserDataHttpAPI):
    """
    Provides access to the Binance Futures User Data HTTP REST API.

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
                f"`BinanceAccountType` not USDT_FUTURES or COIN_FUTURES, was {account_type}",  # pragma: no cover (design-time error)
            )
```


---

## Overview

This file is located at `nautilus_trader/adapters/binance/futures/http/user.py` within the repository.

**Classes defined:** BinanceFuturesUserDataHttpAPI

**Functions defined:** __init__

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `BinanceFuturesUserDataHttpAPI`

**Inherits from:** BinanceUserDataHttpAPI


### Functions

#### `__init__(
        self,
        client: BinanceHttpClient,
        account_type: BinanceAccountType = BinanceAccountType.USDT_FUTURES,
    )`


### Imports

- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.http.client import BinanceHttpClient`
- `from nautilus_trader.adapters.binance.http.user import BinanceUserDataHttpAPI`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.binance.futures.http.user import BinanceFuturesUserDataHttpAPI
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.http.client import BinanceHttpClient`
- `from nautilus_trader.adapters.binance.http.user import BinanceUserDataHttpAPI`

**Directory:** `nautilus_trader/adapters/binance/futures/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


