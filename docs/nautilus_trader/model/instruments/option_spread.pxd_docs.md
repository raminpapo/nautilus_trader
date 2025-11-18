# Documentation: option_spread.pxd

## File Metadata

- **Path**: `nautilus_trader/model/instruments/option_spread.pxd`
- **Size**: 1,918 bytes
- **Lines**: 43
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

from libc.stdint cimport uint64_t

from nautilus_trader.core.rust.model cimport OptionKind
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Price


cdef class OptionSpread(Instrument):
    cdef readonly str exchange
    """The exchang ISO 10383 Market Identifier Code (MIC) where the instrument trades.\n\n:returns: `str` or ``None``"""
    cdef readonly str underlying
    """The underlying asset for the contract.\n\n:returns: `str`"""
    cdef readonly str strategy_type
    """The strategy type of the spread.\n\n:returns: `str`"""
    cdef readonly uint64_t activation_ns
    """UNIX timestamp (nanoseconds) for contract activation.\n\n:returns: `unit64_t`"""
    cdef readonly uint64_t expiration_ns
    """UNIX timestamp (nanoseconds) for contract expiration.\n\n:returns: `unit64_t`"""

    @staticmethod
    cdef OptionSpread from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(OptionSpread obj)

    @staticmethod
    cdef OptionSpread from_pyo3_c(pyo3_instrument)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 34


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Code`, `Copyright`, `GNU`, `General`, `ISO`, `Identifier`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `MIC`, `Market`, `Nautech`, `None`, `OptionKind`, `OptionSpread`, `Price`, `Pty`, `Public`, `See`, `Systems`, `The`, `UNIX`, `Unless` *(+4 more)*

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
*Generated on 2025-11-18T21:55:05.758403Z*
