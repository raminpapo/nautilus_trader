# Documentation: fee.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/models/fee.pxd`
- **Size**: 1,524 bytes
- **Lines**: 39
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
from nautilus_trader.model.orders.base cimport Order


cdef class FeeModel:
    cpdef Money get_commission(self, Order order, Quantity fill_qty, Price fill_px, Instrument instrument)


cdef class MakerTakerFeeModel(FeeModel):
    pass


cdef class FixedFeeModel(FeeModel):
    cdef Money _commission
    cdef Money _zero_commission
    cdef bint _charge_commission_once


cdef class PerContractFeeModel(FeeModel):
    cdef Money _commission

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 31


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `FeeModel`, `FixedFeeModel`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `MakerTakerFeeModel`, `Money`, `Nautech`, `Order`, `PerContractFeeModel`, `Price`, `Pty`, `Public`, `Quantity`, `See`, `Systems`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT` *(+1 more)*

## Related Files

This file is located in `nautilus_trader/backtest/models/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/backtest/models/fee.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.090767Z*
