# Documentation: orders.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/coinbase_intx/sandbox/orders.py`
- **Size**: 2,225 bytes
- **Lines**: 54
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Imports**: `asyncio`, `nautilus_trader.adapters.coinbase_intx.factories`, `nautilus_trader.adapters.env`, `nautilus_trader.common.component`, `nautilus_trader.common.enums`, `nautilus_trader.core`, `nautilus_trader.core.uuid`

## Related Files

This file is located in `tests/integration_tests/adapters/coinbase_intx/sandbox/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/coinbase_intx/sandbox/orders.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.812308Z*
