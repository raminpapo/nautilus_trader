# Documentation: conversion.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/common/conversion.py`
- **Size**: 1,429 bytes
- **Lines**: 41
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`usdce_from_units()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `usdce_from_units`
**Imports**: `nautilus_trader.model.currencies`, `nautilus_trader.model.objects`

## Related Files

This file is located in `nautilus_trader/adapters/polymarket/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.928971Z*
