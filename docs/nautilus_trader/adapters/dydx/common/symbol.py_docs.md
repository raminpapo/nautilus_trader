# Documentation: `nautilus_trader/adapters/dydx/common/symbol.py`
**Generated:** 2025-11-15T19:40:04.245519Z
**File Size:** 2208 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/common/symbol.py`
- **Size:** 2,208 bytes
- **Lines:** 67
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Classes:** 1
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
"""
Represent a dYdX specific symbol containing a product type suffix.
"""

from __future__ import annotations

from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Symbol


class DYDXSymbol(str):
    """
    Represent a dYdX specific symbol containing a product type suffix.
    """

    __slots__ = ()

    def __new__(cls, symbol: str) -> DYDXSymbol:  # noqa: PYI034
        """
        Create a new dYdX symbol.
        """
        PyCondition.valid_string(symbol, "symbol")

        # Format the string on construction to be dYdX compatible
        return super().__new__(
            cls,
            symbol.upper().replace(" ", "").replace("/", "").replace("-PERP", ""),
        )

    @property
    def raw_symbol(self) -> str:
        """
        Return the raw Bybit symbol (without the product type suffix).

        Returns
        -------
        str

        """
        return str(self)

    def to_instrument_id(self) -> InstrumentId:
        """
        Parse the dYdX symbol into a Nautilus instrument ID.

        Returns
        -------
        InstrumentId

        """
        return InstrumentId(Symbol(str(self) + "-PERP"), DYDX_VENUE)
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/common/symbol.py` within the repository.

**Classes defined:** DYDXSymbol

**Functions defined:** __new__, raw_symbol, to_instrument_id

**Import statements:** 5


---

## Detailed Analysis

### Classes

#### `DYDXSymbol`

**Inherits from:** str


### Functions

#### `__new__(cls, symbol: str)`


#### `raw_symbol(self)`


#### `to_instrument_id(self)`


### Imports

- `from __future__ import annotations`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`

**Directory:** `nautilus_trader/adapters/dydx/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


