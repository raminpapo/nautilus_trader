# Documentation: `crates/core/benches/time.rs`
**Generated:** 2025-11-15T19:40:01.863478Z
**File Size:** 1478 bytes
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

- **Path:** `crates/core/benches/time.rs`
- **Size:** 1,478 bytes
- **Lines:** 34
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

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

use criterion::{Criterion, criterion_group, criterion_main};
use nautilus_core::time::{duration_since_unix_epoch, nanos_since_unix_epoch};

// Using `SystemTime` under the hood
fn bench_system_time(c: &mut Criterion) {
    c.bench_function("duration_since_unix_epoch", |b| {
        b.iter(duration_since_unix_epoch);
    });
}

// Using libc `clock_gettime` syscall
fn bench_rdtscp(c: &mut Criterion) {
    c.bench_function("nanos_since_unix_epoch", |b| {
        b.iter(nanos_since_unix_epoch);
    });
}

criterion_group!(benches, bench_system_time, bench_rdtscp);
criterion_main!(benches);
```


---

## Overview

This file is located at `crates/core/benches/time.rs` within the repository.

**Functions defined:** bench_system_time, bench_rdtscp


---

## Detailed Analysis

### Functions

#### `bench_system_time(c: &mut Criterion)`


#### `bench_rdtscp(c: &mut Criterion)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/benches`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


