# Documentation: test_template_providers.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/_template/test_template_providers.py`
- **Size**: 1,260 bytes
- **Lines**: 39
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

from nautilus_trader.adapters._template.providers import TemplateInstrumentProvider


pytestmark = pytest.mark.skip(reason="template")


@pytest.fixture
def instrument_provider():
    return TemplateInstrumentProvider()


def test_load_all_async(instrument_provider):
    pass


def test_load_all(instrument_provider):
    pass


def test_load(instrument_provider):
    pass

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`instrument_provider()`**: Function defined in this file
- **`test_load_all_async()`**: Function defined in this file
- **`test_load_all()`**: Function defined in this file
- **`test_load()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `instrument_provider`, `test_load`, `test_load_all`, `test_load_all_async`
**Imports**: `nautilus_trader.adapters._template.providers`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/_template/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/_template/test_template_providers.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.194776Z*
