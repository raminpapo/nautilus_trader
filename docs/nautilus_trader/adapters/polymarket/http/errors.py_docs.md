# Documentation: `nautilus_trader/adapters/polymarket/http/errors.py`
**Generated:** 2025-11-15T19:40:04.467642Z
**File Size:** 2304 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/http/errors.py`
- **Size:** 2,304 bytes
- **Lines:** 72
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
- **Classes:** 2
- **Functions:** 4

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


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/http/errors.py` within the repository.

**Classes defined:** PolymarketError, PolymarketAPIError

**Functions defined:** __init__, __repr__, __init__, should_retry

**Import statements:** 1


---

## Detailed Analysis

### Classes

#### `PolymarketError`

**Inherits from:** Exception


#### `PolymarketAPIError`

**Inherits from:** PolymarketError


### Functions

#### `__init__(
        self,
        code: int | None,
        message: str | None,
    )`


#### `__repr__(self)`


#### `__init__(self, message: str)`


#### `should_retry(error: BaseException)`


### Imports

- `from py_clob_client.exceptions import PolyApiException`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.http.errors import PolymarketError
```


---

## Related Files

This file imports from the following modules:

- `from py_clob_client.exceptions import PolyApiException`

**Directory:** `nautilus_trader/adapters/polymarket/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


