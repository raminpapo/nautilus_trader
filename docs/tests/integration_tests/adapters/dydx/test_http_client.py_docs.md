# Documentation: `tests/integration_tests/adapters/dydx/test_http_client.py`
**Generated:** 2025-11-15T19:40:07.761564Z
**File Size:** 2026 bytes
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

- **Path:** `tests/integration_tests/adapters/dydx/test_http_client.py`
- **Size:** 2,026 bytes
- **Lines:** 58
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
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
Unit tests for the HTTP client.
"""

from typing import Any

import pytest

from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient


@pytest.mark.parametrize(
    ("payload", "expected_result"),
    [
        (
            {"returnLatestOrders": True, "subaccountNumber": 0},
            "returnLatestOrders=true&subaccountNumber=0",
        ),
        ({"status": ["BEST_EFFORT_OPENED", "OPEN"]}, "status=BEST_EFFORT_OPENED%2COPEN"),
        ({"status": ["BEST_EFFORT_OPENED"]}, "status=BEST_EFFORT_OPENED"),
        ({"limit": 100}, "limit=100"),
        (
            {
                "status": ["BEST_EFFORT_OPENED", "OPEN"],
                "returnLatestOrders": True,
                "subaccountNumber": 0,
            },
            "status=BEST_EFFORT_OPENED%2COPEN&returnLatestOrders=true&subaccountNumber=0",
        ),
    ],
)
def test_payload_urlencode(
    http_client: DYDXHttpClient,
    payload: dict[str, Any],
    expected_result: str,
) -> None:
    """
    Test encoding the payload sent by the client.
    """
    # Act
    result = http_client._urlencode(payload)

    # Assert
    assert result == expected_result
```


---

## Overview

This file is located at `tests/integration_tests/adapters/dydx/test_http_client.py` within the repository.

**Functions defined:** test_payload_urlencode

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_payload_urlencode(
    http_client: DYDXHttpClient,
    payload: dict[str, Any],
    expected_result: str,
)`


### Imports

- `from typing import Any`
- `import pytest`
- `from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.dydx.test_http_client import test_payload_urlencode
```


---

## Related Files

This file imports from the following modules:

- `from typing import Any`
- `import pytest`
- `from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient`

**Directory:** `tests/integration_tests/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


