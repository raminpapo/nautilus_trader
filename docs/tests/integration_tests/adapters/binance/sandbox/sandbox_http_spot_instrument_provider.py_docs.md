# Documentation: `tests/integration_tests/adapters/binance/sandbox/sandbox_http_spot_instrument_provider.py`
**Generated:** 2025-11-15T19:40:07.675455Z
**File Size:** 1751 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/sandbox/sandbox_http_spot_instrument_provider.py`
- **Size:** 1,751 bytes
- **Lines:** 45
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6

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

import os

import pytest

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client
from nautilus_trader.adapters.binance.spot.providers import BinanceSpotInstrumentProvider
from nautilus_trader.common.component import LiveClock


@pytest.mark.asyncio()
async def test_binance_spot_instrument_provider():
    clock = LiveClock()

    client = get_cached_binance_http_client(
        clock=clock,
        account_type=BinanceAccountType.SPOT,
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET"),
        is_testnet=True,  # <-- add this argument to use the testnet
    )

    provider = BinanceSpotInstrumentProvider(
        client=client,
        clock=clock,
    )

    await provider.load_all_async()

    print(provider.count)
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/sandbox/sandbox_http_spot_instrument_provider.py` within the repository.

**Import statements:** 6


---

## Detailed Analysis

### Imports

- `import os`
- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.spot.providers import BinanceSpotInstrumentProvider`
- `from nautilus_trader.common.component import LiveClock`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.binance.sandbox.sandbox_http_spot_instrument_provider
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `import pytest`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.spot.providers import BinanceSpotInstrumentProvider`
- `from nautilus_trader.common.component import LiveClock`

**Directory:** `tests/integration_tests/adapters/binance/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


