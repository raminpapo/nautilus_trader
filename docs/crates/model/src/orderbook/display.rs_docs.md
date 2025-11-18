# Documentation: display.rs

## File Metadata

- **Path**: `crates/model/src/orderbook/display.rs`
- **Size**: 8,222 bytes
- **Lines**: 232
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

//! Functions related to order book display.

use rust_decimal::Decimal;
use tabled::{Table, Tabled, settings::Style};

use super::{BookPrice, level::BookLevel, own::OwnBookLevel};
use crate::{
    enums::OrderSideSpecified,
    orderbook::{OrderBook, own::OwnOrderBook},
};

#[derive(Tabled)]
struct BookLevelDisplay {
    bids: String,
    price: String,
    asks: String,
}

/// Return a [`String`] representation of the order book in a human-readable table format.
#[must_use]
pub(crate) fn pprint_book(
    order_book: &OrderBook,
    num_levels: usize,
    group_size: Option<Decimal>,
) -> String {
    let data: Vec<BookLevelDisplay> = if let Some(group_size) = group_size {
        let bid_quantities = order_book.group_bids(group_size, Some(num_levels));
        let ask_quantities = order_book.group_asks(group_size, Some(num_levels));

        // Use the precision of the group_size for consistent formatting
        let precision = group_size.scale();

        let mut data = Vec::new();

        // Add ask levels (highest to lowest)
        for (price, qty) in ask_quantities.iter().rev() {
            data.push(BookLevelDisplay {
                bids: String::new(),
                price: format!("{price:.precision$}", precision = precision as usize),
                asks: qty.to_string(),
            });
        }

        // Add bid levels (highest to lowest)
        for (price, qty) in &bid_quantities {
            data.push(BookLevelDisplay {
                bids: qty.to_string(),
                price: format!("{price:.precision$}", precision = precision as usize),
                asks: String::new(),
            });
        }

        data
    } else {
        let ask_levels: Vec<(&BookPrice, &BookLevel)> = order_book
            .asks
            .levels
            .iter()
            .take(num_levels)
            .rev()
            .collect();
        let bid_levels: Vec<(&BookPrice, &BookLevel)> =
            order_book.bids.levels.iter().take(num_levels).collect();
        let levels: Vec<(&BookPrice, &BookLevel)> =
            ask_levels.into_iter().chain(bid_levels).collect();

        levels
            .iter()
            .map(|(book_price, level)| {
                let is_bid_level = book_price.side == OrderSideSpecified::Buy;
                let is_ask_level = book_price.side == OrderSideSpecified::Sell;

                let bid_sizes: Vec<String> = level
                    .orders
                    .iter()
                    .filter(|_| is_bid_level)
                    .map(|order| format!("{}", order.1.size))
                    .collect();

                let ask_sizes: Vec<String> = level
                    .orders
                    .iter()
                    .filter(|_| is_ask_level)
                    .map(|order| format!("{}", order.1.size))
                    .collect();

                BookLevelDisplay {
                    bids: if bid_sizes.is_empty() {
                        String::new()
                    } else {
                        format!("[{}]", bid_sizes.join(", "))
                    },
                    price: format!("{}", level.price),
                    asks: if ask_sizes.is_empty() {
                        String::new()
                    } else {
                        format!("[{}]", ask_sizes.join(", "))
                    },
                }
            })
            .collect()
    };

    let table = Table::new(data).with(Style::rounded()).to_string();

    let header = format!(
        "bid_levels: {}\nask_levels: {}\nsequence: {}\nupdate_count: {}\nts_last: {}",
        order_book.bids.levels.len(),
        order_book.asks.levels.len(),
        order_book.sequence,
        order_book.update_count,
        order_book.ts_last,
    );

    format!("{header}\n{table}")
}

/// Return a [`String`] representation of the own order book in a human-readable table format.
#[must_use]
pub(crate) fn pprint_own_book(
    own_order_book: &OwnOrderBook,
    num_levels: usize,
    group_size: Option<Decimal>,
) -> String {
    let data: Vec<BookLevelDisplay> = if let Some(group_size) = group_size {
        let bid_quantities =
            own_order_book.bid_quantity(None, Some(num_levels), Some(group_size), None, None);
        let ask_quantities =
            own_order_book.ask_quantity(None, Some(num_levels), Some(group_size), None, None);

        // Use the precision of the group_size for consistent formatting
        let precision = group_size.scale();

        let mut data = Vec::new();

        // Add ask levels (highest to lowest)
        for (price, qty) in ask_quantities.iter().rev() {
            data.push(BookLevelDisplay {
                bids: String::new(),
                price: format!("{price:.precision$}", precision = precision as usize),
                asks: qty.to_string(),
            });
        }

        // Add bid levels (highest to lowest)
        for (price, qty) in &bid_quantities {
            data.push(BookLevelDisplay {
                bids: qty.to_string(),
                price: format!("{price:.precision$}", precision = precision as usize),
                asks: String::new(),
            });
        }

        data
    } else {
        let ask_levels: Vec<(&BookPrice, &OwnBookLevel)> = own_order_book
            .asks
            .levels
            .iter()
            .take(num_levels)
            .rev()
            .collect();
        let bid_levels: Vec<(&BookPrice, &OwnBookLevel)> =
            own_order_book.bids.levels.iter().take(num_levels).collect();
        let levels: Vec<(&BookPrice, &OwnBookLevel)> =
            ask_levels.into_iter().chain(bid_levels).collect();

        levels
            .iter()
            .map(|(book_price, level)| {
                let is_bid_level = book_price.side == OrderSideSpecified::Buy;
                let is_ask_level = book_price.side == OrderSideSpecified::Sell;

                let bid_sizes: Vec<String> = level
                    .orders
                    .iter()
                    .filter(|_| is_bid_level)
                    .map(|order| format!("{}", order.1.size))
                    .collect();

                let ask_sizes: Vec<String> = level
                    .orders
                    .iter()
                    .filter(|_| is_ask_level)
                    .map(|order| format!("{}", order.1.size))
                    .collect();

                BookLevelDisplay {
                    bids: if bid_sizes.is_empty() {
                        String::new()
                    } else {
                        format!("[{}]", bid_sizes.join(", "))
                    },
                    price: format!("{}", level.price),
                    asks: if ask_sizes.is_empty() {
                        String::new()
                    } else {
                        format!("[{}]", ask_sizes.join(", "))
                    },
                }
            })
            .collect()
    };

    let table = Table::new(data).with(Style::rounded()).to_string();

    let header = format!(
        "bid_levels: {}\nask_levels: {}\nupdate_count: {}\nts_last: {}",
        own_order_book.bids.levels.len(),
        own_order_book.asks.levels.len(),
        own_order_book.update_count,
        own_order_book.ts_last,
    );

    format!("{header}\n{table}")
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`pprint_book()`**: Function defined in this file
- **`pprint_own_book()`**: Function defined in this file

### Classes
- **`BookLevelDisplay`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `pprint_book`, `pprint_own_book`
**Structs**: `BookLevelDisplay`

## Related Files

This file is located in `crates/model/src/orderbook/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.756818Z*
