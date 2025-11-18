# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/core/__init__.py`
- **Size**: 1,788 bytes
- **Lines**: 46
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `nautilus_trader.core.data`, `nautilus_trader.core.message`, `nautilus_trader.core.uuid`

## Related Files

This file is located in `nautilus_trader/core/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.272999Z*
