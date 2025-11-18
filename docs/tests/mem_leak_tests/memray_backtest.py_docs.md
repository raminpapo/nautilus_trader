# Documentation: memray_backtest.py

## File Metadata

- **Path**: `tests/mem_leak_tests/memray_backtest.py`
- **Size**: 4,086 bytes
- **Lines**: 104
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

from decimal import Decimal

from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.backtest.engine import BacktestEngineConfig
from nautilus_trader.config import LoggingConfig
from nautilus_trader.examples.algorithms.twap import TWAPExecAlgorithm
from nautilus_trader.examples.strategies.ema_cross_twap import EMACrossTWAP
from nautilus_trader.examples.strategies.ema_cross_twap import EMACrossTWAPConfig
from nautilus_trader.model.currencies import ETH
from nautilus_trader.model.currencies import USDT
from nautilus_trader.model.data import BarType
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Money
from nautilus_trader.persistence.wranglers import TradeTickDataWrangler
from nautilus_trader.test_kit.providers import TestDataProvider
from nautilus_trader.test_kit.providers import TestInstrumentProvider


count = 0
total_runs = 128

if __name__ == "__main__":
    while count < total_runs:
        print(f"Run: {count}/{total_runs}")

        # Configure backtest engine
        config = BacktestEngineConfig(
            trader_id=TraderId("BACKTESTER-001"),
            logging=LoggingConfig(bypass_logging=True),
        )

        # Build the backtest engine
        engine = BacktestEngine(config=config)

        ETHUSDT_BINANCE = TestInstrumentProvider.ethusdt_binance()

        # Add a trading venue (multiple venues possible)
        BINANCE = Venue("BINANCE")
        engine.add_venue(
            venue=BINANCE,
            oms_type=OmsType.NETTING,
            account_type=AccountType.CASH,  # Spot CASH account (not for perpetuals or futures)
            base_currency=None,  # Multi-currency account
            starting_balances=[Money(1_000_000.0, USDT), Money(10.0, ETH)],
        )

        # Add instruments
        engine.add_instrument(ETHUSDT_BINANCE)

        # Add data
        provider = TestDataProvider()
        wrangler = TradeTickDataWrangler(instrument=ETHUSDT_BINANCE)
        ticks = wrangler.process(provider.read_csv_ticks("binance/ethusdt-trades.csv"))
        engine.add_data(ticks)

        # Configure your strategy
        config = EMACrossTWAPConfig(
            instrument_id=ETHUSDT_BINANCE.id,
            bar_type=BarType.from_str("ETHUSDT.BINANCE-250-TICK-LAST-INTERNAL"),
            trade_size=Decimal("0.05"),
            fast_ema_period=10,
            slow_ema_period=20,
            twap_horizon_secs=10.0,
            twap_interval_secs=2.5,
        )

        # Instantiate and add your strategy
        strategy = EMACrossTWAP(config=config)
        engine.add_strategy(strategy=strategy)

        # Instantiate and add your execution algorithm
        exec_algorithm = TWAPExecAlgorithm()
        engine.add_exec_algorithm(exec_algorithm)

        # Run the engine (from start to end of data)
        engine.run()

        # For repeated backtest runs make sure to reset the engine
        engine.reset()

        # Good practice to dispose of the object
        engine.dispose()

        count += 1

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 12


**Imports**: `decimal`, `nautilus_trader.backtest.engine`, `nautilus_trader.config`, `nautilus_trader.examples.algorithms.twap`, `nautilus_trader.examples.strategies.ema_cross_twap`, `nautilus_trader.model.currencies`, `nautilus_trader.model.data`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `nautilus_trader.persistence.wranglers`, `nautilus_trader.test_kit.providers`

## Related Files

This file is located in `tests/mem_leak_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/mem_leak_tests/memray_backtest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.265495Z*
