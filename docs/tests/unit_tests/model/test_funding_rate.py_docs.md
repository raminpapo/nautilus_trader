# Documentation: `tests/unit_tests/model/test_funding_rate.py`
**Generated:** 2025-11-15T19:40:09.338191Z
**File Size:** 14385 bytes
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

- **Path:** `tests/unit_tests/model/test_funding_rate.py`
- **Size:** 14,385 bytes
- **Lines:** 388
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Classes:** 1
- **Functions:** 19

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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.data import FundingRateUpdate
from nautilus_trader.test_kit.providers import TestInstrumentProvider


BTCUSDT_PERP_BINANCE = TestInstrumentProvider.btcusdt_perp_binance()


class TestFundingRateUpdate:
    def test_fully_qualified_name(self):
        # Arrange, Act, Assert
        assert (
            FundingRateUpdate.fully_qualified_name()
            == "nautilus_trader.model.data:FundingRateUpdate"
        )

    def test_instantiation_with_required_fields_only(self):
        # Arrange, Act
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Assert
        assert funding_rate.instrument_id == BTCUSDT_PERP_BINANCE.id
        assert funding_rate.rate == Decimal("0.0001")
        assert funding_rate.next_funding_ns is None
        assert funding_rate.ts_event == 1_640_000_000_000_000_000
        assert funding_rate.ts_init == 1_640_000_000_000_000_000

    def test_instantiation_with_all_fields(self):
        # Arrange, Act
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Assert
        assert funding_rate.instrument_id == BTCUSDT_PERP_BINANCE.id
        assert funding_rate.rate == Decimal("0.0001")
        assert funding_rate.next_funding_ns == 1_640_000_100_000_000_000
        assert funding_rate.ts_event == 1_640_000_000_000_000_000
        assert funding_rate.ts_init == 1_640_000_000_000_000_000

    def test_hash_str_and_repr_minimal_fields(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act, Assert
        assert isinstance(hash(funding_rate), int)
        expected_str = (
            "FundingRateUpdate("
            "instrument_id=BTCUSDT-PERP.BINANCE, "
            "rate=0.0001, "
            "next_funding_ns=None, "
            "ts_event=1640000000000000000, "
            "ts_init=1640000000000000000)"
        )
        assert str(funding_rate) == expected_str
        assert repr(funding_rate) == expected_str

    def test_hash_str_and_repr_all_fields(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act, Assert
        assert isinstance(hash(funding_rate), int)
        expected_str = (
            "FundingRateUpdate("
            "instrument_id=BTCUSDT-PERP.BINANCE, "
            "rate=0.0001, "
            "next_funding_ns=1640000100000000000, "
            "ts_event=1640000000000000000, "
            "ts_init=1640000000000000000)"
        )
        assert str(funding_rate) == expected_str
        assert repr(funding_rate) == expected_str

    def test_equality(self):
        # Arrange
        funding_rate1 = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )
        funding_rate2 = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )
        funding_rate3 = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0003"),  # Different rate
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act, Assert
        assert funding_rate1 == funding_rate2
        assert funding_rate1 != funding_rate3
        assert hash(funding_rate1) == hash(funding_rate2)
        assert hash(funding_rate1) != hash(funding_rate3)

    def test_to_dict_minimal_fields(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.to_dict(funding_rate)

        # Assert
        assert result == {
            "type": "FundingRateUpdate",
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": Decimal("0.0001"),
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }

    def test_to_dict_all_fields(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.to_dict(funding_rate)

        # Assert
        assert result == {
            "type": "FundingRateUpdate",
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": Decimal("0.0001"),
            "next_funding_ns": 1_640_000_100_000_000_000,
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }

    def test_from_dict_minimal_fields(self):
        # Arrange
        values = {
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": Decimal("0.0001"),
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }

        # Act
        result = FundingRateUpdate.from_dict(values)

        # Assert
        assert result.instrument_id.value == "BTCUSDT-PERP.BINANCE"
        assert result.rate == Decimal("0.0001")
        assert result.next_funding_ns is None
        assert result.ts_event == 1_640_000_000_000_000_000
        assert result.ts_init == 1_640_000_000_000_000_000

    def test_from_dict_all_fields(self):
        # Arrange
        values = {
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": Decimal("0.0001"),
            "next_funding_ns": 1_640_000_100_000_000_000,
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }

        # Act
        result = FundingRateUpdate.from_dict(values)

        # Assert
        assert result.instrument_id.value == "BTCUSDT-PERP.BINANCE"
        assert result.rate == Decimal("0.0001")
        assert result.next_funding_ns == 1_640_000_100_000_000_000
        assert result.ts_event == 1_640_000_000_000_000_000
        assert result.ts_init == 1_640_000_000_000_000_000

    def test_roundtrip_dict_conversion_minimal_fields(self):
        # Arrange
        original = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.from_dict(FundingRateUpdate.to_dict(original))

        # Assert
        assert result == original

    def test_roundtrip_dict_conversion_all_fields(self):
        # Arrange
        original = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.from_dict(FundingRateUpdate.to_dict(original))

        # Assert
        assert result == original

    def test_different_rate_types(self):
        # Arrange, Act
        funding_rate_float = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=0.0001,  # float
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )
        funding_rate_str = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate="0.0001",  # string
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )
        funding_rate_decimal = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),  # Decimal
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Assert - All should work and be comparable
        assert funding_rate_float.rate == 0.0001
        assert funding_rate_str.rate == "0.0001"
        assert funding_rate_decimal.rate == Decimal("0.0001")

    def test_negative_funding_rates(self):
        # Arrange, Act
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("-0.0001"),  # Negative rate
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Assert
        assert funding_rate.rate == Decimal("-0.0001")

    def test_precision_handling(self):
        # Arrange, Act
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.000012345678"),  # High precision rate
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Assert
        assert funding_rate.rate == Decimal("0.000012345678")

    def test_data_interface_compliance(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE.id,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act, Assert - Test that it properly implements Data interface
        assert hasattr(funding_rate, "ts_event")
        assert hasattr(funding_rate, "ts_init")
        assert funding_rate.ts_event == 1_640_000_000_000_000_000
        assert funding_rate.ts_init == 1_640_000_000_000_000_000

    def test_from_pyo3_minimal_fields(self):
        # Arrange
        pyo3_funding_rate = nautilus_pyo3.FundingRateUpdate(
            instrument_id=nautilus_pyo3.InstrumentId.from_str("BTCUSDT-PERP.BINANCE"),
            rate="0.0001",
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.from_pyo3(pyo3_funding_rate)

        # Assert
        assert result.instrument_id.value == "BTCUSDT-PERP.BINANCE"
        assert result.rate == Decimal("0.0001")
        assert result.next_funding_ns is None
        assert result.ts_event == 1_640_000_000_000_000_000
        assert result.ts_init == 1_640_000_000_000_000_000

    def test_from_pyo3_all_fields(self):
        # Arrange
        pyo3_funding_rate = nautilus_pyo3.FundingRateUpdate(
            instrument_id=nautilus_pyo3.InstrumentId.from_str("BTCUSDT-PERP.BINANCE"),
            rate="0.0001",
            next_funding_ns=1_640_000_100_000_000_000,
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.from_pyo3(pyo3_funding_rate)

        # Assert
        assert result.instrument_id.value == "BTCUSDT-PERP.BINANCE"
        assert result.rate == Decimal("0.0001")
        assert result.next_funding_ns == 1_640_000_100_000_000_000
        assert result.ts_event == 1_640_000_000_000_000_000
        assert result.ts_init == 1_640_000_000_000_000_000

    def test_from_pyo3_list(self):
        # Arrange
        pyo3_funding_rates = [
            nautilus_pyo3.FundingRateUpdate(
                instrument_id=nautilus_pyo3.InstrumentId.from_str("BTCUSDT-PERP.BINANCE"),
                rate="0.0001",
                ts_event=1_640_000_000_000_000_000,
                ts_init=1_640_000_000_000_000_000,
            ),
            nautilus_pyo3.FundingRateUpdate(
                instrument_id=nautilus_pyo3.InstrumentId.from_str("ETHUSDT-PERP.BINANCE"),
                rate="0.0002",
                next_funding_ns=1_640_000_100_000_000_000,
                ts_event=1_640_000_001_000_000_000,
                ts_init=1_640_000_001_000_000_000,
            ),
        ]

        # Act
        result = FundingRateUpdate.from_pyo3_list(pyo3_funding_rates)

        # Assert
        assert len(result) == 2
        assert result[0].instrument_id.value == "BTCUSDT-PERP.BINANCE"
        assert result[0].rate == Decimal("0.0001")
        assert result[1].instrument_id.value == "ETHUSDT-PERP.BINANCE"
        assert result[1].rate == Decimal("0.0002")
```


---

## Overview

This file is located at `tests/unit_tests/model/test_funding_rate.py` within the repository.

**Classes defined:** TestFundingRateUpdate

**Functions defined:** test_fully_qualified_name, test_instantiation_with_required_fields_only, test_instantiation_with_all_fields, test_hash_str_and_repr_minimal_fields, test_hash_str_and_repr_all_fields, test_equality, test_to_dict_minimal_fields, test_to_dict_all_fields, test_from_dict_minimal_fields, test_from_dict_all_fields and 9 more

**Import statements:** 4


---

## Detailed Analysis

### Classes

#### `TestFundingRateUpdate`


### Functions

#### `test_fully_qualified_name(self)`


#### `test_instantiation_with_required_fields_only(self)`


#### `test_instantiation_with_all_fields(self)`


#### `test_hash_str_and_repr_minimal_fields(self)`


#### `test_hash_str_and_repr_all_fields(self)`


#### `test_equality(self)`


#### `test_to_dict_minimal_fields(self)`


#### `test_to_dict_all_fields(self)`


#### `test_from_dict_minimal_fields(self)`


#### `test_from_dict_all_fields(self)`


#### `test_roundtrip_dict_conversion_minimal_fields(self)`


#### `test_roundtrip_dict_conversion_all_fields(self)`


#### `test_different_rate_types(self)`


#### `test_negative_funding_rates(self)`


#### `test_precision_handling(self)`


#### `test_data_interface_compliance(self)`


#### `test_from_pyo3_minimal_fields(self)`


#### `test_from_pyo3_all_fields(self)`


#### `test_from_pyo3_list(self)`


### Imports

- `from decimal import Decimal`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.data import FundingRateUpdate`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.test_funding_rate import TestFundingRateUpdate
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.data import FundingRateUpdate`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`

**Directory:** `tests/unit_tests/model`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


