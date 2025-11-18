# Documentation: candles.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/endpoints/market/candles.py`
- **Size**: 2,770 bytes
- **Lines**: 81
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
Define the candles / bars endpoint.
"""


import datetime

import msgspec

from nautilus_trader.adapters.dydx.common.enums import DYDXCandlesResolution
from nautilus_trader.adapters.dydx.common.enums import DYDXEndpointType
from nautilus_trader.adapters.dydx.endpoints.endpoint import DYDXHttpEndpoint
from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient
from nautilus_trader.adapters.dydx.schemas.ws import DYDXCandle
from nautilus_trader.core.nautilus_pyo3 import HttpMethod


class DYDXCandlesGetParams(msgspec.Struct, omit_defaults=True):
    """
    Represent the dYdX list perpetual markets parameters.
    """

    resolution: DYDXCandlesResolution
    limit: int | None = None
    fromISO: datetime.datetime | None = None
    toISO: datetime.datetime | None = None


class DYDXCandlesResponse(msgspec.Struct, forbid_unknown_fields=False):
    """
    Represent the dYdX candles response object.
    """

    candles: list[DYDXCandle]


class DYDXCandlesEndpoint(DYDXHttpEndpoint):
    """
    Define the bars endpoint.
    """

    def __init__(self, client: DYDXHttpClient) -> None:
        """
        Define the bars endpoint.
        """
        url_path = "/candles/perpetualMarkets/"
        super().__init__(
            client=client,
            url_path=url_path,
            endpoint_type=DYDXEndpointType.NONE,
            name="DYDXCandlesEndpoint",
        )
        self.method_type = HttpMethod.GET
        self._decoder = msgspec.json.Decoder(DYDXCandlesResponse)

    async def get(self, symbol: str, params: DYDXCandlesGetParams) -> DYDXCandlesResponse | None:
        """
        Call the bars endpoint.
        """
        url_path = f"/candles/perpetualMarkets/{symbol}"
        raw = await self._method(self.method_type, params=params, url_path=url_path)

        if raw is not None:
            return self._decoder.decode(raw)

        return None

```

## High-Level Overview

This file is part of the NautilusTrader repository. 3 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXCandlesGetParams`**: Class defined in this file
- **`DYDXCandlesResponse`**: Class defined in this file
- **`DYDXCandlesEndpoint`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Classs**: `DYDXCandlesEndpoint`, `DYDXCandlesGetParams`, `DYDXCandlesResponse`
**Imports**: `datetime`, `msgspec`, `nautilus_trader.adapters.dydx.common.enums`, `nautilus_trader.adapters.dydx.endpoints.endpoint`, `nautilus_trader.adapters.dydx.http.client`, `nautilus_trader.adapters.dydx.schemas.ws`, `nautilus_trader.core.nautilus_pyo3`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/endpoints/market/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.740614Z*
