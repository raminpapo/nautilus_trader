# Documentation: urls.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/urls.py`
- **Size**: 1,622 bytes
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`get_http_base_url()`**: Function defined in this file
- **`get_ws_base_url()`**: Function defined in this file
- **`get_grpc_base_url()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `get_grpc_base_url`, `get_http_base_url`, `get_ws_base_url`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.715401Z*
