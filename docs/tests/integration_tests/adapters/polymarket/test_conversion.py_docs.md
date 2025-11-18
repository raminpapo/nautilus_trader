# Documentation: test_conversion.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/polymarket/test_conversion.py`
- **Size**: 2,312 bytes
- **Lines**: 66
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

from decimal import Decimal

import pytest

from nautilus_trader.adapters.polymarket.common.conversion import usdce_from_units
from nautilus_trader.adapters.polymarket.http.conversion import convert_tif_to_polymarket_order_type
from nautilus_trader.model.currencies import USDC_POS
from nautilus_trader.model.enums import TimeInForce


@pytest.mark.parametrize(
    ("units", "expected_amount"),
    [
        [1, Decimal("0.000001")],
        [1000000, Decimal("1.000000")],
    ],
)
def test_usdc_from_units(units: int, expected_amount: float) -> None:
    # Arrange, Act
    usdce = usdce_from_units(units)

    # Assert
    assert usdce.currency == USDC_POS
    assert usdce.as_decimal() == expected_amount


@pytest.mark.parametrize(
    ("time_in_force", "expected_order_type"),
    [
        [TimeInForce.GTC, "GTC"],
        [TimeInForce.GTD, "GTD"],
        [TimeInForce.FOK, "FOK"],
        [TimeInForce.IOC, "FAK"],  # IOC maps to FAK
    ],
)
def test_convert_tif_to_polymarket_order_type(
    time_in_force: TimeInForce,
    expected_order_type: str,
) -> None:
    # Arrange, Act
    result = convert_tif_to_polymarket_order_type(time_in_force)

    # Assert
    assert result == expected_order_type


def test_convert_tif_invalid_time_in_force() -> None:
    # Arrange, Act & Assert
    with pytest.raises(ValueError, match="invalid `TimeInForce` for conversion"):
        convert_tif_to_polymarket_order_type(TimeInForce.DAY)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`test_usdc_from_units()`**: Function defined in this file
- **`test_convert_tif_to_polymarket_order_type()`**: Function defined in this file
- **`test_convert_tif_invalid_time_in_force()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `test_convert_tif_invalid_time_in_force`, `test_convert_tif_to_polymarket_order_type`, `test_usdc_from_units`
**Imports**: `decimal`, `nautilus_trader.adapters.polymarket.common.conversion`, `nautilus_trader.adapters.polymarket.http.conversion`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/polymarket/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/polymarket/test_conversion.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.162900Z*
