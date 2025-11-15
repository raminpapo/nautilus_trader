# Documentation: `crates/common/src/generators/order_list_id.rs`
**Generated:** 2025-11-15T19:40:01.731349Z
**File Size:** 4590 bytes
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

- **Path:** `crates/common/src/generators/order_list_id.rs`
- **Size:** 4,590 bytes
- **Lines:** 139
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 11

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

use nautilus_core::AtomicTime;
use nautilus_model::identifiers::{OrderListId, StrategyId, TraderId};

use super::get_datetime_tag;

#[repr(C)]
#[derive(Debug)]
pub struct OrderListIdGenerator {
    clock: &'static AtomicTime,
    trader_id: TraderId,
    strategy_id: StrategyId,
    count: usize,
}

impl OrderListIdGenerator {
    /// Creates a new [`OrderListIdGenerator`] instance.
    #[must_use]
    pub const fn new(
        trader_id: TraderId,
        strategy_id: StrategyId,
        initial_count: usize,
        clock: &'static AtomicTime,
    ) -> Self {
        Self {
            clock,
            trader_id,
            strategy_id,
            count: initial_count,
        }
    }

    pub const fn set_count(&mut self, count: usize) {
        self.count = count;
    }

    pub const fn reset(&mut self) {
        self.count = 0;
    }

    #[must_use]
    pub const fn count(&self) -> usize {
        self.count
    }

    pub fn generate(&mut self) -> OrderListId {
        let datetime_tag = get_datetime_tag(self.clock.get_time_ms());
        let trader_tag = self.trader_id.get_tag();
        let strategy_tag = self.strategy_id.get_tag();
        self.count += 1;
        let value = format!(
            "OL-{}-{}-{}-{}",
            datetime_tag, trader_tag, strategy_tag, self.count
        );
        OrderListId::from(value)
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use nautilus_core::time::get_atomic_clock_static;
    use nautilus_model::identifiers::{OrderListId, StrategyId, TraderId};
    use rstest::rstest;

    use crate::generators::order_list_id::OrderListIdGenerator;

    fn get_order_list_id_generator(initial_count: Option<usize>) -> OrderListIdGenerator {
        OrderListIdGenerator::new(
            TraderId::default(),
            StrategyId::default(),
            initial_count.unwrap_or(0),
            get_atomic_clock_static(),
        )
    }

    #[rstest]
    fn test_init() {
        let generator = get_order_list_id_generator(None);
        assert_eq!(generator.count(), 0);
    }

    #[rstest]
    fn test_init_with_initial_count() {
        let generator = get_order_list_id_generator(Some(7));
        assert_eq!(generator.count(), 7);
    }

    #[rstest]
    fn test_generate_order_list_id_from_start() {
        let mut generator = get_order_list_id_generator(None);
        let result1 = generator.generate();
        let result2 = generator.generate();
        let result3 = generator.generate();

        assert_eq!(result1, OrderListId::new("OL-19700101-000000-001-001-1"));
        assert_eq!(result2, OrderListId::new("OL-19700101-000000-001-001-2"));
        assert_eq!(result3, OrderListId::new("OL-19700101-000000-001-001-3"));
    }

    #[rstest]
    fn test_generate_order_list_id_from_initial() {
        let mut generator = get_order_list_id_generator(Some(5));
        let result1 = generator.generate();
        let result2 = generator.generate();
        let result3 = generator.generate();

        assert_eq!(result1, OrderListId::new("OL-19700101-000000-001-001-6"));
        assert_eq!(result2, OrderListId::new("OL-19700101-000000-001-001-7"));
        assert_eq!(result3, OrderListId::new("OL-19700101-000000-001-001-8"));
    }

    #[rstest]
    fn test_reset() {
        let mut generator = get_order_list_id_generator(None);
        generator.generate();
        generator.generate();
        generator.reset();
        let result = generator.generate();

        assert_eq!(result, OrderListId::new("OL-19700101-000000-001-001-1"));
    }
}
```


---

## Overview

This file is located at `crates/common/src/generators/order_list_id.rs` within the repository.

**Classes defined:** OrderListIdGenerator, OrderListIdGenerator

**Functions defined:** new, set_count, reset, count, generate, get_order_list_id_generator, test_init, test_init_with_initial_count, test_generate_order_list_id_from_start, test_generate_order_list_id_from_initial and 1 more


---

## Detailed Analysis

### Classes

#### `OrderListIdGenerator`

**Type:** struct


#### `OrderListIdGenerator`

**Type:** impl


### Functions

#### `new(
        trader_id: TraderId,
        strategy_id: StrategyId,
        initial_count: usize,
        clock: &'static AtomicTime,
    )`


#### `set_count(&mut self, count: usize)`


#### `reset(&mut self)`


#### `count(&self)`


#### `generate(&mut self)`


#### `get_order_list_id_generator(initial_count: Option<usize>)`


#### `test_init()`


#### `test_init_with_initial_count()`


#### `test_generate_order_list_id_from_start()`


#### `test_generate_order_list_id_from_initial()`


#### `test_reset()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/generators`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


