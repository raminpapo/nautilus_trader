# Documentation: fuzzy_enums.pxd

## File Metadata

- **Path**: `nautilus_trader/indicators/fuzzy_enums.pxd`
- **Size**: 1,476 bytes
- **Lines**: 47
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

# Consolidated fuzzy enums from fuzzy_enums/ subdirectory

cpdef enum CandleDirection:
    DIRECTION_BEAR = -1
    DIRECTION_NONE = 0  # Doji
    DIRECTION_BULL = 1


cpdef enum CandleSize:
    SIZE_NONE = 0  # Doji
    SIZE_VERY_SMALL = 1
    SIZE_SMALL = 2
    SIZE_MEDIUM = 3
    SIZE_LARGE = 4
    SIZE_VERY_LARGE = 5
    SIZE_EXTREMELY_LARGE = 6


cpdef enum CandleBodySize:
    BODY_NONE = 0  # Doji
    BODY_SMALL = 1
    BODY_MEDIUM = 2
    BODY_LARGE = 3
    BODY_TREND = 4


cpdef enum CandleWickSize:
    WICK_NONE = 0  # No candle wick
    WICK_SMALL = 1
    WICK_MEDIUM = 2
    WICK_LARGE = 3

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 47


**Identifiers**: `ANY`, `All`, `BASIS`, `BODY_LARGE`, `BODY_MEDIUM`, `BODY_NONE`, `BODY_SMALL`, `BODY_TREND`, `CONDITIONS`, `CandleBodySize`, `CandleDirection`, `CandleSize`, `CandleWickSize`, `Consolidated`, `Copyright`, `DIRECTION_BEAR`, `DIRECTION_BULL`, `DIRECTION_NONE`, `Doji`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `SIZE_EXTREMELY_LARGE` *(+17 more)*

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
*Generated on 2025-11-18T21:55:05.542958Z*
