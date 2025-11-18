# Documentation: margin_models.pxd

## File Metadata

- **Path**: `nautilus_trader/accounting/margin_models.pxd`
- **Size**: 1,726 bytes
- **Lines**: 52
- **Language**: Unknown

## Original Source

```
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

from decimal import Decimal

from nautilus_trader.core.rust.model cimport PositionSide
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cdef class MarginModel:
    cpdef Money calculate_margin_init(
        self,
        Instrument instrument,
        Quantity quantity,
        Price price,
        leverage,
        bint use_quote_for_inverse=*,
    )

    cpdef Money calculate_margin_maint(
        self,
        Instrument instrument,
        PositionSide side,
        Quantity quantity,
        Price price,
        leverage,
        bint use_quote_for_inverse=*,
    )


cdef class StandardMarginModel(MarginModel):
    pass


cdef class LeveragedMarginModel(MarginModel):
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `Decimal`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `LeveragedMarginModel`, `License`, `Licensed`, `Ltd`, `MarginModel`, `Money`, `Nautech`, `PositionSide`, `Price`, `Pty`, `Public`, `Quantity`, `See`, `StandardMarginModel`, `Systems`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT` *(+1 more)*

## Related Files

This file is located in `nautilus_trader/accounting/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.436685Z*
