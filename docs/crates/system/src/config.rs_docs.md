# Documentation: config.rs

## File Metadata

- **Path**: `crates/system/src/config.rs`
- **Size**: 8,022 bytes
- **Lines**: 218
- **Language**: Rust

## Original Source

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
//  https://nautechsystems.io
//
//  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
//  You may not use this file except in compliance with the License.
//  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
// -------------------------------------------------------------------------------------------------

use std::{fmt::Debug, time::Duration};

use nautilus_common::{
    cache::CacheConfig, enums::Environment, logging::logger::LoggerConfig,
    msgbus::database::MessageBusConfig,
};
use nautilus_core::UUID4;
use nautilus_data::engine::config::DataEngineConfig;
use nautilus_execution::engine::config::ExecutionEngineConfig;
use nautilus_model::identifiers::TraderId;
use nautilus_persistence::config::StreamingConfig;
use nautilus_portfolio::config::PortfolioConfig;
use nautilus_risk::engine::config::RiskEngineConfig;

/// Configuration trait for a `NautilusKernel` core system instance.
pub trait NautilusKernelConfig: Debug {
    /// Returns the kernel environment context.
    fn environment(&self) -> Environment;
    /// Returns the trader ID for the node.
    fn trader_id(&self) -> TraderId;
    /// Returns if trading strategy state should be loaded from the database on start.
    fn load_state(&self) -> bool;
    /// Returns if trading strategy state should be saved to the database on stop.
    fn save_state(&self) -> bool;
    /// Returns the logging configuration for the kernel.
    fn logging(&self) -> LoggerConfig;
    /// Returns the unique instance identifier for the kernel.
    fn instance_id(&self) -> Option<UUID4>;
    /// Returns the timeout for all clients to connect and initialize.
    fn timeout_connection(&self) -> Duration;
    /// Returns the timeout for execution state to reconcile.
    fn timeout_reconciliation(&self) -> Duration;
    /// Returns the timeout for portfolio to initialize margins and unrealized pnls.
    fn timeout_portfolio(&self) -> Duration;
    /// Returns the timeout for all engine clients to disconnect.
    fn timeout_disconnection(&self) -> Duration;
    /// Returns the timeout after stopping the node to await residual events before final shutdown.
    fn delay_post_stop(&self) -> Duration;
    /// Returns the timeout to await pending tasks cancellation during shutdown.
    fn timeout_shutdown(&self) -> Duration;
    /// Returns the cache configuration.
    fn cache(&self) -> Option<CacheConfig>;
    /// Returns the message bus configuration.
    fn msgbus(&self) -> Option<MessageBusConfig>;
    /// Returns the data engine configuration.
    fn data_engine(&self) -> Option<DataEngineConfig>;
    /// Returns the risk engine configuration.
    fn risk_engine(&self) -> Option<RiskEngineConfig>;
    /// Returns the execution engine configuration.
    fn exec_engine(&self) -> Option<ExecutionEngineConfig>;
    /// Returns the portfolio configuration.
    fn portfolio(&self) -> Option<PortfolioConfig>;
    /// Returns the configuration for streaming to feather files.
    fn streaming(&self) -> Option<StreamingConfig>;
}

/// Basic implementation of `NautilusKernelConfig` for builder and testing.
#[derive(Debug, Clone)]
pub struct KernelConfig {
    /// The kernel environment context.
    pub environment: Environment,
    /// The trader ID for the node (must be a name and ID tag separated by a hyphen).
    pub trader_id: TraderId,
    /// If trading strategy state should be loaded from the database on start.
    pub load_state: bool,
    /// If trading strategy state should be saved to the database on stop.
    pub save_state: bool,
    /// The logging configuration for the kernel.
    pub logging: LoggerConfig,
    /// The unique instance identifier for the kernel
    pub instance_id: Option<UUID4>,
    /// The timeout for all clients to connect and initialize.
    pub timeout_connection: Duration,
    /// The timeout for execution state to reconcile.
    pub timeout_reconciliation: Duration,
    /// The timeout for portfolio to initialize margins and unrealized pnls.
    pub timeout_portfolio: Duration,
    /// The timeout for all engine clients to disconnect.
    pub timeout_disconnection: Duration,
    /// The delay after stopping the node to await residual events before final shutdown.
    pub delay_post_stop: Duration,
    /// The delay to await pending tasks cancellation during shutdown.
    pub timeout_shutdown: Duration,
    /// The cache configuration.
    pub cache: Option<CacheConfig>,
    /// The message bus configuration.
    pub msgbus: Option<MessageBusConfig>,
    /// The data engine configuration.
    pub data_engine: Option<DataEngineConfig>,
    /// The risk engine configuration.
    pub risk_engine: Option<RiskEngineConfig>,
    /// The execution engine configuration.
    pub exec_engine: Option<ExecutionEngineConfig>,
    /// The portfolio configuration.
    pub portfolio: Option<PortfolioConfig>,
    /// The configuration for streaming to feather files.
    pub streaming: Option<StreamingConfig>,
}

