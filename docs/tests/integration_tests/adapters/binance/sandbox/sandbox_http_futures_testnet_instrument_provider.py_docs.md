# Documentation: `tests/integration_tests/adapters/binance/sandbox/sandbox_http_futures_testnet_instrument_provider.py`
**Generated:** 2025-11-15T19:40:07.670284Z
**File Size:** 2129 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/sandbox/sandbox_http_futures_testnet_instrument_provider.py`
- **Size:** 2,129 bytes
- **Lines:** 51
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9

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

from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE
from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client
from nautilus_trader.adapters.binance.futures.providers import BinanceFuturesInstrumentProvider
from nautilus_trader.common.component import LiveClock
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Symbol


@pytest.mark.asyncio()
async def test_binance_futures_testnet_instrument_provider():
    clock = LiveClock()

    client = get_cached_binance_http_client(
        clock=clock,
        account_type=BinanceAccountType.USDT_FUTURES,
        api_key=os.getenv("BINANCE_FUTURES_TESTNET_API_KEY"),
        api_secret=os.getenv("BINANCE_FUTURES_TESTNET_API_SECRET"),
        is_testnet=True,
    )

    provider = BinanceFuturesInstrumentProvider(
        client=client,
        clock=clock,
    )

    # await provider.load_all_async()
    btcusdt_perp = InstrumentId(Symbol("BTCUSDT-PERP"), BINANCE_VENUE)
    await provider.load_ids_async(instrument_ids=[btcusdt_perp])
    await provider.load_all_async()

    print(provider.count)
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/sandbox/sandbox_http_futures_testnet_instrument_provider.py` within the repository.

**Import statements:** 9


---

## Detailed Analysis

### Imports

- `import os`
- `import pytest`
- `from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.futures.providers import BinanceFuturesInstrumentProvider`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.binance.sandbox.sandbox_http_futures_testnet_instrument_provider
```


---

## Related Files

This file imports from the following modules:

- `import os`
- `import pytest`
- `from nautilus_trader.adapters.binance.common.constants import BINANCE_VENUE`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.factories import get_cached_binance_http_client`
- `from nautilus_trader.adapters.binance.futures.providers import BinanceFuturesInstrumentProvider`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`

**Directory:** `tests/integration_tests/adapters/binance/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


