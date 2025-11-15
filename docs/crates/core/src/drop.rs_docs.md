# Documentation: `crates/core/src/drop.rs`
**Generated:** 2025-11-15T19:40:01.881178Z
**File Size:** 1905 bytes
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

- **Path:** `crates/core/src/drop.rs`
- **Size:** 1,905 bytes
- **Lines:** 33
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 1

---

## Source Code

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 Nautech Systems Pty Ltd.
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

//! Explicit, manually-invocable cleanup hook used to break reference cycles before `Drop`.
//!
//! Many long-lived components register callbacks or handlers that retain strong references back to
//! them, creating reference-count cycles that prevent Rust’s automatic destructor (`Drop`) from
//! running.  The `CleanDrop` trait provides an *object-safe* method, `clean_drop`, that can be
//! called explicitly (e.g. during an orderly shutdown) to release such resources.  Implementations
//! should also call `clean_drop` from their `Drop` impl as a final safety net.
//!
//! Design contract:
//! 1. **Idempotent** – multiple calls must be safe.
//! 2. Perform all externally-observable cleanup here (unregister handlers, abort tasks, clear
//!    callbacks, downgrade `Rc`/`Arc` references, etc.).

/// Trait providing an explicit cleanup method that may be invoked prior to `Drop`.
pub trait CleanDrop {
    /// Perform custom cleanup, releasing external resources and breaking strong reference cycles.
    fn clean_drop(&mut self);
}
```


---

## Overview

This file is located at `crates/core/src/drop.rs` within the repository.

**Classes defined:** as

**Functions defined:** clean_drop


---

## Detailed Analysis

### Classes

#### `as`

**Type:** impl


### Functions

#### `clean_drop(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


