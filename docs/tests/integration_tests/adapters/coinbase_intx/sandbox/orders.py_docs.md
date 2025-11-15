# Documentation: `tests/integration_tests/adapters/coinbase_intx/sandbox/orders.py`
**Generated:** 2025-11-15T19:40:07.735555Z
**File Size:** 2225 bytes
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

- **Path:** `tests/integration_tests/adapters/coinbase_intx/sandbox/orders.py`
- **Size:** 2,225 bytes
- **Lines:** 53
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
from nautilus_trader.adapters.env import get_env_key
from nautilus_trader.common.component import init_logging
from nautilus_trader.common.enums import LogLevel
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.core.uuid import UUID4


async def run():
    nautilus_pyo3.init_tracing()
    _guard = init_logging(level_stdout=LogLevel.TRACE)

    http_client = get_coinbase_intx_http_client()

    portfolio_id = get_env_key("COINBASE_INTX_PORTFOLIO_ID")
    account_id = nautilus_pyo3.AccountId(f"COINBASE_INTX-{portfolio_id}")
    symbol = nautilus_pyo3.Symbol("BTC-PERP")
    client_order_id = nautilus_pyo3.ClientOrderId(UUID4().value)

    instrument = await http_client.request_instrument(symbol)
    http_client.add_instrument(instrument)  # Must be cached for further requests

    await http_client.submit_order(
        account_id,
        symbol=symbol,
        client_order_id=client_order_id,
        order_type=nautilus_pyo3.OrderType.MARKET,
        order_side=nautilus_pyo3.OrderSide.BUY,
        quantity=nautilus_pyo3.Quantity.from_str("0.01"),
        time_in_force=nautilus_pyo3.TimeInForce.IOC,
        # price=nautilus_pyo3.Price.from_str("1000.00"),
    )


if __name__ == "__main__":
    asyncio.run(run())
```


---

## Overview

This file is located at `tests/integration_tests/adapters/coinbase_intx/sandbox/orders.py` within the repository.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `import asyncio`
- `from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client`
- `from nautilus_trader.adapters.env import get_env_key`
- `from nautilus_trader.common.component import init_logging`
- `from nautilus_trader.common.enums import LogLevel`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.uuid import UUID4`


---

## Usage Examples

### Importing

```python
import tests.integration_tests.adapters.coinbase_intx.sandbox.orders
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.adapters.coinbase_intx.factories import get_coinbase_intx_http_client`
- `from nautilus_trader.adapters.env import get_env_key`
- `from nautilus_trader.common.component import init_logging`
- `from nautilus_trader.common.enums import LogLevel`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.uuid import UUID4`

**Directory:** `tests/integration_tests/adapters/coinbase_intx/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


