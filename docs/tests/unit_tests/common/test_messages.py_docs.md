# Documentation: test_messages.py

## File Metadata

- **Path**: `tests/unit_tests/common/test_messages.py`
- **Size**: 4,725 bytes
- **Lines**: 128
- **Language**: Python

## Original Source

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


@pytest.mark.skip(reason="Test broken - serialization doesn't fail as expected, needs redesign")
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
        ComponentStateChanged.to_dict(event)

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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`test_shutdown_system_command()`**: Function defined in this file
- **`test_component_state_changed_event()`**: Function defined in this file
- **`test_serializing_component_state_changed_with_unserializable_config_raises()`**: Function defined in this file
- **`test_trading_state_changed()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Functions**: `test_component_state_changed_event`, `test_serializing_component_state_changed_with_unserializable_config_raises`, `test_shutdown_system_command`, `test_trading_state_changed`
**Imports**: `nautilus_trader.common.enums`, `nautilus_trader.common.messages`, `nautilus_trader.config`, `nautilus_trader.core.uuid`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.test_kit.stubs.identifiers`, `pytest`

## Related Files

This file is located in `tests/unit_tests/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/common/test_messages.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.293973Z*
