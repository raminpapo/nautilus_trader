# Documentation: `tests/integration_tests/adapters/polymarket/sandbox/sandbox_websocket.py`
**Generated:** 2025-11-15T19:40:07.935143Z
**File Size:** 1828 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/sandbox/sandbox_websocket.py`
- **Size:** 1,828 bytes
- **Lines:** 47
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3

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

from nautilus_trader.adapters.polymarket.websocket.client import PolymarketWebSocketClient
from nautilus_trader.common.component import LiveClock


async def run_polymarket_websocket():
    clock = LiveClock()
    loop = asyncio.get_running_loop()

    client = PolymarketWebSocketClient(
        clock=clock,
        base_url=None,
        channel="market",
        handler=print,
        handler_reconnect=None,
        loop=loop,
    )

    # market = "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"
    token_yes = "21742633143463906290569050155826241533067272736897614950488156847949938836455"
    token_no = "48331043336612883890938759509493159234755048973500640148014422747788308965732"

    await client.subscribe_book(asset=token_yes)
    await client.subscribe_book(asset=token_no)
    await client.connect()

    await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(run_polymarket_websocket())
```


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/sandbox/sandbox_websocket.py` within the repository.

**Import statements:** 3


---

## Detailed Analysis

### Imports

- `import asyncio`
- `from nautilus_trader.adapters.polymarket.websocket.client import PolymarketWebSocketClient`
- `from nautilus_trader.common.component import LiveClock`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.polymarket.sandbox.sandbox_websocket
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.adapters.polymarket.websocket.client import PolymarketWebSocketClient`
- `from nautilus_trader.common.component import LiveClock`

**Directory:** `tests/integration_tests/adapters/polymarket/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


