# Documentation: `nautilus_trader/adapters/polymarket/common/constants.py`
**Generated:** 2025-11-15T19:40:04.438585Z
**File Size:** 1608 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/common/constants.py`
- **Size:** 1,608 bytes
- **Lines:** 39
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4

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

from typing import Final

from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue


POLYMARKET: Final[str] = "POLYMARKET"
POLYMARKET_VENUE: Final[Venue] = Venue(POLYMARKET)
POLYMARKET_CLIENT_ID: Final[ClientId] = ClientId(POLYMARKET)

POLYMARKET_MAX_PRICE: Final[float] = 0.999
POLYMARKET_MIN_PRICE: Final[float] = 0.001
POLYMARKET_MAX_PRECISION_TAKER: Final[int] = 2
POLYMARKET_MAX_PRECISION_MAKER: Final[int] = 5

VALID_POLYMARKET_TIME_IN_FORCE: Final[set[TimeInForce]] = {
    TimeInForce.GTC,
    TimeInForce.GTD,
    TimeInForce.FOK,
    TimeInForce.IOC,
}

POLYMARKET_INVALID_API_KEY: Final[str] = "Unauthorized/Invalid api key"
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/common/constants.py` within the repository.

**Import statements:** 4


---

## Detailed Analysis

### Imports

- `from typing import Final`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.polymarket.common.constants
```


---

## Related Files

This file imports from the following modules:

- `from typing import Final`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `nautilus_trader/adapters/polymarket/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key, auth. Ensure proper handling of secrets.


