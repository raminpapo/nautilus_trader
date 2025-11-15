# Documentation: `nautilus_trader/adapters/dydx/common/urls.py`
**Generated:** 2025-11-15T19:40:04.247802Z
**File Size:** 1622 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/common/urls.py`
- **Size:** 1,622 bytes
- **Lines:** 47
- **Extension:** `.py`
- **Type:** text
- **Functions:** 3

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
Define base urls for HTTP endpoints and websocket data streams.
"""


def get_http_base_url(is_testnet: bool) -> str:
    """
    Provide the base HTTP url for dYdX.
    """
    if is_testnet:
        return "https://indexer.v4testnet.dydx.exchange/v4"

    return "https://indexer.dydx.trade/v4"


def get_ws_base_url(is_testnet: bool) -> str:
    """
    Provide the base websockets url for dYdX.
    """
    if is_testnet:
        return "wss://indexer.v4testnet.dydx.exchange/v4/ws"

    return "wss://indexer.dydx.trade/v4/ws"


def get_grpc_base_url(is_testnet: bool) -> str:
    """
    Provide the base GRPC url for dYdX.
    """
    if is_testnet:
        return "test-dydx-grpc.kingnodes.com"

    return "dydx-ops-grpc.kingnodes.com:443"
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/common/urls.py` within the repository.

**Functions defined:** get_http_base_url, get_ws_base_url, get_grpc_base_url


---

## Detailed Analysis

### Functions

#### `get_http_base_url(is_testnet: bool)`


#### `get_ws_base_url(is_testnet: bool)`


#### `get_grpc_base_url(is_testnet: bool)`



---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.common.urls import get_http_base_url
```


---

## Related Files

**Directory:** `nautilus_trader/adapters/dydx/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


