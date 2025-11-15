# Documentation: `nautilus_trader/indicators/volume.pxd`
**Generated:** 2025-11-15T19:40:04.973558Z
**File Size:** 2385 bytes
**Extension:** .pxd
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `nautilus_trader/indicators/volume.pxd`
- **Size:** 2,385 bytes
- **Lines:** 68
- **Extension:** `.pxd`
- **Type:** text

---

## Source Code

```python
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


---

## Overview

This file is located at `nautilus_trader/indicators/volume.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/indicators`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


