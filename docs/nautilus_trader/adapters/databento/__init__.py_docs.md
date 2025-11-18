# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/adapters/databento/__init__.py`
- **Size**: 2,544 bytes
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
Databento market data integration adapter.

This subpackage provides a data client factory, instrument provider,
constants, configurations, and data loaders for connecting to and
interacting with the Databento API, and decoding Databento Binary
Encoding (DBN) format data.

For convenience, the most commonly used symbols are re-exported at the
subpackage's top level, so downstream code can simply import from
``nautilus_trader.adapters.databento``.

"""
from nautilus_trader.adapters.databento.config import DatabentoDataClientConfig
from nautilus_trader.adapters.databento.constants import ALL_SYMBOLS
from nautilus_trader.adapters.databento.constants import DATABENTO
from nautilus_trader.adapters.databento.constants import DATABENTO_CLIENT_ID
from nautilus_trader.adapters.databento.factories import DatabentoLiveDataClientFactory
from nautilus_trader.adapters.databento.factories import get_cached_databento_http_client
from nautilus_trader.adapters.databento.factories import get_cached_databento_instrument_provider
from nautilus_trader.adapters.databento.loaders import DatabentoDataLoader
from nautilus_trader.adapters.databento.providers import DatabentoInstrumentProvider
from nautilus_trader.core.nautilus_pyo3 import DatabentoImbalance
from nautilus_trader.core.nautilus_pyo3 import DatabentoStatistics


__all__ = [
    "ALL_SYMBOLS",
    "DATABENTO",
    "DATABENTO_CLIENT_ID",
    "DatabentoDataClientConfig",
    "DatabentoDataLoader",
    "DatabentoImbalance",
    "DatabentoInstrumentProvider",
    "DatabentoLiveDataClientFactory",
    "DatabentoStatistics",
    "get_cached_databento_http_client",
    "get_cached_databento_instrument_provider",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Imports**: `nautilus_trader.adapters.databento.config`, `nautilus_trader.adapters.databento.constants`, `nautilus_trader.adapters.databento.factories`, `nautilus_trader.adapters.databento.loaders`, `nautilus_trader.adapters.databento.providers`, `nautilus_trader.core.nautilus_pyo3`

## Related Files

This file is located in `nautilus_trader/adapters/databento/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.678764Z*
