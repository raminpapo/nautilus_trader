# Documentation: `tests/integration_tests/adapters/interactive_brokers/test_data.py`
**Generated:** 2025-11-15T19:40:07.831740Z
**File Size:** 1491 bytes
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

- **Path:** `tests/integration_tests/adapters/interactive_brokers/test_data.py`
- **Size:** 1,491 bytes
- **Lines:** 37
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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

import asyncio

import pytest


pytestmark = pytest.mark.skip(reason="Skip due currently flaky mocks")


def instrument_setup(data_client, instrument, contract_details):
    data_client.instrument_provider.contract_details[instrument.id.value] = contract_details
    data_client.instrument_provider.contract_id_to_instrument_id[
        contract_details.contract.conId
    ] = instrument.id
    data_client.instrument_provider.add(instrument)


@pytest.mark.asyncio()
async def test_connect(data_client):
    data_client.connect()
    await asyncio.sleep(0)
    await asyncio.sleep(0)
    assert data_client.is_connected
```


---

## Overview

This file is located at `tests/integration_tests/adapters/interactive_brokers/test_data.py` within the repository.

**Functions defined:** instrument_setup

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `instrument_setup(data_client, instrument, contract_details)`


### Imports

- `import asyncio`
- `import pytest`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.interactive_brokers.test_data import instrument_setup
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import pytest`

**Directory:** `tests/integration_tests/adapters/interactive_brokers`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


