# Documentation: any.rs

## File Metadata

- **Path**: `crates/model/src/events/order/any.rs`
- **Size**: 12,774 bytes
- **Lines**: 290
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

use nautilus_core::UnixNanos;
use serde::{Deserialize, Serialize};
use strum::Display;
use ustr::Ustr;

use super::{OrderEvent, OrderEventType};
use crate::{
    events::{
        OrderAccepted, OrderCancelRejected, OrderCanceled, OrderDenied, OrderEmulated,
        OrderExpired, OrderFilled, OrderInitialized, OrderModifyRejected, OrderPendingCancel,
        OrderPendingUpdate, OrderRejected, OrderReleased, OrderSubmitted, OrderTriggered,
        OrderUpdated,
    },
    identifiers::{AccountId, ClientOrderId, InstrumentId, StrategyId, TraderId, VenueOrderId},
};

/// Wraps an `OrderEvent` allowing polymorphism.
#[allow(clippy::large_enum_variant, reason = "TODO fix")]
#[derive(Clone, PartialEq, Eq, Display, Debug, Serialize, Deserialize)]
pub enum OrderEventAny {
    Initialized(OrderInitialized),
    Denied(OrderDenied),
    Emulated(OrderEmulated),
    Released(OrderReleased),
    Submitted(OrderSubmitted),
    Accepted(OrderAccepted),
    Rejected(OrderRejected),
    Canceled(OrderCanceled),
    Expired(OrderExpired),
    Triggered(OrderTriggered),
    PendingUpdate(OrderPendingUpdate),
    PendingCancel(OrderPendingCancel),
    ModifyRejected(OrderModifyRejected),
    CancelRejected(OrderCancelRejected),
    Updated(OrderUpdated),
    Filled(OrderFilled),
}

impl OrderEventAny {
    #[must_use]
    pub fn into_boxed(self) -> Box<dyn OrderEvent> {
        match self {
            Self::Initialized(event) => Box::new(event),
            Self::Denied(event) => Box::new(event),
            Self::Emulated(event) => Box::new(event),
            Self::Released(event) => Box::new(event),
            Self::Submitted(event) => Box::new(event),
            Self::Accepted(event) => Box::new(event),
            Self::Rejected(event) => Box::new(event),
            Self::Canceled(event) => Box::new(event),
            Self::Expired(event) => Box::new(event),
            Self::Triggered(event) => Box::new(event),
            Self::PendingUpdate(event) => Box::new(event),
            Self::PendingCancel(event) => Box::new(event),
            Self::ModifyRejected(event) => Box::new(event),
            Self::CancelRejected(event) => Box::new(event),
            Self::Updated(event) => Box::new(event),
            Self::Filled(event) => Box::new(event),
        }
    }

    #[must_use]
    pub fn event_type(&self) -> OrderEventType {
        match self {
            Self::Initialized(_) => OrderEventType::Initialized,
            Self::Denied(_) => OrderEventType::Denied,
            Self::Emulated(_) => OrderEventType::Emulated,
            Self::Released(_) => OrderEventType::Released,
            Self::Submitted(_) => OrderEventType::Submitted,
            Self::Accepted(_) => OrderEventType::Accepted,
            Self::Rejected(_) => OrderEventType::Rejected,
            Self::Canceled(_) => OrderEventType::Canceled,
            Self::Expired(_) => OrderEventType::Expired,
            Self::Triggered(_) => OrderEventType::Triggered,
            Self::PendingUpdate(_) => OrderEventType::PendingUpdate,
            Self::PendingCancel(_) => OrderEventType::PendingCancel,
            Self::ModifyRejected(_) => OrderEventType::ModifyRejected,
            Self::CancelRejected(_) => OrderEventType::CancelRejected,
            Self::Updated(_) => OrderEventType::Updated,
            Self::Filled(_) => OrderEventType::Filled,
        }
    }

