# Documentation: `tests/integration_tests/adapters/interactive_brokers/test_gateway.py`
**Generated:** 2025-11-15T19:40:07.840933Z
**File Size:** 1834 bytes
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

- **Path:** `tests/integration_tests/adapters/interactive_brokers/test_gateway.py`
- **Size:** 1,834 bytes
- **Lines:** 48
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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


---

## Overview

This file is located at `tests/integration_tests/adapters/interactive_brokers/test_gateway.py` within the repository.

**Functions defined:** test_gateway_start_no_container

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_gateway_start_no_container(mocker)`


### Imports

- `import pytest`
- `from docker.models.containers import ContainerCollection`
- `from nautilus_trader.adapters.interactive_brokers.gateway import DockerizedIBGateway`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.interactive_brokers.test_gateway import test_gateway_start_no_container
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from docker.models.containers import ContainerCollection`
- `from nautilus_trader.adapters.interactive_brokers.gateway import DockerizedIBGateway`

**Directory:** `tests/integration_tests/adapters/interactive_brokers`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


