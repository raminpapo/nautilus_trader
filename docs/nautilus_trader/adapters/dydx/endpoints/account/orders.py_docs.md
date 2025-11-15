# Documentation: `nautilus_trader/adapters/dydx/endpoints/account/orders.py`
**Generated:** 2025-11-15T19:40:04.262654Z
**File Size:** 2926 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/endpoints/account/orders.py`
- **Size:** 2,926 bytes
- **Lines:** 80
- **Extension:** `.py`
- **Type:** text
- **Imports:** 10
- **Classes:** 2
- **Functions:** 1

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
"""
Provide the Get Address HTTP endpoint.
"""

import datetime

import msgspec

from nautilus_trader.adapters.dydx.common.enums import DYDXEndpointType
from nautilus_trader.adapters.dydx.common.enums import DYDXOrderSide
from nautilus_trader.adapters.dydx.common.enums import DYDXOrderStatus
from nautilus_trader.adapters.dydx.common.enums import DYDXOrderType
from nautilus_trader.adapters.dydx.endpoints.endpoint import DYDXHttpEndpoint
from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient
from nautilus_trader.adapters.dydx.schemas.account.orders import DYDXOrderResponse
from nautilus_trader.core.nautilus_pyo3 import HttpMethod


class DYDXGetOrdersGetParams(msgspec.Struct, omit_defaults=True, frozen=True):
    """
    Define the parameters for the order endpoint.
    """

    address: str
    subaccountNumber: int
    limit: int | None = None
    ticker: str | None = None
    side: DYDXOrderSide | None = None
    type: DYDXOrderType | None = None
    status: list[DYDXOrderStatus] | None = None
    goodTilBlockBeforeOrAt: int | None = None
    goodTilBlockTimeBeforeOrAt: datetime.datetime | None = None
    returnLatestOrders: bool | None = None


class DYDXGetOrdersEndpoint(DYDXHttpEndpoint):
    """
    Provide the orders HTTP endpoint.
    """

    def __init__(
        self,
        client: DYDXHttpClient,
    ) -> None:
        """
        Construct a new get address HTTP endpoint.
        """
        url_path = "/orders"
        super().__init__(
            client=client,
            endpoint_type=DYDXEndpointType.ACCOUNT,
            url_path=url_path,
            name="DYDXGetOrdersEndpoint",
        )
        self.http_method = HttpMethod.GET

    async def get(self, params: DYDXGetOrdersGetParams) -> list[DYDXOrderResponse] | None:
        """
        Call the endpoint to list the instruments.
        """
        raw = await self._method(self.http_method, params)

        if raw is not None:
            return msgspec.json.decode(raw, type=list[DYDXOrderResponse], strict=True)

        return None
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/endpoints/account/orders.py` within the repository.

**Classes defined:** DYDXGetOrdersGetParams, DYDXGetOrdersEndpoint

**Functions defined:** __init__

**Import statements:** 10


---

## Detailed Analysis

### Classes

#### `DYDXGetOrdersGetParams`

**Inherits from:** msgspec.Struct, omit_defaults=True, frozen=True


#### `DYDXGetOrdersEndpoint`

**Inherits from:** DYDXHttpEndpoint


### Functions

#### `__init__(
        self,
        client: DYDXHttpClient,
    )`


### Imports

- `import datetime`
- `import msgspec`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXEndpointType`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXOrderSide`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXOrderStatus`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXOrderType`
- `from nautilus_trader.adapters.dydx.endpoints.endpoint import DYDXHttpEndpoint`
- `from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient`
- `from nautilus_trader.adapters.dydx.schemas.account.orders import DYDXOrderResponse`
- `from nautilus_trader.core.nautilus_pyo3 import HttpMethod`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.endpoints.account.orders import DYDXGetOrdersGetParams
```


---

## Related Files

This file imports from the following modules:

- `import datetime`
- `import msgspec`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXEndpointType`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXOrderSide`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXOrderStatus`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXOrderType`
- `from nautilus_trader.adapters.dydx.endpoints.endpoint import DYDXHttpEndpoint`
- `from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient`
- `from nautilus_trader.adapters.dydx.schemas.account.orders import DYDXOrderResponse`
- `from nautilus_trader.core.nautilus_pyo3 import HttpMethod`

**Directory:** `nautilus_trader/adapters/dydx/endpoints/account`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


