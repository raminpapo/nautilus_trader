# Documentation: `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_futures_market.py`
**Generated:** 2025-11-15T19:40:07.679102Z
**File Size:** 1466 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_futures_market.py`
- **Size:** 1,466 bytes
- **Lines:** 41
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4

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

import pytest

from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient
from nautilus_trader.common.component import LiveClock


@pytest.mark.asyncio()
async def test_binance_websocket_client():
    clock = LiveClock()

    loop = asyncio.get_running_loop()

    client = BinanceWebSocketClient(
        clock=clock,
        handler=print,
        base_url="wss://fstream.binance.com",
        loop=loop,
    )

    await client.connect()
    await client.subscribe_book_ticker("BTCUSDT-PERP")

    await asyncio.sleep(4)
    await client.disconnect()
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_futures_market.py` within the repository.

**Import statements:** 4


---

## Detailed Analysis

### Imports

- `import asyncio`
- `import pytest`
- `from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient`
- `from nautilus_trader.common.component import LiveClock`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.binance.sandbox.sandbox_ws_futures_market
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import pytest`
- `from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient`
- `from nautilus_trader.common.component import LiveClock`

**Directory:** `tests/integration_tests/adapters/binance/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


