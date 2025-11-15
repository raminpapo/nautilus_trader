# Documentation: `tests/integration_tests/adapters/dydx/conftest.py`
**Generated:** 2025-11-15T19:40:07.750526Z
**File Size:** 3048 bytes
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

- **Path:** `tests/integration_tests/adapters/dydx/conftest.py`
- **Size:** 3,048 bytes
- **Lines:** 117
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Functions:** 10

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
Create fixtures for commonly used objects.
"""

import sys

import pytest


def pytest_ignore_collect(collection_path, config):
    """
    Prevent collection of test files on Python 3.14.
    """
    if sys.version_info >= (3, 14):
        return True
    return False


# Add pytestmark to skip all dYdX tests on Python 3.14 due to coincurve compatibility
pytestmark = pytest.mark.skipif(
    sys.version_info >= (3, 14),
    reason="dYdX adapter requires Python < 3.14 (coincurve incompatibility)",
)

# Skip imports if Python 3.14+ to avoid ImportError during collection
if sys.version_info < (3, 14):
    from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE
    from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol
    from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient
    from nautilus_trader.common.component import LiveClock
    from nautilus_trader.model.identifiers import InstrumentId
    from nautilus_trader.model.identifiers import Venue
else:
    # Dummy imports for Python 3.14+ to avoid NameError
    DYDX_VENUE = None
    DYDXSymbol = None
    DYDXHttpClient = None
    LiveClock = None
    InstrumentId = None
    Venue = None


@pytest.fixture
def symbol() -> DYDXSymbol:
    """
    Create a stub symbol.
    """
    return DYDXSymbol("BTC-USD")


@pytest.fixture
def instrument_id() -> InstrumentId:
    """
    Create a stub instrument id.
    """
    return InstrumentId.from_str("BTC-USD-PERP.DYDX")


@pytest.fixture(scope="session")
def live_clock() -> LiveClock:
    """
    Create a stub live clock.
    """
    return LiveClock()


@pytest.fixture(scope="session")
def http_client(live_clock: LiveClock) -> DYDXHttpClient:
    """
    Create a stub HTTP client.
    """
    return DYDXHttpClient(
        clock=live_clock,
        base_url="https://indexer.v4testnet.dydx.exchange/v4",
    )


@pytest.fixture()
def venue() -> Venue:
    """
    Create a stub dYdX venue.
    """
    return DYDX_VENUE


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

This file is located at `tests/integration_tests/adapters/dydx/conftest.py` within the repository.

**Functions defined:** pytest_ignore_collect, symbol, instrument_id, live_clock, http_client, venue, data_client, exec_client, instrument, account_state

**Import statements:** 8


---

## Detailed Analysis

### Functions

#### `pytest_ignore_collect(collection_path, config)`


#### `symbol()`


#### `instrument_id()`


#### `live_clock()`


#### `http_client(live_clock: LiveClock)`


#### `venue()`


#### `data_client()`


#### `exec_client()`


#### `instrument()`


#### `account_state()`


### Imports

- `import sys`
- `import pytest`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol`
- `from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.dydx.conftest import pytest_ignore_collect
```


---

## Related Files

This file imports from the following modules:

- `import sys`
- `import pytest`
- `from nautilus_trader.adapters.dydx.common.constants import DYDX_VENUE`
- `from nautilus_trader.adapters.dydx.common.symbol import DYDXSymbol`
- `from nautilus_trader.adapters.dydx.http.client import DYDXHttpClient`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `tests/integration_tests/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: session. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


