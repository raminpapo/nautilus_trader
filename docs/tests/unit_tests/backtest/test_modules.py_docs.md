# Documentation: `tests/unit_tests/backtest/test_modules.py`
**Generated:** 2025-11-15T19:40:09.009393Z
**File Size:** 4248 bytes
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

- **Path:** `tests/unit_tests/backtest/test_modules.py`
- **Size:** 4,248 bytes
- **Lines:** 105
- **Extension:** `.py`
- **Type:** text
- **Imports:** 18
- **Classes:** 3
- **Functions:** 9

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


---

## Overview

This file is located at `tests/unit_tests/backtest/test_modules.py` within the repository.

**Classes defined:** TestSimulationModules, PythonModule, PythonModule

**Functions defined:** create_engine, test_fx_rollover_interest_module, test_python_module, process, log_diagnostics, test_pre_process_custom_order_fill, pre_process, process, log_diagnostics

**Import statements:** 18


---

## Detailed Analysis

### Classes

#### `TestSimulationModules`


#### `PythonModule`

**Inherits from:** SimulationModule


#### `PythonModule`

**Inherits from:** SimulationModule


### Functions

#### `create_engine(self, modules: list)`


#### `test_fx_rollover_interest_module(self)`


#### `test_python_module(self)`


#### `process(self, ts_now: int)`


#### `log_diagnostics(self, log: Logger)`


#### `test_pre_process_custom_order_fill(self)`


#### `pre_process(self, data: Data)`


#### `process(self, ts_now: int)`


#### `log_diagnostics(self, log: Logger)`


### Imports

- `import pandas as pd`
- `from nautilus_trader.backtest.engine import BacktestEngine`
- `from nautilus_trader.backtest.modules import FXRolloverInterestConfig`
- `from nautilus_trader.backtest.modules import FXRolloverInterestModule`
- `from nautilus_trader.backtest.modules import SimulationModule`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.config import BacktestEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.config import SimulationModuleConfig`
- `from nautilus_trader.core.data import Data`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.enums import AccountType`
- `from nautilus_trader.model.enums import OmsType`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler`
- `from nautilus_trader.test_kit.providers import TestDataProvider`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.backtest.test_modules import TestSimulationModules
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `from nautilus_trader.backtest.engine import BacktestEngine`
- `from nautilus_trader.backtest.modules import FXRolloverInterestConfig`
- `from nautilus_trader.backtest.modules import FXRolloverInterestModule`
- `from nautilus_trader.backtest.modules import SimulationModule`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.config import BacktestEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.config import SimulationModuleConfig`
- `from nautilus_trader.core.data import Data`

*... and 8 more*

**Directory:** `tests/unit_tests/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


