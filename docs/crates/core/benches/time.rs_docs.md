# Documentation: time.rs

## File Metadata

- **Path**: `crates/core/benches/time.rs`
- **Size**: 1,478 bytes
- **Lines**: 35
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`bench_system_time()`**: Function defined in this file
- **`bench_rdtscp()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `bench_rdtscp`, `bench_system_time`

## Related Files

This file is located in `crates/core/benches/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.333664Z*
