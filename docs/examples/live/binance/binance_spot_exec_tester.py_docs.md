# Documentation: `examples/live/binance/binance_spot_exec_tester.py`
**Generated:** 2025-11-15T19:40:03.886856Z
**File Size:** 5474 bytes
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

- **Path:** `examples/live/binance/binance_spot_exec_tester.py`
- **Size:** 5,474 bytes
- **Lines:** 143
- **Extension:** `.py`
- **Type:** text
- **Imports:** 16

---

## Source Code

```python
#!/usr/bin/env python3
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

from decimal import Decimal

from nautilus_trader.adapters.binance import BINANCE
from nautilus_trader.adapters.binance import BinanceAccountType
from nautilus_trader.adapters.binance import BinanceDataClientConfig
from nautilus_trader.adapters.binance import BinanceExecClientConfig
from nautilus_trader.adapters.binance import BinanceLiveDataClientFactory
from nautilus_trader.adapters.binance import BinanceLiveExecClientFactory
from nautilus_trader.config import InstrumentProviderConfig
from nautilus_trader.config import LiveExecEngineConfig
from nautilus_trader.config import LoggingConfig
from nautilus_trader.config import TradingNodeConfig
from nautilus_trader.live.node import TradingNode
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.test_kit.strategies.tester_exec import ExecTester
from nautilus_trader.test_kit.strategies.tester_exec import ExecTesterConfig


# *** THIS IS A TEST STRATEGY WITH NO ALPHA ADVANTAGE WHATSOEVER. ***
# *** IT IS NOT INTENDED TO BE USED TO TRADE LIVE WITH REAL MONEY. ***

# Strategy config params
symbol = "ETHUSDT"
instrument_id = InstrumentId.from_str(f"{symbol}.{BINANCE}")
order_qty = Decimal("0.01")

# Configure the trading node
config_node = TradingNodeConfig(
    trader_id=TraderId("TESTER-001"),
    logging=LoggingConfig(
        log_level="INFO",
        # log_level_file="DEBUG",
        # log_file_format="json",
        use_pyo3=True,
    ),
    exec_engine=LiveExecEngineConfig(
        reconciliation=True,
        # snapshot_orders=True,
        # snapshot_positions=True,
        # snapshot_positions_interval_secs=5.0,
        open_check_interval_secs=5.0,
        # manage_own_order_books=True,
    ),
    # cache=CacheConfig(
    #     # database=DatabaseConfig(),
    #     timestamps_as_iso8601=True,
    #     buffer_interval_ms=100,
    #     flush_on_start=False,
    # ),
    # message_bus=MessageBusConfig(
    #     database=DatabaseConfig(),
    #     encoding="json",
    #     timestamps_as_iso8601=True,
    #     buffer_interval_ms=100,
    #     streams_prefix="quoters",
    #     use_instance_id=False,
    #     types_filter=[QuoteTick],
    #     autotrim_mins=30,
    #     heartbeat_interval_secs=1,
    # ),
    # streaming=StreamingConfig(catalog_path="catalog"),
    data_clients={
        BINANCE: BinanceDataClientConfig(
            api_key=None,  # 'BINANCE_API_KEY' env var
            api_secret=None,  # 'BINANCE_API_SECRET' env var
            # key_type=BinanceKeyType.ED25519,
            account_type=BinanceAccountType.SPOT,
            base_url_http=None,  # Override with custom endpoint
            base_url_ws=None,  # Override with custom endpoint
            us=False,  # If client is for Binance US
            testnet=False,  # If client uses the testnet
            instrument_provider=InstrumentProviderConfig(load_all=True),
        ),
    },
    exec_clients={
        BINANCE: BinanceExecClientConfig(
            api_key=None,  # 'BINANCE_API_KEY' env var
            api_secret=None,  # 'BINANCE_API_SECRET' env var
            # key_type=BinanceKeyType.ED25519,
            account_type=BinanceAccountType.SPOT,
            base_url_http=None,  # Override with custom endpoint
            base_url_ws=None,  # Override with custom endpoint
            us=False,  # If client is for Binance US
            testnet=False,  # If client uses the testnet
            instrument_provider=InstrumentProviderConfig(load_all=True),
            max_retries=3,
        ),
    },
    timeout_connection=30.0,
    timeout_reconciliation=10.0,
    timeout_portfolio=10.0,
    timeout_disconnection=10.0,
    timeout_post_stop=5.0,
)

# Instantiate the node with a configuration
node = TradingNode(config=config_node)

# Configure your strategy
config_strat = ExecTesterConfig(
    instrument_id=instrument_id,
    external_order_claims=[instrument_id],
    order_qty=order_qty,
    # open_position_on_start_qty=order_qty,
    # tob_offset_ticks=0,
    # log_data=False,
)

# Instantiate your strategy
strategy = ExecTester(config=config_strat)

# Add your strategies and modules
node.trader.add_strategy(strategy)

# Register your client factories with the node (can take user-defined factories)
node.add_data_client_factory(BINANCE, BinanceLiveDataClientFactory)
node.add_exec_client_factory(BINANCE, BinanceLiveExecClientFactory)
node.build()


# Stop and dispose of the node with SIGINT/CTRL+C
if __name__ == "__main__":
    try:
        node.run()
    finally:
        node.dispose()
```


---

## Overview

This file is located at `examples/live/binance/binance_spot_exec_tester.py` within the repository.

**Import statements:** 16


---

## Detailed Analysis

### Imports

- `from decimal import Decimal`
- `from nautilus_trader.adapters.binance import BINANCE`
- `from nautilus_trader.adapters.binance import BinanceAccountType`
- `from nautilus_trader.adapters.binance import BinanceDataClientConfig`
- `from nautilus_trader.adapters.binance import BinanceExecClientConfig`
- `from nautilus_trader.adapters.binance import BinanceLiveDataClientFactory`
- `from nautilus_trader.adapters.binance import BinanceLiveExecClientFactory`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.config import LiveExecEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.config import TradingNodeConfig`
- `from nautilus_trader.live.node import TradingNode`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import TraderId`
- `from nautilus_trader.test_kit.strategies.tester_exec import ExecTester`
- `from nautilus_trader.test_kit.strategies.tester_exec import ExecTesterConfig`


---

## Usage Examples

### Importing

```python
import examples.live.binance.binance_spot_exec_tester
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from nautilus_trader.adapters.binance import BINANCE`
- `from nautilus_trader.adapters.binance import BinanceAccountType`
- `from nautilus_trader.adapters.binance import BinanceDataClientConfig`
- `from nautilus_trader.adapters.binance import BinanceExecClientConfig`
- `from nautilus_trader.adapters.binance import BinanceLiveDataClientFactory`
- `from nautilus_trader.adapters.binance import BinanceLiveExecClientFactory`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.config import LiveExecEngineConfig`
- `from nautilus_trader.config import LoggingConfig`

*... and 6 more*

**Directory:** `examples/live/binance`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


