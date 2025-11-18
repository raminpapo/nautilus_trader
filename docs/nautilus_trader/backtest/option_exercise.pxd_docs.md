# Documentation: option_exercise.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/option_exercise.pxd`
- **Size**: 1,735 bytes
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

from libc.stdint cimport uint64_t

from nautilus_trader.backtest.modules cimport SimulationModule
from nautilus_trader.cache.cache cimport Cache
from nautilus_trader.core.data cimport Data
from nautilus_trader.model.identifiers cimport InstrumentId
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.instruments.crypto_option cimport CryptoOption
from nautilus_trader.model.instruments.option_contract cimport OptionContract
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.position cimport Position


cdef class OptionExerciseModule(SimulationModule):
    cdef public object config
    cdef public Cache cache
    cdef public dict expiry_timers
    cdef public set processed_expiries

    cpdef void pre_process(self, Data data)
    cpdef Instrument _get_underlying_instrument(self, object option)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 32


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Cache`, `Copyright`, `CryptoOption`, `Data`, `GNU`, `General`, `Instrument`, `InstrumentId`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `OptionContract`, `OptionExerciseModule`, `Position`, `Price`, `Pty`, `Public`, `See`, `SimulationModule`, `Systems`, `Unless`, `Version`, `WARRANTIES` *(+2 more)*

## Related Files

This file is located in `nautilus_trader/backtest/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/backtest/option_exercise.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.113768Z*
