# Documentation: `nautilus_trader/adapters/polymarket/common/symbol.py`
**Generated:** 2025-11-15T19:40:04.448868Z
**File Size:** 1915 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/common/symbol.py`
- **Size:** 1,915 bytes
- **Lines:** 41
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 3

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

from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE
from nautilus_trader.model.identifiers import InstrumentId


def get_polymarket_instrument_id(condition_id: str, token_id: str | int) -> InstrumentId:
    return InstrumentId.from_str(f"{condition_id}-{token_id}.{POLYMARKET_VENUE}")


def get_polymarket_condition_id(instrument_id: InstrumentId) -> str:
    parts = instrument_id.symbol.value.split("-")
    if len(parts) != 2 or not parts[0]:
        raise ValueError(
            f"Invalid Polymarket instrument ID format: expected "
            f"'{{condition_id}}-{{token_id}}', got '{instrument_id.symbol.value}'",
        )
    return parts[0]


def get_polymarket_token_id(instrument_id: InstrumentId) -> str:
    parts = instrument_id.symbol.value.split("-")
    if len(parts) != 2 or not parts[1]:
        raise ValueError(
            f"Invalid Polymarket instrument ID format: expected "
            f"'{{condition_id}}-{{token_id}}', got '{instrument_id.symbol.value}'",
        )
    return parts[1]
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/common/symbol.py` within the repository.

**Functions defined:** get_polymarket_instrument_id, get_polymarket_condition_id, get_polymarket_token_id

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `get_polymarket_instrument_id(condition_id: str, token_id: str | int)`


#### `get_polymarket_condition_id(instrument_id: InstrumentId)`


#### `get_polymarket_token_id(instrument_id: InstrumentId)`


### Imports

- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE`
- `from nautilus_trader.model.identifiers import InstrumentId`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE`
- `from nautilus_trader.model.identifiers import InstrumentId`

**Directory:** `nautilus_trader/adapters/polymarket/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.


