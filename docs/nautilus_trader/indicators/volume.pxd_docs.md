# Documentation: volume.pxd

## File Metadata

- **Path**: `nautilus_trader/indicators/volume.pxd`
- **Size**: 2,385 bytes
- **Lines**: 69
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

from nautilus_trader.core.rust.model cimport AggressorSide
from nautilus_trader.core.rust.model cimport PriceType
from nautilus_trader.indicators.averages cimport MovingAverage
from nautilus_trader.indicators.base cimport Indicator
from nautilus_trader.model.data cimport Bar
from nautilus_trader.model.data cimport TradeTick


cdef class OnBalanceVolume(Indicator):
    cdef object _obv

    cdef readonly int period
    cdef readonly double value

    cpdef void update_raw(self, double open, double close, double volume)


cdef class VolumeWeightedAveragePrice(Indicator):
    cdef int _day
    cdef double _price_volume
    cdef double _volume_total

    cdef readonly double value

    cpdef void update_raw(self, double price, double volume, datetime timestamp)


cdef class KlingerVolumeOscillator(Indicator):
    cdef MovingAverage _fast_ma
    cdef MovingAverage _slow_ma
    cdef MovingAverage _signal_ma
    cdef double _hlc3
    cdef double _previous_hlc3

    cdef readonly int fast_period
    cdef readonly int slow_period
    cdef readonly int signal_period
    cdef readonly double value

    cpdef void update_raw(self, double high, double low, double close, double volume)


cdef class Pressure(Indicator):
    cdef object _atr
    cdef MovingAverage _average_volume

    cdef readonly int period
    cdef readonly double value
    cdef readonly double value_cumulative

    cpdef void update_raw(self, double high, double low, double close, double volume)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 32


**Identifiers**: `ANY`, `AggressorSide`, `All`, `BASIS`, `Bar`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `Indicator`, `KIND`, `KlingerVolumeOscillator`, `Lesser`, `License`, `Licensed`, `Ltd`, `MovingAverage`, `Nautech`, `OnBalanceVolume`, `Pressure`, `PriceType`, `Pty`, `Public`, `See`, `Systems`, `TradeTick`, `Unless`, `Version`, `VolumeWeightedAveragePrice`, `WARRANTIES` *(+2 more)*

## Related Files

This file is located in `nautilus_trader/indicators/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.562452Z*
