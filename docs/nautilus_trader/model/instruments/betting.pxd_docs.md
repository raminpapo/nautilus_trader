# Documentation: betting.pxd

## File Metadata

- **Path**: `nautilus_trader/model/instruments/betting.pxd`
- **Size**: 1,891 bytes
- **Lines**: 49
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

from cpython.datetime cimport datetime

from nautilus_trader.core.rust.model cimport OrderSide
from nautilus_trader.model.instruments.base cimport Instrument


cdef class BettingInstrument(Instrument):
    cdef readonly int event_type_id
    cdef readonly str event_type_name
    cdef readonly int competition_id
    cdef readonly str competition_name
    cdef readonly int event_id
    cdef readonly str event_name
    cdef readonly str event_country_code
    cdef readonly datetime event_open_date
    cdef readonly str betting_type
    cdef readonly str market_id
    cdef readonly str market_name
    cdef readonly datetime market_start_time
    cdef readonly str market_type
    cdef readonly int selection_id
    cdef readonly str selection_name
    cdef readonly float selection_handicap

    @staticmethod
    cdef BettingInstrument from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(BettingInstrument obj)


cpdef double null_handicap()
cpdef object order_side_to_bet_side(OrderSide order_side)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 25


**Identifiers**: `ANY`, `All`, `BASIS`, `BettingInstrument`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `OrderSide`, `Pty`, `Public`, `See`, `Systems`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/model/instruments/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.700396Z*
