# Documentation: macd.rs

## File Metadata

- **Path**: `crates/indicators/src/momentum/macd.rs`
- **Size**: 7,784 bytes
- **Lines**: 260
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

use std::fmt::{Display, Formatter};

use nautilus_model::{
    data::{Bar, QuoteTick, TradeTick},
    enums::PriceType,
};

use crate::{
    average::{MovingAverageFactory, MovingAverageType},
    indicator::{Indicator, MovingAverage},
};

#[repr(C)]
#[derive(Debug)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.indicators", unsendable)
)]
pub struct MovingAverageConvergenceDivergence {
    pub fast_period: usize,
    pub slow_period: usize,
    pub ma_type: MovingAverageType,
    pub count: usize,
    pub price_type: PriceType,
    pub value: f64,
    pub initialized: bool,
    has_inputs: bool,
    fast_ma: Box<dyn MovingAverage + Send + 'static>,
    slow_ma: Box<dyn MovingAverage + Send + 'static>,
}

impl Display for MovingAverageConvergenceDivergence {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{}({},{},{},{})",
            self.name(),
            self.fast_period,
            self.slow_period,
            self.ma_type,
            self.price_type
        )
    }
}

impl Indicator for MovingAverageConvergenceDivergence {
    fn name(&self) -> String {
        stringify!(MovingAverageConvergenceDivergence).to_string()
    }

    fn has_inputs(&self) -> bool {
        self.has_inputs
    }

    fn initialized(&self) -> bool {
        self.initialized
    }

    fn handle_quote(&mut self, quote: &QuoteTick) {
        self.update_raw(quote.extract_price(self.price_type).into());
    }

    fn handle_trade(&mut self, trade: &TradeTick) {
        self.update_raw((&trade.price).into());
    }

    fn handle_bar(&mut self, bar: &Bar) {
        self.update_raw((&bar.close).into());
    }

    fn reset(&mut self) {
        self.value = 0.0;
        self.fast_ma.reset();
        self.slow_ma.reset();
        self.has_inputs = false;
        self.initialized = false;
    }
}

impl MovingAverageConvergenceDivergence {
    /// Creates a new [`MovingAverageConvergenceDivergence`] instance.
    #[must_use]
    pub fn new(
        fast_period: usize,
        slow_period: usize,
        ma_type: Option<MovingAverageType>,
        price_type: Option<PriceType>,
    ) -> Self {
        Self {
            fast_period,
            slow_period,
            ma_type: ma_type.unwrap_or(MovingAverageType::Simple),
            price_type: price_type.unwrap_or(PriceType::Last),
            value: 0.0,
            count: 0,
            initialized: false,
            has_inputs: false,
            fast_ma: MovingAverageFactory::create(
                ma_type.unwrap_or(MovingAverageType::Simple),
                fast_period,
            ),
            slow_ma: MovingAverageFactory::create(
                ma_type.unwrap_or(MovingAverageType::Simple),
                slow_period,
            ),
        }
    }
}

impl MovingAverage for MovingAverageConvergenceDivergence {
    fn value(&self) -> f64 {
        self.value
    }

    fn count(&self) -> usize {
        self.count
    }

