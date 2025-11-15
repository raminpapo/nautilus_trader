# Documentation: `tests/integration_tests/adapters/sandbox/conftest.py`
**Generated:** 2025-11-15T19:40:07.955623Z
**File Size:** 2262 bytes
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

- **Path:** `tests/integration_tests/adapters/sandbox/conftest.py`
- **Size:** 2,262 bytes
- **Lines:** 73
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Functions:** 5

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

from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig
from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient
from nautilus_trader.model.events import AccountState
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.events import TestEventStubs


@pytest.fixture()
def venue() -> Venue:
    return Venue("SANDBOX")


@pytest.fixture()
def exec_client(
    instrument,
    event_loop,
    portfolio,
    msgbus,
    cache,
    clock,
    venue,
):
    cache.add_instrument(instrument)  # <-- This might be redundant now

    config = SandboxExecutionClientConfig(
        venue=venue.value,
        starting_balances=["100_000 USD"],
        base_currency="USD",
        account_type="CASH",
    )
    return SandboxExecutionClient(
        loop=event_loop,
        portfolio=portfolio,
        msgbus=msgbus,
        cache=cache,
        clock=clock,
        config=config,
    )


@pytest.fixture()
def instrument():
    return TestInstrumentProvider.equity("AAPL", "SANDBOX")


@pytest.fixture()
def account_state() -> AccountState:
    return TestEventStubs.cash_account_state(account_id=AccountId("SANDBOX-001"))


@pytest.fixture()
def data_client():
    pass
```


---

## Overview

This file is located at `tests/integration_tests/adapters/sandbox/conftest.py` within the repository.

**Functions defined:** venue, exec_client, instrument, account_state, data_client

**Import statements:** 8


---

## Detailed Analysis

### Functions

#### `venue()`


#### `exec_client(
    instrument,
    event_loop,
    portfolio,
    msgbus,
    cache,
    clock,
    venue,
)`


#### `instrument()`


#### `account_state()`


#### `data_client()`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig`
- `from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient`
- `from nautilus_trader.model.events import AccountState`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.events import TestEventStubs`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.sandbox.conftest import venue
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig`
- `from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient`
- `from nautilus_trader.model.events import AccountState`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.events import TestEventStubs`

**Directory:** `tests/integration_tests/adapters/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


