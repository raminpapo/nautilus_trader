# Documentation: types_pyo3.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/rust/types_pyo3.py`
- **Size**: 1,879 bytes
- **Lines**: 40
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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestTypesProviderPyo3`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `TestTypesProviderPyo3`
**Imports**: `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.test_kit.rust.identifiers_pyo3`

## Related Files

This file is located in `nautilus_trader/test_kit/rust/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/rust/types_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.991177Z*
