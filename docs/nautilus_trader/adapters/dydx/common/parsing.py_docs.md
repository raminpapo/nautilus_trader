# Documentation: `nautilus_trader/adapters/dydx/common/parsing.py`
**Generated:** 2025-11-15T19:40:04.244271Z
**File Size:** 1372 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/common/parsing.py`
- **Size:** 1,372 bytes
- **Lines:** 29
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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
"""
Define common methods for parsing messages from dYdX.
"""

from nautilus_trader.adapters.dydx.common.enums import DYDXCandlesResolution
from nautilus_trader.adapters.dydx.common.enums import DYDXEnumParser
from nautilus_trader.model.data import BarType


def get_interval_from_bar_type(bar_type: BarType) -> DYDXCandlesResolution:
    """
    Convert a nautilus bar type to a dYdX candles resolution enum.
    """
    enum_parser = DYDXEnumParser()
    return enum_parser.parse_dydx_kline(bar_type)
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/common/parsing.py` within the repository.

**Functions defined:** get_interval_from_bar_type

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `get_interval_from_bar_type(bar_type: BarType)`


### Imports

- `from nautilus_trader.adapters.dydx.common.enums import DYDXCandlesResolution`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXEnumParser`
- `from nautilus_trader.model.data import BarType`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.common.parsing import get_interval_from_bar_type
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.dydx.common.enums import DYDXCandlesResolution`
- `from nautilus_trader.adapters.dydx.common.enums import DYDXEnumParser`
- `from nautilus_trader.model.data import BarType`

**Directory:** `nautilus_trader/adapters/dydx/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


