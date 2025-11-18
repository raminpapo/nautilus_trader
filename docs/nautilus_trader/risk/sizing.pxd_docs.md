# Documentation: sizing.pxd

## File Metadata

- **Path**: `nautilus_trader/risk/sizing.pxd`
- **Size**: 1,747 bytes
- **Lines**: 46
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

from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cdef class PositionSizer:
    cdef readonly Instrument instrument
    """The instrument for position sizing.\n\n:returns: `Instrument`"""

    cpdef void update_instrument(self, Instrument instrument)
    cpdef Quantity calculate(
        self,
        Price entry,
        Price stop_loss,
        Money equity,
        risk,
        commission_rate=*,
        exchange_rate=*,
        hard_limit=*,
        unit_batch_size=*,
        int units=*,
    )

    cdef object _calculate_risk_ticks(self, Price entry, Price stop_loss)
    cdef object _calculate_riskable_money(self, equity, risk, commission_rate)


cdef class FixedRiskSizer(PositionSizer):
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 29


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `FixedRiskSizer`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Money`, `Nautech`, `PositionSizer`, `Price`, `Pty`, `Public`, `Quantity`, `See`, `Systems`, `The`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/risk/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.908098Z*
