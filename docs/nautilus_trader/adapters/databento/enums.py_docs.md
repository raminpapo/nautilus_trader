# Documentation: `nautilus_trader/adapters/databento/enums.py`
**Generated:** 2025-11-15T19:40:04.227383Z
**File Size:** 1449 bytes
**Extension:** .py
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

- **Path:** `nautilus_trader/adapters/databento/enums.py`
- **Size:** 1,449 bytes
- **Lines:** 43
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
- **Classes:** 1

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


---

## Overview

This file is located at `nautilus_trader/adapters/databento/enums.py` within the repository.

**Classes defined:** DatabentoSchema

**Import statements:** 1


---

## Detailed Analysis

### Classes

#### `DatabentoSchema`

**Inherits from:** Enum


### Imports

- `from enum import Enum`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.databento.enums import DatabentoSchema
```


---

## Related Files

This file imports from the following modules:

- `from enum import Enum`

**Directory:** `nautilus_trader/adapters/databento`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


