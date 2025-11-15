# Documentation: `nautilus_trader/adapters/kraken/__init__.py`
**Generated:** 2025-11-15T19:40:04.404043Z
**File Size:** 2142 bytes
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

- **Path:** `nautilus_trader/adapters/kraken/__init__.py`
- **Size:** 2,142 bytes
- **Lines:** 47
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9

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


---

## Overview

This file is located at `nautilus_trader/adapters/kraken/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 9


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.kraken.config import KrakenDataClientConfig`
- `from nautilus_trader.adapters.kraken.constants import KRAKEN`
- `from nautilus_trader.adapters.kraken.constants import KRAKEN_CLIENT_ID`
- `from nautilus_trader.adapters.kraken.constants import KRAKEN_VENUE`
- `from nautilus_trader.adapters.kraken.data import KrakenDataClient`
- `from nautilus_trader.adapters.kraken.factories import KrakenLiveDataClientFactory`
- `from nautilus_trader.adapters.kraken.providers import KrakenInstrumentProvider`
- `from nautilus_trader.adapters.kraken.types import KRAKEN_INSTRUMENT_TYPES`
- `from nautilus_trader.adapters.kraken.types import KrakenInstrument`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.kraken.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.kraken.config import KrakenDataClientConfig`
- `from nautilus_trader.adapters.kraken.constants import KRAKEN`
- `from nautilus_trader.adapters.kraken.constants import KRAKEN_CLIENT_ID`
- `from nautilus_trader.adapters.kraken.constants import KRAKEN_VENUE`
- `from nautilus_trader.adapters.kraken.data import KrakenDataClient`
- `from nautilus_trader.adapters.kraken.factories import KrakenLiveDataClientFactory`
- `from nautilus_trader.adapters.kraken.providers import KrakenInstrumentProvider`
- `from nautilus_trader.adapters.kraken.types import KRAKEN_INSTRUMENT_TYPES`
- `from nautilus_trader.adapters.kraken.types import KrakenInstrument`

**Directory:** `nautilus_trader/adapters/kraken`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


