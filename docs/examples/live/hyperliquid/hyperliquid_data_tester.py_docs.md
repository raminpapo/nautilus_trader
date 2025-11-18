# Documentation: hyperliquid_data_tester.py

## File Metadata

- **Path**: `examples/live/hyperliquid/hyperliquid_data_tester.py`
- **Size**: 4,175 bytes
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

from nautilus_trader.adapters.hyperliquid import HYPERLIQUID
from nautilus_trader.adapters.hyperliquid import HyperliquidDataClientConfig
from nautilus_trader.adapters.hyperliquid import HyperliquidLiveDataClientFactory
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

# *** THIS INTEGRATION IS STILL UNDER CONSTRUCTION. ***
# *** CONSIDER IT TO BE IN AN UNSTABLE BETA PHASE AND EXERCISE CAUTION. ***

instrument_ids = [
    InstrumentId.from_str("BTC-USD-PERP.HYPERLIQUID"),
    InstrumentId.from_str("ETH-USD-PERP.HYPERLIQUID"),
    InstrumentId.from_str("HYPE-USDC-SPOT.HYPERLIQUID"),
]

bar_types = [
    BarType.from_str("BTC-USD-PERP.HYPERLIQUID-1-MINUTE-LAST-EXTERNAL"),
    BarType.from_str("HYPE-USDC-SPOT.HYPERLIQUID-1-MINUTE-LAST-EXTERNAL"),
]

if __name__ == "__main__":
    # Configure the trading node
    config_node = TradingNodeConfig(
        trader_id=TraderId("TESTER-001"),
        logging=LoggingConfig(
            log_level="INFO",
            # log_level_file="DEBUG",
            use_pyo3=True,
        ),
        exec_engine=LiveExecEngineConfig(
            reconciliation=False,  # Not required for data testing
        ),
        data_clients={
            HYPERLIQUID: HyperliquidDataClientConfig(
                instrument_provider=InstrumentProviderConfig(load_all=True),
                testnet=False,  # If client uses the testnet
            ),
        },
        timeout_connection=20.0,
        timeout_reconciliation=10.0,
        timeout_portfolio=10.0,
        timeout_disconnection=10.0,
        timeout_post_stop=2.0,
    )

    # Instantiate the node with a configuration
    node = TradingNode(config=config_node)

    # Configure your strategy
    config_strat = DataTesterConfig(
        instrument_ids=instrument_ids,
        bar_types=bar_types,
        # subscribe_book_at_interval=True,
        # book_interval_ms=10,
        # subscribe_quotes=True,
        subscribe_trades=True,
        subscribe_mark_prices=True,
        subscribe_index_prices=True,
        subscribe_funding_rates=True,
        # subscribe_bars=True,
        # request_bars=True,
    )
    # Instantiate your strategy
    strategy = DataTester(config=config_strat)

    # Add your actors and modules
    node.trader.add_actor(strategy)

    # Register your client factories with the node (can take user-defined factories)
    node.add_data_client_factory(HYPERLIQUID, HyperliquidLiveDataClientFactory)
    node.build()

    # Stop and dispose of the node with SIGINT/CTRL+C
    if __name__ == "__main__":
        try:
            node.run()
        finally:
            node.dispose()

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Imports**: `nautilus_trader.adapters.hyperliquid`, `nautilus_trader.config`, `nautilus_trader.live.node`, `nautilus_trader.model.data`, `nautilus_trader.model.identifiers`, `nautilus_trader.test_kit.strategies.tester_data`

## Related Files

This file is located in `examples/live/hyperliquid/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/live/hyperliquid/hyperliquid_data_tester.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.337576Z*
