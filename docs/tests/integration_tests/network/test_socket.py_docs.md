# Documentation: test_socket.py

## File Metadata

- **Path**: `tests/integration_tests/network/test_socket.py`
- **Size**: 3,835 bytes
- **Lines**: 130
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

from nautilus_trader.core.nautilus_pyo3 import SocketClient
from nautilus_trader.core.nautilus_pyo3 import SocketConfig
from nautilus_trader.test_kit.functions import eventually


pytestmark = pytest.mark.skip()
# pytestmark = pytest.mark.skipif(sys.platform != "linux", reason="Run socket tests on Linux only")


def _config(socket_server, handler):
    host, port = socket_server
    server_url = f"{host}:{port}"
    return SocketConfig(
        url=server_url,
        ssl=False,
        handler=handler,
        suffix=b"\r\n",
    )


@pytest.mark.asyncio
async def test_connect_and_disconnect(socket_server):
    # Arrange
    store = []

    config = _config(socket_server, store.append)
    client = await SocketClient.connect(config)

    # Act, Assert
    await eventually(lambda: client.is_active())
    await client.close()
    await eventually(lambda: not client.is_active())


@pytest.mark.asyncio
async def test_client_send_recv(socket_server):
    # Arrange
    store = []
    config = _config(socket_server, store.append)
    client = await SocketClient.connect(config)

    await eventually(lambda: client.is_active())

    # Act
    num_messages = 3
    for _ in range(num_messages):
        await client.send(b"Hello")
    await asyncio.sleep(0.1)

    await client.close()
    await eventually(lambda: not client.is_active())

    # Assert
    await eventually(lambda: store == [b"connected"] + [b"hello"] * 2)
    await asyncio.sleep(0.1)


# @pytest.mark.asyncio()
# async def test_client_send_recv_json(socket_server):
#     # Arrange
#     store = []
#     config = _config(socket_server, store.append)
#     client = await SocketClient.connect(config)
#
#     await eventually(lambda: client.is_alive())
#
#     # Act
#     num_messages = 3
#     for _ in range(num_messages):
#         await client.send(msgspec.json.encode({"method": "SUBSCRIBE"}))
#     await asyncio.sleep(0.3)
#     await client.disconnect()
#
#     expected = [b"connected"] + [b'{"method":"SUBSCRIBE"}-response'] * 3
#     assert store == expected
#     await client.disconnect()
#     await eventually(lambda: not client.is_alive())


@pytest.mark.asyncio
async def test_reconnect_after_close(closing_socket_server):
    # Arrange
    store = []
    config = _config(closing_socket_server, store.append)
    client = await SocketClient.connect(config)

    await eventually(lambda: client.is_active())

    # Act
    await asyncio.sleep(2)

    # Assert
    await eventually(lambda: store == [b"connected"] * 2)


# @pytest.mark.asyncio()
# async def test_exponential_backoff(self, websocket_server):
#     # Arrange
#     store = []
#     client = await WebSocketClient.connect(
#         url=_server_url(websocket_server),
#         handler=store.append,
#     )
#
#     # Act
#     for _ in range(2):
#         await self.client.send(b"close")
#         await asyncio.sleep(0.1)
#
#     assert client.connection_retry_count == 2

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`_config()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `_config`
**Imports**: `asyncio`, `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.test_kit.functions`, `pytest`

## Related Files

This file is located in `tests/integration_tests/network/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/network/test_socket.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.258800Z*
