# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/adapters/tardis/__init__.py`
- **Size**: 2,163 bytes
- **Lines**: 46
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
Tardis crypto market data integration adapter https://tardis.dev/.

This subpackage provides instrument providers, data client configuration,
factories, constants, and data loaders for connecting to and interacting with
Tardis APIs and the Tardis Machine server.

For convenience, the most commonly used symbols are re-exported at the subpackage's
top level, so downstream code can simply import from ``nautilus_trader.adapters.tardis``.

"""
from nautilus_trader.adapters.tardis.config import TardisDataClientConfig
from nautilus_trader.adapters.tardis.constants import TARDIS
from nautilus_trader.adapters.tardis.constants import TARDIS_CLIENT_ID
from nautilus_trader.adapters.tardis.factories import TardisLiveDataClientFactory
from nautilus_trader.adapters.tardis.factories import get_tardis_http_client
from nautilus_trader.adapters.tardis.factories import get_tardis_instrument_provider
from nautilus_trader.adapters.tardis.loaders import TardisCSVDataLoader
from nautilus_trader.adapters.tardis.providers import TardisInstrumentProvider


__all__ = [
    "TARDIS",
    "TARDIS_CLIENT_ID",
    "TardisCSVDataLoader",
    "TardisDataClientConfig",
    "TardisInstrumentProvider",
    "TardisLiveDataClientFactory",
    "get_tardis_http_client",
    "get_tardis_instrument_provider",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Imports**: `nautilus_trader.adapters.tardis.config`, `nautilus_trader.adapters.tardis.constants`, `nautilus_trader.adapters.tardis.factories`, `nautilus_trader.adapters.tardis.loaders`, `nautilus_trader.adapters.tardis.providers`

## Related Files

This file is located in `nautilus_trader/adapters/tardis/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.995308Z*
