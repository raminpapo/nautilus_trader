# Documentation: `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_spot_user.py`
**Generated:** 2025-11-15T19:40:07.680388Z
**File Size:** 1988 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_spot_user.py`
- **Size:** 1,988 bytes
- **Lines:** 55
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8

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
import os

import pytest

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client
from nautilus_trader.adapters.binance.spot.http.user import BinanceSpotUserDataHttpAPI
from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient
from nautilus_trader.common.component import LiveClock


@pytest.mark.asyncio()
async def test_binance_websocket_client():
    clock = LiveClock()

    client = get_cached_binance_http_client(
        clock=clock,
        account_type=BinanceAccountType.SPOT,
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET"),
    )

    user = BinanceSpotUserDataHttpAPI(client=client)
    response = await user.create_listen_key()
    key = response["listenKey"]

    loop = asyncio.get_running_loop()

    ws = BinanceWebSocketClient(
        clock=clock,
        handler=print,
        loop=loop,
    )

    ws.subscribe(key=key)

    await ws.connect()
    await asyncio.sleep(4)
    await ws.disconnect()
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_spot_user.py` within the repository.

**Import statements:** 8


---

## Detailed Analysis

### Imports

- `import asyncio`
- `import os`
- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.spot.http.user import BinanceSpotUserDataHttpAPI`
- `from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient`
- `from nautilus_trader.common.component import LiveClock`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.binance.sandbox.sandbox_ws_spot_user
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import os`
- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.spot.http.user import BinanceSpotUserDataHttpAPI`
- `from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient`
- `from nautilus_trader.common.component import LiveClock`

**Directory:** `tests/integration_tests/adapters/binance/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


