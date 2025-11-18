# Documentation: mode.rs

## File Metadata

- **Path**: `crates/network/src/mode.rs`
- **Size**: 3,686 bytes
- **Lines**: 104
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

//! Connection mode enumeration for socket clients.

use std::sync::atomic::{AtomicU8, Ordering};

use strum::{AsRefStr, Display, EnumString};

/// Connection mode for a socket client.
///
/// The client can be in one of four modes (managed via an atomic flag).
#[derive(Clone, Copy, Debug, Default, Display, Hash, PartialEq, Eq, AsRefStr, EnumString)]
#[repr(u8)]
#[strum(serialize_all = "UPPERCASE")]
pub enum ConnectionMode {
    #[default]
    /// The client is fully connected and operational.
    /// All tasks (reading, writing, heartbeat) are running normally.
    Active = 0,
    /// The client has been disconnected or has been explicitly signaled to reconnect.
    /// In this state, active tasks are paused until a new connection is established.
    Reconnect = 1,
    /// The client has been explicitly signaled to disconnect.
    /// No further reconnection attempts will be made, and cleanup procedures are initiated.
    Disconnect = 2,
    /// The client is permanently closed.
    /// All associated tasks have been terminated and the connection is no longer available.
    Closed = 3,
}

impl ConnectionMode {
    /// Convert a u8 to [`ConnectionMode`], useful when loading from an `AtomicU8`.
    ///
    /// # Panics
    ///
    /// Panics if `value` is not a valid `ConnectionMode` discriminant (must be between 0 and 3 inclusive).
    #[inline]
    #[must_use]
    pub fn from_u8(value: u8) -> Self {
        match value {
            0 => Self::Active,
            1 => Self::Reconnect,
            2 => Self::Disconnect,
            3 => Self::Closed,
            _ => panic!("Invalid `ConnectionMode` value: {value}"),
        }
    }

    /// Load a [`ConnectionMode`] from an [`AtomicU8`] using sequential consistency ordering.
    #[inline]
    #[must_use]
    pub fn from_atomic(value: &AtomicU8) -> Self {
        Self::from_u8(value.load(Ordering::SeqCst))
    }

    /// Convert a [`ConnectionMode`] to a u8, useful when storing to an `AtomicU8`.
    #[inline]
    #[must_use]
    pub const fn as_u8(self) -> u8 {
        self as u8
    }

    /// Returns true if the client is in an active state.
    #[inline]
    #[must_use]
    pub const fn is_active(&self) -> bool {
        matches!(self, Self::Active)
    }

    /// Returns true if the client is attempting to reconnect.
    #[inline]
    #[must_use]
    pub const fn is_reconnect(&self) -> bool {
        matches!(self, Self::Reconnect)
    }

    /// Returns true if the client is attempting to disconnect.
    #[inline]
    #[must_use]
    pub const fn is_disconnect(&self) -> bool {
        matches!(self, Self::Disconnect)
    }

    /// Returns true if the client connection is closed.
    #[inline]
    #[must_use]
    pub const fn is_closed(&self) -> bool {
        matches!(self, Self::Closed)
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s).

## Detailed Walkthrough

### Functions
- **`from_u8()`**: Function defined in this file
- **`from_atomic()`**: Function defined in this file
- **`as_u8()`**: Function defined in this file
- **`is_active()`**: Function defined in this file
- **`is_reconnect()`**: Function defined in this file
- **`is_disconnect()`**: Function defined in this file
- **`is_closed()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Enums**: `ConnectionMode`
**Functions**: `as_u8`, `from_atomic`, `from_u8`, `is_active`, `is_closed`, `is_disconnect`, `is_reconnect`
**Impls**: `ConnectionMode`

## Related Files

This file is located in `crates/network/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.357826Z*
