# Documentation: `tests/integration_tests/adapters/binance/sandbox/sandbox_http_futures_account.py`
**Generated:** 2025-11-15T19:40:07.667684Z
**File Size:** 4212 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/sandbox/sandbox_http_futures_account.py`
- **Size:** 4,212 bytes
- **Lines:** 104
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5

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

import pytest

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client
from nautilus_trader.adapters.binance.futures.http.account import BinanceFuturesAccountHttpAPI
from nautilus_trader.common.component import LiveClock


@pytest.mark.asyncio()
async def test_binance_futures_account_http_client():
    clock = LiveClock()

    client = get_cached_binance_http_client(
        clock=clock,
        account_type=BinanceAccountType.USDT_FUTURES,
    )

    http_account = BinanceFuturesAccountHttpAPI(
        clock=clock,
        client=client,
        account_type=BinanceAccountType.USDT_FUTURES,
    )

    ############################################################################
    # ACCOUNT STATUS
    ############################################################################
    response = await http_account.account(recv_window=5000)
    print(response)

    ############################################################################
    # NEW ORDER (MARKET)
    ############################################################################
    # response = await http_account.new_order(
    #     symbol="ETHUSDT",
    #     side="BUY",
    #     type="MARKET",
    #     quantity="0.01",
    #     # stop_price="4200",
    #     # new_client_order_id="O-20211120-021300-001-001-1",
    #     # recv_window=5000,
    # )
    # print(json.dumps(response, indent=4))

    ############################################################################
    # NEW ORDER (LIMIT)
    ############################################################################
    # response = await http_account.new_order(
    #     symbol="ETHUSDT",
    #     side="BUY",
    #     type="LIMIT",
    #     quantity="0.01",
    #     time_in_force="GTC",
    #     price="1000",
    #     # stop_price="4200",
    #     # new_client_order_id="O-20211120-021300-001-001-1",
    #     # recv_window=5000,
    # )
    # print(json.dumps(response, indent=4))

    ############################################################################
    # CANCEL ORDER
    ############################################################################
    # response = await http_account.cancel_order(
    #     symbol="ETHUSDT",
    #     orig_client_order_id="fxSU6k85PZlwQEDFODh4Ad",
    #     #new_client_order_id=str(uuid.uuid4()),
    #     #recv_window=5000,
    # )
    # print(json.dumps(response, indent=4))

    ############################################################################
    # CANCEL ALL ORDERS
    ############################################################################
    # response = await http_account.cancel_open_orders(symbol="ETHUSDT")
    # print(json.dumps(response, indent=4))

    ############################################################################
    # OPEN ORDERS
    ############################################################################
    orders = await http_account.get_open_orders()
    print(orders)

    ############################################################################
    # POSITIONS
    ############################################################################
    positions = await http_account.get_position_risk()
    print(positions)

    await client.disconnect()
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/sandbox/sandbox_http_futures_account.py` within the repository.

**Import statements:** 5


---

## Detailed Analysis

### Imports

- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.futures.http.account import BinanceFuturesAccountHttpAPI`
- `from nautilus_trader.common.component import LiveClock`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.binance.sandbox.sandbox_http_futures_account
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.futures.http.account import BinanceFuturesAccountHttpAPI`
- `from nautilus_trader.common.component import LiveClock`

**Directory:** `tests/integration_tests/adapters/binance/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


