# Documentation: config.py

## File Metadata

- **Path**: `nautilus_trader/adapters/hyperliquid/config.py`
- **Size**: 4,412 bytes
- **Lines**: 106
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

from __future__ import annotations

from nautilus_trader.common.config import PositiveInt
from nautilus_trader.config import LiveDataClientConfig
from nautilus_trader.config import LiveExecClientConfig


class HyperliquidDataClientConfig(LiveDataClientConfig, frozen=True):
    """
    Configuration for ``HyperliquidDataClient`` instances.

    Parameters
    ----------
    base_url_http : str, optional
        The HTTP client custom endpoint override.
    base_url_ws : str, optional
        The WebSocket client custom endpoint override.
    http_proxy_url : str, optional
        Optional HTTP proxy URL.
    ws_proxy_url : str, optional
        Optional WebSocket proxy URL.
        Note: WebSocket proxy support is not yet implemented. This field is reserved
        for future functionality. Use `http_proxy_url` for REST API proxy support.
    testnet : bool, default False
        If the client is connecting to the Hyperliquid testnet API.
    http_timeout_secs : PositiveInt, default 10
        The timeout (seconds) for HTTP requests.

    """

    base_url_http: str | None = None
    base_url_ws: str | None = None
    http_proxy_url: str | None = None
    ws_proxy_url: str | None = None
    testnet: bool = False
    http_timeout_secs: PositiveInt = 10


class HyperliquidExecClientConfig(LiveExecClientConfig, frozen=True):
    """
    Configuration for ``HyperliquidExecutionClient`` instances.

    Parameters
    ----------
    private_key : str, optional
        The Hyperliquid EVM private key.
        If ``None`` then will source the `HYPERLIQUID_PK` or `HYPERLIQUID_TESTNET_PK`
        environment variable (depending on the `testnet` setting).
    vault_address : str, optional
        The vault address for vault trading.
        If ``None`` then will source the `HYPERLIQUID_VAULT` or `HYPERLIQUID_TESTNET_VAULT`
        environment variable (depending on the `testnet` setting).
    base_url_http : str, optional
        The HTTP client custom endpoint override.
    base_url_ws : str, optional
        The WebSocket client custom endpoint override.
    http_proxy_url : str, optional
        Optional HTTP proxy URL.
    ws_proxy_url : str, optional
        Optional WebSocket proxy URL.
        Note: WebSocket proxy support is not yet implemented. This field is reserved
        for future functionality. Use `http_proxy_url` for REST API proxy support.
    testnet : bool, default False
        If the client is connecting to the Hyperliquid testnet API.
    max_retries : PositiveInt, optional
        The maximum number of times a submit, cancel or modify order request will be retried.
    retry_delay_initial_ms : PositiveInt, optional
        The initial delay (milliseconds) between retries. Short delays with frequent retries may result in account bans.
    retry_delay_max_ms : PositiveInt, optional
        The maximum delay (milliseconds) between retries.
    http_timeout_secs : PositiveInt, default 10
        The timeout (seconds) for HTTP requests.

    Warnings
    --------
    A short `retry_delay` with frequent retries may result in account bans.

    """

    private_key: str | None = None
    vault_address: str | None = None
    base_url_http: str | None = None
    base_url_ws: str | None = None
    http_proxy_url: str | None = None
    ws_proxy_url: str | None = None
    testnet: bool = False
    max_retries: PositiveInt | None = None
    retry_delay_initial_ms: PositiveInt | None = None
    retry_delay_max_ms: PositiveInt | None = None
    http_timeout_secs: PositiveInt = 10

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`HyperliquidDataClientConfig`**: Class defined in this file
- **`HyperliquidExecClientConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `HyperliquidDataClientConfig`, `HyperliquidExecClientConfig`
**Imports**: `__future__`, `nautilus_trader.common.config`, `nautilus_trader.config`

## Related Files

This file is located in `nautilus_trader/adapters/hyperliquid/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.793620Z*
