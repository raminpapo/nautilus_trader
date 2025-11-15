# Documentation: `nautilus_trader/adapters/hyperliquid/enums.py`
**Generated:** 2025-11-15T19:40:04.325952Z
**File Size:** 1412 bytes
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

- **Path:** `nautilus_trader/adapters/hyperliquid/enums.py`
- **Size:** 1,412 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 1
- **Functions:** 2

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

from __future__ import annotations

from enum import Enum
from enum import unique


@unique
class HyperliquidProductType(str, Enum):
    """
    Supported Hyperliquid product types for instrument discovery.
    """

    SPOT = "spot"
    PERP = "perp"

    @property
    def is_spot(self) -> bool:
        return self is HyperliquidProductType.SPOT

    @property
    def is_perp(self) -> bool:
        return self is HyperliquidProductType.PERP


DEFAULT_PRODUCT_TYPES = frozenset({HyperliquidProductType.SPOT, HyperliquidProductType.PERP})
```


---

## Overview

This file is located at `nautilus_trader/adapters/hyperliquid/enums.py` within the repository.

**Classes defined:** HyperliquidProductType

**Functions defined:** is_spot, is_perp

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `HyperliquidProductType`

**Inherits from:** str, Enum


### Functions

#### `is_spot(self)`


#### `is_perp(self)`


### Imports

- `from __future__ import annotations`
- `from enum import Enum`
- `from enum import unique`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.hyperliquid.enums import HyperliquidProductType
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from enum import Enum`
- `from enum import unique`

**Directory:** `nautilus_trader/adapters/hyperliquid`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


