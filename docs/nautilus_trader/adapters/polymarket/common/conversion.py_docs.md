# Documentation: `nautilus_trader/adapters/polymarket/common/conversion.py`
**Generated:** 2025-11-15T19:40:04.439612Z
**File Size:** 1429 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/common/conversion.py`
- **Size:** 1,429 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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

from nautilus_trader.model.currencies import USDC_POS
from nautilus_trader.model.objects import HIGH_PRECISION
from nautilus_trader.model.objects import Money


def usdce_from_units(units: int) -> Money:
    """
    Return USDC.e money from the given units amount.

    Parameters
    ----------
    units : int
        The amount as an integer of fractional subunits.

    Returns
    -------
    Money

    """
    if HIGH_PRECISION:
        factor = 10_000_000_000
    else:
        factor = 1_000

    return Money.from_raw(int(units * factor), USDC_POS)
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/common/conversion.py` within the repository.

**Functions defined:** usdce_from_units

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `usdce_from_units(units: int)`


### Imports

- `from nautilus_trader.model.currencies import USDC_POS`
- `from nautilus_trader.model.objects import HIGH_PRECISION`
- `from nautilus_trader.model.objects import Money`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.common.conversion import usdce_from_units
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.currencies import USDC_POS`
- `from nautilus_trader.model.objects import HIGH_PRECISION`
- `from nautilus_trader.model.objects import Money`

**Directory:** `nautilus_trader/adapters/polymarket/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


