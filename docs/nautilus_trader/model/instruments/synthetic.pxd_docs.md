# Documentation: synthetic.pxd

## File Metadata

- **Path**: `nautilus_trader/model/instruments/synthetic.pxd`
- **Size**: 1,555 bytes
- **Lines**: 37
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

from nautilus_trader.core.data cimport Data
from nautilus_trader.core.rust.core cimport CVec
from nautilus_trader.core.rust.model cimport SyntheticInstrument_API
from nautilus_trader.model.identifiers cimport InstrumentId
from nautilus_trader.model.objects cimport Price


cdef class SyntheticInstrument(Data):
    cdef SyntheticInstrument_API _mem

    cdef readonly InstrumentId id
    """The instrument ID.\n\n:returns: `InstrumentId`"""

    cpdef void change_formula(self, str formula)
    cpdef Price calculate(self, list[double] inputs)

    @staticmethod
    cdef SyntheticInstrument from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(SyntheticInstrument obj)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 29


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `CVec`, `Copyright`, `Data`, `GNU`, `General`, `InstrumentId`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Price`, `Pty`, `Public`, `See`, `SyntheticInstrument`, `SyntheticInstrument_API`, `Systems`, `The`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

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
*Generated on 2025-11-18T21:55:05.762046Z*