impl NautilusKernelConfig for KernelConfig {
    fn environment(&self) -> Environment {
        self.environment
    }

    fn trader_id(&self) -> TraderId {
        self.trader_id
    }

    fn load_state(&self) -> bool {
        self.load_state
    }

    fn save_state(&self) -> bool {
        self.save_state
    }

    fn logging(&self) -> LoggerConfig {
        self.logging.clone()
    }

    fn instance_id(&self) -> Option<UUID4> {
        self.instance_id
    }

    fn timeout_connection(&self) -> Duration {
        self.timeout_connection
    }

    fn timeout_reconciliation(&self) -> Duration {
        self.timeout_reconciliation
    }

    fn timeout_portfolio(&self) -> Duration {
        self.timeout_portfolio
    }

    fn timeout_disconnection(&self) -> Duration {
        self.timeout_disconnection
    }

    fn delay_post_stop(&self) -> Duration {
        self.delay_post_stop
    }

    fn timeout_shutdown(&self) -> Duration {
        self.timeout_shutdown
    }

    fn cache(&self) -> Option<CacheConfig> {
        self.cache.clone()
    }

    fn msgbus(&self) -> Option<MessageBusConfig> {
        self.msgbus.clone()
    }

    fn data_engine(&self) -> Option<DataEngineConfig> {
        self.data_engine.clone()
    }

    fn risk_engine(&self) -> Option<RiskEngineConfig> {
        self.risk_engine.clone()
    }

    fn exec_engine(&self) -> Option<ExecutionEngineConfig> {
        self.exec_engine.clone()
    }

    fn portfolio(&self) -> Option<PortfolioConfig> {
        self.portfolio.clone()
    }

    fn streaming(&self) -> Option<StreamingConfig> {
        self.streaming.clone()
    }
}

impl Default for KernelConfig {
    fn default() -> Self {
        Self {
            environment: Environment::Backtest,
            trader_id: TraderId::default(),
            load_state: false,
            save_state: false,
            logging: LoggerConfig::default(),
            instance_id: None,
            timeout_connection: Duration::from_secs(60),
            timeout_reconciliation: Duration::from_secs(30),
            timeout_portfolio: Duration::from_secs(10),
            timeout_disconnection: Duration::from_secs(10),
            delay_post_stop: Duration::from_secs(10),
            timeout_shutdown: Duration::from_secs(5),
            cache: None,
            msgbus: None,
            data_engine: None,
            risk_engine: None,
            exec_engine: None,
            portfolio: None,
            streaming: None,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 39 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`environment()`**: Function defined in this file
- **`trader_id()`**: Function defined in this file
- **`load_state()`**: Function defined in this file
- **`save_state()`**: Function defined in this file
- **`logging()`**: Function defined in this file
- **`instance_id()`**: Function defined in this file
- **`timeout_connection()`**: Function defined in this file
- **`timeout_reconciliation()`**: Function defined in this file
- **`timeout_portfolio()`**: Function defined in this file
- **`timeout_disconnection()`**: Function defined in this file
- **`delay_post_stop()`**: Function defined in this file
- **`timeout_shutdown()`**: Function defined in this file
- **`cache()`**: Function defined in this file
- **`msgbus()`**: Function defined in this file
- **`data_engine()`**: Function defined in this file
- **`risk_engine()`**: Function defined in this file
- **`exec_engine()`**: Function defined in this file
- **`portfolio()`**: Function defined in this file
- **`streaming()`**: Function defined in this file
- **`environment()`**: Function defined in this file

*...and 19 more functions*

### Classes
- **`KernelConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 24


**Functions**: `cache`, `data_engine`, `default`, `delay_post_stop`, `environment`, `exec_engine`, `instance_id`, `load_state`, `logging`, `msgbus`, `portfolio`, `risk_engine`, `save_state`, `streaming`, `timeout_connection`, `timeout_disconnection`, `timeout_portfolio`, `timeout_reconciliation`, `timeout_shutdown`, `trader_id`
**Impls**: `Default`, `NautilusKernelConfig`
**Structs**: `KernelConfig`
**Traits**: `NautilusKernelConfig`, `for`

## Related Files

This file is located in `crates/system/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.158386Z*
