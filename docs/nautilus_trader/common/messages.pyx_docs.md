# Documentation: `nautilus_trader/common/messages.pyx`
**Generated:** 2025-11-15T19:40:04.704750Z
**File Size:** 15175 bytes
**Extension:** .pyx
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

- **Path:** `nautilus_trader/common/messages.pyx`
- **Size:** 15,175 bytes
- **Lines:** 534
- **Extension:** `.pyx`
- **Type:** text
- **Imports:** 3
- **Functions:** 31

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

import decimal
import json
import re

from libc.stdint cimport uint64_t

from nautilus_trader.common.component cimport component_state_from_str
from nautilus_trader.common.component cimport component_state_to_str
from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.core.message cimport Command
from nautilus_trader.core.message cimport Event
from nautilus_trader.core.rust.common cimport ComponentState
from nautilus_trader.core.rust.model cimport TradingState
from nautilus_trader.core.uuid cimport UUID4
from nautilus_trader.model.functions cimport trading_state_from_str
from nautilus_trader.model.functions cimport trading_state_to_str
from nautilus_trader.model.identifiers cimport ComponentId
from nautilus_trader.model.identifiers cimport Identifier
from nautilus_trader.model.identifiers cimport TraderId


cdef class ShutdownSystem(Command):
    """
    Represents a command to shut down a system and terminate the process.

    Parameters
    ----------
    trader_id : TraderId
        The trader ID associated with the event.
    component_id : Identifier
        The component ID associated with the event.
    command_id : UUID4
        The command ID.
    ts_init : uint64_t
        UNIX timestamp (nanoseconds) when the object was initialized.
    reason : str, optional
        The reason for the shutdown command (can be None).
    """

    def __init__(
        self,
        TraderId trader_id not None,
        Identifier component_id not None,
        UUID4 command_id not None,
        uint64_t ts_init,
        str reason = None,
        UUID4 correlation_id = None,
    ) -> None:
        super().__init__(command_id, ts_init, correlation_id)
        self.trader_id = trader_id
        self.component_id = component_id
        self.reason = reason
        self._command_id = command_id
        self._ts_init = ts_init

    def __eq__(self, Command other) -> bool:
        return self._command_id == other.id

    def __hash__(self) -> int:
        return hash(self._command_id)

    def __str__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"trader_id={self.trader_id.to_str()}, "
            f"component_id={self.component_id.to_str()}, "
            f"reason='{self.reason}', "
            f"command_id={self._command_id.to_str()})"
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"trader_id={self.trader_id.to_str()}, "
            f"component_id={self.component_id.to_str()}, "
            f"reason='{self.reason}', "
            f"command_id={self._command_id.to_str()}, "
            f"ts_init={self._ts_init})"
        )

    @staticmethod
    cdef ShutdownSystem from_dict_c(dict values):
        Condition.not_none(values, "values")
        return ShutdownSystem(
            trader_id=TraderId(values["trader_id"]),
            component_id=ComponentId(values["component_id"]),
            reason=values["reason"],
            command_id=UUID4.from_str_c(values["command_id"]),
            ts_init=values["ts_init"],
            correlation_id=UUID4.from_str_c(values["correlation_id"]) if values.get("correlation_id") else None,
        )

    @staticmethod
    cdef dict to_dict_c(ShutdownSystem obj):
        Condition.not_none(obj, "obj")
        return {
            "type": "ShutdownSystem",
            "trader_id": obj.trader_id.to_str(),
            "component_id": obj.component_id.to_str(),
            "reason": obj.reason,
            "command_id": obj._command_id.to_str(),
            "ts_init": obj._ts_init,
        }

    @staticmethod
    def from_dict(dict values) -> ShutdownSystem:
        """
        Return a shutdown system command from the given dict values.

        Parameters
        ----------
        values : dict[str, object]
            The values for initialization.

        Returns
        -------
        ShutdownSystem

        """
        return ShutdownSystem.from_dict_c(values)

    @staticmethod
    def to_dict(ShutdownSystem obj):
        """
        Return a dictionary representation of this object.

        Returns
        -------
        dict[str, object]

        """
        return ShutdownSystem.to_dict_c(obj)



