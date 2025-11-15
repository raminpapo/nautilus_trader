# Documentation: `tests/unit_tests/core/test_fsm.py`
**Generated:** 2025-11-15T19:40:09.081326Z
**File Size:** 2494 bytes
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

- **Path:** `tests/unit_tests/core/test_fsm.py`
- **Size:** 2,494 bytes
- **Lines:** 59
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
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

from nautilus_trader.common.component import ComponentFSMFactory
from nautilus_trader.common.enums import ComponentState
from nautilus_trader.common.enums import ComponentTrigger
from nautilus_trader.common.enums import component_state_to_str
from nautilus_trader.core.fsm import FiniteStateMachine
from nautilus_trader.core.fsm import InvalidStateTrigger


class TestFiniteStateMachine:
    def setup(self):
        # Fixture Setup
        self.fsm = FiniteStateMachine(
            state_transition_table=ComponentFSMFactory.get_state_transition_table(),
            initial_state=ComponentState.READY,
            state_parser=component_state_to_str,
        )

    def test_fsm_initialization(self):
        # Arrange, Act, Assert
        assert self.fsm.state == ComponentState.READY
        assert self.fsm.state_string == "READY"

    def test_trigger_with_invalid_transition_raises_exception(self):
        # Arrange
        fsm = FiniteStateMachine(
            state_transition_table=ComponentFSMFactory.get_state_transition_table(),
            initial_state=ComponentState.READY,
            state_parser=None,
            trigger_parser=None,
        )  # Invalid trigger will call parsers for ex msg

        # Act, Assert
        with pytest.raises(InvalidStateTrigger):
            fsm.trigger(ComponentState.RUNNING)

    def test_trigger_with_valid_transition_results_in_expected_state(self):
        # Arrange, Act
        self.fsm.trigger(ComponentTrigger.START)

        # Assert
        assert self.fsm.state == ComponentState.STARTING
        assert self.fsm.state_string == "STARTING"
```


---

## Overview

This file is located at `tests/unit_tests/core/test_fsm.py` within the repository.

**Classes defined:** TestFiniteStateMachine

**Functions defined:** setup, test_fsm_initialization, test_trigger_with_invalid_transition_raises_exception, test_trigger_with_valid_transition_results_in_expected_state

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `TestFiniteStateMachine`


### Functions

#### `setup(self)`


#### `test_fsm_initialization(self)`


#### `test_trigger_with_invalid_transition_raises_exception(self)`


#### `test_trigger_with_valid_transition_results_in_expected_state(self)`


### Imports

- `import pytest`
- `from nautilus_trader.common.component import ComponentFSMFactory`
- `from nautilus_trader.common.enums import ComponentState`
- `from nautilus_trader.common.enums import ComponentTrigger`
- `from nautilus_trader.common.enums import component_state_to_str`
- `from nautilus_trader.core.fsm import FiniteStateMachine`
- `from nautilus_trader.core.fsm import InvalidStateTrigger`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.core.test_fsm import TestFiniteStateMachine
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.common.component import ComponentFSMFactory`
- `from nautilus_trader.common.enums import ComponentState`
- `from nautilus_trader.common.enums import ComponentTrigger`
- `from nautilus_trader.common.enums import component_state_to_str`
- `from nautilus_trader.core.fsm import FiniteStateMachine`
- `from nautilus_trader.core.fsm import InvalidStateTrigger`

**Directory:** `tests/unit_tests/core`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


