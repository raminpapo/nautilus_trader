# Documentation: crypto_perpetual.pxd

## File Metadata

- **Path**: `nautilus_trader/model/instruments/crypto_perpetual.pxd`
- **Size**: 1,563 bytes
- **Lines**: 36
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
from nautilus_trader.model.objects cimport Currency


cdef class CryptoPerpetual(Instrument):
    cdef readonly Currency base_currency
    """The base currency for the instrument.\n\n:returns: `Currency`"""
    cdef readonly Currency settlement_currency
    """The settlement currency for the instrument.\n\n:returns: `Currency`"""
    cdef readonly bint is_quanto
    """If the instrument is quanto.\n\n:returns: `bool`"""

    @staticmethod
    cdef CryptoPerpetual from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(CryptoPerpetual obj)

    @staticmethod
    cdef CryptoPerpetual from_pyo3_c(pyo3_instrument)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 26


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `CryptoPerpetual`, `Currency`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `See`, `Systems`, `The`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

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
*Generated on 2025-11-18T21:55:05.723373Z*
