# Documentation: `nautilus_trader/adapters/dydx/grpc/errors.py`
**Generated:** 2025-11-15T19:40:04.289586Z
**File Size:** 1315 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/grpc/errors.py`
- **Size:** 1,315 bytes
- **Lines:** 31
- **Extension:** `.py`
- **Type:** text
- **Classes:** 1
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
Define a dYdX exception thrown by the GRPC client.
"""


class DYDXGRPCError(Exception):
    """
    Define the class for all dYdX specific errors thrown by the GRPC client.
    """

    def __init__(self, code: int | None, message: str) -> None:
        """
        Define the class for all dYdX specific errors thrown by the GRPC client.
        """
        super().__init__(message)
        self.code = code
        self.message = message
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/grpc/errors.py` within the repository.

**Classes defined:** DYDXGRPCError

**Functions defined:** __init__


---

## Detailed Analysis

### Classes

#### `DYDXGRPCError`

**Inherits from:** Exception


### Functions

#### `__init__(self, code: int | None, message: str)`



---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.grpc.errors import DYDXGRPCError
```


---

## Related Files

**Directory:** `nautilus_trader/adapters/dydx/grpc`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


