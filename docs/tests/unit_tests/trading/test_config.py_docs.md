# Documentation: test_config.py

## File Metadata

- **Path**: `tests/unit_tests/trading/test_config.py`
- **Size**: 2,965 bytes
- **Lines**: 73
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

import msgspec

from nautilus_trader.config import ImportableStrategyConfig
from nautilus_trader.config import StrategyFactory
from nautilus_trader.examples.strategies.ema_cross import EMACross


class TestStrategyFactory:
    def test_create_from_path(self):
        # Arrange
        config = {
            "instrument_id": "AUD/USD.SIM",
            "bar_type": "AUD/USD.SIM-15-MINUTE-BID-EXTERNAL",
            "trade_size": 1_000_000,
            "fast_ema_period": 10,
            "slow_ema_period": 20,
        }
        importable = ImportableStrategyConfig(
            strategy_path="nautilus_trader.examples.strategies.ema_cross:EMACross",
            config_path="nautilus_trader.examples.strategies.ema_cross:EMACrossConfig",
            config=config,
        )

        # Act
        strategy = StrategyFactory.create(importable)

        # Assert
        assert isinstance(strategy, EMACross)
        assert (
            repr(config)
            == "{'instrument_id': 'AUD/USD.SIM', 'bar_type': 'AUD/USD.SIM-15-MINUTE-BID-EXTERNAL',"
            " 'trade_size': 1000000, 'fast_ema_period': 10, 'slow_ema_period': 20}"
        )

    def test_create_from_raw(self):
        # Arrange
        raw = msgspec.json.encode(
            {
                "strategy_path": "nautilus_trader.examples.strategies.volatility_market_maker:VolatilityMarketMaker",
                "config_path": "nautilus_trader.examples.strategies.volatility_market_maker:VolatilityMarketMakerConfig",
                "config": {
                    "instrument_id": "ETHUSDT-PERP.BINANCE",
                    "bar_type": "ETHUSDT-PERP.BINANCE-1-MINUTE-LAST-EXTERNAL",
                    "atr_period": "20",
                    "atr_multiple": "6.0",
                    "trade_size": "0.01",
                },
            },
        )

        # Act
        config = ImportableStrategyConfig.parse(raw)

        # Assert
        assert isinstance(config, ImportableStrategyConfig)
        assert config.config["instrument_id"] == "ETHUSDT-PERP.BINANCE"
        assert config.config["atr_period"] == "20"

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestStrategyFactory`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestStrategyFactory`
**Imports**: `msgspec`, `nautilus_trader.config`, `nautilus_trader.examples.strategies.ema_cross`

## Related Files

This file is located in `tests/unit_tests/trading/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/trading/test_config.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.788574Z*