    fn update_raw(&mut self, close: f64) {
        self.fast_ma.update_raw(close);
        self.slow_ma.update_raw(close);
        self.value = self.fast_ma.value() - self.slow_ma.value();

        // Initialization logic
        if !self.initialized {
            self.has_inputs = true;
            if self.fast_ma.initialized() && self.slow_ma.initialized() {
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
    use nautilus_model::data::{Bar, QuoteTick, TradeTick};
    use rstest::rstest;

    use crate::{
        indicator::{Indicator, MovingAverage},
        momentum::macd::MovingAverageConvergenceDivergence,
        stubs::*,
        testing::approx_equal,
    };

    #[rstest]
    fn test_macd_initialized(macd_10: MovingAverageConvergenceDivergence) {
        let display_st = format!("{macd_10}");
        assert_eq!(
            display_st,
            "MovingAverageConvergenceDivergence(10,8,SIMPLE,BID)"
        );
        assert_eq!(macd_10.fast_period, 10);
        assert_eq!(macd_10.slow_period, 8);
        assert!(!macd_10.initialized());
        assert!(!macd_10.has_inputs());
    }

    #[rstest]
    fn test_initialized_with_required_input(mut macd_10: MovingAverageConvergenceDivergence) {
        for i in 1..10 {
            macd_10.update_raw(f64::from(i));
        }
        assert!(!macd_10.initialized);
        macd_10.update_raw(10.0);
        assert!(macd_10.initialized);
    }

    #[rstest]
    fn test_value_with_one_input(mut macd_10: MovingAverageConvergenceDivergence) {
        macd_10.update_raw(1.0);
        assert_eq!(macd_10.value, 0.0);
    }

    #[rstest]
    fn test_value_with_three_inputs(mut macd_10: MovingAverageConvergenceDivergence) {
        macd_10.update_raw(1.0);
        macd_10.update_raw(2.0);
        macd_10.update_raw(3.0);
        assert_eq!(macd_10.value, 0.0);
    }

    #[rstest]
    fn test_value_with_ten_inputs(mut macd_10: MovingAverageConvergenceDivergence) {
        macd_10.update_raw(1.00000);
        macd_10.update_raw(1.00010);
        macd_10.update_raw(1.00020);
        macd_10.update_raw(1.00030);
        macd_10.update_raw(1.00040);
        macd_10.update_raw(1.00050);
        macd_10.update_raw(1.00040);
        macd_10.update_raw(1.00030);
        macd_10.update_raw(1.00020);
        macd_10.update_raw(1.00010);
        macd_10.update_raw(1.00000);
        assert!(
            approx_equal(macd_10.value, -2.5e-5),
            "MACD value {:.17e} not within tolerance of –2.5e-5",
            macd_10.value
        );
    }

    #[rstest]
    fn test_handle_quote_tick(
        mut macd_10: MovingAverageConvergenceDivergence,
        stub_quote: QuoteTick,
    ) {
        macd_10.handle_quote(&stub_quote);
        assert_eq!(macd_10.value, 0.0);
    }

    #[rstest]
    fn test_handle_trade_tick(
        mut macd_10: MovingAverageConvergenceDivergence,
        stub_trade: TradeTick,
    ) {
        macd_10.handle_trade(&stub_trade);
        assert_eq!(macd_10.value, 0.0);
    }

    #[rstest]
    fn test_handle_bar(
        mut macd_10: MovingAverageConvergenceDivergence,
        bar_ethusdt_binance_minute_bid: Bar,
    ) {
        macd_10.handle_bar(&bar_ethusdt_binance_minute_bid);
        assert_eq!(macd_10.value, 0.0);
        assert!(!macd_10.initialized);
    }

    #[rstest]
    fn test_reset(mut macd_10: MovingAverageConvergenceDivergence) {
        macd_10.update_raw(1.0);
        macd_10.reset();
        assert_eq!(macd_10.value, 0.0);
        assert_eq!(macd_10.fast_ma.value(), 0.0);
        assert_eq!(macd_10.slow_ma.value(), 0.0);
        assert!(!macd_10.has_inputs);
        assert!(!macd_10.initialized);
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 21 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`has_inputs()`**: Function defined in this file
- **`initialized()`**: Function defined in this file
- **`handle_quote()`**: Function defined in this file
- **`handle_trade()`**: Function defined in this file
- **`handle_bar()`**: Function defined in this file
- **`reset()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`value()`**: Function defined in this file
- **`count()`**: Function defined in this file
- **`update_raw()`**: Function defined in this file
- **`test_macd_initialized()`**: Function defined in this file
- **`test_initialized_with_required_input()`**: Function defined in this file
- **`test_value_with_one_input()`**: Function defined in this file
- **`test_value_with_three_inputs()`**: Function defined in this file
- **`test_value_with_ten_inputs()`**: Function defined in this file
- **`test_handle_quote_tick()`**: Function defined in this file
- **`test_handle_trade_tick()`**: Function defined in this file
- **`test_handle_bar()`**: Function defined in this file

*...and 1 more functions*

### Classes
- **`MovingAverageConvergenceDivergence`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 25


**Functions**: `count`, `fmt`, `handle_bar`, `handle_quote`, `handle_trade`, `has_inputs`, `initialized`, `name`, `new`, `reset`, `test_handle_bar`, `test_handle_quote_tick`, `test_handle_trade_tick`, `test_initialized_with_required_input`, `test_macd_initialized`, `test_reset`, `test_value_with_one_input`, `test_value_with_ten_inputs`, `test_value_with_three_inputs`, `update_raw`, `value`
**Impls**: `Display`, `Indicator`, `MovingAverage`, `MovingAverageConvergenceDivergence`
**Structs**: `MovingAverageConvergenceDivergence`

## Related Files

This file is located in `crates/indicators/src/momentum/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.828416Z*
