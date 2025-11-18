# Documentation: test_modules.py

## File Metadata

- **Path**: `tests/unit_tests/backtest/test_modules.py`
- **Size**: 4,248 bytes
- **Lines**: 106
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

import pandas as pd

from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.backtest.modules import FXRolloverInterestConfig
from nautilus_trader.backtest.modules import FXRolloverInterestModule
from nautilus_trader.backtest.modules import SimulationModule
from nautilus_trader.common.component import Logger
from nautilus_trader.config import BacktestEngineConfig
from nautilus_trader.config import LoggingConfig
from nautilus_trader.config import SimulationModuleConfig
from nautilus_trader.core.data import Data
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Money
from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler
from nautilus_trader.test_kit.providers import TestDataProvider
from nautilus_trader.test_kit.providers import TestInstrumentProvider


USDJPY_SIM = TestInstrumentProvider.default_fx_ccy("USD/JPY")


class TestSimulationModules:
    def create_engine(self, modules: list) -> BacktestEngine:
        engine = BacktestEngine(BacktestEngineConfig(logging=LoggingConfig(bypass_logging=True)))
        engine.add_venue(
            venue=Venue("SIM"),
            oms_type=OmsType.HEDGING,
            account_type=AccountType.MARGIN,
            base_currency=USD,
            starting_balances=[Money(1_000_000, USD)],
            modules=modules,
        )
        wrangler = QuoteTickDataWrangler(USDJPY_SIM)
        provider = TestDataProvider()
        ticks = wrangler.process_bar_data(
            bid_data=provider.read_csv_bars("fxcm/usdjpy-m1-bid-2013.csv")[:10],
            ask_data=provider.read_csv_bars("fxcm/usdjpy-m1-ask-2013.csv")[:10],
        )
        engine.add_instrument(USDJPY_SIM)
        engine.add_data(ticks)
        return engine

    def test_fx_rollover_interest_module(self):
        # Arrange
        config = FXRolloverInterestConfig(pd.DataFrame(columns=["LOCATION"]))
        module = FXRolloverInterestModule(config)
        engine = self.create_engine(modules=[module])

        # Act, Assert
        [venue] = engine.list_venues()
        assert venue

    def test_python_module(self):
        # Arrange
        class PythonModule(SimulationModule):
            def process(self, ts_now: int) -> None:
                assert self.exchange

            def log_diagnostics(self, log: Logger) -> None:
                pass

        config = SimulationModuleConfig()
        engine = self.create_engine(modules=[PythonModule(config)])

        # Act
        engine.run()

    def test_pre_process_custom_order_fill(self):
        # Arrange
        class PythonModule(SimulationModule):
            def pre_process(self, data: Data) -> None:
                if data.ts_init == 1359676979900000000:
                    assert data
                    matching_engine = self.exchange.get_matching_engine(data.instrument_id)
                    assert matching_engine

            def process(self, ts_now: int) -> None:
                assert self.exchange

            def log_diagnostics(self, log: Logger) -> None:
                pass

        config = SimulationModuleConfig()
        engine = self.create_engine(modules=[PythonModule(config)])

        # Act
        engine.run()

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestSimulationModules`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Classs**: `TestSimulationModules`
**Imports**: `nautilus_trader.backtest.engine`, `nautilus_trader.backtest.modules`, `nautilus_trader.common.component`, `nautilus_trader.config`, `nautilus_trader.core.data`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `nautilus_trader.persistence.wranglers`, `nautilus_trader.test_kit.providers`, `pandas`

## Related Files

This file is located in `tests/unit_tests/backtest/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/backtest/test_modules.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.227705Z*
