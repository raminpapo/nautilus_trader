# Documentation: `nautilus_trader/common/__init__.py`
**Generated:** 2025-11-15T19:40:04.650671Z
**File Size:** 1571 bytes
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

- **Path:** `nautilus_trader/common/__init__.py`
- **Size:** 1,571 bytes
- **Lines:** 40
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
"""
The `common` subpackage provides generic/common parts for assembling the frameworks
various components.

More domain specific concepts are introduced above the `core` base layer. The
ID cache is implemented, a base `Clock` with `Test` and `Live`
implementations which can control many `Timer` instances.

Trading domain specific components for generating `Order` and `Identifier` objects,
common logging components, a high performance `Queue` and `UUID4` factory.

"""

from enum import Enum
from enum import unique


@unique
class Environment(Enum):
    """
    Represents the environment context for a Nautilus system.
    """

    BACKTEST = "backtest"
    SANDBOX = "sandbox"
    LIVE = "live"
```


---

## Overview

This file is located at `nautilus_trader/common/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Classes defined:** Environment

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `Environment`

**Inherits from:** Enum


### Imports

- `from enum import Enum`
- `from enum import unique`


---

## Usage Examples

### Importing

```python
from nautilus_trader.common.__init__ import Environment
```


---

## Related Files

This file imports from the following modules:

- `from enum import Enum`
- `from enum import unique`

**Directory:** `nautilus_trader/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


