# Documentation: `crates/indicators/src/indicator.rs`
**Generated:** 2025-11-15T19:40:02.165703Z
**File Size:** 2777 bytes
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

- **Path:** `crates/indicators/src/indicator.rs`
- **Size:** 2,777 bytes
- **Lines:** 84
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 16

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

//! A common `Indicator` trait.

use std::fmt::Debug;

use nautilus_model::{
    data::{Bar, OrderBookDelta, OrderBookDeltas, OrderBookDepth10, QuoteTick, TradeTick},
    orderbook::OrderBook,
};

const IMPL_ERR: &str = "is not implemented for";

#[allow(unused_variables)]
pub trait Indicator {
    fn name(&self) -> String;

    fn has_inputs(&self) -> bool;

    fn initialized(&self) -> bool;

    fn handle_delta(&mut self, delta: &OrderBookDelta) {
        panic!("`handle_delta` {IMPL_ERR} `{}`", self.name());
    }

    fn handle_deltas(&mut self, deltas: &OrderBookDeltas) {
        panic!("`handle_deltas` {IMPL_ERR} `{}`", self.name());
    }

    fn handle_depth(&mut self, depth: &OrderBookDepth10) {
        panic!("`handle_depth` {IMPL_ERR} `{}`", self.name());
    }

    fn handle_book(&mut self, book: &OrderBook) {
        panic!("`handle_book_mbo` {IMPL_ERR} `{}`", self.name());
    }

    fn handle_quote(&mut self, quote: &QuoteTick) {
        panic!("`handle_quote_tick` {IMPL_ERR} `{}`", self.name());
    }

    fn handle_trade(&mut self, trade: &TradeTick) {
        panic!("`handle_trade_tick` {IMPL_ERR} `{}`", self.name());
    }

    fn handle_bar(&mut self, bar: &Bar) {
        panic!("`handle_bar` {IMPL_ERR} `{}`", self.name());
    }

    fn reset(&mut self);
}

pub trait MovingAverage: Indicator {
    fn value(&self) -> f64;
    fn count(&self) -> usize;
    fn update_raw(&mut self, value: f64);
}

impl Debug for dyn Indicator + Send {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        // Implement custom formatting for the Indicator trait object
        write!(f, "Indicator {{ ... }}")
    }
}

impl Debug for dyn MovingAverage + Send {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        // Implement custom formatting for the Indicator trait object
        write!(f, "MovingAverage()")
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/indicator.rs` within the repository.

**Classes defined:** Debug, Debug

**Functions defined:** name, has_inputs, initialized, handle_delta, handle_deltas, handle_depth, handle_book, handle_quote, handle_trade, handle_bar and 6 more


---

## Detailed Analysis

### Classes

#### `Debug`

**Type:** impl


#### `Debug`

**Type:** impl


### Functions

#### `name(&self)`


#### `has_inputs(&self)`


#### `initialized(&self)`


#### `handle_delta(&mut self, delta: &OrderBookDelta)`


#### `handle_deltas(&mut self, deltas: &OrderBookDeltas)`


#### `handle_depth(&mut self, depth: &OrderBookDepth10)`


#### `handle_book(&mut self, book: &OrderBook)`


#### `handle_quote(&mut self, quote: &QuoteTick)`


#### `handle_trade(&mut self, trade: &TradeTick)`


#### `handle_bar(&mut self, bar: &Bar)`


#### `reset(&mut self)`


#### `value(&self)`


#### `count(&self)`


#### `update_raw(&mut self, value: f64)`


#### `fmt(&self, f: &mut std::fmt::Formatter)`


#### `fmt(&self, f: &mut std::fmt::Formatter)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


