# Documentation: `nautilus_trader/core/__init__.py`
**Generated:** 2025-11-15T19:40:04.714553Z
**File Size:** 1788 bytes
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

- **Path:** `nautilus_trader/core/__init__.py`
- **Size:** 1,788 bytes
- **Lines:** 45
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
The `core` subpackage groups core constants, functions and low-level components used
throughout the framework.

The main focus here is on efficiency and re-usability as this forms the base
layer of the entire framework. Message passing is a core design philosophy and
the base massage types are contained here.

A generic `FiniteStateMachine` operates with C-level enums, ensuring correct
state transitions for both domain entities and more complex components.

"""

from nautilus_trader.core.data import Data
from nautilus_trader.core.message import Command
from nautilus_trader.core.message import Document
from nautilus_trader.core.message import Event
from nautilus_trader.core.message import Request
from nautilus_trader.core.message import Response
from nautilus_trader.core.uuid import UUID4


__all__ = [
    "UUID4",
    "Command",
    "Data",
    "Document",
    "Event",
    "Request",
    "Response",
]
```


---

## Overview

This file is located at `nautilus_trader/core/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.core.message import Command`
- `from nautilus_trader.core.message import Document`
- `from nautilus_trader.core.message import Event`
- `from nautilus_trader.core.message import Request`
- `from nautilus_trader.core.message import Response`
- `from nautilus_trader.core.uuid import UUID4`


---

## Usage Examples

### Importing

```python
import nautilus_trader.core.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.core.message import Command`
- `from nautilus_trader.core.message import Document`
- `from nautilus_trader.core.message import Event`
- `from nautilus_trader.core.message import Request`
- `from nautilus_trader.core.message import Response`
- `from nautilus_trader.core.uuid import UUID4`

**Directory:** `nautilus_trader/core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


