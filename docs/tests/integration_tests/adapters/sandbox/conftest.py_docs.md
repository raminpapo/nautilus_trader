# Documentation: conftest.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/sandbox/conftest.py`
- **Size**: 2,252 bytes
- **Lines**: 74
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

from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig
from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient
from nautilus_trader.model.events import AccountState
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.events import TestEventStubs


@pytest.fixture
def venue() -> Venue:
    return Venue("SANDBOX")


@pytest.fixture
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


@pytest.fixture
def instrument():
    return TestInstrumentProvider.equity("AAPL", "SANDBOX")


@pytest.fixture
def account_state() -> AccountState:
    return TestEventStubs.cash_account_state(account_id=AccountId("SANDBOX-001"))


@pytest.fixture
def data_client():
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`venue()`**: Function defined in this file
- **`exec_client()`**: Function defined in this file
- **`instrument()`**: Function defined in this file
- **`account_state()`**: Function defined in this file
- **`data_client()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Functions**: `account_state`, `data_client`, `exec_client`, `instrument`, `venue`
**Imports**: `nautilus_trader.adapters.sandbox.config`, `nautilus_trader.adapters.sandbox.execution`, `nautilus_trader.model.events`, `nautilus_trader.model.identifiers`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.events`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/sandbox/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.189155Z*
