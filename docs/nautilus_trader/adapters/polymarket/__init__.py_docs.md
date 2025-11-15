# Documentation: `nautilus_trader/adapters/polymarket/__init__.py`
**Generated:** 2025-11-15T19:40:04.435567Z
**File Size:** 3399 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/__init__.py`
- **Size:** 3,399 bytes
- **Lines:** 64
- **Extension:** `.py`
- **Type:** text
- **Imports:** 17

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
Polymarket decentralized prediction market integration adapter.

This subpackage provides instrument providers, data and execution client configurations,
factories, constants, and credential helpers for connecting to and interacting with
the Polymarket Central Limit Order Book (CLOB) API.

For convenience, the most commonly used symbols are re-exported at the subpackage's
top level, so downstream code can simply import from ``nautilus_trader.adapters.polymarket``.

"""

from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET
from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_CLIENT_ID
from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRECISION_MAKER
from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRECISION_TAKER
from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRICE
from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MIN_PRICE
from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE
from nautilus_trader.adapters.polymarket.common.parsing import parse_polymarket_instrument
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id
from nautilus_trader.adapters.polymarket.config import PolymarketDataClientConfig
from nautilus_trader.adapters.polymarket.config import PolymarketExecClientConfig
from nautilus_trader.adapters.polymarket.factories import PolymarketLiveDataClientFactory
from nautilus_trader.adapters.polymarket.factories import PolymarketLiveExecClientFactory
from nautilus_trader.adapters.polymarket.factories import get_polymarket_http_client
from nautilus_trader.adapters.polymarket.factories import get_polymarket_instrument_provider
from nautilus_trader.adapters.polymarket.loaders import PolymarketDataLoader
from nautilus_trader.adapters.polymarket.providers import PolymarketInstrumentProvider


__all__ = [
    "POLYMARKET",
    "POLYMARKET_CLIENT_ID",
    "POLYMARKET_MAX_PRECISION_MAKER",
    "POLYMARKET_MAX_PRECISION_TAKER",
    "POLYMARKET_MAX_PRICE",
    "POLYMARKET_MIN_PRICE",
    "POLYMARKET_VENUE",
    "PolymarketDataClientConfig",
    "PolymarketDataLoader",
    "PolymarketExecClientConfig",
    "PolymarketInstrumentProvider",
    "PolymarketLiveDataClientFactory",
    "PolymarketLiveExecClientFactory",
    "get_polymarket_http_client",
    "get_polymarket_instrument_id",
    "get_polymarket_instrument_provider",
    "parse_polymarket_instrument",
]
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 17


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_CLIENT_ID`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRECISION_MAKER`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRECISION_TAKER`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRICE`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MIN_PRICE`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE`
- `from nautilus_trader.adapters.polymarket.common.parsing import parse_polymarket_instrument`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id`
- `from nautilus_trader.adapters.polymarket.config import PolymarketDataClientConfig`
- `from nautilus_trader.adapters.polymarket.config import PolymarketExecClientConfig`
- `from nautilus_trader.adapters.polymarket.factories import PolymarketLiveDataClientFactory`
- `from nautilus_trader.adapters.polymarket.factories import PolymarketLiveExecClientFactory`
- `from nautilus_trader.adapters.polymarket.factories import get_polymarket_http_client`
- `from nautilus_trader.adapters.polymarket.factories import get_polymarket_instrument_provider`
- `from nautilus_trader.adapters.polymarket.loaders import PolymarketDataLoader`
- `from nautilus_trader.adapters.polymarket.providers import PolymarketInstrumentProvider`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.polymarket.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_CLIENT_ID`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRECISION_MAKER`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRECISION_TAKER`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MAX_PRICE`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_MIN_PRICE`
- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE`
- `from nautilus_trader.adapters.polymarket.common.parsing import parse_polymarket_instrument`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id`
- `from nautilus_trader.adapters.polymarket.config import PolymarketDataClientConfig`

*... and 7 more*

**Directory:** `nautilus_trader/adapters/polymarket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: credential. Ensure proper handling of secrets.


