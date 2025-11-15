# Documentation: `tests/unit_tests/common/test_enums.py`
**Generated:** 2025-11-15T19:40:09.049225Z
**File Size:** 5382 bytes
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

- **Path:** `tests/unit_tests/common/test_enums.py`
- **Size:** 5,382 bytes
- **Lines:** 130
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Classes:** 2
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
from nautilus_trader.common.enums import ComponentTrigger
from nautilus_trader.common.enums import component_state_from_str
from nautilus_trader.common.enums import component_state_to_str
from nautilus_trader.common.enums import component_trigger_from_str
from nautilus_trader.common.enums import component_trigger_to_str


class TestComponentState:
    @pytest.mark.parametrize(
        ("enum", "expected"),
        [
            [ComponentState.PRE_INITIALIZED, "PRE_INITIALIZED"],
            [ComponentState.READY, "READY"],
            [ComponentState.STARTING, "STARTING"],
            [ComponentState.RUNNING, "RUNNING"],
            [ComponentState.STOPPING, "STOPPING"],
            [ComponentState.STOPPED, "STOPPED"],
            [ComponentState.RESUMING, "RESUMING"],
            [ComponentState.RESETTING, "RESETTING"],
            [ComponentState.DISPOSING, "DISPOSING"],
            [ComponentState.DISPOSED, "DISPOSED"],
            [ComponentState.DEGRADING, "DEGRADING"],
            [ComponentState.DEGRADED, "DEGRADED"],
            [ComponentState.FAULTING, "FAULTING"],
            [ComponentState.FAULTED, "FAULTED"],
        ],
    )
    def test_component_state_to_str(self, enum, expected):
        # Arrange, Act
        result = component_state_to_str(enum)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        ("string", "expected"),
        [
            ["PRE_INITIALIZED", ComponentState.PRE_INITIALIZED],
            ["READY", ComponentState.READY],
            ["STARTING", ComponentState.STARTING],
            ["RUNNING", ComponentState.RUNNING],
            ["STOPPING", ComponentState.STOPPING],
            ["STOPPED", ComponentState.STOPPED],
            ["RESUMING", ComponentState.RESUMING],
            ["RESETTING", ComponentState.RESETTING],
            ["DISPOSING", ComponentState.DISPOSING],
            ["DISPOSED", ComponentState.DISPOSED],
            ["DEGRADING", ComponentState.DEGRADING],
            ["DEGRADED", ComponentState.DEGRADED],
            ["FAULTING", ComponentState.FAULTING],
            ["FAULTED", ComponentState.FAULTED],
        ],
    )
    def test_component_state_from_str(self, string, expected):
        # Arrange, Act
        result = component_state_from_str(string)

        # Assert
        assert result == expected


class TestComponentTrigger:
    @pytest.mark.parametrize(
        ("enum", "expected"),
        [
            [ComponentTrigger.INITIALIZE, "INITIALIZE"],
            [ComponentTrigger.START, "START"],
            [ComponentTrigger.START_COMPLETED, "START_COMPLETED"],
            [ComponentTrigger.STOP, "STOP"],
            [ComponentTrigger.STOP_COMPLETED, "STOP_COMPLETED"],
            [ComponentTrigger.RESUME, "RESUME"],
            [ComponentTrigger.RESUME, "RESUME"],
            [ComponentTrigger.RESET, "RESET"],
            [ComponentTrigger.DISPOSE, "DISPOSE"],
            [ComponentTrigger.DISPOSE_COMPLETED, "DISPOSE_COMPLETED"],
            [ComponentTrigger.DEGRADE, "DEGRADE"],
            [ComponentTrigger.DEGRADE_COMPLETED, "DEGRADE_COMPLETED"],
            [ComponentTrigger.FAULT, "FAULT"],
            [ComponentTrigger.FAULT_COMPLETED, "FAULT_COMPLETED"],
        ],
    )
    def test_component_trigger_to_str(self, enum, expected):
        # Arrange, Act
        result = component_trigger_to_str(enum)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        ("string", "expected"),
        [
            ["INITIALIZE", ComponentTrigger.INITIALIZE],
            ["START", ComponentTrigger.START],
            ["START_COMPLETED", ComponentTrigger.START_COMPLETED],
            ["STOP", ComponentTrigger.STOP],
            ["STOP_COMPLETED", ComponentTrigger.STOP_COMPLETED],
            ["RESUME", ComponentTrigger.RESUME],
            ["RESET", ComponentTrigger.RESET],
            ["DISPOSE", ComponentTrigger.DISPOSE],
            ["DISPOSE_COMPLETED", ComponentTrigger.DISPOSE_COMPLETED],
            ["DEGRADE", ComponentTrigger.DEGRADE],
            ["DEGRADE_COMPLETED", ComponentTrigger.DEGRADE_COMPLETED],
            ["FAULT", ComponentTrigger.FAULT],
            ["FAULT_COMPLETED", ComponentTrigger.FAULT_COMPLETED],
        ],
    )
    def test_component_trigger_from_str(self, string, expected):
        # Arrange, Act
        result = component_trigger_from_str(string)

        # Assert
        assert result == expected
```


---

## Overview

This file is located at `tests/unit_tests/common/test_enums.py` within the repository.

**Classes defined:** TestComponentState, TestComponentTrigger

**Functions defined:** test_component_state_to_str, test_component_state_from_str, test_component_trigger_to_str, test_component_trigger_from_str

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `TestComponentState`


#### `TestComponentTrigger`


### Functions

#### `test_component_state_to_str(self, enum, expected)`


#### `test_component_state_from_str(self, string, expected)`


#### `test_component_trigger_to_str(self, enum, expected)`


#### `test_component_trigger_from_str(self, string, expected)`


### Imports

- `import pytest`
- `from nautilus_trader.common.enums import ComponentState`
- `from nautilus_trader.common.enums import ComponentTrigger`
- `from nautilus_trader.common.enums import component_state_from_str`
- `from nautilus_trader.common.enums import component_state_to_str`
- `from nautilus_trader.common.enums import component_trigger_from_str`
- `from nautilus_trader.common.enums import component_trigger_to_str`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_enums import TestComponentState
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.common.enums import ComponentState`
- `from nautilus_trader.common.enums import ComponentTrigger`
- `from nautilus_trader.common.enums import component_state_from_str`
- `from nautilus_trader.common.enums import component_state_to_str`
- `from nautilus_trader.common.enums import component_trigger_from_str`
- `from nautilus_trader.common.enums import component_trigger_to_str`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


