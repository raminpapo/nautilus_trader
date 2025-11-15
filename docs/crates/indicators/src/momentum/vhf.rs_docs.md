# Documentation: `crates/indicators/src/momentum/vhf.rs`
**Generated:** 2025-11-15T19:40:02.202673Z
**File Size:** 6669 bytes
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

- **Path:** `crates/indicators/src/momentum/vhf.rs`
- **Size:** 6,669 bytes
- **Lines:** 219
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
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

use std::fmt::Display;

use arraydeque::{ArrayDeque, Wrapping};
use nautilus_model::data::Bar;

use crate::{
    average::{MovingAverageFactory, MovingAverageType},
    indicator::{Indicator, MovingAverage},
};

const MAX_PERIOD: usize = 1_024;

#[repr(C)]
#[derive(Debug)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.indicators", unsendable)
)]
pub struct VerticalHorizontalFilter {
    pub period: usize,
    pub ma_type: MovingAverageType,
    pub value: f64,
    pub initialized: bool,
    ma: Box<dyn MovingAverage + Send + 'static>,
    has_inputs: bool,
    previous_close: f64,
    prices: ArrayDeque<f64, MAX_PERIOD, Wrapping>,
}

impl Display for VerticalHorizontalFilter {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}({},{})", self.name(), self.period, self.ma_type,)
    }
}

impl Indicator for VerticalHorizontalFilter {
    fn name(&self) -> String {
        stringify!(VerticalHorizontalFilter).to_string()
    }

    fn has_inputs(&self) -> bool {
        self.has_inputs
    }

    fn initialized(&self) -> bool {
        self.initialized
    }

    fn handle_bar(&mut self, bar: &Bar) {
        self.update_raw((&bar.close).into());
    }

    fn reset(&mut self) {
        self.prices.clear();
        self.ma.reset();
        self.previous_close = 0.0;
        self.value = 0.0;
        self.has_inputs = false;
        self.initialized = false;
    }
}

impl VerticalHorizontalFilter {
    /// Creates a new [`VerticalHorizontalFilter`] instance.
    ///
    /// # Panics
    ///
    /// This function panics if:
    /// - `period` is less than or equal to 0.
    /// - `period` exceeds `MAX_PERIOD`.
    #[must_use]
    pub fn new(period: usize, ma_type: Option<MovingAverageType>) -> Self {
        assert!(
            period > 0 && period <= MAX_PERIOD,
            "VerticalHorizontalFilter: period {period} exceeds MAX_PERIOD ({MAX_PERIOD})"
        );

        let ma_kind = ma_type.unwrap_or(MovingAverageType::Simple);

        Self {
            period,
            ma_type: ma_kind,
            value: 0.0,
            previous_close: 0.0,
            ma: MovingAverageFactory::create(ma_kind, period),
            has_inputs: false,
            initialized: false,
            prices: ArrayDeque::new(),
        }
    }

    pub fn update_raw(&mut self, close: f64) {
        if !self.has_inputs {
            self.previous_close = close;
        }

        let _ = self.prices.push_back(close);

        let max_price = self
            .prices
            .iter()
            .copied()
            .fold(f64::NEG_INFINITY, f64::max);

        let min_price = self.prices.iter().copied().fold(f64::INFINITY, f64::min);

        self.ma.update_raw(f64::abs(close - self.previous_close));

        if self.initialized {
            self.value = f64::abs(max_price - min_price) / self.period as f64 / self.ma.value();
        }

        self.previous_close = close;
        self._check_initialized();
    }

