# Documentation: commodity.pxd

## File Metadata

- **Path**: `nautilus_trader/model/instruments/commodity.pxd`
- **Size**: 1,296 bytes
- **Lines**: 31
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


cdef class Commodity(Instrument):
    cdef readonly str isin
    """The instruments International Securities Identification Number (ISIN).\n\n:returns: `str` or ``None``"""

    @staticmethod
    cdef Commodity from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(Commodity obj)

    @staticmethod
    cdef Commodity from_pyo3_c(pyo3_instrument)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Commodity`, `Copyright`, `GNU`, `General`, `ISIN`, `Identification`, `Instrument`, `International`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `None`, `Number`, `Pty`, `Public`, `Securities`, `See`, `Systems`, `The`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT` *(+1 more)*

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
*Generated on 2025-11-18T21:55:05.711016Z*
