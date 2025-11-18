# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/__init__.py`
- **Size**: 2,512 bytes
- **Lines**: 54
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
The dYdX cryptocurrency decentralized exchange integration adapter.

This subpackage provides instrument provider, data and execution client configurations,
factories, and common constants/functions for connecting to and interacting with the
dYdX API.

For convenience, the most commonly used symbols are re-exported at the subpackage's
top level, so downstream code can simply import from ``nautilus_trader.adapters.dydx``.

"""
from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags
from nautilus_trader.adapters.dydx.common.constants import DYDX
from nautilus_trader.adapters.dydx.common.constants import DYDX_CLIENT_ID
from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE
from nautilus_trader.adapters.dydx.config import DYDXDataClientConfig
from nautilus_trader.adapters.dydx.config import DYDXExecClientConfig
from nautilus_trader.adapters.dydx.factories import DYDXLiveDataClientFactory
from nautilus_trader.adapters.dydx.factories import DYDXLiveExecClientFactory
from nautilus_trader.adapters.dydx.factories import get_dydx_grcp_client
from nautilus_trader.adapters.dydx.factories import get_dydx_http_client
from nautilus_trader.adapters.dydx.factories import get_dydx_instrument_provider
from nautilus_trader.adapters.dydx.providers import DYDXInstrumentProvider


__all__ = [
    "DYDX",
    "DYDX_CLIENT_ID",
    "DYDX_VENUE",
    "DYDXDataClientConfig",
    "DYDXExecClientConfig",
    "DYDXInstrumentProvider",
    "DYDXLiveDataClientFactory",
    "DYDXLiveExecClientFactory",
    "DYDXOrderTags",
    "get_dydx_grcp_client",
    "get_dydx_http_client",
    "get_dydx_instrument_provider",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Imports**: `nautilus_trader.adapters.dydx.common.common`, `nautilus_trader.adapters.dydx.common.constants`, `nautilus_trader.adapters.dydx.config`, `nautilus_trader.adapters.dydx.factories`, `nautilus_trader.adapters.dydx.providers`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.702483Z*
