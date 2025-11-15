# Documentation: `examples/live/kraken/kraken_data_tester.py`
**Generated:** 2025-11-15T19:40:03.936410Z
**File Size:** 3907 bytes
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

- **Path:** `examples/live/kraken/kraken_data_tester.py`
- **Size:** 3,907 bytes
- **Lines:** 100
- **Extension:** `.py`
- **Type:** text
- **Imports:** 13

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

from nautilus_trader.adapters.kraken import KRAKEN
from nautilus_trader.adapters.kraken import KrakenDataClientConfig
from nautilus_trader.adapters.kraken import KrakenLiveDataClientFactory
from nautilus_trader.config import InstrumentProviderConfig
from nautilus_trader.config import LiveExecEngineConfig
from nautilus_trader.config import LoggingConfig
from nautilus_trader.config import TradingNodeConfig
from nautilus_trader.live.node import TradingNode
from nautilus_trader.model.data import BarType
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.test_kit.strategies.tester_data import DataTester
from nautilus_trader.test_kit.strategies.tester_data import DataTesterConfig


# *** THIS IS A TEST STRATEGY WITH NO ALPHA ADVANTAGE WHATSOEVER. ***
# *** IT IS NOT INTENDED TO BE USED TO TRADE LIVE WITH REAL MONEY. ***

# Configuration - Change symbol for different trading pairs
# SPOT examples: "BTC/USD", "ETH/USD", "SOL/USD"
# PERP examples: "PF_XBTUSD", "PF_ETHUSD", "PF_SOLUSD"
symbol = "ETH/USD"  # Spot pair
instrument_id = InstrumentId.from_str(f"{symbol}.{KRAKEN}")

# Configure the trading node
config_node = TradingNodeConfig(
    trader_id=TraderId("TESTER-001"),
    logging=LoggingConfig(
        log_level="INFO",
        # log_level_file="DEBUG",
        use_pyo3=True,
    ),
    exec_engine=LiveExecEngineConfig(
        reconciliation=False,  # Not applicable
    ),
    data_clients={
        KRAKEN: KrakenDataClientConfig(
            api_key=None,  # 'KRAKEN_API_KEY' env var
            api_secret=None,  # 'KRAKEN_API_SECRET' env var
            base_url_http=None,  # Override with custom endpoint
            base_url_ws=None,  # Override with custom endpoint
            instrument_provider=InstrumentProviderConfig(load_all=True),
            update_instruments_interval_mins=60,  # Update instruments every hour
        ),
    },
    timeout_connection=20.0,
    timeout_disconnection=5.0,
    timeout_post_stop=5.0,
)

# Instantiate the node with a configuration
node = TradingNode(config=config_node)

# Configure and initialize the tester
config_tester = DataTesterConfig(
    instrument_ids=[instrument_id],
    bar_types=[BarType.from_str(f"{instrument_id.value}-1-MINUTE-LAST-EXTERNAL")],
    subscribe_instrument=True,
    subscribe_quotes=True,
    subscribe_trades=True,
    # subscribe_bars=True,
    # subscribe_book_deltas=True,
    # subscribe_book_depth=True,
    # subscribe_book_at_interval=True,
    # book_depth=10,
    # book_interval_ms=10,
    # request_bars=True,
    # request_trades=True,
)
tester = DataTester(config=config_tester)

node.trader.add_actor(tester)

# Register your client factories with the node (can take user-defined factories)
node.add_data_client_factory(KRAKEN, KrakenLiveDataClientFactory)
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

This file is located at `examples/live/kraken/kraken_data_tester.py` within the repository.

**Import statements:** 13


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.kraken import KRAKEN`
- `from nautilus_trader.adapters.kraken import KrakenDataClientConfig`
- `from nautilus_trader.adapters.kraken import KrakenLiveDataClientFactory`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.config import LiveExecEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.config import TradingNodeConfig`
- `from nautilus_trader.live.node import TradingNode`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import TraderId`
- `from nautilus_trader.test_kit.strategies.tester_data import DataTester`
- `from nautilus_trader.test_kit.strategies.tester_data import DataTesterConfig`


---

## Usage Examples

### Importing

```python
import examples.live.kraken.kraken_data_tester
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.kraken import KRAKEN`
- `from nautilus_trader.adapters.kraken import KrakenDataClientConfig`
- `from nautilus_trader.adapters.kraken import KrakenLiveDataClientFactory`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.config import LiveExecEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.config import TradingNodeConfig`
- `from nautilus_trader.live.node import TradingNode`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.identifiers import InstrumentId`

*... and 3 more*

**Directory:** `examples/live/kraken`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


