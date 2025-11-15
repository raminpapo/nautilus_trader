# Documentation: `nautilus_trader/adapters/dydx/http/errors.py`
**Generated:** 2025-11-15T19:40:04.297702Z
**File Size:** 2230 bytes
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

- **Path:** `nautilus_trader/adapters/dydx/http/errors.py`
- **Size:** 2,230 bytes
- **Lines:** 64
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 1
- **Functions:** 2

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
Define a dYdX exception.
"""

from typing import Any

from grpc.aio._call import AioRpcError
from msgspec import DecodeError

from nautilus_trader.adapters.dydx.common.constants import DYDX_RETRY_ERRORS_GRPC
from nautilus_trader.adapters.dydx.grpc.errors import DYDXGRPCError
from nautilus_trader.core.nautilus_pyo3 import HttpError
from nautilus_trader.core.nautilus_pyo3 import HttpTimeoutError
from nautilus_trader.core.nautilus_pyo3 import WebSocketClientError


class DYDXError(Exception):
    """
    Define the class for all dYdX specific errors.
    """

    def __init__(self, status: int, message: str, headers: dict[str, Any]) -> None:
        """
        Define the base class for all dYdX specific errors.
        """
        super().__init__(message)
        self.status = status
        self.message = message
        self.headers = headers


def should_retry(error: BaseException) -> bool:
    """
    Determine if a retry should be attempted.

    Parameters
    ----------
    error : BaseException
        The error to check.

    Returns
    -------
    bool
        True if should retry, otherwise False.

    """
    if isinstance(error, DYDXGRPCError):
        return error.code in DYDX_RETRY_ERRORS_GRPC

    return bool(isinstance(error, AioRpcError | DYDXError | HttpError | HttpTimeoutError | WebSocketClientError | DecodeError))
```


---

## Overview

This file is located at `nautilus_trader/adapters/dydx/http/errors.py` within the repository.

**Classes defined:** DYDXError

**Functions defined:** __init__, should_retry

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `DYDXError`

**Inherits from:** Exception


### Functions

#### `__init__(self, status: int, message: str, headers: dict[str, Any])`


#### `should_retry(error: BaseException)`


### Imports

- `from typing import Any`
- `from grpc.aio._call import AioRpcError`
- `from msgspec import DecodeError`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_RETRY_ERRORS_GRPC`
- `from nautilus_trader.adapters.dydx.grpc.errors import DYDXGRPCError`
- `from nautilus_trader.core.nautilus_pyo3 import HttpError`
- `from nautilus_trader.core.nautilus_pyo3 import HttpTimeoutError`
- `from nautilus_trader.core.nautilus_pyo3 import WebSocketClientError`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.dydx.http.errors import DYDXError
```


---

## Related Files

This file imports from the following modules:

- `from typing import Any`
- `from grpc.aio._call import AioRpcError`
- `from msgspec import DecodeError`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_RETRY_ERRORS_GRPC`
- `from nautilus_trader.adapters.dydx.grpc.errors import DYDXGRPCError`
- `from nautilus_trader.core.nautilus_pyo3 import HttpError`
- `from nautilus_trader.core.nautilus_pyo3 import HttpTimeoutError`
- `from nautilus_trader.core.nautilus_pyo3 import WebSocketClientError`

**Directory:** `nautilus_trader/adapters/dydx/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


