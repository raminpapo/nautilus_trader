# Documentation: test_data.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/interactive_brokers/test_data.py`
- **Size**: 1,483 bytes
- **Lines**: 38
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

import asyncio

import pytest


pytestmark = pytest.mark.skip(reason="Skip due currently flaky mocks")


def instrument_setup(data_client, instrument, contract_details):
    data_client.instrument_provider.contract_details[instrument.id] = contract_details
    data_client.instrument_provider.contract_id_to_instrument_id[
        contract_details.contract.conId
    ] = instrument.id
    data_client.instrument_provider.add(instrument)


@pytest.mark.asyncio
async def test_connect(data_client):
    data_client.connect()
    await asyncio.sleep(0)
    await asyncio.sleep(0)
    assert data_client.is_connected

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`instrument_setup()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `instrument_setup`
**Imports**: `asyncio`, `pytest`

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
pytest tests/integration_tests/adapters/interactive_brokers/test_data.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.011448Z*
