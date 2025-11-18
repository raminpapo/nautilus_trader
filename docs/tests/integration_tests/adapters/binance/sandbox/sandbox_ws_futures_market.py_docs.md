# Documentation: sandbox_ws_futures_market.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/sandbox/sandbox_ws_futures_market.py`
- **Size**: 1,464 bytes
- **Lines**: 42
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

import pytest

from nautilus_trader.adapters.binance.websocket.client import BinanceWebSocketClient
from nautilus_trader.common.component import LiveClock


@pytest.mark.asyncio
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Imports**: `asyncio`, `nautilus_trader.adapters.binance.websocket.client`, `nautilus_trader.common.component`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/sandbox/sandbox_ws_futures_market.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.739771Z*
