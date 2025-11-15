# Documentation: `nautilus_trader/common/events.py`
**Generated:** 2025-11-15T19:40:04.686552Z
**File Size:** 1215 bytes
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

- **Path:** `nautilus_trader/common/events.py`
- **Size:** 1,215 bytes
- **Lines:** 27
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4

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

from nautilus_trader.common.component import TimeEvent
from nautilus_trader.common.messages import ComponentStateChanged
from nautilus_trader.common.messages import RiskEvent
from nautilus_trader.common.messages import TradingStateChanged


__all__ = [
    "ComponentStateChanged",
    "RiskEvent",
    "TimeEvent",
    "TradingStateChanged",
]
```


---

## Overview

This file is located at `nautilus_trader/common/events.py` within the repository.

**Import statements:** 4


---

## Detailed Analysis

### Imports

- `from nautilus_trader.common.component import TimeEvent`
- `from nautilus_trader.common.messages import ComponentStateChanged`
- `from nautilus_trader.common.messages import RiskEvent`
- `from nautilus_trader.common.messages import TradingStateChanged`


---

## Usage Examples

### Importing

```python
import nautilus_trader.common.events
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.component import TimeEvent`
- `from nautilus_trader.common.messages import ComponentStateChanged`
- `from nautilus_trader.common.messages import RiskEvent`
- `from nautilus_trader.common.messages import TradingStateChanged`

**Directory:** `nautilus_trader/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


