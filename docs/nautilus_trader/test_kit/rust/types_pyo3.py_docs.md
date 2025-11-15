# Documentation: `nautilus_trader/test_kit/rust/types_pyo3.py`
**Generated:** 2025-11-15T19:40:05.362839Z
**File Size:** 1879 bytes
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

- **Path:** `nautilus_trader/test_kit/rust/types_pyo3.py`
- **Size:** 1,879 bytes
- **Lines:** 39
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 1
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

from nautilus_trader.core.nautilus_pyo3 import AccountBalance
from nautilus_trader.core.nautilus_pyo3 import Currency
from nautilus_trader.core.nautilus_pyo3 import InstrumentId
from nautilus_trader.core.nautilus_pyo3 import MarginBalance
from nautilus_trader.core.nautilus_pyo3 import Money
from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3


class TestTypesProviderPyo3:
    @staticmethod
    def account_balance(
        total: Money = Money.from_str("1525000 USD"),
        locked: Money = Money.from_str("25000 USD"),
        free: Money = Money.from_str("1500000 USD"),
    ) -> AccountBalance:
        return AccountBalance(total, locked, free)

    @staticmethod
    def margin_balance(
        initial: Money = Money(1, Currency.from_str("USD")),
        maintenance: Money = Money(1, Currency.from_str("USD")),
        instrument_id: InstrumentId = TestIdProviderPyo3.audusd_id(),
    ) -> MarginBalance:
        return MarginBalance(initial, maintenance, instrument_id)
```


---

## Overview

This file is located at `nautilus_trader/test_kit/rust/types_pyo3.py` within the repository.

**Classes defined:** TestTypesProviderPyo3

**Functions defined:** account_balance, margin_balance

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `TestTypesProviderPyo3`


### Functions

#### `account_balance(
        total: Money = Money.from_str("1525000 USD")`


#### `margin_balance(
        initial: Money = Money(1, Currency.from_str("USD")`


### Imports

- `from nautilus_trader.core.nautilus_pyo3 import AccountBalance`
- `from nautilus_trader.core.nautilus_pyo3 import Currency`
- `from nautilus_trader.core.nautilus_pyo3 import InstrumentId`
- `from nautilus_trader.core.nautilus_pyo3 import MarginBalance`
- `from nautilus_trader.core.nautilus_pyo3 import Money`
- `from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.rust.types_pyo3 import TestTypesProviderPyo3
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.nautilus_pyo3 import AccountBalance`
- `from nautilus_trader.core.nautilus_pyo3 import Currency`
- `from nautilus_trader.core.nautilus_pyo3 import InstrumentId`
- `from nautilus_trader.core.nautilus_pyo3 import MarginBalance`
- `from nautilus_trader.core.nautilus_pyo3 import Money`
- `from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3`

**Directory:** `nautilus_trader/test_kit/rust`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


