# Documentation: `crates/adapters/okx/src/websocket/subscription.rs`
**Generated:** 2025-11-15T19:40:01.366711Z
**File Size:** 2302 bytes
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

- **Path:** `crates/adapters/okx/src/websocket/subscription.rs`
- **Size:** 2,302 bytes
- **Lines:** 71
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 3

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


---

## Overview

This file is located at `crates/adapters/okx/src/websocket/subscription.rs` within the repository.

**Functions defined:** topic_from_parts, topic_from_subscription_arg, topic_from_websocket_arg


---

## Detailed Analysis

### Functions

#### `topic_from_parts(
    channel: &OKXWsChannel,
    inst_id: Option<&Ustr>,
    inst_family: Option<&Ustr>,
    inst_type: Option<&OKXInstrumentType>,
    bar: Option<&Ustr>,
)`


#### `topic_from_subscription_arg(arg: &OKXSubscriptionArg)`


#### `topic_from_websocket_arg(arg: &OKXWebSocketArg)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


