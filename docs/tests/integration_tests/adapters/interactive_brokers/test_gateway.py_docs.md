# Documentation: test_gateway.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/interactive_brokers/test_gateway.py`
- **Size**: 1,834 bytes
- **Lines**: 49
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
from docker.models.containers import ContainerCollection

from nautilus_trader.adapters.interactive_brokers.gateway import DockerizedIBGateway


pytestmark = pytest.mark.skip(reason="Skip due currently flaky mocks")


def test_gateway_start_no_container(mocker):
    # Arrange
    mock_docker = mocker.patch.object(ContainerCollection, "run")
    gateway = DockerizedIBGateway(username="test", password="test")

    # Act
    gateway.start(wait=None)

    # Assert
    expected = {
        "image": "ghcr.io/unusualalpha/ib-gateway",
        "name": "nautilus-ib-gateway",
        "detach": True,
        "ports": {"4001": "4001", "4002": "4002", "5900": "5900"},
        "platform": "amd64",
        "environment": {
            "TWS_USERID": "test",
            "TWS_PASSWORD": "test",
            "TRADING_MODE": "paper",
            "READ_ONLY_API": "yes",
        },
    }
    result = mock_docker.call_args.kwargs
    assert result == expected

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_gateway_start_no_container()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `test_gateway_start_no_container`
**Imports**: `docker.models.containers`, `nautilus_trader.adapters.interactive_brokers.gateway`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/interactive_brokers/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/interactive_brokers/test_gateway.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:07.022173Z*
