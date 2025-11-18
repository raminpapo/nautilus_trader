# Documentation: sizing.rs

## File Metadata

- **Path**: `crates/risk/src/sizing.rs`
- **Size**: 11,151 bytes
- **Lines**: 338
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

//! Position sizing calculation functions.
use nautilus_model::{
    instruments::{Instrument, InstrumentAny},
    types::{Money, Price, Quantity},
};
use rust_decimal::{
    Decimal,
    prelude::{FromPrimitive, ToPrimitive},
};

/// Calculates the position size based on fixed risk parameters.
///
/// # Panics
///
/// Panics if converting `units` to a decimal fails,
/// or if converting the final size to `f64` fails.
#[must_use]
#[allow(clippy::too_many_arguments)]
pub fn calculate_fixed_risk_position_size(
    instrument: InstrumentAny,
    entry: Price,
    stop_loss: Price,
    equity: Money,
    risk: Decimal,
    commission_rate: Decimal,
    exchange_rate: Decimal,
    hard_limit: Option<Decimal>,
    unit_batch_size: Decimal,
    units: usize,
) -> Quantity {
    if exchange_rate.is_zero() {
        return instrument.make_qty(0.0, None);
    }

    let risk_points = calculate_risk_ticks(entry, stop_loss, &instrument);
    let risk_money = calculate_riskable_money(equity.as_decimal(), risk, commission_rate);

    if risk_points <= Decimal::ZERO {
        return instrument.make_qty(0.0, None);
    }

    let mut position_size =
        ((risk_money / exchange_rate) / risk_points) / instrument.price_increment().as_decimal();

    if let Some(hard_limit) = hard_limit {
        position_size = position_size.min(hard_limit);
    }

    let mut position_size_batched = (position_size
        / Decimal::from_usize(units).expect("Error: Failed to convert units to decimal"))
    .max(Decimal::ZERO);

    if unit_batch_size > Decimal::ZERO {
        position_size_batched = (position_size_batched / unit_batch_size).floor() * unit_batch_size;
    }

    let final_size: Decimal = position_size_batched.min(
        instrument
            .max_quantity()
            .unwrap_or_else(|| instrument.make_qty(0.0, None))
            .as_decimal(),
    );

    Quantity::new(
        final_size
            .to_f64()
            .expect("Error: Decimal to f64 conversion failed"),
        instrument.size_precision(),
    )
}

// Helper functions
fn calculate_risk_ticks(entry: Price, stop_loss: Price, instrument: &InstrumentAny) -> Decimal {
    (entry - stop_loss).as_decimal().abs() / instrument.price_increment().as_decimal()
}

fn calculate_riskable_money(equity: Decimal, risk: Decimal, commission_rate: Decimal) -> Decimal {
    if equity <= Decimal::ZERO {
        return Decimal::ZERO;
    }

    let risk_money = equity * risk;
    let commission = risk_money * commission_rate * Decimal::TWO; // (round turn)

    risk_money - commission
}

#[cfg(test)]
mod tests {
    use nautilus_model::{
        identifiers::Symbol, instruments::stubs::default_fx_ccy, types::Currency,
    };
    use rstest::*;

    use super::*;

    const EXCHANGE_RATE: Decimal = Decimal::ONE;

    #[fixture]
    fn instrument_gbpusd() -> InstrumentAny {
        InstrumentAny::CurrencyPair(default_fx_ccy(Symbol::from_str_unchecked("GBP/USD"), None))
    }

    #[rstest]
    fn test_calculate_with_zero_equity_returns_quantity_zero(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(0.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(1.00100, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 3), // 0.001%
            Decimal::ZERO,
            EXCHANGE_RATE,
            None,
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("0.0"));
    }

    #[rstest]
    fn test_calculate_with_zero_exchange_rate(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(100000.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(1.00100, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 3), // 0.001%
            Decimal::ZERO,
            Decimal::ZERO, // Zero exchange rate
            None,
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("0.0"));
    }

    #[rstest]
    fn test_calculate_with_zero_risk(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(100000.0, instrument_gbpusd.quote_currency());
        let price = Price::new(1.00100, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            price,
            price, // Same price = no risk
            equity,
            Decimal::new(1, 3), // 0.001%
            Decimal::ZERO,
            EXCHANGE_RATE,
            None,
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("0.0"));
    }

