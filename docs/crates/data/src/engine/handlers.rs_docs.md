# Documentation: handlers.rs

## File Metadata

- **Path**: `crates/data/src/engine/handlers.rs`
- **Size**: 4,461 bytes
- **Lines**: 139
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

use std::{any::Any, cell::RefCell, rc::Rc};

use nautilus_common::msgbus::handler::MessageHandler;
use nautilus_core::WeakCell;
use nautilus_model::data::{Bar, BarType, QuoteTick, TradeTick};
use ustr::Ustr;

use crate::aggregation::BarAggregator;

/// Message handler for processing quote ticks through bar aggregators.
///
/// This handler receives quote tick messages and forwards them to the underlying
/// bar aggregator for processing. It's used as part of the data engine's message
/// routing infrastructure to build bars from incoming quote data.
#[derive(Debug)]
pub struct BarQuoteHandler {
    aggregator: WeakCell<Box<dyn BarAggregator>>,
    bar_type: BarType,
}

impl BarQuoteHandler {
    pub(crate) fn new(aggregator: Rc<RefCell<Box<dyn BarAggregator>>>, bar_type: BarType) -> Self {
        Self {
            aggregator: WeakCell::from(Rc::downgrade(&aggregator)),
            bar_type,
        }
    }
}

impl MessageHandler for BarQuoteHandler {
    fn id(&self) -> Ustr {
        Ustr::from(&format!("BarQuoteHandler|{}", self.bar_type))
    }

    fn handle(&self, msg: &dyn Any) {
        if let Some(quote) = msg.downcast_ref::<QuoteTick>()
            && let Some(agg) = self.aggregator.upgrade()
        {
            agg.borrow_mut().handle_quote(*quote);
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

/// Message handler for processing trade ticks through bar aggregators.
///
/// This handler receives trade tick messages and forwards them to the underlying
/// bar aggregator for processing. It's used as part of the data engine's message
/// routing infrastructure to build bars from incoming trade data.
#[derive(Debug)]
pub struct BarTradeHandler {
    aggregator: WeakCell<Box<dyn BarAggregator>>,
    bar_type: BarType,
}

impl BarTradeHandler {
    pub(crate) fn new(aggregator: Rc<RefCell<Box<dyn BarAggregator>>>, bar_type: BarType) -> Self {
        Self {
            aggregator: WeakCell::from(Rc::downgrade(&aggregator)),
            bar_type,
        }
    }
}

impl MessageHandler for BarTradeHandler {
    fn id(&self) -> Ustr {
        Ustr::from(&format!("BarTradeHandler|{}", self.bar_type))
    }

    fn handle(&self, msg: &dyn Any) {
        if let Some(trade) = msg.downcast_ref::<TradeTick>()
            && let Some(agg) = self.aggregator.upgrade()
        {
            agg.borrow_mut().handle_trade(*trade);
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

/// Message handler for processing bars through composite bar aggregators.
///
/// This handler receives bar messages and forwards them to the underlying
/// bar aggregator for further processing. It's used for building composite
/// bars from existing bars, such as creating higher timeframe bars from
/// lower timeframe bars.
#[derive(Debug)]
pub struct BarBarHandler {
    aggregator: WeakCell<Box<dyn BarAggregator>>,
    bar_type: BarType,
}

impl BarBarHandler {
    pub(crate) fn new(aggregator: Rc<RefCell<Box<dyn BarAggregator>>>, bar_type: BarType) -> Self {
        Self {
            aggregator: WeakCell::from(Rc::downgrade(&aggregator)),
            bar_type,
        }
    }
}

impl MessageHandler for BarBarHandler {
    fn id(&self) -> Ustr {
        Ustr::from(&format!("BarBarHandler|{}", self.bar_type))
    }

    fn handle(&self, msg: &dyn Any) {
        if let Some(bar) = msg.downcast_ref::<Bar>()
            && let Some(agg) = self.aggregator.upgrade()
        {
            agg.borrow_mut().handle_bar(*bar);
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 12 function(s) and 3 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file

### Classes
- **`BarQuoteHandler`**: Class defined in this file
- **`BarTradeHandler`**: Class defined in this file
- **`BarBarHandler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `as_any`, `handle`, `id`, `new`
**Impls**: `BarBarHandler`, `BarQuoteHandler`, `BarTradeHandler`, `MessageHandler`
**Structs**: `BarBarHandler`, `BarQuoteHandler`, `BarTradeHandler`

## Related Files

This file is located in `crates/data/src/engine/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.522602Z*
