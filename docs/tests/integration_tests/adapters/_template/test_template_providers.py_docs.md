# Documentation: `tests/integration_tests/adapters/_template/test_template_providers.py`
**Generated:** 2025-11-15T19:40:05.564582Z
**File Size:** 1262 bytes
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

- **Path:** `tests/integration_tests/adapters/_template/test_template_providers.py`
- **Size:** 1,262 bytes
- **Lines:** 38
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
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

from nautilus_trader.adapters._template.providers import TemplateInstrumentProvider


pytestmark = pytest.mark.skip(reason="template")


@pytest.fixture()
def instrument_provider():
    return TemplateInstrumentProvider()


def test_load_all_async(instrument_provider):
    pass


def test_load_all(instrument_provider):
    pass


def test_load(instrument_provider):
    pass
```


---

## Overview

This file is located at `tests/integration_tests/adapters/_template/test_template_providers.py` within the repository.

**Functions defined:** instrument_provider, test_load_all_async, test_load_all, test_load

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `instrument_provider()`


#### `test_load_all_async(instrument_provider)`


#### `test_load_all(instrument_provider)`


#### `test_load(instrument_provider)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters._template.providers import TemplateInstrumentProvider`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters._template.test_template_providers import instrument_provider
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters._template.providers import TemplateInstrumentProvider`

**Directory:** `tests/integration_tests/adapters/_template`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