    #[rstest]
    fn test_calculate_single_unit_size(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(1_000_000.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(1.00100, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 3), // 0.001%
            Decimal::ZERO,
            EXCHANGE_RATE,
            None,
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("1000000.0"));
    }

    #[rstest]
    fn test_calculate_single_unit_with_exchange_rate(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(1_000_000.0, Currency::USD());
        let entry = Price::new(110.010, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(110.000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 3), // 0.1%
            Decimal::ZERO,
            Decimal::from_f64(0.00909).unwrap(), // 1/110
            None,
            Decimal::from(1),
            1,
        );

        assert_eq!(result, Quantity::from("1000000.0"));
    }

    #[rstest]
    fn test_calculate_single_unit_size_when_risk_too_high(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(100000.0, Currency::USD());
        let entry = Price::new(3.00000, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 2), // 1%
            Decimal::ZERO,
            EXCHANGE_RATE,
            None,
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("0.0"));
    }

    #[rstest]
    fn test_impose_hard_limit(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(1_000_000.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(1.00010, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 2), // 1%
            Decimal::ZERO,
            EXCHANGE_RATE,
            Some(Decimal::from(500000)),
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("500000.0"));
    }

    #[rstest]
    fn test_calculate_multiple_unit_size(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(1_000_000.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(1.00010, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 3), // 0.1%
            Decimal::ZERO,
            EXCHANGE_RATE,
            None,
            Decimal::from(1000),
            3, // 3 units
        );

        assert_eq!(result, Quantity::from("1000000.0"));
    }

    #[rstest]
    fn test_calculate_multiple_unit_size_larger_batches(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(1_000_000.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(1.00087, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(1.00000, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 3), // 0.1%
            Decimal::ZERO,
            EXCHANGE_RATE,
            None,
            Decimal::from(25000),
            4, // 4 units
        );

        assert_eq!(result, Quantity::from("275000.0"));
    }

    #[rstest]
    fn test_calculate_for_gbpusd_with_commission(instrument_gbpusd: InstrumentAny) {
        let equity = Money::new(1_000_000.0, instrument_gbpusd.quote_currency());
        let entry = Price::new(107.703, instrument_gbpusd.price_precision());
        let stop_loss = Price::new(107.403, instrument_gbpusd.price_precision());

        let result = calculate_fixed_risk_position_size(
            instrument_gbpusd,
            entry,
            stop_loss,
            equity,
            Decimal::new(1, 2),                   // 1%
            Decimal::new(2, 4),                   // 0.0002
            Decimal::from_f64(0.009931).unwrap(), // 1/107.403
            None,
            Decimal::from(1000),
            1,
        );

        assert_eq!(result, Quantity::from("1000000.0"));
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 14 function(s).

## Detailed Walkthrough

### Functions
- **`calculate_fixed_risk_position_size()`**: Function defined in this file
- **`calculate_risk_ticks()`**: Function defined in this file
- **`calculate_riskable_money()`**: Function defined in this file
- **`instrument_gbpusd()`**: Function defined in this file
- **`test_calculate_with_zero_equity_returns_quantity_zero()`**: Function defined in this file
- **`test_calculate_with_zero_exchange_rate()`**: Function defined in this file
- **`test_calculate_with_zero_risk()`**: Function defined in this file
- **`test_calculate_single_unit_size()`**: Function defined in this file
- **`test_calculate_single_unit_with_exchange_rate()`**: Function defined in this file
- **`test_calculate_single_unit_size_when_risk_too_high()`**: Function defined in this file
- **`test_impose_hard_limit()`**: Function defined in this file
- **`test_calculate_multiple_unit_size()`**: Function defined in this file
- **`test_calculate_multiple_unit_size_larger_batches()`**: Function defined in this file
- **`test_calculate_for_gbpusd_with_commission()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `calculate_fixed_risk_position_size`, `calculate_risk_ticks`, `calculate_riskable_money`, `instrument_gbpusd`, `test_calculate_for_gbpusd_with_commission`, `test_calculate_multiple_unit_size`, `test_calculate_multiple_unit_size_larger_batches`, `test_calculate_single_unit_size`, `test_calculate_single_unit_size_when_risk_too_high`, `test_calculate_single_unit_with_exchange_rate`, `test_calculate_with_zero_equity_returns_quantity_zero`, `test_calculate_with_zero_exchange_rate`, `test_calculate_with_zero_risk`, `test_impose_hard_limit`

## Related Files

This file is located in `crates/risk/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.670144Z*
