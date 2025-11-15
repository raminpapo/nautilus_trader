# Documentation: `nautilus_trader/risk/config.py`
**Generated:** 2025-11-15T19:40:05.286323Z
**File Size:** 1975 bytes
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

- **Path:** `nautilus_trader/risk/config.py`
- **Size:** 1,975 bytes
- **Lines:** 45
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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

from __future__ import annotations

from nautilus_trader.common.config import NautilusConfig


class RiskEngineConfig(NautilusConfig, frozen=True):
    """
    Configuration for ``RiskEngine`` instances.

    Parameters
    ----------
    bypass : bool, default False
        If True, then will bypass all pre-trade risk checks and rate limits (will still check for duplicate IDs).
    max_order_submit_rate : str, default 100/00:00:01
        The maximum rate of submit order commands per timedelta.
    max_order_modify_rate : str, default 100/00:00:01
        The maximum rate of modify order commands per timedelta.
    max_notional_per_order : dict[str, int], default empty dict
        The maximum notional value of an order per instrument ID.
        The value should be a valid decimal format.
    debug : bool, default False
        If debug mode is active (will provide extra debug logging).

    """

    bypass: bool = False
    max_order_submit_rate: str = "100/00:00:01"
    max_order_modify_rate: str = "100/00:00:01"
    max_notional_per_order: dict[str, int] = {}
    debug: bool = False
```


---

## Overview

This file is located at `nautilus_trader/risk/config.py` within the repository.

**Classes defined:** RiskEngineConfig

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `RiskEngineConfig`

**Inherits from:** NautilusConfig, frozen=True


### Imports

- `from __future__ import annotations`
- `from nautilus_trader.common.config import NautilusConfig`


---

## Usage Examples

### Importing

```python
from nautilus_trader.risk.config import RiskEngineConfig
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from nautilus_trader.common.config import NautilusConfig`

**Directory:** `nautilus_trader/risk`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


