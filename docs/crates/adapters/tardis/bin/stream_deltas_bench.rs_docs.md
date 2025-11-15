# Documentation: `crates/adapters/tardis/bin/stream_deltas_bench.rs`
**Generated:** 2025-11-15T19:40:01.434245Z
**File Size:** 3463 bytes
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

- **Path:** `crates/adapters/tardis/bin/stream_deltas_bench.rs`
- **Size:** 3,463 bytes
- **Lines:** 98
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

use std::{path::Path, time::Instant};

use nautilus_tardis::csv::stream_deltas;

fn main() {
    let test_data_path = Path::new(
        "tests/test_data/large/tardis_deribit_incremental_book_L2_2020-04-01_BTC-PERPETUAL.csv.gz",
    );

    if !test_data_path.exists() {
        eprintln!("Test data file not found: {test_data_path:?}");
        return;
    }

    println!("Running stream_deltas benchmarks...");
    println!("Test data: {test_data_path:?}");
    println!();

    // Benchmark 1: Small chunks
    println!("Small chunks (100 records per chunk)");
    let start = Instant::now();
    let stream = stream_deltas(
        test_data_path,
        100,  // Small chunk size
        None, // Auto-detect price precision
        None, // Auto-detect size precision
        None, // No instrument filter
        None, // No limit
    )
    .unwrap();
    let count: usize = stream.map(|chunk| chunk.unwrap().len()).sum();
    let duration = start.elapsed();
    println!("Processed {count} records in {duration:?}");
    println!(
        "  Rate: {:.0} records/second",
        count as f64 / duration.as_secs_f64()
    );
    println!();

    // Benchmark 2: Large chunks
    println!("Large chunks (100,000 records per chunk)");
    let start = Instant::now();
    let stream = stream_deltas(
        test_data_path,
        100_000, // Large chunk size
        None,    // Auto-detect price precision
        None,    // Auto-detect size precision
        None,    // No instrument filter
        None,    // No limit
    )
    .unwrap();
    let count: usize = stream.map(|chunk| chunk.unwrap().len()).sum();
    let duration = start.elapsed();
    println!("Processed {count} records in {duration:?}");
    println!(
        "  Rate: {:.0} records/second",
        count as f64 / duration.as_secs_f64()
    );
    println!();

    // Benchmark 3: With fixed precision
    println!("With fixed precision (1,000 records per chunk)");
    let start = Instant::now();
    let stream = stream_deltas(
        test_data_path,
        1_000,   // Medium chunk size
        Some(2), // Fixed price precision
        Some(4), // Fixed size precision
        None,    // No instrument filter
        None,    // No limit
    )
    .unwrap();
    let count: usize = stream.map(|chunk| chunk.unwrap().len()).sum();
    let duration = start.elapsed();
    println!("Processed {count} records in {duration:?}");
    println!(
        "  Rate: {:.0} records/second",
        count as f64 / duration.as_secs_f64()
    );
    println!();

    println!("Benchmarks completed!");
}
```


---

## Overview

This file is located at `crates/adapters/tardis/bin/stream_deltas_bench.rs` within the repository.

**Functions defined:** main


---

## Detailed Analysis

### Functions

#### `main()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/bin`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


