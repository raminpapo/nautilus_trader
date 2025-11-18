# Documentation: logging.rs

## File Metadata

- **Path**: `crates/network/src/logging.rs`
- **Size**: 1,348 bytes
- **Lines**: 30
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`log_task_started()`**: Function defined in this file
- **`log_task_stopped()`**: Function defined in this file
- **`log_task_aborted()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `log_task_aborted`, `log_task_started`, `log_task_stopped`

## Related Files

This file is located in `crates/network/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.356040Z*
