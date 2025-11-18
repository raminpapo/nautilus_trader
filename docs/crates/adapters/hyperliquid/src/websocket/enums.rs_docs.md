# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/hyperliquid/src/websocket/enums.rs`
- **Size**: 8,104 bytes
- **Lines**: 231
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

use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumIter, EnumString};

/// WebSocket channel names for Hyperliquid.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
pub enum HyperliquidWsChannel {
    #[serde(rename = "subscriptionResponse")]
    SubscriptionResponse,
    #[serde(rename = "trades")]
    Trades,
    #[serde(rename = "l2Book")]
    L2Book,
    #[serde(rename = "bbo")]
    Bbo,
    #[serde(rename = "candle")]
    Candle,
    #[serde(rename = "allMids")]
    AllMids,
    #[serde(rename = "notification")]
    Notification,
    #[serde(rename = "orderUpdates")]
    OrderUpdates,
    #[serde(rename = "userEvents")]
    UserEvents,
    #[serde(rename = "userFills")]
    UserFills,
    #[serde(rename = "userFundings")]
    UserFundings,
    #[serde(rename = "userNonFundingLedgerUpdates")]
    UserNonFundingLedgerUpdates,
    #[serde(rename = "post")]
    Post,
    #[serde(rename = "pong")]
    Pong,
    #[serde(rename = "error")]
    Error,
}

