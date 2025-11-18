# Documentation: test_live_node.py

## File Metadata

- **Path**: `tests/integration_tests/live/test_live_node.py`
- **Size**: 7,737 bytes
- **Lines**: 218
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

import msgspec
import pytest

from nautilus_trader.adapters.binance.config import BinanceDataClientConfig
from nautilus_trader.adapters.binance.config import BinanceExecClientConfig
from nautilus_trader.adapters.binance.factories import BinanceLiveDataClientFactory
from nautilus_trader.adapters.binance.factories import BinanceLiveExecClientFactory
from nautilus_trader.config import LoggingConfig
from nautilus_trader.config import TradingNodeConfig
from nautilus_trader.live.node import TradingNode
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.test_kit.functions import ensure_all_tasks_completed


RAW_CONFIG = msgspec.json.encode(
    {
        "environment": "live",
        "trader_id": "Test-111",
        "logging": {"bypass_logging": True},
        "exec_engine": {
            "reconciliation_lookback_mins": 1440,
        },
        "data_clients": {
            "BINANCE": {
                "path": "nautilus_trader.adapters.binance.config:BinanceDataClientConfig",
                "factory": {
                    "path": "nautilus_trader.adapters.binance.factories:BinanceLiveDataClientFactory",
                },
                "config": {
                    "instrument_provider": {
                        "instrument_provider": {"load_all": False},
                    },
                },
            },
        },
        "exec_clients": {
            "BINANCE": {
                "factory": {
                    "path": "nautilus_trader.adapters.binance.factories:BinanceLiveExecClientFactory",
                },
                "path": "nautilus_trader.adapters.binance.config:BinanceExecClientConfig",
                "config": {
                    "instrument_provider": {
                        "instrument_provider": {"load_all": False},
                    },
                },
            },
        },
        "timeout_connection": 5.0,
        "timeout_reconciliation": 5.0,
        "timeout_portfolio": 5.0,
        "timeout_disconnection": 1.0,  # Short timeouts for testing
        "timeout_post_stop": 1.0,  # Short timeouts for testing
        "strategies": [
            {
                "strategy_path": "nautilus_trader.examples.strategies.volatility_market_maker:VolatilityMarketMaker",
                "config_path": "nautilus_trader.examples.strategies.volatility_market_maker:VolatilityMarketMakerConfig",
                "config": {
                    "instrument_id": "ETHUSDT-PERP.BINANCE",
                    "bar_type": "ETHUSDT-PERP.BINANCE-1-MINUTE-LAST-EXTERNAL",
                    "atr_period": 20,
                    "atr_multiple": 6.0,
                    "trade_size": "0.01",
                },
            },
        ],
    },
)


class TestTradingNodeConfiguration:
    def teardown(self):
        ensure_all_tasks_completed()

    def test_config_with_in_memory_execution_database(self, event_loop_for_setup):
        # Arrange
        loop = event_loop_for_setup

        config = TradingNodeConfig(
            logging=LoggingConfig(bypass_logging=True),
        )

        # Act
        node = TradingNode(config=config, loop=loop)

        # Assert
        assert node is not None

    def test_config_with_redis_execution_database(self, event_loop_for_setup):
        # Arrange, Act
        loop = event_loop_for_setup

        config = TradingNodeConfig(
            logging=LoggingConfig(bypass_logging=True),
        )
        node = TradingNode(config=config, loop=loop)

        # Assert
        assert node is not None

    def test_node_config_from_raw(self, event_loop_for_setup):
        # Arrange, Act
        loop = event_loop_for_setup

        config = TradingNodeConfig.parse(RAW_CONFIG)
        node = TradingNode(config=config, loop=loop)

        # Assert
        assert node.trader.id.value == "Test-111"
        assert node.trader.strategy_ids() == [StrategyId("VolatilityMarketMaker-000")]

    def test_setting_instance_id(self, monkeypatch, event_loop_for_setup):
        # Arrange
        loop = event_loop_for_setup

        monkeypatch.setenv("BINANCE_FUTURES_API_KEY", "SOME_API_KEY")
        monkeypatch.setenv("BINANCE_FUTURES_API_SECRET", "SOME_API_SECRET")

        config = TradingNodeConfig.parse(RAW_CONFIG)

        # Act
        node = TradingNode(config=config, loop=loop)
        assert len(node.kernel.instance_id.value) == 36


class TestTradingNodeOperation:
    def teardown(self):
        ensure_all_tasks_completed()

    def test_get_event_loop_returns_a_loop(self, event_loop_for_setup):
        # Arrange
        loop = event_loop_for_setup

        config = TradingNodeConfig(logging=LoggingConfig(bypass_logging=True))
        node = TradingNode(config=config, loop=loop)

        # Act
        loop = node.get_event_loop()

        # Assert
        assert isinstance(loop, asyncio.AbstractEventLoop)
        assert loop == node.kernel.loop

    def test_build_called_twice_raises_runtime_error(self):
        # Arrange
        config = TradingNodeConfig(logging=LoggingConfig(bypass_logging=True))
        node = TradingNode(config=config)
        node.build()

        # Act
        with pytest.raises(RuntimeError):
            node.build()

    @pytest.mark.asyncio
    async def test_run_when_not_built_raises_runtime_error(self):
        # Arrange, Act, Assert
        loop = asyncio.get_running_loop()

        config = TradingNodeConfig(
            logging=LoggingConfig(bypass_logging=True),
            data_clients={
                "BINANCE": BinanceDataClientConfig(),
            },
            exec_clients={
                "BINANCE": BinanceExecClientConfig(),
            },
        )
        node = TradingNode(config=config, loop=loop)

        with pytest.raises(RuntimeError):
            await node.run_async()

    @pytest.mark.asyncio
    async def test_run_and_stop_with_client_factories(self, monkeypatch):
        # Arrange
        loop = asyncio.get_running_loop()
        monkeypatch.setenv("BINANCE_API_KEY", "SOME_API_KEY")
        monkeypatch.setenv("BINANCE_API_SECRET", "SOME_API_SECRET")

        config = TradingNodeConfig(
            logging=LoggingConfig(bypass_logging=True),
            data_clients={
                "BINANCE": BinanceDataClientConfig(),
            },
            exec_clients={
                "BINANCE": BinanceExecClientConfig(),
            },
            timeout_disconnection=1.0,  # Short timeout for testing
            timeout_post_stop=1.0,  # Short timeout for testing
        )
        node = TradingNode(config=config, loop=loop)

        node.add_data_client_factory("BINANCE", BinanceLiveDataClientFactory)
        node.add_exec_client_factory("BINANCE", BinanceLiveExecClientFactory)
        node.build()

        # Act, Assert
        node.run()
        await asyncio.sleep(2.0)
        await node.stop_async()

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`TestTradingNodeConfiguration`**: Class defined in this file
- **`TestTradingNodeOperation`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Classs**: `TestTradingNodeConfiguration`, `TestTradingNodeOperation`
**Imports**: `asyncio`, `msgspec`, `nautilus_trader.adapters.binance.config`, `nautilus_trader.adapters.binance.factories`, `nautilus_trader.config`, `nautilus_trader.live.node`, `nautilus_trader.model.identifiers`, `nautilus_trader.test_kit.functions`, `pytest`

## Related Files

This file is located in `tests/integration_tests/live/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/live/test_live_node.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.242902Z*
