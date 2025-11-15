# Documentation: `examples/other/state_machine/run_example.py`
**Generated:** 2025-11-15T19:40:03.954410Z
**File Size:** 5230 bytes
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

- **Path:** `examples/other/state_machine/run_example.py`
- **Size:** 5,230 bytes
- **Lines:** 125
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 2
- **Functions:** 5

---

## Source Code

```python
#!/usr/bin/env python3
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

from enum import IntEnum  # IntEnum is used to create enumerated types with integer values

from nautilus_trader.core.fsm import FiniteStateMachine
from nautilus_trader.core.fsm import InvalidStateTrigger


if __name__ == "__main__":

    # Step 1: Define all possible states of our application.
    # Each state represents a distinct condition the application can be in.
    # We use IntEnum to ensure each state has an integer value, which is required by Nautilus FSM
    # (i.e. similar StrEnum is not supported by FSM now)

    class AppState(IntEnum):

        INITIALIZED = 0  # Initial setup complete
        READY = 1  # Ready to start operations
        ACTIVE = 2  # Currently running/operating
        PAUSED = 3  # Temporarily paused
        STOPPED = 4  # Operations terminated

        @staticmethod
        def parse_from_code_to_str(code: int) -> str:
            try:
                return AppState(code).name
            except ValueError:
                raise ValueError(f"Invalid code '{code}' for AppState.")

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"{self.name} ({self.value})"

    # Step 2: Define all possible triggers (actions / commands) that can cause state transitions
    # between application's states. Only IntEnum is supported (not StrEnum).

    class AppTrigger(IntEnum):

        START = 0  # Begin operations
        PAUSE = 1  # Temporarily suspend operations
        RESUME = 2  # Continue operations after being paused
        STOP = 3  # End operations

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"{self.name} ({self.value})"

    # Step 3: Define the valid state transitions
    # This dictionary defines which state transitions are allowed and what their results should be
    # Format: (CURRENT_STATE, TRIGGER_ACTION): NEW_STATE
    # Any combination not listed here is considered invalid and will raise an exception

    STATE_TRANSITIONS: dict[tuple[AppState, AppTrigger], AppState] = {
        (AppState.READY, AppTrigger.START): AppState.ACTIVE,
        (AppState.ACTIVE, AppTrigger.PAUSE): AppState.PAUSED,
        (AppState.ACTIVE, AppTrigger.STOP): AppState.STOPPED,
        (AppState.PAUSED, AppTrigger.RESUME): AppState.ACTIVE,
        (AppState.PAUSED, AppTrigger.STOP): AppState.STOPPED,
    }

    # -----------------------------------------------
    # Example: Creating and Using State Machine
    # -----------------------------------------------

    # Create a new FSM instance with our defined states and transitions
    fsm = FiniteStateMachine(
        state_transition_table=STATE_TRANSITIONS,  # Our defined valid transitions
        initial_state=AppState.READY,  # Starting state of the FSM
        # Parsing function required to make work `fsm.state_string`
        state_parser=AppState.parse_from_code_to_str,
    )

    # -----------------------------------------------
    # Demo: Using the State Machine
    # The main operations are:
    # 1. Checking current state (fsm.state_string)
    # 2. Triggering state changes (fsm.trigger())
    # -----------------------------------------------

    # Print initial state
    print(f"Current (initial) state: {fsm.state_string}")

    # Demonstrate a series of valid state transitions
    print(f"Invoking trigger: {AppTrigger.START}")
    fsm.trigger(AppTrigger.START)  # READY -> ACTIVE
    print(f"Current state: {fsm.state_string}")

    print(f"Invoking trigger: {AppTrigger.PAUSE}")
    fsm.trigger(AppTrigger.PAUSE)  # ACTIVE -> PAUSED
    print(f"Current state: {fsm.state_string}")

    print(f"Invoking trigger: {AppTrigger.RESUME}")
    fsm.trigger(AppTrigger.RESUME)  # PAUSED -> ACTIVE
    print(f"Current state: {fsm.state_string}")

    print(f"Invoking trigger: {AppTrigger.STOP}")
    fsm.trigger(AppTrigger.STOP)  # ACTIVE -> STOPPED
    print(f"Current state: {fsm.state_string}")

    # Demonstrate invalid state transition
    # Once STOPPED, we cannot RESUME (this transition isn't in our STATE_TRANSITIONS table)
    try:
        print(f"Invoking trigger: {AppTrigger.RESUME}")
        fsm.trigger(AppTrigger.RESUME)  # This will fail - cannot RESUME from STOPPED state
    except InvalidStateTrigger:
        print("We got expected exception: InvalidStateTrigger")
```


---

## Overview

This file is located at `examples/other/state_machine/run_example.py` within the repository.

**Classes defined:** AppState, AppTrigger

**Functions defined:** parse_from_code_to_str, __str__, __repr__, __str__, __repr__

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `AppState`

**Inherits from:** IntEnum


#### `AppTrigger`

**Inherits from:** IntEnum


### Functions

#### `parse_from_code_to_str(code: int)`


#### `__str__(self)`


#### `__repr__(self)`


#### `__str__(self)`


#### `__repr__(self)`


### Imports

- `from enum import IntEnum  # IntEnum is used to create enumerated types with integer values`
- `from nautilus_trader.core.fsm import FiniteStateMachine`
- `from nautilus_trader.core.fsm import InvalidStateTrigger`


---

## Usage Examples

### Importing

```python
from examples.other.state_machine.run_example import AppState
```


---

## Related Files

This file imports from the following modules:

- `from enum import IntEnum  # IntEnum is used to create enumerated types with integer values`
- `from nautilus_trader.core.fsm import FiniteStateMachine`
- `from nautilus_trader.core.fsm import InvalidStateTrigger`

**Directory:** `examples/other/state_machine`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


