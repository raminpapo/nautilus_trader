# Documentation: `tests/integration_tests/network/conftest.py`
**Generated:** 2025-11-15T19:40:08.010181Z
**File Size:** 3447 bytes
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

- **Path:** `tests/integration_tests/network/conftest.py`
- **Size:** 3,447 bytes
- **Lines:** 108
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
import weakref

import pytest
import pytest_asyncio
from aiohttp import WSCloseCode
from aiohttp import WSMsgType
from aiohttp import web
from aiohttp.test_utils import TestServer


async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    tasks = set()

    async def write():
        writer.write(b"connected\r\n")
        while True:
            writer.write(b"hello\r\n")
            await asyncio.sleep(0.1)

    loop = asyncio.get_running_loop()

    task = loop.create_task(write())
    tasks.add(task)

    while True:
        req = await reader.readline()
        if req.strip() == b"close":
            writer.close()


@pytest_asyncio.fixture()
async def socket_server():
    server = await asyncio.start_server(handle_echo, "127.0.0.1", 0)
    addr = server.sockets[0].getsockname()
    async with server:
        await server.start_serving()
        yield addr


@pytest_asyncio.fixture(name="closing_socket_server")
async def fixture_closing_socket_server():
    async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        async def write():
            writer.write(b"connected\r\n")
            await asyncio.sleep(0.1)
            await writer.drain()
            writer.close()
            await writer.wait_closed()
            # print("Server closed")

        await write()

    server = await asyncio.start_server(handler, "127.0.0.1", 0)
    addr = server.sockets[0].getsockname()
    async with server:
        yield addr


@pytest_asyncio.fixture(name="websocket_server")
@pytest.mark.asyncio()
async def fixture_websocket_server(event_loop):
    async def handler(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        request.app["websockets"].add(ws)

        await ws.send_bytes(b"connected")

        async for msg in ws:
            if msg.type == WSMsgType.BINARY:
                if msg.data == b"close":
                    await ws.close(code=257)
                else:
                    await ws.send_bytes(msg.data + b"-response")
        return ws

    app = web.Application()
    app["websockets"] = weakref.WeakSet()
    app.add_routes([web.get("/ws", handler)])

    async def on_shutdown(app):
        for ws in set(app["websockets"]):
            await ws.close(code=WSCloseCode.GOING_AWAY, message="Server shutdown")

    app.on_shutdown.append(on_shutdown)

    server = TestServer(app)
    await server.start_server(loop=event_loop)
    yield server
    await app.shutdown()
    await app.cleanup()
    await server.close()
```


---

## Overview

This file is located at `tests/integration_tests/network/conftest.py` within the repository.

**Import statements:** 8


---

## Detailed Analysis

### Imports

- `import asyncio`
- `import weakref`
- `import pytest`
- `import pytest_asyncio`
- `from aiohttp import WSCloseCode`
- `from aiohttp import WSMsgType`
- `from aiohttp import web`
- `from aiohttp.test_utils import TestServer`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.network.conftest
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import weakref`
- `import pytest`
- `import pytest_asyncio`
- `from aiohttp import WSCloseCode`
- `from aiohttp import WSMsgType`
- `from aiohttp import web`
- `from aiohttp.test_utils import TestServer`

**Directory:** `tests/integration_tests/network`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


