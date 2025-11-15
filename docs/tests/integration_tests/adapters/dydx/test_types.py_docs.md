# Documentation: `tests/integration_tests/adapters/dydx/test_types.py`
**Generated:** 2025-11-15T19:40:07.768154Z
**File Size:** 1621 bytes
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

- **Path:** `tests/integration_tests/adapters/dydx/test_types.py`
- **Size:** 1,621 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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


---

## Overview

This file is located at `tests/integration_tests/adapters/dydx/test_types.py` within the repository.

**Functions defined:** test_dydx_oracle_price

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_dydx_oracle_price(instrument_id: InstrumentId)`


### Imports

- `from decimal import Decimal`
- `from nautilus_trader.adapters.dydx.common.types import DYDXOraclePrice`
- `from nautilus_trader.model.identifiers import InstrumentId`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.dydx.test_types import test_dydx_oracle_price
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from nautilus_trader.adapters.dydx.common.types import DYDXOraclePrice`
- `from nautilus_trader.model.identifiers import InstrumentId`

**Directory:** `tests/integration_tests/adapters/dydx`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


