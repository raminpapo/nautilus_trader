# Documentation: `nautilus_trader/model/tick_scheme/__init__.py`
**Generated:** 2025-11-15T19:40:05.222097Z
**File Size:** 1889 bytes
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

- **Path:** `nautilus_trader/model/tick_scheme/__init__.py`
- **Size:** 1,889 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7

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
Defines a scheme for modeling the tick space for various instruments.
"""

from nautilus_trader.model.tick_scheme.base import get_tick_scheme
from nautilus_trader.model.tick_scheme.base import register_tick_scheme
from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_3DECIMAL_TICK_SCHEME
from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_5DECIMAL_TICK_SCHEME
from nautilus_trader.model.tick_scheme.implementations.fixed import FixedTickScheme
from nautilus_trader.model.tick_scheme.implementations.tiered import TOPIX100_TICK_SCHEME
from nautilus_trader.model.tick_scheme.implementations.tiered import TieredTickScheme


register_tick_scheme(TOPIX100_TICK_SCHEME)
register_tick_scheme(FOREX_3DECIMAL_TICK_SCHEME)
register_tick_scheme(FOREX_5DECIMAL_TICK_SCHEME)

__all__ = [
    "FOREX_3DECIMAL_TICK_SCHEME",
    "FOREX_5DECIMAL_TICK_SCHEME",
    "TOPIX100_TICK_SCHEME",
    "FixedTickScheme",
    "TieredTickScheme",
    "get_tick_scheme",
    "register_tick_scheme",
]
```


---

## Overview

This file is located at `nautilus_trader/model/tick_scheme/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `from nautilus_trader.model.tick_scheme.base import get_tick_scheme`
- `from nautilus_trader.model.tick_scheme.base import register_tick_scheme`
- `from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_3DECIMAL_TICK_SCHEME`
- `from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_5DECIMAL_TICK_SCHEME`
- `from nautilus_trader.model.tick_scheme.implementations.fixed import FixedTickScheme`
- `from nautilus_trader.model.tick_scheme.implementations.tiered import TOPIX100_TICK_SCHEME`
- `from nautilus_trader.model.tick_scheme.implementations.tiered import TieredTickScheme`


---

## Usage Examples

### Importing

```python
import nautilus_trader.model.tick_scheme.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.tick_scheme.base import get_tick_scheme`
- `from nautilus_trader.model.tick_scheme.base import register_tick_scheme`
- `from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_3DECIMAL_TICK_SCHEME`
- `from nautilus_trader.model.tick_scheme.implementations.fixed import FOREX_5DECIMAL_TICK_SCHEME`
- `from nautilus_trader.model.tick_scheme.implementations.fixed import FixedTickScheme`
- `from nautilus_trader.model.tick_scheme.implementations.tiered import TOPIX100_TICK_SCHEME`
- `from nautilus_trader.model.tick_scheme.implementations.tiered import TieredTickScheme`

**Directory:** `nautilus_trader/model/tick_scheme`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


