# Documentation: asset_positions.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/endpoints/account/asset_positions.py`
- **Size**: 2,531 bytes
- **Lines**: 72
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
Provide the Get AssetPositions HTTP endpoint.
"""

import msgspec

from nautilus_trader.adapters.dydx.common.enums import DYDXEndpointType
from nautilus_trader.adapters.dydx.endpoints.endpoint import DYDXHttpEndpoint
from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient
from nautilus_trader.adapters.dydx.schemas.account.asset_positions import DYDXAssetPositionsResponse
from nautilus_trader.core.nautilus_pyo3 import HttpMethod


class DYDXGetAssetPositionsGetParams(msgspec.Struct, omit_defaults=True, frozen=True):
    """
    Define the parameters for the Get Asset Positions endpoint.
    """

    address: str
    subaccountNumber: int


class DYDXGetAssetPositionsEndpoint(DYDXHttpEndpoint):
    """
    Provide the Get Asset Positions HTTP endpoint.
    """

    def __init__(
        self,
        client: DYDXHttpClient,
    ) -> None:
        """
        Construct a new get address HTTP endpoint.
        """
        url_path = "/assetPositions"
        super().__init__(
            client=client,
            endpoint_type=DYDXEndpointType.ACCOUNT,
            url_path=url_path,
            name="DYDXGetAssetPositionsEndpoint",
        )
        self.http_method = HttpMethod.GET
        self._get_resp_decoder = msgspec.json.Decoder(DYDXAssetPositionsResponse)

    async def get(
        self,
        params: DYDXGetAssetPositionsGetParams,
    ) -> DYDXAssetPositionsResponse | None:
        """
        Call the endpoint to list the instruments.
        """
        raw = await self._method(self.http_method, params)

        if raw is not None:
            return self._get_resp_decoder.decode(raw)

        return None

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXGetAssetPositionsGetParams`**: Class defined in this file
- **`DYDXGetAssetPositionsEndpoint`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `DYDXGetAssetPositionsEndpoint`, `DYDXGetAssetPositionsGetParams`
**Imports**: `msgspec`, `nautilus_trader.adapters.dydx.common.enums`, `nautilus_trader.adapters.dydx.endpoints.endpoint`, `nautilus_trader.adapters.dydx.http.client`, `nautilus_trader.adapters.dydx.schemas.account.asset_positions`, `nautilus_trader.core.nautilus_pyo3`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/endpoints/account/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.728043Z*