impl HyperliquidWsChannel {
    /// Returns the string representation of the channel.
    pub fn as_str(&self) -> &'static str {
        match self {
            Self::SubscriptionResponse => "subscriptionResponse",
            Self::Trades => "trades",
            Self::L2Book => "l2Book",
            Self::Bbo => "bbo",
            Self::Candle => "candle",
            Self::AllMids => "allMids",
            Self::Notification => "notification",
            Self::OrderUpdates => "orderUpdates",
            Self::UserEvents => "userEvents",
            Self::UserFills => "userFills",
            Self::UserFundings => "userFundings",
            Self::UserNonFundingLedgerUpdates => "userNonFundingLedgerUpdates",
            Self::Post => "post",
            Self::Pong => "pong",
            Self::Error => "error",
        }
    }

    /// Returns true if this is a public channel (does not require authentication).
    pub fn is_public(&self) -> bool {
        matches!(
            self,
            Self::SubscriptionResponse
                | Self::Trades
                | Self::L2Book
                | Self::Bbo
                | Self::Candle
                | Self::AllMids
                | Self::Notification
                | Self::Pong
                | Self::Error
        )
    }

    /// Returns true if this is a private channel (requires authentication).
    pub fn is_private(&self) -> bool {
        !self.is_public()
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;
    use serde_json;

    use super::*;

    #[rstest]
    #[case(HyperliquidWsChannel::Trades, r#""trades""#)]
    #[case(HyperliquidWsChannel::L2Book, r#""l2Book""#)]
    #[case(HyperliquidWsChannel::UserFills, r#""userFills""#)]
    #[case(HyperliquidWsChannel::Bbo, r#""bbo""#)]
    #[case(
        HyperliquidWsChannel::SubscriptionResponse,
        r#""subscriptionResponse""#
    )]
    fn test_channel_serialization(#[case] channel: HyperliquidWsChannel, #[case] expected: &str) {
        assert_eq!(serde_json::to_string(&channel).unwrap(), expected);
    }

    #[rstest]
    #[case(r#""trades""#, HyperliquidWsChannel::Trades)]
    #[case(r#""l2Book""#, HyperliquidWsChannel::L2Book)]
    #[case(r#""userEvents""#, HyperliquidWsChannel::UserEvents)]
    #[case(r#""bbo""#, HyperliquidWsChannel::Bbo)]
    #[case(r#""pong""#, HyperliquidWsChannel::Pong)]
    fn test_channel_deserialization(#[case] json: &str, #[case] expected: HyperliquidWsChannel) {
        assert_eq!(
            serde_json::from_str::<HyperliquidWsChannel>(json).unwrap(),
            expected
        );
    }

    #[rstest]
    #[case(HyperliquidWsChannel::Trades, "trades")]
    #[case(HyperliquidWsChannel::L2Book, "l2Book")]
    #[case(HyperliquidWsChannel::UserFills, "userFills")]
    #[case(
        HyperliquidWsChannel::UserNonFundingLedgerUpdates,
        "userNonFundingLedgerUpdates"
    )]
    #[case(HyperliquidWsChannel::Bbo, "bbo")]
    fn test_as_str_method(#[case] channel: HyperliquidWsChannel, #[case] expected: &str) {
        assert_eq!(channel.as_str(), expected);
    }

    #[rstest]
    fn test_display_trait() {
        assert_eq!(format!("{}", HyperliquidWsChannel::Trades), "Trades");
        assert_eq!(format!("{}", HyperliquidWsChannel::L2Book), "L2Book");
        assert_eq!(format!("{}", HyperliquidWsChannel::UserFills), "UserFills");
    }

    #[rstest]
    fn test_is_public_channel() {
        assert!(HyperliquidWsChannel::Trades.is_public());
        assert!(HyperliquidWsChannel::L2Book.is_public());
        assert!(HyperliquidWsChannel::Bbo.is_public());
        assert!(HyperliquidWsChannel::SubscriptionResponse.is_public());
        assert!(HyperliquidWsChannel::Pong.is_public());

        assert!(!HyperliquidWsChannel::OrderUpdates.is_public());
        assert!(!HyperliquidWsChannel::UserEvents.is_public());
        assert!(!HyperliquidWsChannel::UserFills.is_public());
        assert!(!HyperliquidWsChannel::UserFundings.is_public());
        assert!(!HyperliquidWsChannel::UserNonFundingLedgerUpdates.is_public());
        assert!(!HyperliquidWsChannel::Post.is_public());
    }

    #[rstest]
    fn test_is_private_channel() {
        assert!(!HyperliquidWsChannel::Trades.is_private());
        assert!(!HyperliquidWsChannel::L2Book.is_private());
        assert!(!HyperliquidWsChannel::Bbo.is_private());

        assert!(HyperliquidWsChannel::OrderUpdates.is_private());
        assert!(HyperliquidWsChannel::UserEvents.is_private());
        assert!(HyperliquidWsChannel::UserFills.is_private());
        assert!(HyperliquidWsChannel::UserFundings.is_private());
        assert!(HyperliquidWsChannel::UserNonFundingLedgerUpdates.is_private());
        assert!(HyperliquidWsChannel::Post.is_private());
    }

    #[rstest]
    fn test_enum_iter() {
        use strum::IntoEnumIterator;

        let channels: Vec<HyperliquidWsChannel> = HyperliquidWsChannel::iter().collect();
        assert_eq!(channels.len(), 15);
        assert!(channels.contains(&HyperliquidWsChannel::Trades));
        assert!(channels.contains(&HyperliquidWsChannel::L2Book));
        assert!(channels.contains(&HyperliquidWsChannel::UserFills));
        assert!(channels.contains(&HyperliquidWsChannel::Candle));
        assert!(channels.contains(&HyperliquidWsChannel::AllMids));
        assert!(channels.contains(&HyperliquidWsChannel::Notification));
    }

    #[rstest]
    fn test_from_str() {
        use std::str::FromStr;

        assert_eq!(
            HyperliquidWsChannel::from_str("Trades").unwrap(),
            HyperliquidWsChannel::Trades
        );
        assert_eq!(
            HyperliquidWsChannel::from_str("L2Book").unwrap(),
            HyperliquidWsChannel::L2Book
        );
        assert_eq!(
            HyperliquidWsChannel::from_str("UserFills").unwrap(),
            HyperliquidWsChannel::UserFills
        );

        assert!(HyperliquidWsChannel::from_str("InvalidChannel").is_err());
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s).

## Detailed Walkthrough

### Functions
- **`as_str()`**: Function defined in this file
- **`is_public()`**: Function defined in this file
- **`is_private()`**: Function defined in this file
- **`test_channel_serialization()`**: Function defined in this file
- **`test_channel_deserialization()`**: Function defined in this file
- **`test_as_str_method()`**: Function defined in this file
- **`test_display_trait()`**: Function defined in this file
- **`test_is_public_channel()`**: Function defined in this file
- **`test_is_private_channel()`**: Function defined in this file
- **`test_enum_iter()`**: Function defined in this file
- **`test_from_str()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Enums**: `HyperliquidWsChannel`
**Functions**: `as_str`, `is_private`, `is_public`, `test_as_str_method`, `test_channel_deserialization`, `test_channel_serialization`, `test_display_trait`, `test_enum_iter`, `test_from_str`, `test_is_private_channel`, `test_is_public_channel`
**Impls**: `HyperliquidWsChannel`

## Related Files

This file is located in `crates/adapters/hyperliquid/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.096246Z*
