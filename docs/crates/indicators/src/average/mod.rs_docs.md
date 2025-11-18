# Documentation: mod.rs

## File Metadata

- **Path**: `crates/indicators/src/average/mod.rs`
- **Size**: 2,799 bytes
- **Lines**: 94
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

//! Moving average type indicators.

pub mod ama;
pub mod dema;
pub mod ema;
pub mod hma;
pub mod lr;
pub mod rma;
pub mod sma;
pub mod vidya;
pub mod vwap;
pub mod wma;

use nautilus_model::enums::PriceType;
use strum::{AsRefStr, Display, EnumIter, EnumString, FromRepr};

use crate::{
    average::{
        dema::DoubleExponentialMovingAverage, ema::ExponentialMovingAverage,
        hma::HullMovingAverage, rma::WilderMovingAverage, sma::SimpleMovingAverage,
    },
    indicator::MovingAverage,
};

#[repr(C)]
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    Hash,
    PartialEq,
    Eq,
    PartialOrd,
    Ord,
    AsRefStr,
    FromRepr,
    EnumIter,
    EnumString,
)]
#[strum(ascii_case_insensitive)]
#[strum(serialize_all = "SCREAMING_SNAKE_CASE")]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(eq, eq_int, module = "nautilus_trader.core.nautilus_pyo3.indicators")
)]
pub enum MovingAverageType {
    Simple,
    Exponential,
    DoubleExponential,
    Wilder,
    Hull,
}

#[derive(Debug)]
pub struct MovingAverageFactory;

impl MovingAverageFactory {
    #[must_use]
    pub fn create(
        moving_average_type: MovingAverageType,
        period: usize,
    ) -> Box<dyn MovingAverage + Send + Sync> {
        let price_type = Some(PriceType::Last);

        match moving_average_type {
            MovingAverageType::Simple => Box::new(SimpleMovingAverage::new(period, price_type)),
            MovingAverageType::Exponential => {
                Box::new(ExponentialMovingAverage::new(period, price_type))
            }
            MovingAverageType::DoubleExponential => {
                Box::new(DoubleExponentialMovingAverage::new(period, price_type))
            }
            MovingAverageType::Wilder => Box::new(WilderMovingAverage::new(period, price_type)),
            MovingAverageType::Hull => Box::new(HullMovingAverage::new(period, price_type)),
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`create()`**: Function defined in this file

### Classes
- **`MovingAverageFactory`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Enums**: `MovingAverageType`
**Functions**: `create`
**Impls**: `MovingAverageFactory`
**Structs**: `MovingAverageFactory`

## Related Files

This file is located in `crates/indicators/src/average/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.772757Z*
