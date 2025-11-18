# Documentation: symbol.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/symbol.py`
- **Size**: 2,208 bytes
- **Lines**: 68
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXSymbol`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `DYDXSymbol`
**Imports**: `__future__`, `nautilus_trader.adapters.dydx.common.constants`, `nautilus_trader.core.correctness`, `nautilus_trader.model.identifiers`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.712753Z*
