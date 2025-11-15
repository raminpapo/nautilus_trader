# Documentation: `tests/integration_tests/adapters/interactive_brokers/client/test_client_connection.py`
**Generated:** 2025-11-15T19:40:07.778272Z
**File Size:** 4213 bytes
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

- **Path:** `tests/integration_tests/adapters/interactive_brokers/client/test_client_connection.py`
- **Size:** 4,213 bytes
- **Lines:** 114
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6

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
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

import pytest
from ibapi.const import NO_VALID_ID
from ibapi.errors import CONNECT_FAIL


@pytest.mark.asyncio
async def test_connect_success(ib_client):
    ib_client._initialize_connection_params = MagicMock()
    ib_client._connect_socket = AsyncMock()
    ib_client._send_version_info = AsyncMock()
    ib_client._receive_server_info = AsyncMock()
    ib_client._eclient.connTime = MagicMock()
    ib_client._eclient.setConnState = MagicMock()

    await ib_client._connect()

    ib_client._initialize_connection_params.assert_called_once()
    ib_client._connect_socket.assert_awaited_once()
    ib_client._send_version_info.assert_awaited_once()
    ib_client._receive_server_info.assert_awaited_once()
    ib_client._eclient.setConnState.assert_called_with(ib_client._eclient.CONNECTED)


@pytest.mark.asyncio
async def test_connect_cancelled(ib_client):
    ib_client._initialize_connection_params = MagicMock()
    ib_client._connect_socket = AsyncMock(side_effect=asyncio.CancelledError())
    ib_client._disconnect = AsyncMock()

    await ib_client._connect()

    ib_client._disconnect.assert_not_awaited()


@pytest.mark.asyncio
async def test_connect_fail(ib_client):
    ib_client._initialize_connection_params = MagicMock()
    ib_client._connect_socket = AsyncMock(side_effect=Exception("Connection failed"))
    ib_client._disconnect = AsyncMock()
    ib_client._handle_reconnect = AsyncMock()
    ib_client._eclient.wrapper.error = MagicMock()

    await ib_client._connect()

    ib_client._eclient.wrapper.error.assert_called_with(
        NO_VALID_ID,
        CONNECT_FAIL.code(),
        CONNECT_FAIL.msg(),
    )
    ib_client._handle_reconnect.assert_not_awaited()


# Test for successful reconnection
@pytest.mark.asyncio
async def test_reconnect_success(ib_client):
    """
    Test case for a successful reconnection.
    """
    # Mocking the disconnect and connect methods
    ib_client.disconnect = AsyncMock()
    ib_client.connect = AsyncMock()

    # Simulating a successful reconnection by having isConnected return False first and then True
    ib_client.isConnected = MagicMock(side_effect=[False, True])

    # Attempting to reconnect
    await ib_client.disconnect()
    await ib_client.connect()

    # Assertions to ensure disconnect and connect methods were called
    ib_client.disconnect.assert_awaited_once()
    ib_client.connect.assert_awaited_once()


# Test for failed reconnection
@pytest.mark.asyncio
async def test_reconnect_fail(ib_client):
    """
    Test case for a failed reconnection.
    """
    # Mocking the disconnect and connect methods
    ib_client.disconnect = AsyncMock()
    ib_client.connect = AsyncMock(side_effect=Exception("Failed to reconnect"))

    # Simulating a failed reconnection by having isConnected return False both times
    ib_client.isConnected = MagicMock(side_effect=[False, False])

    # Attempting to reconnect and expecting an exception due to failed reconnection
    with pytest.raises(Exception, match="Failed to reconnect"):
        await ib_client.disconnect()
        await ib_client.connect()

    # Assertions to ensure disconnect and connect methods were called
    ib_client.disconnect.assert_awaited_once()
    ib_client.connect.assert_awaited_once()
```


---

## Overview

This file is located at `tests/integration_tests/adapters/interactive_brokers/client/test_client_connection.py` within the repository.

**Import statements:** 6


---

## Detailed Analysis

### Imports

- `import asyncio`
- `from unittest.mock import AsyncMock`
- `from unittest.mock import MagicMock`
- `import pytest`
- `from ibapi.const import NO_VALID_ID`
- `from ibapi.errors import CONNECT_FAIL`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.interactive_brokers.client.test_client_connection
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from unittest.mock import AsyncMock`
- `from unittest.mock import MagicMock`
- `import pytest`
- `from ibapi.const import NO_VALID_ID`
- `from ibapi.errors import CONNECT_FAIL`

**Directory:** `tests/integration_tests/adapters/interactive_brokers/client`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


