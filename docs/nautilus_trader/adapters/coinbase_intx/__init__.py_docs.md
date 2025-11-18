# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/adapters/coinbase_intx/__init__.py`
- **Size**: 2,564 bytes
- **Lines**: 51
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
Coinbase International crypto exchange integration adapter.

This subpackage provides an instrument provider, data and execution clients,
configurations, data types and constants for connecting to and interacting with
Coinbase International's API.

For convenience, the most commonly used symbols are re-exported at the
subpackage's top level, so downstream code can simply import from
``nautilus_trader.adapters.coinbase_intx``.

"""
from nautilus_trader.adapters.coinbase_intx.config import CoinbaseIntxDataClientConfig
from nautilus_trader.adapters.coinbase_intx.config import CoinbaseIntxExecClientConfig
from nautilus_trader.adapters.coinbase_intx.constants import COINBASE_INTX
from nautilus_trader.adapters.coinbase_intx.constants import COINBASE_INTX_CLIENT_ID
from nautilus_trader.adapters.coinbase_intx.constants import COINBASE_INTX_VENUE
from nautilus_trader.adapters.coinbase_intx.factories import CoinbaseIntxLiveDataClientFactory
from nautilus_trader.adapters.coinbase_intx.factories import CoinbaseIntxLiveExecClientFactory
from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client
from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_instrument_provider
from nautilus_trader.adapters.coinbase_intx.providers import CoinbaseIntxInstrumentProvider


__all__ = [
    "COINBASE_INTX",
    "COINBASE_INTX_CLIENT_ID",
    "COINBASE_INTX_VENUE",
    "CoinbaseIntxDataClientConfig",
    "CoinbaseIntxExecClientConfig",
    "CoinbaseIntxInstrumentProvider",
    "CoinbaseIntxLiveDataClientFactory",
    "CoinbaseIntxLiveExecClientFactory",
    "get_coinbase_intx_http_client",
    "get_coinbase_intx_instrument_provider",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Imports**: `nautilus_trader.adapters.coinbase_intx.config`, `nautilus_trader.adapters.coinbase_intx.constants`, `nautilus_trader.adapters.coinbase_intx.factories`, `nautilus_trader.adapters.coinbase_intx.providers`

## Related Files

This file is located in `nautilus_trader/adapters/coinbase_intx/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.653930Z*
