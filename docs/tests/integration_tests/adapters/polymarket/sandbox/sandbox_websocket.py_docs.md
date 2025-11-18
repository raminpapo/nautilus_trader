# Documentation: sandbox_websocket.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/sandbox/sandbox_websocket.py`
- **Size**: 1,828 bytes
- **Lines**: 48
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `asyncio`, `nautilus_trader.adapters.polymarket.websocket.client`, `nautilus_trader.common.component`

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/sandbox/sandbox_websocket.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.161555Z*
