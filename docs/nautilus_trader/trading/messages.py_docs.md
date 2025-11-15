# Documentation: `nautilus_trader/trading/messages.py`
**Generated:** 2025-11-15T19:40:05.398599Z
**File Size:** 6136 bytes
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

- **Path:** `nautilus_trader/trading/messages.py`
- **Size:** 6,136 bytes
- **Lines:** 239
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 8
- **Functions:** 8

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

from nautilus_trader.common.config import ImportableActorConfig
from nautilus_trader.core.message import Command
from nautilus_trader.core.uuid import UUID4
from nautilus_trader.model.identifiers import ComponentId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.trading.config import ImportableStrategyConfig


class CreateActor(Command):
    """
    Represents a command to create an actor.

    Parameters
    ----------
    actor_config : ImportableActorConfig
        The configuration for the actor.
    start: bool, optional
        If True, start the actor after creation, by default True.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        actor_config: ImportableActorConfig,
        start: bool = True,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:

        super().__init__(command_id or UUID4(), ts_init)

        self.actor_config = actor_config
        self.start = start


class CreateStrategy(Command):
    """
    Represents a command to create a strategy.

    Parameters
    ----------
    strategy_config : ImportableStrategyConfig
        The configuration for the strategy.
    start: bool, optional
        If True, start the strategy after creation, by default True.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        strategy_config: ImportableStrategyConfig,
        start: bool = True,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:

        super().__init__(command_id or UUID4(), ts_init)

        self.strategy_config = strategy_config
        self.start = start


class StartActor(Command):
    """
    Represents a command to start an actor.

    Parameters
    ----------
    actor_id : ComponentId
        The ID of the actor to start.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        actor_id: ComponentId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:
        super().__init__(command_id or UUID4(), ts_init)

        self.actor_id = actor_id


class StartStrategy(Command):
    """
    Represents a command to start a strategy.

    Parameters
    ----------
    strategy_id : StrategyId
        The ID of the strategy to start.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        strategy_id: StrategyId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:
        super().__init__(command_id or UUID4(), ts_init)

        self.strategy_id = strategy_id


class StopActor(Command):
    """
    Represents a command to strop an actor.

    Parameters
    ----------
    actor_id : ComponentId
        The ID of the actor to start.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        actor_id: ComponentId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:
        super().__init__(command_id or UUID4(), ts_init)

        self.actor_id = actor_id


class StopStrategy(Command):
    """
    Represents a command to stop a strategy.

    Parameters
    ----------
    strategy_id : StrategyId
        The ID of the strategy to start.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        strategy_id: StrategyId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:
        super().__init__(command_id or UUID4(), ts_init)

        self.strategy_id = strategy_id


class RemoveActor(Command):
    """
    Represents a command to remove an actor.

    Parameters
    ----------
    actor_id : ComponentId
        The ID of the actor to start.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        actor_id: ComponentId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:
        super().__init__(command_id or UUID4(), ts_init)

        self.actor_id = actor_id


class RemoveStrategy(Command):
    """
    Represents a command to remove a strategy.

    Parameters
    ----------
    strategy_id : StrategyId
        The ID of the strategy to start.
    command_id : UUID4
        The command ID.
    ts_init : int
        UNIX timestamp (nanoseconds) when the object was initialized.

    """

    def __init__(
        self,
        strategy_id: StrategyId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    ) -> None:
        super().__init__(command_id or UUID4(), ts_init)

        self.strategy_id = strategy_id
```


---

## Overview

This file is located at `nautilus_trader/trading/messages.py` within the repository.

**Classes defined:** CreateActor, CreateStrategy, StartActor, StartStrategy, StopActor, StopStrategy, RemoveActor, RemoveStrategy

**Functions defined:** __init__, __init__, __init__, __init__, __init__, __init__, __init__, __init__

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `CreateActor`

**Inherits from:** Command


#### `CreateStrategy`

**Inherits from:** Command


#### `StartActor`

**Inherits from:** Command


#### `StartStrategy`

**Inherits from:** Command


#### `StopActor`

**Inherits from:** Command


#### `StopStrategy`

**Inherits from:** Command


#### `RemoveActor`

**Inherits from:** Command


#### `RemoveStrategy`

**Inherits from:** Command


### Functions

#### `__init__(
        self,
        actor_config: ImportableActorConfig,
        start: bool = True,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        strategy_config: ImportableStrategyConfig,
        start: bool = True,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        actor_id: ComponentId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        strategy_id: StrategyId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        actor_id: ComponentId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        strategy_id: StrategyId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        actor_id: ComponentId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


#### `__init__(
        self,
        strategy_id: StrategyId,
        command_id: UUID4 | None = None,
        ts_init: int = 0,
    )`


### Imports

- `from nautilus_trader.common.config import ImportableActorConfig`
- `from nautilus_trader.core.message import Command`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.identifiers import ComponentId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.trading.config import ImportableStrategyConfig`


---

## Usage Examples

### Importing

```python
from nautilus_trader.trading.messages import CreateActor
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.config import ImportableActorConfig`
- `from nautilus_trader.core.message import Command`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.identifiers import ComponentId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.trading.config import ImportableStrategyConfig`

**Directory:** `nautilus_trader/trading`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


