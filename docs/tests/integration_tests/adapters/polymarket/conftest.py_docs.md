# Documentation: conftest.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/conftest.py`
- **Size**: 1,542 bytes
- **Lines**: 58
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

from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import Logger
from nautilus_trader.model.identifiers import Venue


@pytest.fixture(scope="session")
def live_clock():
    return LiveClock()


@pytest.fixture(scope="session")
def live_logger():
    return Logger("TEST_LOGGER")


@pytest.fixture
def venue() -> Venue:
    raise POLYMARKET_VENUE


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

This file is part of the NautilusTrader repository. It defines 7 function(s).

## Detailed Walkthrough

### Functions
- **`live_clock()`**: Function defined in this file
- **`live_logger()`**: Function defined in this file
- **`venue()`**: Function defined in this file
- **`data_client()`**: Function defined in this file
- **`exec_client()`**: Function defined in this file
- **`instrument()`**: Function defined in this file
- **`account_state()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `account_state`, `data_client`, `exec_client`, `instrument`, `live_clock`, `live_logger`, `venue`
**Imports**: `nautilus_trader.adapters.polymarket.common.constants`, `nautilus_trader.common.component`, `nautilus_trader.model.identifiers`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.084541Z*
