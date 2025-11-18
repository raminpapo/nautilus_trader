# Documentation: errors.py

## File Metadata

- **Path**: `nautilus_trader/adapters/dydx/http/errors.py`
- **Size**: 2,230 bytes
- **Lines**: 65
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`should_retry()`**: Function defined in this file

### Classes
- **`DYDXError`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `DYDXError`
**Functions**: `should_retry`
**Imports**: `grpc.aio._call`, `msgspec`, `nautilus_trader.adapters.dydx.common.constants`, `nautilus_trader.adapters.dydx.grpc.errors`, `nautilus_trader.core.nautilus_pyo3`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/dydx/http/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.768867Z*
