# Documentation: endpoint.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/endpoints/endpoint.py`
- **Size**: 3,602 bytes
- **Lines**: 99
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
"""
Define the base class for dYdX endpoints.
"""

from typing import Any

import msgspec
from msgspec import DecodeError

from nautilus_trader.adapters.dydx.common.enums import DYDXEndpointType
from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient
from nautilus_trader.adapters.dydx.http.errors import DYDXError
from nautilus_trader.adapters.dydx.http.errors import should_retry
from nautilus_trader.common.component import Logger
from nautilus_trader.core.nautilus_pyo3 import HttpError
from nautilus_trader.core.nautilus_pyo3 import HttpMethod
from nautilus_trader.core.nautilus_pyo3 import HttpTimeoutError
from nautilus_trader.live.retry import RetryManagerPool


class DYDXHttpEndpoint:
    """
    Define the base class for dYdX endpoints.
    """

    def __init__(
        self,
        client: DYDXHttpClient,
        endpoint_type: DYDXEndpointType,
        url_path: str | None = None,
        name: str | None = None,
    ) -> None:
        """
        Construct the base class for dYdX endpoints.
        """
        self.client = client
        self.endpoint_type = endpoint_type
        self.url_path = url_path
        self.name = name

        self.decoder = msgspec.json.Decoder()
        self.encoder = msgspec.json.Encoder()

        self._method_request: dict[DYDXEndpointType, Any] = {
            DYDXEndpointType.NONE: self.client.send_request,
            DYDXEndpointType.ACCOUNT: self.client.send_request,
        }

        self._retry_manager_pool = RetryManagerPool[None](
            pool_size=100,
            max_retries=5,
            delay_initial_ms=100,
            delay_max_ms=5_000,
            backoff_factor=2,
            logger=Logger(name="DYDXHttpEndpoint"),
            exc_types=(HttpTimeoutError, HttpError, DYDXError, DecodeError),
            retry_check=should_retry,
        )

    async def _method(
        self,
        method_type: HttpMethod,
        params: Any | None = None,
        url_path: str | None = None,
    ) -> bytes | None:
        payload: dict[str, Any] = self.decoder.decode(self.encoder.encode(params))
        method_call = self._method_request[self.endpoint_type]
        url_path = url_path or self.url_path
        retry_name = self.name or "http_call"

        retry_manager = await self._retry_manager_pool.acquire()
        try:
            result: bytes | None = await retry_manager.run(
                name=retry_name,
                details=[url_path, str(params)],
                func=method_call,
                http_method=method_type,
                url_path=url_path,
                payload=payload,
            )
        finally:
            await self._retry_manager_pool.release(retry_manager)

        return result

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXHttpEndpoint`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Classs**: `DYDXHttpEndpoint`
**Imports**: `msgspec`, `nautilus_trader.adapters.dydx.common.enums`, `nautilus_trader.adapters.dydx.http.client`, `nautilus_trader.adapters.dydx.http.errors`, `nautilus_trader.common.component`, `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.live.retry`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/endpoints/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.737571Z*