    #[must_use]
    pub fn trader_id(&self) -> TraderId {
        match self {
            Self::Initialized(event) => event.trader_id,
            Self::Denied(event) => event.trader_id,
            Self::Emulated(event) => event.trader_id,
            Self::Released(event) => event.trader_id,
            Self::Submitted(event) => event.trader_id,
            Self::Accepted(event) => event.trader_id,
            Self::Rejected(event) => event.trader_id,
            Self::Canceled(event) => event.trader_id,
            Self::Expired(event) => event.trader_id,
            Self::Triggered(event) => event.trader_id,
            Self::PendingUpdate(event) => event.trader_id,
            Self::PendingCancel(event) => event.trader_id,
            Self::ModifyRejected(event) => event.trader_id,
            Self::CancelRejected(event) => event.trader_id,
            Self::Updated(event) => event.trader_id,
            Self::Filled(event) => event.trader_id,
        }
    }

    #[must_use]
    pub fn client_order_id(&self) -> ClientOrderId {
        match self {
            Self::Initialized(event) => event.client_order_id,
            Self::Denied(event) => event.client_order_id,
            Self::Emulated(event) => event.client_order_id,
            Self::Released(event) => event.client_order_id,
            Self::Submitted(event) => event.client_order_id,
            Self::Accepted(event) => event.client_order_id,
            Self::Rejected(event) => event.client_order_id,
            Self::Canceled(event) => event.client_order_id,
            Self::Expired(event) => event.client_order_id,
            Self::Triggered(event) => event.client_order_id,
            Self::PendingUpdate(event) => event.client_order_id,
            Self::PendingCancel(event) => event.client_order_id,
            Self::ModifyRejected(event) => event.client_order_id,
            Self::CancelRejected(event) => event.client_order_id,
            Self::Updated(event) => event.client_order_id,
            Self::Filled(event) => event.client_order_id,
        }
    }

    #[must_use]
    pub fn venue_order_id(&self) -> Option<VenueOrderId> {
        match self {
            Self::Initialized(event) => event.venue_order_id(),
            Self::Denied(event) => event.venue_order_id(),
            Self::Emulated(event) => event.venue_order_id(),
            Self::Released(event) => event.venue_order_id(),
            Self::Submitted(event) => event.venue_order_id(),
            Self::Accepted(event) => event.venue_order_id(),
            Self::Rejected(event) => event.venue_order_id(),
            Self::Canceled(event) => event.venue_order_id(),
            Self::Expired(event) => event.venue_order_id(),
            Self::Triggered(event) => event.venue_order_id(),
            Self::PendingUpdate(event) => event.venue_order_id(),
            Self::PendingCancel(event) => event.venue_order_id(),
            Self::ModifyRejected(event) => event.venue_order_id(),
            Self::CancelRejected(event) => event.venue_order_id(),
            Self::Updated(event) => event.venue_order_id(),
            Self::Filled(event) => event.venue_order_id(),
        }
    }

    #[must_use]
    pub fn account_id(&self) -> Option<AccountId> {
        match self {
            Self::Initialized(event) => event.account_id(),
            Self::Denied(event) => event.account_id(),
            Self::Emulated(event) => event.account_id(),
            Self::Released(event) => event.account_id(),
            Self::Submitted(event) => event.account_id(),
            Self::Accepted(event) => event.account_id(),
            Self::Rejected(event) => event.account_id(),
            Self::Canceled(event) => event.account_id(),
            Self::Expired(event) => event.account_id(),
            Self::Triggered(event) => event.account_id(),
            Self::PendingUpdate(event) => event.account_id(),
            Self::PendingCancel(event) => event.account_id(),
            Self::ModifyRejected(event) => event.account_id(),
            Self::CancelRejected(event) => event.account_id(),
            Self::Updated(event) => event.account_id(),
            Self::Filled(event) => event.account_id(),
        }
    }

    #[must_use]
    pub fn instrument_id(&self) -> InstrumentId {
        match self {
            Self::Initialized(event) => event.instrument_id(),
            Self::Denied(event) => event.instrument_id(),
            Self::Emulated(event) => event.instrument_id(),
            Self::Released(event) => event.instrument_id(),
            Self::Submitted(event) => event.instrument_id(),
            Self::Accepted(event) => event.instrument_id(),
            Self::Rejected(event) => event.instrument_id(),
            Self::Canceled(event) => event.instrument_id(),
            Self::Expired(event) => event.instrument_id(),
            Self::Triggered(event) => event.instrument_id(),
            Self::PendingUpdate(event) => event.instrument_id(),
            Self::PendingCancel(event) => event.instrument_id(),
            Self::ModifyRejected(event) => event.instrument_id(),
            Self::CancelRejected(event) => event.instrument_id(),
            Self::Updated(event) => event.instrument_id(),
            Self::Filled(event) => event.instrument_id(),
        }
    }

