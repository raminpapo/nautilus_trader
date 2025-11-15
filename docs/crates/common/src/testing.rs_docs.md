# Documentation: `crates/common/src/testing.rs`
**Generated:** 2025-11-15T19:40:01.845531Z
**File Size:** 3320 bytes
**Extension:** .rs
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

- **Path:** `crates/common/src/testing.rs`
- **Size:** 3,320 bytes
- **Lines:** 116
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 3

---

## Source Code

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


---

## Overview

This file is located at `crates/common/src/testing.rs` within the repository.

**Functions defined:** init_logger_for_testing, wait_until, wait_until_async


---

## Detailed Analysis

### Functions

#### `init_logger_for_testing(stdout_level: Option<log::LevelFilter>)`


#### `wait_until(mut condition: F, timeout: Duration)`


#### `wait_until_async(mut condition: F, timeout: Duration)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


