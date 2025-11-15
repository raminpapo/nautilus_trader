# Documentation: `tests/integration_tests/adapters/interactive_brokers/client/test_client_contract.py`
**Generated:** 2025-11-15T19:40:07.779555Z
**File Size:** 2096 bytes
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

- **Path:** `tests/integration_tests/adapters/interactive_brokers/client/test_client_contract.py`
- **Size:** 2,096 bytes
- **Lines:** 61
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4

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

from unittest.mock import Mock
from unittest.mock import patch

import pytest

from tests.integration_tests.adapters.interactive_brokers.test_kit import IBTestContractStubs


@pytest.mark.asyncio
async def test_get_contract_details(ib_client):
    # Arrange
    ib_client._request_id_seq = 1
    contract = IBTestContractStubs.aapl_equity_contract()
    ib_client._eclient.reqContractDetails = Mock()

    # Act
    with patch("asyncio.wait_for"):
        await ib_client.get_contract_details(contract)

    # Assert
    ib_client._eclient.reqContractDetails.assert_called_once_with(
        reqId=1,
        contract=contract,
    )


@pytest.mark.asyncio
async def test_get_option_chains(ib_client):
    # Arrange
    ib_client._request_id_seq = 1
    underlying = IBTestContractStubs.aapl_equity_contract()

    ib_client._eclient.reqSecDefOptParams = Mock()

    # Act
    with patch("asyncio.wait_for"):
        await ib_client.get_option_chains(underlying)

    # Assert
    ib_client._eclient.reqSecDefOptParams.assert_called_once_with(
        reqId=1,
        underlyingSymbol=underlying.symbol,
        futFopExchange="",
        underlyingSecType=underlying.secType,
        underlyingConId=underlying.conId,
    )
```


---

## Overview

This file is located at `tests/integration_tests/adapters/interactive_brokers/client/test_client_contract.py` within the repository.

**Import statements:** 4


---

## Detailed Analysis

### Imports

- `from unittest.mock import Mock`
- `from unittest.mock import patch`
- `import pytest`
- `from tests.integration_tests.adapters.interactive_brokers.test_kit import IBTestContractStubs`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.interactive_brokers.client.test_client_contract
```


---

## Related Files

This file imports from the following modules:

- `from unittest.mock import Mock`
- `from unittest.mock import patch`
- `import pytest`
- `from tests.integration_tests.adapters.interactive_brokers.test_kit import IBTestContractStubs`

**Directory:** `tests/integration_tests/adapters/interactive_brokers/client`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


