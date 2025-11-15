# Documentation: `tests/unit_tests/common/test_config.py`
**Generated:** 2025-11-15T19:40:09.046263Z
**File Size:** 2050 bytes
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

- **Path:** `tests/unit_tests/common/test_config.py`
- **Size:** 2,050 bytes
- **Lines:** 62
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Functions:** 2

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

from nautilus_trader.common.config import InstrumentProviderConfig
from nautilus_trader.config import ActorFactory
from nautilus_trader.config import ImportableActorConfig
from nautilus_trader.test_kit.mocks.actors import MockActor


@pytest.mark.parametrize(
    "filters",
    [
        None,
        {},
        {"A": 1, "B": 2, "C": 3},
    ],
)
def test_instrument_provider_config_hash(filters: dict | None) -> None:
    # Arrange
    config = InstrumentProviderConfig(filters=filters)

    # Act
    result = hash(config)

    # Assert
    assert isinstance(result, int)


def test_create_actor_from_importable_config() -> None:
    # Arrange
    config = {
        "component_id": "MyActor",
    }
    importable = ImportableActorConfig(
        actor_path="nautilus_trader.test_kit.mocks.actors:MockActor",
        config_path="nautilus_trader.test_kit.mocks.actors:MockActorConfig",
        config=config,
    )

    # Act
    actor = ActorFactory.create(importable)

    # Assert
    assert isinstance(actor, MockActor)
    assert (
        repr(actor.config)
        == "MockActorConfig(component_id='MyActor', log_events=True, log_commands=True)"
    )
```


---

## Overview

This file is located at `tests/unit_tests/common/test_config.py` within the repository.

**Functions defined:** test_instrument_provider_config_hash, test_create_actor_from_importable_config

**Import statements:** 5


---

## Detailed Analysis

### Functions

#### `test_instrument_provider_config_hash(filters: dict | None)`


#### `test_create_actor_from_importable_config()`


### Imports

- `import pytest`
- `from nautilus_trader.common.config import InstrumentProviderConfig`
- `from nautilus_trader.config import ActorFactory`
- `from nautilus_trader.config import ImportableActorConfig`
- `from nautilus_trader.test_kit.mocks.actors import MockActor`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_config import test_instrument_provider_config_hash
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.common.config import InstrumentProviderConfig`
- `from nautilus_trader.config import ActorFactory`
- `from nautilus_trader.config import ImportableActorConfig`
- `from nautilus_trader.test_kit.mocks.actors import MockActor`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


