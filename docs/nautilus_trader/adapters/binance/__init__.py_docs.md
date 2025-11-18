# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/adapters/binance/__init__.py`
- **Size**: 4,449 bytes
- **Lines**: 109
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
Binance cryptocurreny exchange integration adapter.

This subpackage provides an instrument provider, data and execution clients,
configurations, data types and constants for connecting to and interacting with
Binance's API.

For convenience, the most commonly used symbols are re-exported at the
subpackage's top level, so downstream code can simply import from
``nautilus_trader.adapters.binance``.

"""
from typing import Final

import pyarrow as pa

from nautilus_trader.adapters.binance.common.constants import BINANCE
from nautilus_trader.adapters.binance.common.constants import BINANCE_CLIENT_ID
from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE
from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.common.enums import BinanceKeyType
from nautilus_trader.adapters.binance.common.types import BinanceBar
from nautilus_trader.adapters.binance.common.types import BinanceTicker
from nautilus_trader.adapters.binance.config import BinanceDataClientConfig
from nautilus_trader.adapters.binance.config import BinanceExecClientConfig
from nautilus_trader.adapters.binance.factories import BinanceLiveDataClientFactory
from nautilus_trader.adapters.binance.factories import BinanceLiveExecClientFactory
from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client
from nautilus_trader.adapters.binance.futures.providers import BinanceFuturesInstrumentProvider
from nautilus_trader.adapters.binance.futures.types import BinanceFuturesMarkPriceUpdate
from nautilus_trader.adapters.binance.loaders import BinanceOrderBookDeltaDataLoader
from nautilus_trader.adapters.binance.spot.providers import BinanceSpotInstrumentProvider
from nautilus_trader.serialization import register_serializable_type
from nautilus_trader.serialization.arrow.schema import NAUTILUS_ARROW_SCHEMA
from nautilus_trader.serialization.arrow.serializer import make_dict_deserializer
from nautilus_trader.serialization.arrow.serializer import make_dict_serializer
from nautilus_trader.serialization.arrow.serializer import register_arrow


register_serializable_type(
    BinanceBar,
    BinanceBar.to_dict,
    BinanceBar.from_dict,
)

register_serializable_type(
    BinanceTicker,
    BinanceTicker.to_dict,
    BinanceTicker.from_dict,
)

BINANCE_BAR_ARROW_SCHEMA: Final[pa.schema] = pa.schema(
    {
        "bar_type": pa.dictionary(pa.int16(), pa.string()),
        "instrument_id": pa.dictionary(pa.int64(), pa.string()),
        "open": pa.string(),
        "high": pa.string(),
        "low": pa.string(),
        "close": pa.string(),
        "volume": pa.string(),
        "quote_volume": pa.string(),
        "count": pa.uint64(),
        "taker_buy_base_volume": pa.string(),
        "taker_buy_quote_volume": pa.string(),
        "ts_event": pa.uint64(),
        "ts_init": pa.uint64(),
    },
)

NAUTILUS_ARROW_SCHEMA[BinanceBar] = BINANCE_BAR_ARROW_SCHEMA

register_arrow(
    BinanceBar,
    BINANCE_BAR_ARROW_SCHEMA,
    encoder=make_dict_serializer(BINANCE_BAR_ARROW_SCHEMA),
    decoder=make_dict_deserializer(BinanceBar),
)

__all__ = [
    "BINANCE",
    "BINANCE_CLIENT_ID",
    "BINANCE_VENUE",
    "BinanceAccountType",
    "BinanceDataClientConfig",
    "BinanceExecClientConfig",
    "BinanceFuturesInstrumentProvider",
    "BinanceFuturesMarkPriceUpdate",
    "BinanceKeyType",
    "BinanceLiveDataClientFactory",
    "BinanceLiveExecClientFactory",
    "BinanceOrderBookDeltaDataLoader",
    "BinanceSpotInstrumentProvider",
    "get_cached_binance_http_client",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 14


**Imports**: `nautilus_trader.adapters.binance.common.constants`, `nautilus_trader.adapters.binance.common.enums`, `nautilus_trader.adapters.binance.common.types`, `nautilus_trader.adapters.binance.config`, `nautilus_trader.adapters.binance.factories`, `nautilus_trader.adapters.binance.futures.providers`, `nautilus_trader.adapters.binance.futures.types`, `nautilus_trader.adapters.binance.loaders`, `nautilus_trader.adapters.binance.spot.providers`, `nautilus_trader.serialization`, `nautilus_trader.serialization.arrow.schema`, `nautilus_trader.serialization.arrow.serializer`, `pyarrow`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/binance/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.494458Z*
