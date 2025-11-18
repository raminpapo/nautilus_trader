# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/config/__init__.py`
- **Size**: 6,635 bytes
- **Lines**: 152
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
"""
The `config` subpackage groups all configuration classes and factories.

All configurations inherit from :class:`NautilusConfig` which in turn inherits from :class:`msgspec.Struct`.

"""

from nautilus_trader.backtest.config import BacktestDataConfig
from nautilus_trader.backtest.config import BacktestEngineConfig
from nautilus_trader.backtest.config import BacktestRunConfig
from nautilus_trader.backtest.config import BacktestVenueConfig
from nautilus_trader.backtest.config import FeeModelFactory
from nautilus_trader.backtest.config import FillModelConfig
from nautilus_trader.backtest.config import FillModelFactory
from nautilus_trader.backtest.config import FixedFeeModelConfig
from nautilus_trader.backtest.config import FXRolloverInterestConfig
from nautilus_trader.backtest.config import ImportableFeeModelConfig
from nautilus_trader.backtest.config import ImportableFillModelConfig
from nautilus_trader.backtest.config import ImportableLatencyModelConfig
from nautilus_trader.backtest.config import LatencyModelConfig
from nautilus_trader.backtest.config import LatencyModelFactory
from nautilus_trader.backtest.config import MakerTakerFeeModelConfig
from nautilus_trader.backtest.config import PerContractFeeModelConfig
from nautilus_trader.backtest.config import SimulationModuleConfig
from nautilus_trader.cache.config import CacheConfig
from nautilus_trader.common.config import ActorConfig
from nautilus_trader.common.config import ActorFactory
from nautilus_trader.common.config import DatabaseConfig
from nautilus_trader.common.config import ImportableActorConfig
from nautilus_trader.common.config import ImportableConfig
from nautilus_trader.common.config import InstrumentProviderConfig
from nautilus_trader.common.config import InvalidConfiguration
from nautilus_trader.common.config import LoggingConfig
from nautilus_trader.common.config import MessageBusConfig
from nautilus_trader.common.config import NautilusConfig
from nautilus_trader.common.config import NonNegativeFloat
from nautilus_trader.common.config import NonNegativeInt
from nautilus_trader.common.config import OrderEmulatorConfig
from nautilus_trader.common.config import PositiveFloat
from nautilus_trader.common.config import PositiveInt
from nautilus_trader.common.config import msgspec_decoding_hook
from nautilus_trader.common.config import msgspec_encoding_hook
from nautilus_trader.common.config import register_config_decoding
from nautilus_trader.common.config import register_config_encoding
from nautilus_trader.common.config import resolve_config_path
from nautilus_trader.common.config import resolve_path
from nautilus_trader.common.config import tokenize_config
from nautilus_trader.data.config import DataEngineConfig
from nautilus_trader.execution.config import ExecAlgorithmConfig
from nautilus_trader.execution.config import ExecAlgorithmFactory
from nautilus_trader.execution.config import ExecEngineConfig
from nautilus_trader.execution.config import ImportableExecAlgorithmConfig
from nautilus_trader.live.config import ControllerConfig
from nautilus_trader.live.config import ControllerFactory
from nautilus_trader.live.config import ImportableControllerConfig
from nautilus_trader.live.config import LiveDataClientConfig
from nautilus_trader.live.config import LiveDataEngineConfig
from nautilus_trader.live.config import LiveExecClientConfig
from nautilus_trader.live.config import LiveExecEngineConfig
from nautilus_trader.live.config import LiveRiskEngineConfig
from nautilus_trader.live.config import RoutingConfig
from nautilus_trader.live.config import TradingNodeConfig
from nautilus_trader.persistence.config import DataCatalogConfig
from nautilus_trader.persistence.config import StreamingConfig
from nautilus_trader.portfolio.config import PortfolioConfig
from nautilus_trader.risk.config import RiskEngineConfig
from nautilus_trader.system.config import NautilusKernelConfig
from nautilus_trader.trading.config import ImportableStrategyConfig
from nautilus_trader.trading.config import StrategyConfig
from nautilus_trader.trading.config import StrategyFactory


__all__ = [
    "ActorConfig",
    "ActorFactory",
    "BacktestDataConfig",
    "BacktestEngineConfig",
    "BacktestRunConfig",
    "BacktestVenueConfig",
    "CacheConfig",
    "ControllerConfig",
    "ControllerFactory",
    "DataCatalogConfig",
    "DataEngineConfig",
    "DatabaseConfig",
    "ExecAlgorithmConfig",
    "ExecAlgorithmFactory",
    "ExecEngineConfig",
    "FXRolloverInterestConfig",
    "FeeModelFactory",
    "FillModelConfig",
    "FillModelFactory",
    "FixedFeeModelConfig",
    "ImportableActorConfig",
    "ImportableConfig",
    "ImportableControllerConfig",
    "ImportableExecAlgorithmConfig",
    "ImportableFeeModelConfig",
    "ImportableFillModelConfig",
    "ImportableLatencyModelConfig",
    "ImportableStrategyConfig",
    "InstrumentProviderConfig",
    "InvalidConfiguration",
    "LatencyModelConfig",
    "LatencyModelFactory",
    "LiveDataClientConfig",
    "LiveDataEngineConfig",
    "LiveExecClientConfig",
    "LiveExecEngineConfig",
    "LiveRiskEngineConfig",
    "LoggingConfig",
    "MakerTakerFeeModelConfig",
    "MessageBusConfig",
    "NautilusConfig",
    "NautilusKernelConfig",
    "NonNegativeFloat",
    "NonNegativeInt",
    "OrderEmulatorConfig",
    "PerContractFeeModelConfig",
    "PortfolioConfig",
    "PositiveFloat",
    "PositiveInt",
    "RiskEngineConfig",
    "RoutingConfig",
    "SimulationModuleConfig",
    "StrategyConfig",
    "StrategyFactory",
    "StreamingConfig",
    "TradingNodeConfig",
    "msgspec_decoding_hook",
    "msgspec_encoding_hook",
    "register_config_decoding",
    "register_config_encoding",
    "resolve_config_path",
    "resolve_path",
    "tokenize_config",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Imports**: `nautilus_trader.backtest.config`, `nautilus_trader.cache.config`, `nautilus_trader.common.config`, `nautilus_trader.data.config`, `nautilus_trader.execution.config`, `nautilus_trader.live.config`, `nautilus_trader.persistence.config`, `nautilus_trader.portfolio.config`, `nautilus_trader.risk.config`, `nautilus_trader.system.config`, `nautilus_trader.trading.config`

## Related Files

This file is located in `nautilus_trader/config/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.270713Z*
