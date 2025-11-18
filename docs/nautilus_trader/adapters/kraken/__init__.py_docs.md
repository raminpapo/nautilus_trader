# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/adapters/kraken/__init__.py`
- **Size**: 2,142 bytes
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
Kraken cryptocurrency exchange integration adapter.

This subpackage provides an instrument provider, data client,
configurations, and constants for connecting to and interacting with Kraken's API.

For convenience, the most commonly used symbols are re-exported at the
subpackage's top level, so downstream code can simply import from
``nautilus_trader.adapters.kraken``.

"""
from nautilus_trader.adapters.kraken.config import KrakenDataClientConfig
from nautilus_trader.adapters.kraken.constants import KRAKEN
from nautilus_trader.adapters.kraken.constants import KRAKEN_CLIENT_ID
from nautilus_trader.adapters.kraken.constants import KRAKEN_VENUE
from nautilus_trader.adapters.kraken.data import KrakenDataClient
from nautilus_trader.adapters.kraken.factories import KrakenLiveDataClientFactory
from nautilus_trader.adapters.kraken.providers import KrakenInstrumentProvider
from nautilus_trader.adapters.kraken.types import KRAKEN_INSTRUMENT_TYPES
from nautilus_trader.adapters.kraken.types import KrakenInstrument


__all__ = [
    "KRAKEN",
    "KRAKEN_CLIENT_ID",
    "KRAKEN_INSTRUMENT_TYPES",
    "KRAKEN_VENUE",
    "KrakenDataClient",
    "KrakenDataClientConfig",
    "KrakenInstrument",
    "KrakenInstrumentProvider",
    "KrakenLiveDataClientFactory",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Imports**: `nautilus_trader.adapters.kraken.config`, `nautilus_trader.adapters.kraken.constants`, `nautilus_trader.adapters.kraken.data`, `nautilus_trader.adapters.kraken.factories`, `nautilus_trader.adapters.kraken.providers`, `nautilus_trader.adapters.kraken.types`

## Related Files

This file is located in `nautilus_trader/adapters/kraken/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.883032Z*
