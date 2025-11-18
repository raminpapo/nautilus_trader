# Documentation: conftest.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/conftest.py`
- **Size**: 1,928 bytes
- **Lines**: 70
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


import pytest

from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE
from nautilus_trader.adapters.binance.http.client import BinanceHttpClient
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import Logger
from nautilus_trader.model.identifiers import Venue


@pytest.fixture(scope="session")
def live_clock():
    return LiveClock()


@pytest.fixture(scope="session")
def live_logger():
    return Logger("TEST_LOGGER")


@pytest.fixture(scope="session")
def binance_http_client(session_event_loop, live_clock):
    client = BinanceHttpClient(
        clock=live_clock,
        api_key="SOME_BINANCE_API_KEY",
        api_secret="SOME_BINANCE_API_SECRET",
        base_url="https://api.binance.com/",  # Spot/Margin
    )
    return client


@pytest.fixture
def venue() -> Venue:
    raise BINANCE_VENUE


@pytest.fixture
def data_client():
    pass


@pytest.fixture
def exec_client():
    pass


@pytest.fixture
def instrument():
    pass


@pytest.fixture
def account_state():
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`live_clock()`**: Function defined in this file
- **`live_logger()`**: Function defined in this file
- **`binance_http_client()`**: Function defined in this file
- **`venue()`**: Function defined in this file
- **`data_client()`**: Function defined in this file
- **`exec_client()`**: Function defined in this file
- **`instrument()`**: Function defined in this file
- **`account_state()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Functions**: `account_state`, `binance_http_client`, `data_client`, `exec_client`, `instrument`, `live_clock`, `live_logger`, `venue`
**Imports**: `nautilus_trader.adapters.binance.common.constants`, `nautilus_trader.adapters.binance.http.client`, `nautilus_trader.common.component`, `nautilus_trader.model.identifiers`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:06.598218Z*
