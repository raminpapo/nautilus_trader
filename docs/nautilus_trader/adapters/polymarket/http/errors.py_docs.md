# Documentation: errors.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/http/errors.py`
- **Size**: 2,304 bytes
- **Lines**: 73
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

from py_clob_client.exceptions import PolyApiException


class PolymarketError(Exception):
    """
    Represents a Polymarket specific error.
    """

    def __init__(
        self,
        code: int | None,
        message: str | None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.message = message

    def __repr__(self) -> str:
        return f"{type(self).__name__}(code={self.code}, message='{self.message}')"


class PolymarketAPIError(PolymarketError):
    """
    Represents an error response from the Polymarket CLOB API.

    Raised when the API returns an error string instead of expected data.

    """

    def __init__(self, message: str) -> None:
        super().__init__(code=None, message=message)


def should_retry(error: BaseException) -> bool:
    """
    Determine if a retry should be attempted based on the error code.

    Parameters
    ----------
    error : BaseException
        The error to check.

    Returns
    -------
    bool
        True if should retry, otherwise False.

    """
    if isinstance(error, PolyApiException):
        # https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/exceptions.py
        status_code = getattr(error, "status_code", None)

        # Retry on rate limits and server errors
        if status_code == 429 or (status_code is not None and status_code >= 500):
            return True

    return False

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`should_retry()`**: Function defined in this file

### Classes
- **`PolymarketError`**: Class defined in this file
- **`PolymarketAPIError`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `PolymarketAPIError`, `PolymarketError`
**Functions**: `should_retry`
**Imports**: `py_clob_client.exceptions`

## Related Files

This file is located in `nautilus_trader/adapters/polymarket/http/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.962276Z*
