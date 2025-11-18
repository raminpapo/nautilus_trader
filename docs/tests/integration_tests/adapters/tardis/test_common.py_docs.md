# Documentation: test_common.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/tardis/test_common.py`
- **Size**: 1,216 bytes
- **Lines**: 30
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

from nautilus_trader.core import nautilus_pyo3


def test_normalize_symbol_str() -> None:
    # Arrange, Act
    result = nautilus_pyo3.tardis_normalize_symbol_str(
        symbol="BTCUSDT",
        exchange="binance-futures",
        instrument_type="perpetual",
        is_inverse=False,
    )

    # Assert
    assert result == "BTCUSDT-PERP"

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_normalize_symbol_str()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `test_normalize_symbol_str`
**Imports**: `nautilus_trader.core`

## Related Files

This file is located in `tests/integration_tests/adapters/tardis/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/tardis/test_common.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.213481Z*
