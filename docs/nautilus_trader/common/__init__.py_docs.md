# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/common/__init__.py`
- **Size**: 1,571 bytes
- **Lines**: 41
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`Environment`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Classs**: `Environment`
**Imports**: `enum`

## Related Files

This file is located in `nautilus_trader/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.196451Z*
