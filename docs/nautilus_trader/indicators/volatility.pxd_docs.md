# Documentation: volatility.pxd

## File Metadata

- **Path**: `nautilus_trader/indicators/volatility.pxd`
- **Size**: 3,604 bytes
- **Lines**: 112
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

from nautilus_trader.indicators.averages cimport MovingAverage
from nautilus_trader.indicators.base cimport Indicator
from nautilus_trader.model.data cimport Bar


cdef class AverageTrueRange(Indicator):
    cdef MovingAverage _ma
    cdef bint _use_previous
    cdef double _value_floor
    cdef double _previous_close

    cdef readonly int period
    """The window period.\n\n:returns: `int`"""
    cdef readonly double value
    """The current value.\n\n:returns: `double`"""

    cpdef void update_raw(self, double high, double low, double close)
    cdef void _floor_value(self)
    cdef void _check_initialized(self)


cdef class BollingerBands(Indicator):
    cdef object _prices
    cdef MovingAverage _ma

    cdef readonly int period
    """The period for the moving average.\n\n:returns: `int`"""
    cdef readonly double k
    """The standard deviation multiple.\n\n:returns: `double`"""
    cdef readonly double upper
    """The current value of the upper band.\n\n:returns: `double`"""
    cdef readonly double middle
    """The current value of the middle band.\n\n:returns: `double`"""
    cdef readonly double lower
    """The current value of the lower band.\n\n:returns: `double`"""

    cpdef void update_raw(self, double high, double low, double close)


cdef class DonchianChannel(Indicator):
    cdef object _upper_prices
    cdef object _lower_prices

    cdef readonly int period
    cdef readonly double upper
    cdef readonly double middle
    cdef readonly double lower

    cpdef void update_raw(self, double high, double low)


cdef class KeltnerChannel(Indicator):
    cdef MovingAverage _ma
    cdef AverageTrueRange _atr

    cdef readonly int period
    cdef readonly double k_multiplier
    cdef readonly double upper
    cdef readonly double middle
    cdef readonly double lower

    cpdef void update_raw(self, double high, double low, double close)


cdef class VerticalHorizontalFilter(Indicator):
    cdef MovingAverage _ma
    cdef object _prices
    cdef double _previous_close

    cdef readonly int period
    cdef readonly double value

    cpdef void update_raw(self, double close)
    cdef void _check_initialized(self)


cdef class VolatilityRatio(Indicator):
    cdef AverageTrueRange _atr_fast
    cdef AverageTrueRange _atr_slow

    cdef readonly int fast_period
    cdef readonly int slow_period
    cdef readonly double value

    cpdef void update_raw(self, double high, double low, double close)
    cdef void _check_initialized(self)


cdef class KeltnerPosition(Indicator):
    cdef KeltnerChannel _kc

    cdef readonly int period
    cdef readonly double k_multiplier
    cdef readonly double value

    cpdef void update_raw(self, double high, double low, double close)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 33


**Identifiers**: `ANY`, `All`, `AverageTrueRange`, `BASIS`, `Bar`, `BollingerBands`, `CONDITIONS`, `Copyright`, `DonchianChannel`, `GNU`, `General`, `Indicator`, `KIND`, `KeltnerChannel`, `KeltnerPosition`, `Lesser`, `License`, `Licensed`, `Ltd`, `MovingAverage`, `Nautech`, `Pty`, `Public`, `See`, `Systems`, `The`, `Unless`, `Version`, `VerticalHorizontalFilter`, `VolatilityRatio` *(+3 more)*

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
*Generated on 2025-11-18T21:55:05.557159Z*
