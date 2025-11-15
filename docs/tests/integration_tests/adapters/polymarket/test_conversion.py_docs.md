# Documentation: `tests/integration_tests/adapters/polymarket/test_conversion.py`
**Generated:** 2025-11-15T19:40:07.936337Z
**File Size:** 2312 bytes
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

- **Path:** `tests/integration_tests/adapters/polymarket/test_conversion.py`
- **Size:** 2,312 bytes
- **Lines:** 65
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Functions:** 3

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


---

## Overview

This file is located at `tests/integration_tests/adapters/polymarket/test_conversion.py` within the repository.

**Functions defined:** test_usdc_from_units, test_convert_tif_to_polymarket_order_type, test_convert_tif_invalid_time_in_force

**Import statements:** 6


---

## Detailed Analysis

### Functions

#### `test_usdc_from_units(units: int, expected_amount: float)`


#### `test_convert_tif_to_polymarket_order_type(
    time_in_force: TimeInForce,
    expected_order_type: str,
)`


#### `test_convert_tif_invalid_time_in_force()`


### Imports

- `from decimal import Decimal`
- `import pytest`
- `from nautilus_trader.adapters.polymarket.common.conversion import usdce_from_units`
- `from nautilus_trader.adapters.polymarket.http.conversion import convert_tif_to_polymarket_order_type`
- `from nautilus_trader.model.currencies import USDC_POS`
- `from nautilus_trader.model.enums import TimeInForce`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.polymarket.test_conversion import test_usdc_from_units
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `import pytest`
- `from nautilus_trader.adapters.polymarket.common.conversion import usdce_from_units`
- `from nautilus_trader.adapters.polymarket.http.conversion import convert_tif_to_polymarket_order_type`
- `from nautilus_trader.model.currencies import USDC_POS`
- `from nautilus_trader.model.enums import TimeInForce`

**Directory:** `tests/integration_tests/adapters/polymarket`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


