# Documentation: test_template_execution.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/_template/test_template_execution.py`
- **Size**: 1,905 bytes
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

import pytest

from nautilus_trader.adapters._template.execution import TemplateLiveExecutionClient
from nautilus_trader.live.execution_client import LiveExecutionClient


pytestmark = pytest.mark.skip(reason="template")


@pytest.fixture
def execution_client() -> LiveExecutionClient:
    return TemplateLiveExecutionClient()  # type: ignore


def test_connect(execution_client: LiveExecutionClient):
    execution_client.connect()
    assert execution_client.is_connected


def test_disconnect(execution_client: LiveExecutionClient):
    execution_client.connect()
    execution_client.disconnect()
    assert not execution_client.is_connected


def test_submit_order(execution_client: LiveExecutionClient):
    pass


def test_submit_bracket_order(execution_client: LiveExecutionClient):
    pass


def test_modify_order(execution_client: LiveExecutionClient):
    pass


def test_cancel_order(execution_client: LiveExecutionClient):
    pass


def test_generate_order_status_report(execution_client: LiveExecutionClient):
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`execution_client()`**: Function defined in this file
- **`test_connect()`**: Function defined in this file
- **`test_disconnect()`**: Function defined in this file
- **`test_submit_order()`**: Function defined in this file
- **`test_submit_bracket_order()`**: Function defined in this file
- **`test_modify_order()`**: Function defined in this file
- **`test_cancel_order()`**: Function defined in this file
- **`test_generate_order_status_report()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `execution_client`, `test_cancel_order`, `test_connect`, `test_disconnect`, `test_generate_order_status_report`, `test_modify_order`, `test_submit_bracket_order`, `test_submit_order`
**Imports**: `nautilus_trader.adapters._template.execution`, `nautilus_trader.live.execution_client`, `pytest`

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
pytest tests/integration_tests/adapters/_template/test_template_execution.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.193518Z*
