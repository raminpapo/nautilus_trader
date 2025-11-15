# Documentation: `crates/common/src/generators/position_id.rs`
**Generated:** 2025-11-15T19:40:01.732803Z
**File Size:** 5862 bytes
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

- **Path:** `crates/common/src/generators/position_id.rs`
- **Size:** 5,862 bytes
- **Lines:** 153
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 13

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

use std::{cell::RefCell, collections::HashMap, fmt::Debug, rc::Rc};

use nautilus_model::identifiers::{PositionId, StrategyId, TraderId};

use super::get_datetime_tag;
use crate::clock::Clock;

#[repr(C)]
pub struct PositionIdGenerator {
    clock: Rc<RefCell<dyn Clock>>,
    trader_id: TraderId,
    counts: HashMap<StrategyId, usize>,
}

impl Debug for PositionIdGenerator {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct(stringify!(PositionIdGenerator))
            .field("trader_id", &self.trader_id)
            .field("counts", &self.counts)
            .finish()
    }
}

impl PositionIdGenerator {
    /// Creates a new [`PositionIdGenerator`] instance.
    #[must_use]
    pub fn new(trader_id: TraderId, clock: Rc<RefCell<dyn Clock>>) -> Self {
        Self {
            clock,
            trader_id,
            counts: HashMap::new(),
        }
    }

    pub fn set_count(&mut self, count: usize, strategy_id: StrategyId) {
        self.counts.insert(strategy_id, count);
    }

    pub fn reset(&mut self) {
        self.counts.clear();
    }

    #[must_use]
    pub fn count(&self, strategy_id: StrategyId) -> usize {
        *self.counts.get(&strategy_id).unwrap_or(&0)
    }

    pub fn generate(&mut self, strategy_id: StrategyId, flipped: bool) -> PositionId {
        let strategy = strategy_id;
        let next_count = self.count(strategy_id) + 1;
        self.set_count(next_count, strategy_id);
        let datetime_tag = get_datetime_tag(self.clock.borrow().timestamp_ms());
        let trader_tag = self.trader_id.get_tag();
        let strategy_tag = strategy.get_tag();
        let flipped = if flipped { "F" } else { "" };
        let value = format!("P-{datetime_tag}-{trader_tag}-{strategy_tag}-{next_count}{flipped}");
        PositionId::from(value)
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use std::{cell::RefCell, rc::Rc};

    use nautilus_model::identifiers::{PositionId, StrategyId, TraderId};
    use rstest::rstest;

    use crate::{clock::TestClock, generators::position_id::PositionIdGenerator};

    fn get_position_id_generator() -> PositionIdGenerator {
        PositionIdGenerator::new(TraderId::default(), Rc::new(RefCell::new(TestClock::new())))
    }

    #[rstest]
    fn test_generate_position_id_one_strategy() {
        let mut generator = get_position_id_generator();
        let result1 = generator.generate(StrategyId::from("S-001"), false);
        let result2 = generator.generate(StrategyId::from("S-001"), false);

        assert_eq!(result1, PositionId::from("P-19700101-000000-001-001-1"));
        assert_eq!(result2, PositionId::from("P-19700101-000000-001-001-2"));
    }

    #[rstest]
    fn test_generate_position_id_multiple_strategies() {
        let mut generator = get_position_id_generator();
        let result1 = generator.generate(StrategyId::from("S-001"), false);
        let result2 = generator.generate(StrategyId::from("S-002"), false);
        let result3 = generator.generate(StrategyId::from("S-002"), false);

        assert_eq!(result1, PositionId::from("P-19700101-000000-001-001-1"));
        assert_eq!(result2, PositionId::from("P-19700101-000000-001-002-1"));
        assert_eq!(result3, PositionId::from("P-19700101-000000-001-002-2"));
    }

    #[rstest]
    fn test_generate_position_id_with_flipped_appends_correctly() {
        let mut generator = get_position_id_generator();
        let result1 = generator.generate(StrategyId::from("S-001"), false);
        let result2 = generator.generate(StrategyId::from("S-002"), true);
        let result3 = generator.generate(StrategyId::from("S-001"), true);

        assert_eq!(result1, PositionId::from("P-19700101-000000-001-001-1"));
        assert_eq!(result2, PositionId::from("P-19700101-000000-001-002-1F"));
        assert_eq!(result3, PositionId::from("P-19700101-000000-001-001-2F"));
    }

    #[rstest]
    fn test_get_count_when_strategy_id_has_not_been_used() {
        let generator = get_position_id_generator();
        let result = generator.count(StrategyId::from("S-001"));

        assert_eq!(result, 0);
    }

    #[rstest]
    fn set_count_with_valid_strategy() {
        let mut generator = get_position_id_generator();
        generator.set_count(7, StrategyId::from("S-001"));
        let result = generator.count(StrategyId::from("S-001"));

        assert_eq!(result, 7);
    }

    #[rstest]
    fn test_reset() {
        let mut generator = get_position_id_generator();
        generator.generate(StrategyId::from("S-001"), false);
        generator.generate(StrategyId::from("S-001"), false);
        generator.reset();
        let result = generator.generate(StrategyId::from("S-001"), false);

        assert_eq!(result, PositionId::from("P-19700101-000000-001-001-1"));
    }
}
```


---

## Overview

This file is located at `crates/common/src/generators/position_id.rs` within the repository.

**Classes defined:** PositionIdGenerator, Debug, PositionIdGenerator

**Functions defined:** fmt, new, set_count, reset, count, generate, get_position_id_generator, test_generate_position_id_one_strategy, test_generate_position_id_multiple_strategies, test_generate_position_id_with_flipped_appends_correctly and 3 more


---

## Detailed Analysis

### Classes

#### `PositionIdGenerator`

**Type:** struct


#### `Debug`

**Type:** impl


#### `PositionIdGenerator`

**Type:** impl


### Functions

#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `new(trader_id: TraderId, clock: Rc<RefCell<dyn Clock>>)`


#### `set_count(&mut self, count: usize, strategy_id: StrategyId)`


#### `reset(&mut self)`


#### `count(&self, strategy_id: StrategyId)`


#### `generate(&mut self, strategy_id: StrategyId, flipped: bool)`


#### `get_position_id_generator()`


#### `test_generate_position_id_one_strategy()`


#### `test_generate_position_id_multiple_strategies()`


#### `test_generate_position_id_with_flipped_appends_correctly()`


#### `test_get_count_when_strategy_id_has_not_been_used()`


#### `set_count_with_valid_strategy()`


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