    pub fn _check_initialized(&mut self) {
        if !self.initialized {
            self.has_inputs = true;
            if self.ma.initialized() {
                self.initialized = true;
            }
        }
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use nautilus_model::data::Bar;
    use rstest::rstest;

    use crate::{indicator::Indicator, momentum::vhf::VerticalHorizontalFilter, stubs::*};

    #[rstest]
    fn test_dema_initialized(vhf_10: VerticalHorizontalFilter) {
        let display_str = format!("{vhf_10}");
        assert_eq!(display_str, "VerticalHorizontalFilter(10,SIMPLE)");
        assert_eq!(vhf_10.period, 10);
        assert!(!vhf_10.initialized);
        assert!(!vhf_10.has_inputs);
    }

    #[rstest]
    fn test_value_with_one_input(mut vhf_10: VerticalHorizontalFilter) {
        vhf_10.update_raw(1.0);
        assert_eq!(vhf_10.value, 0.0);
    }

    #[rstest]
    fn test_value_with_three_inputs(mut vhf_10: VerticalHorizontalFilter) {
        vhf_10.update_raw(1.0);
        vhf_10.update_raw(2.0);
        vhf_10.update_raw(3.0);
        assert_eq!(vhf_10.value, 0.0);
    }

    #[rstest]
    fn test_value_with_ten_inputs(mut vhf_10: VerticalHorizontalFilter) {
        vhf_10.update_raw(1.00000);
        vhf_10.update_raw(1.00010);
        vhf_10.update_raw(1.00020);
        vhf_10.update_raw(1.00030);
        vhf_10.update_raw(1.00040);
        vhf_10.update_raw(1.00050);
        vhf_10.update_raw(1.00040);
        vhf_10.update_raw(1.00030);
        vhf_10.update_raw(1.00020);
        vhf_10.update_raw(1.00010);
        vhf_10.update_raw(1.00000);
        assert_eq!(vhf_10.value, 0.5);
    }

    #[rstest]
    fn test_initialized_with_required_input(mut vhf_10: VerticalHorizontalFilter) {
        for i in 1..10 {
            vhf_10.update_raw(f64::from(i));
        }
        assert!(!vhf_10.initialized);
        vhf_10.update_raw(10.0);
        assert!(vhf_10.initialized);
    }

    #[rstest]
    fn test_handle_bar(mut vhf_10: VerticalHorizontalFilter, bar_ethusdt_binance_minute_bid: Bar) {
        vhf_10.handle_bar(&bar_ethusdt_binance_minute_bid);
        assert_eq!(vhf_10.value, 0.0);
        assert!(vhf_10.has_inputs);
        assert!(!vhf_10.initialized);
    }

    #[rstest]
    fn test_reset(mut vhf_10: VerticalHorizontalFilter) {
        vhf_10.update_raw(1.0);
        assert_eq!(vhf_10.prices.len(), 1);
        vhf_10.reset();
        assert_eq!(vhf_10.value, 0.0);
        assert_eq!(vhf_10.prices.len(), 0);
        assert!(!vhf_10.has_inputs);
        assert!(!vhf_10.initialized);
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/momentum/vhf.rs` within the repository.

**Classes defined:** VerticalHorizontalFilter, Display, Indicator, VerticalHorizontalFilter

**Functions defined:** fmt, name, has_inputs, initialized, handle_bar, reset, new, update_raw, _check_initialized, test_dema_initialized and 6 more


---

## Detailed Analysis

### Classes

#### `VerticalHorizontalFilter`

**Type:** struct


#### `Display`

**Type:** impl


#### `Indicator`

**Type:** impl


#### `VerticalHorizontalFilter`

**Type:** impl


### Functions

#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `name(&self)`


#### `has_inputs(&self)`


#### `initialized(&self)`


#### `handle_bar(&mut self, bar: &Bar)`


#### `reset(&mut self)`


#### `new(period: usize, ma_type: Option<MovingAverageType>)`


#### `update_raw(&mut self, close: f64)`


#### `_check_initialized(&mut self)`


#### `test_dema_initialized(vhf_10: VerticalHorizontalFilter)`


#### `test_value_with_one_input(mut vhf_10: VerticalHorizontalFilter)`


#### `test_value_with_three_inputs(mut vhf_10: VerticalHorizontalFilter)`


#### `test_value_with_ten_inputs(mut vhf_10: VerticalHorizontalFilter)`


#### `test_initialized_with_required_input(mut vhf_10: VerticalHorizontalFilter)`


#### `test_handle_bar(mut vhf_10: VerticalHorizontalFilter, bar_ethusdt_binance_minute_bid: Bar)`


#### `test_reset(mut vhf_10: VerticalHorizontalFilter)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src/momentum`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


