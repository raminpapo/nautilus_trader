# Documentation: common.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/common/common.py`
- **Size**: 1,406 bytes
- **Lines**: 35
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DYDXOrderTags`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `DYDXOrderTags`
**Imports**: `nautilus_trader.config`, `nautilus_trader.model.objects`

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
*Generated on 2025-11-18T21:55:04.704938Z*