    #[must_use]
    pub fn strategy_id(&self) -> StrategyId {
        match self {
            Self::Initialized(event) => event.strategy_id,
            Self::Denied(event) => event.strategy_id,
            Self::Emulated(event) => event.strategy_id,
            Self::Released(event) => event.strategy_id,
            Self::Submitted(event) => event.strategy_id,
            Self::Accepted(event) => event.strategy_id,
            Self::Rejected(event) => event.strategy_id,
            Self::Canceled(event) => event.strategy_id,
            Self::Expired(event) => event.strategy_id,
            Self::Triggered(event) => event.strategy_id,
            Self::PendingUpdate(event) => event.strategy_id,
            Self::PendingCancel(event) => event.strategy_id,
            Self::ModifyRejected(event) => event.strategy_id,
            Self::CancelRejected(event) => event.strategy_id,
            Self::Updated(event) => event.strategy_id,
            Self::Filled(event) => event.strategy_id,
        }
    }

    #[must_use]
    pub fn ts_event(&self) -> UnixNanos {
        match self {
            Self::Initialized(event) => event.ts_event,
            Self::Denied(event) => event.ts_event,
            Self::Emulated(event) => event.ts_event,
            Self::Released(event) => event.ts_event,
            Self::Submitted(event) => event.ts_event,
            Self::Accepted(event) => event.ts_event,
            Self::Rejected(event) => event.ts_event,
            Self::Canceled(event) => event.ts_event,
            Self::Expired(event) => event.ts_event,
            Self::Triggered(event) => event.ts_event,
            Self::PendingUpdate(event) => event.ts_event,
            Self::PendingCancel(event) => event.ts_event,
            Self::ModifyRejected(event) => event.ts_event,
            Self::CancelRejected(event) => event.ts_event,
            Self::Updated(event) => event.ts_event,
            Self::Filled(event) => event.ts_event,
        }
    }

    #[must_use]
    pub fn message(&self) -> Option<Ustr> {
        match self {
            Self::Initialized(_) => None,
            Self::Denied(event) => Some(event.reason),
            Self::Emulated(_) => None,
            Self::Released(_) => None,
            Self::Submitted(_) => None,
            Self::Accepted(_) => None,
            Self::Rejected(event) => Some(event.reason),
            Self::Canceled(_) => None,
            Self::Expired(_) => None,
            Self::Triggered(_) => None,
            Self::PendingUpdate(_) => None,
            Self::PendingCancel(_) => None,
            Self::ModifyRejected(event) => Some(event.reason),
            Self::CancelRejected(event) => Some(event.reason),
            Self::Updated(_) => None,
            Self::Filled(_) => None,
        }
    }
}

/// Converts an `OrderEventAny` into an `OrderFilled`.
///
/// # Panics
///
/// Panics if `event` is not a `Filled` variant.
impl From<OrderEventAny> for OrderFilled {
    #[inline]
    fn from(event: OrderEventAny) -> Self {
        match event {
            OrderEventAny::Filled(event) => event,
            _ => panic!("Invalid `OrderEventAny` not `OrderFilled`, was {event:?}"),
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s).

## Detailed Walkthrough

### Functions
- **`into_boxed()`**: Function defined in this file
- **`event_type()`**: Function defined in this file
- **`trader_id()`**: Function defined in this file
- **`client_order_id()`**: Function defined in this file
- **`venue_order_id()`**: Function defined in this file
- **`account_id()`**: Function defined in this file
- **`instrument_id()`**: Function defined in this file
- **`strategy_id()`**: Function defined in this file
- **`ts_event()`**: Function defined in this file
- **`message()`**: Function defined in this file
- **`from()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Enums**: `OrderEventAny`
**Functions**: `account_id`, `client_order_id`, `event_type`, `from`, `instrument_id`, `into_boxed`, `message`, `strategy_id`, `trader_id`, `ts_event`, `venue_order_id`
**Impls**: `From`, `OrderEventAny`

## Related Files

This file is located in `crates/model/src/events/order/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.463585Z*
