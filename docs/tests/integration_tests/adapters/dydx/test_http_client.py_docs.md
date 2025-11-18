# Documentation: test_http_client.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/dydx/test_http_client.py`
- **Size**: 2,026 bytes
- **Lines**: 59
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_payload_urlencode()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `test_payload_urlencode`
**Imports**: `nautilus_trader.adapters.dydx.http.client`, `pytest`, `typing`

## Related Files

This file is located in `tests/integration_tests/adapters/dydx/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/dydx/test_http_client.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.845840Z*
