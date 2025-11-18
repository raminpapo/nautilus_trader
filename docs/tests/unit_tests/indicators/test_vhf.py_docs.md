# Documentation: test_vhf.py

## File Metadata

- **Path**: `tests/unit_tests/indicators/test_vhf.py`
- **Size**: 2,979 bytes
- **Lines**: 84
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

from nautilus_trader.indicators import VerticalHorizontalFilter
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestVerticalHorizontalFilter:
    def setup(self):
        # Fixture Setup
        self.period = 10
        self.vhf = VerticalHorizontalFilter(period=self.period)

    def test_init(self):
        assert not self.vhf.initialized
        assert not self.vhf.has_inputs
        assert self.vhf.period == self.period
        assert self.vhf.value == 0

    def test_name_returns_expected_string(self):
        assert self.vhf.name == "VerticalHorizontalFilter"

    def test_handle_bar_updates_indicator(self):
        for _ in range(self.period):
            self.vhf.handle_bar(TestDataStubs.bar_5decimal())

        assert self.vhf.has_inputs
        assert self.vhf.value == 0

    def test_value_with_one_input(self):
        self.vhf.update_raw(56.87)

        assert self.vhf.value == 0

    def test_value_with_twenty_inputs(self):
        self.vhf.update_raw(56.87)
        self.vhf.update_raw(56.96)
        self.vhf.update_raw(57.17)
        self.vhf.update_raw(57.54)
        self.vhf.update_raw(57.88)
        self.vhf.update_raw(57.85)
        self.vhf.update_raw(57.86)
        self.vhf.update_raw(57.97)
        self.vhf.update_raw(58.07)
        self.vhf.update_raw(58.04)
        self.vhf.update_raw(57.96)
        self.vhf.update_raw(57.98)
        self.vhf.update_raw(58.05)
        self.vhf.update_raw(57.94)
        self.vhf.update_raw(57.99)
        self.vhf.update_raw(58.11)
        self.vhf.update_raw(58.22)
        self.vhf.update_raw(58.19)
        self.vhf.update_raw(58.04)
        self.vhf.update_raw(58.02)

        assert self.vhf.value == 0.36842105263158487

    def test_reset(self):
        self.vhf.update_raw(56.87)

        self.vhf.reset()

        assert not self.vhf.initialized
        assert not self.vhf.has_inputs
        assert self.vhf.period == self.period
        assert self.vhf.value == 0

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestVerticalHorizontalFilter`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestVerticalHorizontalFilter`
**Imports**: `nautilus_trader.indicators`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.data`

## Related Files

This file is located in `tests/unit_tests/indicators/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/indicators/test_vhf.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.453582Z*
