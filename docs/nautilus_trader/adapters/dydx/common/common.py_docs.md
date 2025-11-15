# Documentation: `nautilus_trader/adapters/dydx/common/common.py`
**Generated:** 2025-11-15T19:40:04.239110Z
**File Size:** 1406 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/common/common.py`
- **Size:** 1,406 bytes
- **Lines:** 34
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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

from nautilus_trader.config import NautilusConfig
from nautilus_trader.model.objects import Price


class DYDXOrderTags(NautilusConfig, frozen=True, repr_omit_defaults=True):
    """
    Used to attach to Nautilus Order Tags for dYdX specific order parameters.
    """

    is_short_term_order: bool = True
    num_blocks_open: int = 20
    market_order_price: Price | None = None

    @property
    def value(self) -> str:
        return f"DYDXOrderTags:{self.json().decode()}"

    def __str__(self) -> str:
        return self.value
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/common/common.py` within the repository.

**Classes defined:** DYDXOrderTags

**Functions defined:** value, __str__

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `DYDXOrderTags`

**Inherits from:** NautilusConfig, frozen=True, repr_omit_defaults=True


### Functions

#### `value(self)`


#### `__str__(self)`


### Imports

- `from nautilus_trader.config import NautilusConfig`
- `from nautilus_trader.model.objects import Price`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.common.common import DYDXOrderTags
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.config import NautilusConfig`
- `from nautilus_trader.model.objects import Price`

**Directory:** `nautilus_trader/adapters/dydx/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


