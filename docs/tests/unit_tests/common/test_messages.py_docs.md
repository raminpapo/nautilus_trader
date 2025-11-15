# Documentation: `tests/unit_tests/common/test_messages.py`
**Generated:** 2025-11-15T19:40:09.060501Z
**File Size:** 4642 bytes
**Extension:** .py
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

- **Path:** `tests/unit_tests/common/test_messages.py`
- **Size:** 4,642 bytes
- **Lines:** 126
- **Extension:** `.py`
- **Type:** text
- **Imports:** 10
- **Classes:** 1
- **Functions:** 4

---

## Source Code

```python
# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

import pytest

from nautilus_trader.common.enums import ComponentState
from nautilus_trader.common.messages import ComponentStateChanged
from nautilus_trader.common.messages import ShutdownSystem
from nautilus_trader.common.messages import TradingStateChanged
from nautilus_trader.config import ActorConfig
from nautilus_trader.core.uuid import UUID4
from nautilus_trader.model.enums import TradingState
from nautilus_trader.model.identifiers import ComponentId
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


def test_shutdown_system_command():
    # Arrange
    uuid = UUID4()
    command = ShutdownSystem(
        trader_id=TestIdStubs.trader_id(),
        component_id=ComponentId("Controller"),
        reason="Maintenance",
        command_id=uuid,
        ts_init=0,
    )

    # Act, Assert
    assert ShutdownSystem.from_dict(ShutdownSystem.to_dict(command)) == command
    assert (
        str(command)
        == f"ShutdownSystem(trader_id=TESTER-000, component_id=Controller, reason='Maintenance', command_id={uuid})"
    )
    assert (
        repr(command)
        == f"ShutdownSystem(trader_id=TESTER-000, component_id=Controller, reason='Maintenance', command_id={uuid}, ts_init=0)"
    )


def test_component_state_changed_event():
    # Arrange
    uuid = UUID4()
    event = ComponentStateChanged(
        trader_id=TestIdStubs.trader_id(),
        component_id=ComponentId("MyActor-001"),
        component_type="MyActor",
        state=ComponentState.RUNNING,
        config={"do_something": True},
        event_id=uuid,
        ts_event=0,
        ts_init=0,
    )

    # Act, Assert
    assert ComponentStateChanged.from_dict(ComponentStateChanged.to_dict(event)) == event
    assert (
        str(event)
        == f"ComponentStateChanged(trader_id=TESTER-000, component_id=MyActor-001, component_type=MyActor, state=RUNNING, config={{'do_something': True}}, event_id={uuid})"
    )
    assert (
        repr(event)
        == f"ComponentStateChanged(trader_id=TESTER-000, component_id=MyActor-001, component_type=MyActor, state=RUNNING, config={{'do_something': True}}, event_id={uuid}, ts_init=0)"
    )


def test_serializing_component_state_changed_with_unserializable_config_raises() -> None:
    # Arrange
    class MyType(ActorConfig, frozen=True):
        values: list[int]

    config = {"key": MyType(values=[1, 2, 3])}
    event = ComponentStateChanged(
        trader_id=TestIdStubs.trader_id(),
        component_id=ComponentId("MyActor-001"),
        component_type="MyActor",
        state=ComponentState.RUNNING,
        config=config,
        event_id=UUID4(),
        ts_event=0,
        ts_init=0,
    )

    # Act
    with pytest.raises(TypeError) as e:
        TradingStateChanged.to_dict(event)

        # Assert
        assert e.value == TypeError(
            "Cannot serialize config as Type is not JSON serializable: MyType. You can register a new serializer for `MyType` through `Default.register_serializer`.",
        )


def test_trading_state_changed():
    # Arrange
    uuid = UUID4()
    event = TradingStateChanged(
        trader_id=TestIdStubs.trader_id(),
        state=TradingState.HALTED,
        config={"max_order_submit_rate": "100/00:00:01"},
        event_id=uuid,
        ts_event=0,
        ts_init=0,
    )

    # Act, Assert
    assert TradingStateChanged.from_dict(TradingStateChanged.to_dict(event)) == event
    assert (
        str(event)
        == f"TradingStateChanged(trader_id=TESTER-000, state=HALTED, config={{'max_order_submit_rate': '100/00:00:01'}}, event_id={uuid})"
    )
    assert (
        repr(event)
        == f"TradingStateChanged(trader_id=TESTER-000, state=HALTED, config={{'max_order_submit_rate': '100/00:00:01'}}, event_id={uuid}, ts_init=0)"
    )
```


---

## Overview

This file is located at `tests/unit_tests/common/test_messages.py` within the repository.

**Classes defined:** MyType

**Functions defined:** test_shutdown_system_command, test_component_state_changed_event, test_serializing_component_state_changed_with_unserializable_config_raises, test_trading_state_changed

**Import statements:** 10


---

## Detailed Analysis

### Classes

#### `MyType`

**Inherits from:** ActorConfig, frozen=True


### Functions

#### `test_shutdown_system_command()`


#### `test_component_state_changed_event()`


#### `test_serializing_component_state_changed_with_unserializable_config_raises()`


#### `test_trading_state_changed()`


### Imports

- `import pytest`
- `from nautilus_trader.common.enums import ComponentState`
- `from nautilus_trader.common.messages import ComponentStateChanged`
- `from nautilus_trader.common.messages import ShutdownSystem`
- `from nautilus_trader.common.messages import TradingStateChanged`
- `from nautilus_trader.config import ActorConfig`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.enums import TradingState`
- `from nautilus_trader.model.identifiers import ComponentId`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_messages import MyType
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.common.enums import ComponentState`
- `from nautilus_trader.common.messages import ComponentStateChanged`
- `from nautilus_trader.common.messages import ShutdownSystem`
- `from nautilus_trader.common.messages import TradingStateChanged`
- `from nautilus_trader.config import ActorConfig`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.enums import TradingState`
- `from nautilus_trader.model.identifiers import ComponentId`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


