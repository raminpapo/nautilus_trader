# Documentation: test_providers.py

## File Metadata

- **Path**: `tests/unit_tests/common/test_providers.py`
- **Size**: 1,510 bytes
- **Lines**: 41
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

from nautilus_trader.common.providers import InstrumentProvider
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


AUDUSD = TestIdStubs.audusd_id()


class TestInstrumentProvider:
    def setup(self):
        # Fixture Setup
        self.provider = InstrumentProvider()

    def test_get_all_when_no_instruments_returns_empty_dict(self):
        # Arrange, Act
        result = self.provider.get_all()

        # Assert
        assert result == {}

    def test_find_when_no_instruments_returns_none(self):
        # Arrange, Act
        result = self.provider.find(AUDUSD)

        # Assert
        assert result is None

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestInstrumentProvider`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `TestInstrumentProvider`
**Imports**: `nautilus_trader.common.providers`, `nautilus_trader.test_kit.stubs.identifiers`

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
pytest tests/unit_tests/common/test_providers.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.295250Z*
