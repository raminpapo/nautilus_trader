# Documentation: `crates/network/src/logging.rs`
**Generated:** 2025-11-15T19:40:03.214711Z
**File Size:** 1348 bytes
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

- **Path:** `crates/network/src/logging.rs`
- **Size:** 1,348 bytes
- **Lines:** 29
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

/// Logs that a task has started using `tracing::debug!`.
pub fn log_task_started(task_name: &str) {
    tracing::debug!("Started task '{task_name}'");
}

/// Logs that a task has stopped using `tracing::debug!`.
pub fn log_task_stopped(task_name: &str) {
    tracing::debug!("Stopped task '{task_name}'");
}

/// Logs that a task was aborted using `tracing::debug!`.
pub fn log_task_aborted(task_name: &str) {
    tracing::debug!("Aborted task '{task_name}'");
}
```


---

## Overview

This file is located at `crates/network/src/logging.rs` within the repository.

**Functions defined:** log_task_started, log_task_stopped, log_task_aborted


---

## Detailed Analysis

### Functions

#### `log_task_started(task_name: &str)`


#### `log_task_stopped(task_name: &str)`


#### `log_task_aborted(task_name: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/network/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


