# Documentation: testing.rs

## File Metadata

- **Path**: `crates/common/src/testing.rs`
- **Size**: 3,320 bytes
- **Lines**: 117
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

//! Common test related helper functions.

use std::{
    future::Future,
    thread,
    time::{Duration, Instant},
};

use nautilus_core::UUID4;
use nautilus_model::identifiers::TraderId;

use crate::logging::{
    init_logging,
    logger::{LogGuard, LoggerConfig},
    writer::FileWriterConfig,
};

/// # Errors
///
/// Returns an error if initializing the logger fails.
pub fn init_logger_for_testing(stdout_level: Option<log::LevelFilter>) -> anyhow::Result<LogGuard> {
    let mut config = LoggerConfig::default();
    config.stdout_level = stdout_level.unwrap_or(log::LevelFilter::Trace);
    init_logging(
        TraderId::default(),
        UUID4::new(),
        config,
        FileWriterConfig::default(),
    )
}

/// Repeatedly evaluates a condition with a delay until it becomes true or a timeout occurs.
///
/// # Panics
///
/// This function panics if the timeout duration is exceeded without the condition being met.
///
/// # Examples
///
/// ```
/// use std::time::Duration;
/// use std::thread;
/// use nautilus_common::testing::wait_until;
///
/// let start_time = std::time::Instant::now();
/// let timeout = Duration::from_secs(5);
///
/// wait_until(|| {
///     if start_time.elapsed().as_secs() > 2 {
///         true
///     } else {
///         false
///     }
/// }, timeout);
/// ```
///
/// In the above example, the `wait_until` function will block for at least 2 seconds, as that's how long
/// it takes for the condition to be met. If the condition was not met within 5 seconds, it would panic.
pub fn wait_until<F>(mut condition: F, timeout: Duration)
where
    F: FnMut() -> bool,
{
    let start_time = Instant::now();

    loop {
        if condition() {
            break;
        }

        assert!(
            start_time.elapsed() <= timeout,
            "Timeout waiting for condition"
        );

        thread::sleep(Duration::from_millis(100));
    }
}

/// # Panics
///
/// Panics if the timeout duration is exceeded without the condition being met.
pub async fn wait_until_async<F, Fut>(mut condition: F, timeout: Duration)
where
    F: FnMut() -> Fut,
    Fut: Future<Output = bool>,
{
    let start_time = Instant::now();

    loop {
        if condition().await {
            break;
        }

        assert!(
            start_time.elapsed() <= timeout,
            "Timeout waiting for condition"
        );

        tokio::time::sleep(Duration::from_millis(100)).await;
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`init_logger_for_testing()`**: Function defined in this file
- **`wait_until()`**: Function defined in this file
- **`wait_until_async()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `init_logger_for_testing`, `wait_until`, `wait_until_async`

## Related Files

This file is located in `crates/common/src/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/common/src/testing.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:01.307852Z*
