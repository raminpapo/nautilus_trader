# Documentation: enums.py

## File Metadata

- **Path**: `nautilus_trader/adapters/databento/enums.py`
- **Size**: 1,449 bytes
- **Lines**: 44
- **Language**: Python

## Original Source

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

from enum import Enum


class DatabentoSchema(Enum):
    """
    Represents a Databento schema.
    """

    MBO = "mbo"
    MBP_1 = "mbp-1"
    MBP_10 = "mbp-10"
    BBO_1S = "bbo-1s"
    BBO_1M = "bbo-1m"
    CMBP_1 = "cmbp-1"
    CBBO_1S = "cbbo-1s"
    CBBO_1M = "cbbo-1m"
    TCBBO = "tcbbo"
    TBBO = "tbbo"
    TRADES = "trades"
    OHLCV_1S = "ohlcv-1s"
    OHLCV_1M = "ohlcv-1m"
    OHLCV_1H = "ohlcv-1h"
    OHLCV_1D = "ohlcv-1d"
    OHLCV_EOD = "ohlcv-eod"
    DEFINITION = "definition"
    IMBALANCE = "imbalance"
    STATISTICS = "statistics"
    STATUS = "status"

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DatabentoSchema`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Classs**: `DatabentoSchema`
**Imports**: `enum`

## Related Files

This file is located in `nautilus_trader/adapters/databento/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.691122Z*
