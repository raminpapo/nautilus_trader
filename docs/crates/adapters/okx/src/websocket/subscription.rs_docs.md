# Documentation: subscription.rs

## File Metadata

- **Path**: `crates/adapters/okx/src/websocket/subscription.rs`
- **Size**: 2,302 bytes
- **Lines**: 72
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

//! OKX-specific subscription helpers.

use ustr::Ustr;

use crate::{
    common::enums::OKXInstrumentType,
    websocket::{
        enums::OKXWsChannel,
        messages::{OKXSubscriptionArg, OKXWebSocketArg},
    },
};

fn topic_from_parts(
    channel: &OKXWsChannel,
    inst_id: Option<&Ustr>,
    inst_family: Option<&Ustr>,
    inst_type: Option<&OKXInstrumentType>,
    bar: Option<&Ustr>,
) -> String {
    let base = channel.as_ref();

    if let Some(inst_id) = inst_id {
        let inst_id = inst_id.as_str();
        if let Some(bar) = bar {
            format!("{base}:{inst_id}:{}", bar.as_str())
        } else {
            format!("{base}:{inst_id}")
        }
    } else if let Some(inst_family) = inst_family {
        format!("{base}:{}", inst_family.as_str())
    } else if let Some(inst_type) = inst_type {
        format!("{base}:{}", inst_type.as_ref())
    } else {
        base.to_string()
    }
}

pub(crate) fn topic_from_subscription_arg(arg: &OKXSubscriptionArg) -> String {
    topic_from_parts(
        &arg.channel,
        arg.inst_id.as_ref(),
        arg.inst_family.as_ref(),
        arg.inst_type.as_ref(),
        None,
    )
}

pub(crate) fn topic_from_websocket_arg(arg: &OKXWebSocketArg) -> String {
    topic_from_parts(
        &arg.channel,
        arg.inst_id.as_ref(),
        arg.inst_family.as_ref(),
        arg.inst_type.as_ref(),
        arg.bar.as_ref(),
    )
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`topic_from_parts()`**: Function defined in this file
- **`topic_from_subscription_arg()`**: Function defined in this file
- **`topic_from_websocket_arg()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `topic_from_parts`, `topic_from_subscription_arg`, `topic_from_websocket_arg`

## Related Files

This file is located in `crates/adapters/okx/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.521086Z*
