# Documentation: bitmex_data_tester.py

## File Metadata

- **Path**: `examples/live/bitmex/bitmex_data_tester.py`
- **Size**: 4,095 bytes
- **Lines**: 107
- **Language**: Python

## Original Source

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

from nautilus_trader.adapters.bitmex import BITMEX
from nautilus_trader.adapters.bitmex import BitmexDataClientConfig
from nautilus_trader.adapters.bitmex import BitmexLiveDataClientFactory
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

# Example symbols for different BitMEX products
# Perpetual swap: XBTUSD (Bitcoin perpetual)
# Futures: XBTH25 (Bitcoin futures expiring March 2025)
# Alt perpetuals: ETHUSD, SOLUSD, etc.

testnet = False  # If client uses the testnet API
symbol = "XBTUSD"  # Bitcoin perpetual swap
# symbol = "SOLUSDT"  # Solana spot
# symbol = "ETHUSDT"  # Ethereum spot
# symbol = ".BXBT"  # Bitcoin index

# Configure the trading node
config_node = TradingNodeConfig(
    trader_id=TraderId("TESTER-001"),
    logging=LoggingConfig(log_level="INFO", use_pyo3=True),
    exec_engine=LiveExecEngineConfig(
        reconciliation=False,  # Not applicable
    ),
    data_clients={
        BITMEX: BitmexDataClientConfig(
            api_key=None,  # 'BITMEX_API_KEY' env var
            api_secret=None,  # 'BITMEX_API_SECRET' env var
            base_url_http=None,  # Override with custom endpoint
            base_url_ws=None,  # Override with custom endpoint
            instrument_provider=InstrumentProviderConfig(load_all=True),
            testnet=testnet,  # If client uses the testnet API
        ),
    },
    timeout_connection=10.0,
    timeout_reconciliation=10.0,
    timeout_disconnection=2.0,
    timeout_post_stop=1.0,
)

# Configure the data tester actor
config_tester = DataTesterConfig(
    instrument_ids=[InstrumentId.from_str(f"{symbol}.{BITMEX}")],
    bar_types=[BarType.from_str(f"{symbol}.{BITMEX}-1-MINUTE-LAST-EXTERNAL")],
    subscribe_instrument=True,
    subscribe_quotes=True,
    subscribe_trades=True,
    subscribe_mark_prices=True,
    subscribe_index_prices=True,
    subscribe_funding_rates=True,
    subscribe_bars=True,
    # subscribe_book_deltas=True,
    # subscribe_book_depth=True,  # Not yet supported
    # subscribe_book_at_interval=True,
    # book_type=BookType.L2_MBP,
    # book_depth=25,
    # book_interval_ms=10,
    # request_trades=True,
    # request_bars=True,
)

# Setup and run the trading node
node = TradingNode(config=config_node)

# Add the strategy to the node
node.trader.add_actor(DataTester(config=config_tester))

# Register the data client factory
node.add_data_client_factory(BITMEX, BitmexLiveDataClientFactory)
node.build()

# Run the node
try:
    node.run()
except KeyboardInterrupt:
    node.stop()
finally:
    node.dispose()

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Imports**: `nautilus_trader.adapters.bitmex`, `nautilus_trader.config`, `nautilus_trader.live.node`, `nautilus_trader.model.data`, `nautilus_trader.model.identifiers`, `nautilus_trader.test_kit.strategies.tester_data`

## Related Files

This file is located in `examples/live/bitmex/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/live/bitmex/bitmex_data_tester.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:04.306549Z*
