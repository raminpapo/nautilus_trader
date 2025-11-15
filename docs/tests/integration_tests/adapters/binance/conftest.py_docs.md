# Documentation: `tests/integration_tests/adapters/binance/conftest.py`
**Generated:** 2025-11-15T19:40:07.583246Z
**File Size:** 1938 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/conftest.py`
- **Size:** 1,938 bytes
- **Lines:** 69
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Functions:** 8

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


@pytest.fixture()
def venue() -> Venue:
    raise BINANCE_VENUE


@pytest.fixture()
def data_client():
    pass


@pytest.fixture()
def exec_client():
    pass


@pytest.fixture()
def instrument():
    pass


@pytest.fixture()
def account_state():
    pass
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/conftest.py` within the repository.

**Functions defined:** live_clock, live_logger, binance_http_client, venue, data_client, exec_client, instrument, account_state

**Import statements:** 6


---

## Detailed Analysis

### Functions

#### `live_clock()`


#### `live_logger()`


#### `binance_http_client(session_event_loop, live_clock)`


#### `venue()`


#### `data_client()`


#### `exec_client()`


#### `instrument()`


#### `account_state()`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE`
- `from nautilus_trader.adapters.binance.http.client import BinanceHttpClient`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.binance.conftest import live_clock
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE`
- `from nautilus_trader.adapters.binance.http.client import BinanceHttpClient`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `tests/integration_tests/adapters/binance`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key, session. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


