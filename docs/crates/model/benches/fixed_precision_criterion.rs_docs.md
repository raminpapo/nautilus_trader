# Documentation: `crates/model/benches/fixed_precision_criterion.rs`
**Generated:** 2025-11-15T19:40:02.427141Z
**File Size:** 1472 bytes
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

- **Path:** `crates/model/benches/fixed_precision_criterion.rs`
- **Size:** 1,472 bytes
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

use std::hint::black_box;

use criterion::{Criterion, criterion_group};
use nautilus_model::types::fixed::{f64_to_fixed_i64, f64_to_fixed_i128};

pub fn bench_fixed_i64(c: &mut Criterion) {
    c.bench_function("f64_to_fixed_i64", |b| {
        b.iter(|| f64_to_fixed_i64(black_box(-1.0), black_box(1)));
    });
}

pub fn bench_fixed_i128(c: &mut Criterion) {
    c.bench_function("f64_to_fixed_i128", |b| {
        b.iter(|| f64_to_fixed_i128(black_box(-1.0), black_box(1)));
    });
}

criterion_group!(benches, bench_fixed_i64, bench_fixed_i128);
criterion::criterion_main!(benches);
```


---

## Overview

This file is located at `crates/model/benches/fixed_precision_criterion.rs` within the repository.

**Functions defined:** bench_fixed_i64, bench_fixed_i128


---

## Detailed Analysis

### Functions

#### `bench_fixed_i64(c: &mut Criterion)`


#### `bench_fixed_i128(c: &mut Criterion)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/benches`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


