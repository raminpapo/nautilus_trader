# Documentation: `crates/execution/src/engine/stubs.rs`
**Generated:** 2025-11-15T19:40:02.039483Z
**File Size:** 4549 bytes
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

- **Path:** `crates/execution/src/engine/stubs.rs`
- **Size:** 4,549 bytes
- **Lines:** 151
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 18

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

use std::{cell::RefCell, rc::Rc};

use nautilus_common::{
    cache::Cache,
    clock::Clock,
    messages::execution::{
        BatchCancelOrders, CancelAllOrders, CancelOrder, ModifyOrder, QueryAccount, QueryOrder,
        SubmitOrder, SubmitOrderList,
    },
};
use nautilus_core::UnixNanos;
use nautilus_model::{
    accounts::AccountAny,
    enums::OmsType,
    identifiers::{AccountId, ClientId, Venue},
    types::{AccountBalance, MarginBalance},
};

use crate::client::ExecutionClient;

/// A stub execution client for testing purposes.
///
/// This client provides a minimal implementation of the `ExecutionClient` trait
/// that can be used in unit tests without requiring actual venue connectivity.
#[derive(Clone, Debug)]
#[allow(dead_code)]
pub struct StubExecutionClient {
    client_id: ClientId,
    account_id: AccountId,
    venue: Venue,
    oms_type: OmsType,
    is_connected: bool,
    clock: Rc<RefCell<dyn Clock>>,
    cache: Rc<RefCell<Cache>>,
}

impl StubExecutionClient {
    /// Creates a new [`StubExecutionClient`] instance.
    #[allow(dead_code)]
    pub fn new(
        client_id: ClientId,
        account_id: AccountId,
        venue: Venue,
        oms_type: OmsType,
        clock: Option<Rc<RefCell<dyn Clock>>>,
    ) -> Self {
        Self {
            client_id,
            account_id,
            venue,
            oms_type,
            is_connected: false,
            clock: clock
                .unwrap_or_else(|| Rc::new(RefCell::new(nautilus_common::clock::TestClock::new()))),
            cache: Rc::new(RefCell::new(Cache::new(None, None))),
        }
    }
}

impl ExecutionClient for StubExecutionClient {
    fn is_connected(&self) -> bool {
        self.is_connected
    }

    fn client_id(&self) -> ClientId {
        self.client_id
    }

    fn account_id(&self) -> AccountId {
        self.account_id
    }

    fn venue(&self) -> Venue {
        self.venue
    }

    fn oms_type(&self) -> OmsType {
        self.oms_type
    }

    fn get_account(&self) -> Option<AccountAny> {
        None // Stub implementation returns None
    }

    fn generate_account_state(
        &self,
        _balances: Vec<AccountBalance>,
        _margins: Vec<MarginBalance>,
        _reported: bool,
        _ts_event: UnixNanos,
    ) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn start(&mut self) -> anyhow::Result<()> {
        self.is_connected = true;
        Ok(())
    }

    fn stop(&mut self) -> anyhow::Result<()> {
        self.is_connected = false;
        Ok(())
    }

    fn submit_order(&self, _cmd: &SubmitOrder) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn submit_order_list(&self, _cmd: &SubmitOrderList) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn modify_order(&self, _cmd: &ModifyOrder) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn cancel_order(&self, _cmd: &CancelOrder) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn cancel_all_orders(&self, _cmd: &CancelAllOrders) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn batch_cancel_orders(&self, _cmd: &BatchCancelOrders) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn query_account(&self, _cmd: &QueryAccount) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }

    fn query_order(&self, _cmd: &QueryOrder) -> anyhow::Result<()> {
        Ok(()) // Stub implementation always succeeds
    }
}
```


---

## Overview

This file is located at `crates/execution/src/engine/stubs.rs` within the repository.

**Classes defined:** StubExecutionClient, StubExecutionClient, ExecutionClient

**Functions defined:** new, is_connected, client_id, account_id, venue, oms_type, get_account, generate_account_state, start, stop and 8 more


---

## Detailed Analysis

### Classes

#### `StubExecutionClient`

**Type:** struct


#### `StubExecutionClient`

**Type:** impl


#### `ExecutionClient`

**Type:** impl


### Functions

#### `new(
        client_id: ClientId,
        account_id: AccountId,
        venue: Venue,
        oms_type: OmsType,
        clock: Option<Rc<RefCell<dyn Clock>>>,
    )`


#### `is_connected(&self)`


#### `client_id(&self)`


#### `account_id(&self)`


#### `venue(&self)`


#### `oms_type(&self)`


#### `get_account(&self)`


#### `generate_account_state(
        &self,
        _balances: Vec<AccountBalance>,
        _margins: Vec<MarginBalance>,
        _reported: bool,
        _ts_event: UnixNanos,
    )`


#### `start(&mut self)`


#### `stop(&mut self)`


#### `submit_order(&self, _cmd: &SubmitOrder)`


#### `submit_order_list(&self, _cmd: &SubmitOrderList)`


#### `modify_order(&self, _cmd: &ModifyOrder)`


#### `cancel_order(&self, _cmd: &CancelOrder)`


#### `cancel_all_orders(&self, _cmd: &CancelAllOrders)`


#### `batch_cancel_orders(&self, _cmd: &BatchCancelOrders)`


#### `query_account(&self, _cmd: &QueryAccount)`


#### `query_order(&self, _cmd: &QueryOrder)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution/src/engine`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


