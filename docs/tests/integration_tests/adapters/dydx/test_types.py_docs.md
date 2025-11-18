# Documentation: test_types.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/dydx/test_types.py`
- **Size**: 1,621 bytes
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
"""
Unit tests for the dYdX types.
"""

from decimal import Decimal

from nautilus_trader.adapters.dydx.common.types import DYDXOraclePrice
from nautilus_trader.model.identifiers import InstrumentId


def test_dydx_oracle_price(instrument_id: InstrumentId) -> None:
    """
    Test the DYDXOraclePrice type.
    """
    # Arrange
    data = DYDXOraclePrice(instrument_id=instrument_id, price=Decimal(5), ts_init=5, ts_event=6)

    # Act
    data_dict = data.to_dict()
    data_from_dict = DYDXOraclePrice.from_dict(data_dict)

    # Assert
    assert data.instrument_id == data_from_dict.instrument_id
    assert data.price == data_from_dict.price
    assert data.ts_event == data_from_dict.ts_event
    assert data.ts_init == data_from_dict.ts_init

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_dydx_oracle_price()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `test_dydx_oracle_price`
**Imports**: `decimal`, `nautilus_trader.adapters.dydx.common.types`, `nautilus_trader.model.identifiers`

## Related Files

This file is located in `tests/integration_tests/adapters/dydx/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/dydx/test_types.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.853329Z*
