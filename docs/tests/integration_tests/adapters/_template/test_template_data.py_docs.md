# Documentation: test_template_data.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/_template/test_template_data.py`
- **Size**: 1,598 bytes
- **Lines**: 47
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

from nautilus_trader.adapters._template.data import TemplateLiveMarketDataClient
from nautilus_trader.live.data_client import LiveMarketDataClient


pytestmark = pytest.mark.skip(reason="template")


@pytest.fixture
def data_client() -> LiveMarketDataClient:
    return TemplateLiveMarketDataClient()  # type: ignore


def test_connect(data_client: LiveMarketDataClient):
    data_client.connect()
    assert data_client.is_connected


def test_disconnect(data_client: LiveMarketDataClient):
    data_client.connect()
    data_client.disconnect()
    assert not data_client.is_connected


def test_reset(data_client: LiveMarketDataClient):
    pass


def test_dispose(data_client: LiveMarketDataClient):
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`data_client()`**: Function defined in this file
- **`test_connect()`**: Function defined in this file
- **`test_disconnect()`**: Function defined in this file
- **`test_reset()`**: Function defined in this file
- **`test_dispose()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `data_client`, `test_connect`, `test_disconnect`, `test_dispose`, `test_reset`
**Imports**: `nautilus_trader.adapters._template.data`, `nautilus_trader.live.data_client`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/_template/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/_template/test_template_data.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.192218Z*
