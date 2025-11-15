# Documentation: `tests/integration_tests/adapters/coinbase_intx/sandbox/instrument_provider.py`
**Generated:** 2025-11-15T19:40:07.734295Z
**File Size:** 1917 bytes
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

- **Path:** `tests/integration_tests/adapters/coinbase_intx/sandbox/instrument_provider.py`
- **Size:** 1,917 bytes
- **Lines:** 47
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7

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

from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client
from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_instrument_provider
from nautilus_trader.common.component import init_logging
from nautilus_trader.common.config import InstrumentProviderConfig
from nautilus_trader.common.enums import LogLevel
from nautilus_trader.core import nautilus_pyo3


async def run():
    nautilus_pyo3.init_tracing()
    _guard = init_logging(level_stdout=LogLevel.TRACE)

    http_client = get_coinbase_intx_http_client()

    filters = {}

    # config = InstrumentProviderConfig(load_ids=frozenset(instrument_ids))
    config = InstrumentProviderConfig(load_all=True, filters=filters)
    provider = get_coinbase_intx_instrument_provider(http_client, config)

    await provider.initialize()

    for instrument in provider.list_all():
        print(repr(instrument))

    print(f"Loaded {len(provider.list_all())} instruments")


if __name__ == "__main__":
    asyncio.run(run())
```


---

## Overview

This file is located at `tests/integration_tests/adapters/coinbase_intx/sandbox/instrument_provider.py` within the repository.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `import asyncio`
- `from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client`
- `from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_instrument_provider`
- `from nautilus_trader.common.component import init_logging`
- `from nautilus_trader.common.config import InstrumentProviderConfig`
- `from nautilus_trader.common.enums import LogLevel`
- `from nautilus_trader.core import nautilus_pyo3`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.coinbase_intx.sandbox.instrument_provider
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client`
- `from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_instrument_provider`
- `from nautilus_trader.common.component import init_logging`
- `from nautilus_trader.common.config import InstrumentProviderConfig`
- `from nautilus_trader.common.enums import LogLevel`
- `from nautilus_trader.core import nautilus_pyo3`

**Directory:** `tests/integration_tests/adapters/coinbase_intx/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