cdef class ComponentStateChanged(Event):
    """
    Represents an event which includes information on the state of a component.

    Parameters
    ----------
    trader_id : TraderId
        The trader ID associated with the event.
    component_id : Identifier
        The component ID associated with the event.
    component_type : str
        The component type.
    state : ComponentState
        The component state.
    config : dict[str, Any]
        The component configuration for the event.
    event_id : UUID4
        The event ID.
    ts_event : uint64_t
        UNIX timestamp (nanoseconds) when the component state event occurred.
    ts_init : uint64_t
        UNIX timestamp (nanoseconds) when the object was initialized.
    """

    def __init__(
        self,
        TraderId trader_id not None,
        Identifier component_id not None,
        str component_type not None,
        ComponentState state,
        dict config not None,
        UUID4 event_id not None,
        uint64_t ts_event,
        uint64_t ts_init,
    ) -> None:
        self.trader_id = trader_id
        self.component_id = component_id
        self.component_type = component_type
        self.state = state
        self.config = config
        self._event_id = event_id
        self._ts_event = ts_event
        self._ts_init = ts_init

    def __eq__(self, Event other) -> bool:
        return self._event_id == other.id

    def __hash__(self) -> int:
        return hash(self._event_id)

    def __str__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"trader_id={self.trader_id.to_str()}, "
            f"component_id={self.component_id.to_str()}, "
            f"component_type={self.component_type}, "
            f"state={component_state_to_str(self.state)}, "
            f"config={self.config}, "
            f"event_id={self._event_id.to_str()})"
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"trader_id={self.trader_id.to_str()}, "
            f"component_id={self.component_id.to_str()}, "
            f"component_type={self.component_type}, "
            f"state={component_state_to_str(self.state)}, "
            f"config={self.config}, "
            f"event_id={self._event_id.to_str()}, "
            f"ts_init={self._ts_init})"
        )

    @property
    def id(self) -> UUID4:
        """
        The event message identifier.

        Returns
        -------
        UUID4

        """
        return self._event_id

    @property
    def ts_event(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the event occurred.

        Returns
        -------
        int

        """
        return self._ts_event

    @property
    def ts_init(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the object was initialized.

        Returns
        -------
        int

        """
        return self._ts_init

    @staticmethod
    cdef ComponentStateChanged from_dict_c(dict values):
        Condition.not_none(values, "values")
        return ComponentStateChanged(
            trader_id=TraderId(values["trader_id"]),
            component_id=ComponentId(values["component_id"]),
            component_type=values["component_type"],
            state=component_state_from_str(values["state"]),
            config=values["config"],
            event_id=UUID4.from_str_c(values["event_id"]),
            ts_event=values["ts_event"],
            ts_init=values["ts_init"],
        )

    @staticmethod
    cdef dict to_dict_c(ComponentStateChanged obj):
        Condition.not_none(obj, "obj")
        return {
            "type": "ComponentStateChanged",
            "trader_id": obj.trader_id.to_str(),
            "component_id": obj.component_id.to_str(),
            "component_type": obj.component_type,
            "state": component_state_to_str(obj.state),
            "config": obj.config,
            "event_id": obj._event_id.to_str(),
            "ts_event": obj._ts_event,
            "ts_init": obj._ts_init,
        }

    @staticmethod
    def from_dict(dict values) -> ComponentStateChanged:
        """
        Return a component state changed event from the given dict values.

        Parameters
        ----------
        values : dict[str, object]
            The values for initialization.

        Returns
        -------
        ComponentStateChanged

        """
        return ComponentStateChanged.from_dict_c(values)

    @staticmethod
    def to_dict(ComponentStateChanged obj):
        """
        Return a dictionary representation of this object.

        Returns
        -------
        dict[str, object]

        """
        return ComponentStateChanged.to_dict_c(obj)


cdef class RiskEvent(Event):
    """
    The base class for all risk events.

    Parameters
    ----------
    trader_id : TraderId
        The trader ID associated with the event.
    event_id : UUID4
        The event ID.
    ts_event : uint64_t
        UNIX timestamp (nanoseconds) when the component state event occurred.
    ts_init : uint64_t
        UNIX timestamp (nanoseconds) when the object was initialized.
    """

    def __init__(
        self,
        TraderId trader_id not None,
        UUID4 event_id not None,
        uint64_t ts_event,
        uint64_t ts_init,
    ) -> None:
        self.trader_id = trader_id
        self._event_id = event_id
        self._ts_event = ts_event
        self._ts_init = ts_init

    def __eq__(self, Event other) -> bool:
        return self._event_id == other.id

    def __hash__(self) -> int:
        return hash(self._event_id)

    @property
    def id(self) -> UUID4:
        """
        The event message identifier.

        Returns
        -------
        UUID4

        """
        return self._event_id

    @property
    def ts_event(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the event occurred.

        Returns
        -------
        int

        """
        return self._ts_event

    @property
    def ts_init(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the object was initialized.

        Returns
        -------
        int

        """
        return self._ts_init


cdef class TradingStateChanged(RiskEvent):
    """
    Represents an event where trading state has changed at the `RiskEngine`.

    Parameters
    ----------
    trader_id : TraderId
        The trader ID associated with the event.
    state : TradingState
        The trading state for the event.
    config : dict[str, Any]
        The configuration of the risk engine.
    event_id : UUID4
        The event ID.
    ts_event : uint64_t
        UNIX timestamp (nanoseconds) when the component state event occurred.
    ts_init : uint64_t
        UNIX timestamp (nanoseconds) when the object was initialized.
    """

    def __init__(
        self,
        TraderId trader_id not None,
        TradingState state,
        dict config not None,
        UUID4 event_id not None,
        uint64_t ts_event,
        uint64_t ts_init,
    ) -> None:
        self.trader_id = trader_id
        self.state = state
        self.config = config
        self._event_id = event_id
        self._ts_event = ts_event
        self._ts_init = ts_init

    def __str__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"trader_id={self.trader_id.to_str()}, "
            f"state={trading_state_to_str(self.state)}, "
            f"config={self.config}, "
            f"event_id={self._event_id.to_str()})"
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"trader_id={self.trader_id.to_str()}, "
            f"state={trading_state_to_str(self.state)}, "
            f"config={self.config}, "
            f"event_id={self._event_id.to_str()}, "
            f"ts_init={self._ts_init})"
        )

    @property
    def id(self) -> UUID4:
        """
        The event message identifier.

        Returns
        -------
        UUID4

        """
        return self._event_id

    @property
    def ts_event(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the event occurred.

        Returns
        -------
        int

        """
        return self._ts_event

    @property
    def ts_init(self) -> int:
        """
        UNIX timestamp (nanoseconds) when the object was initialized.

        Returns
        -------
        int

        """
        return self._ts_init

    @staticmethod
    cdef TradingStateChanged from_dict_c(dict values):
        Condition.not_none(values, "values")
        return TradingStateChanged(
            trader_id=TraderId(values["trader_id"]),
            state=trading_state_from_str(values["state"]),
            config=values["config"],
            event_id=UUID4.from_str_c(values["event_id"]),
            ts_event=values["ts_event"],
            ts_init=values["ts_init"],
        )

    @staticmethod
    cdef dict to_dict_c(TradingStateChanged obj):
        Condition.not_none(obj, "obj")

        return {
            "type": "TradingStateChanged",
            "trader_id": obj.trader_id.to_str(),
            "state": trading_state_to_str(obj.state),
            "config": obj.config,
            "event_id": obj._event_id.to_str(),
            "ts_event": obj._ts_event,
            "ts_init": obj._ts_init,
        }

    @staticmethod
    def from_dict(dict values) -> TradingStateChanged:
        """
        Return a trading state changed event from the given dict values.

        Parameters
        ----------
        values : dict[str, object]
            The values for initialization.

        Returns
        -------
        TradingStateChanged

        """
        return TradingStateChanged.from_dict_c(values)

    @staticmethod
    def to_dict(TradingStateChanged obj):
        """
        Return a dictionary representation of this object.

        Returns
        -------
        dict[str, object]

        """
        return TradingStateChanged.to_dict_c(obj)
```


---

## Overview

This file is located at `nautilus_trader/common/messages.pyx` within the repository.

**Functions defined:** __init__, __eq__, __hash__, __str__, __repr__, from_dict, to_dict, __init__, __eq__, __hash__ and 21 more

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `__init__(
        self,
        TraderId trader_id not None,
        Identifier component_id not None,
        UUID4 command_id not None,
        uint64_t ts_init,
        str reason = None,
        UUID4 correlation_id = None,
    )`


#### `__eq__(self, Command other)`


#### `__hash__(self)`


#### `__str__(self)`


#### `__repr__(self)`


#### `from_dict(dict values)`


#### `to_dict(ShutdownSystem obj)`


#### `__init__(
        self,
        TraderId trader_id not None,
        Identifier component_id not None,
        str component_type not None,
        ComponentState state,
        dict config not None,
        UUID4 event_id not None,
        uint64_t ts_event,
        uint64_t ts_init,
    )`


#### `__eq__(self, Event other)`


#### `__hash__(self)`


#### `__str__(self)`


#### `__repr__(self)`


#### `id(self)`


#### `ts_event(self)`


#### `ts_init(self)`


#### `from_dict(dict values)`


#### `to_dict(ComponentStateChanged obj)`


#### `__init__(
        self,
        TraderId trader_id not None,
        UUID4 event_id not None,
        uint64_t ts_event,
        uint64_t ts_init,
    )`


#### `__eq__(self, Event other)`


#### `__hash__(self)`


#### `id(self)`


#### `ts_event(self)`


#### `ts_init(self)`


#### `__init__(
        self,
        TraderId trader_id not None,
        TradingState state,
        dict config not None,
        UUID4 event_id not None,
        uint64_t ts_event,
        uint64_t ts_init,
    )`


#### `__str__(self)`


#### `__repr__(self)`


#### `id(self)`


#### `ts_event(self)`


#### `ts_init(self)`


#### `from_dict(dict values)`


#### `to_dict(TradingStateChanged obj)`


### Imports

- `import decimal`
- `import json`
- `import re`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `import decimal`
- `import json`
- `import re`

**Directory:** `nautilus_trader/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


