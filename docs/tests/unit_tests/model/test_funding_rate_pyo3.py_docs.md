# Documentation: `tests/unit_tests/model/test_funding_rate_pyo3.py`
**Generated:** 2025-11-15T19:40:09.340062Z
**File Size:** 10751 bytes
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

- **Path:** `tests/unit_tests/model/test_funding_rate_pyo3.py`
- **Size:** 10,751 bytes
- **Lines:** 307
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 1
- **Functions:** 16

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

import pickle
from decimal import Decimal

from nautilus_trader.core.nautilus_pyo3 import FundingRateUpdate
from nautilus_trader.core.nautilus_pyo3 import InstrumentId
from nautilus_trader.core.nautilus_pyo3 import Symbol
from nautilus_trader.core.nautilus_pyo3 import Venue


BTCUSDT_PERP_BINANCE = InstrumentId(Symbol("BTCUSDT-PERP"), Venue("BINANCE"))


class TestFundingRateUpdate:
    def test_fully_qualified_name(self):
        # Arrange, Act, Assert
        assert (
            FundingRateUpdate.fully_qualified_name()
            == "nautilus_trader.core.nautilus_pyo3.model:FundingRateUpdate"
        )

    def test_funding_rate_update_new_minimal(self):
        # Arrange, Act
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Assert
        assert funding_rate.instrument_id == BTCUSDT_PERP_BINANCE
        assert funding_rate.rate == Decimal("0.0001")
        assert funding_rate.next_funding_ns is None
        assert funding_rate.ts_event == 1_640_000_000_000_000_000
        assert funding_rate.ts_init == 1_640_000_000_000_000_000

    def test_funding_rate_update_new_complete(self):
        # Arrange, Act
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
            next_funding_ns=1_640_000_100_000_000_000,
        )

        # Assert
        assert funding_rate.instrument_id == BTCUSDT_PERP_BINANCE
        assert funding_rate.rate == Decimal("0.0001")
        assert funding_rate.next_funding_ns == 1_640_000_100_000_000_000
        assert funding_rate.ts_event == 1_640_000_000_000_000_000
        assert funding_rate.ts_init == 1_640_000_000_000_000_000

    def test_hash_str_and_repr(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act, Assert
        assert isinstance(hash(funding_rate), int)
        assert (
            str(funding_rate)
            == "BTCUSDT-PERP.BINANCE,0.0001,None,1640000000000000000,1640000000000000000"
        )
        assert (
            repr(funding_rate)
            == 'FundingRateUpdate { instrument_id: "BTCUSDT-PERP.BINANCE", rate: 0.0001, next_funding_ns: None, ts_event: UnixNanos(1640000000000000000), ts_init: UnixNanos(1640000000000000000) }'
        )

    def test_equality(self):
        # Arrange
        funding_rate1 = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )
        funding_rate2 = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )
        funding_rate3 = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0002"),  # Different rate
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
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = funding_rate.to_dict()

        # Assert
        expected = {
            "type": "FundingRateUpdate",
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": "0.0001",
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }
        # Check all expected keys exist and values match
        for key, expected_value in expected.items():
            assert key in result
            assert result[key] == expected_value

    def test_to_dict_all_fields(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
            next_funding_ns=1_640_000_100_000_000_000,
        )

        # Act
        result = funding_rate.to_dict()

        # Assert
        expected = {
            "type": "FundingRateUpdate",
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": "0.0001",
            "next_funding_ns": 1_640_000_100_000_000_000,
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }
        # Check all expected keys exist and values match
        for key, expected_value in expected.items():
            assert key in result
            assert result[key] == expected_value

    def test_from_dict_minimal_fields(self):
        # Arrange
        values = {
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": "0.0001",
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }

        # Act
        result = FundingRateUpdate.from_dict(values)

        # Assert
        assert result.instrument_id == BTCUSDT_PERP_BINANCE
        assert result.rate == Decimal("0.0001")
        assert result.next_funding_ns is None
        assert result.ts_event == 1_640_000_000_000_000_000
        assert result.ts_init == 1_640_000_000_000_000_000

    def test_from_dict_all_fields(self):
        # Arrange
        values = {
            "instrument_id": "BTCUSDT-PERP.BINANCE",
            "rate": "0.0001",
            "next_funding_ns": 1_640_000_100_000_000_000,
            "ts_event": 1_640_000_000_000_000_000,
            "ts_init": 1_640_000_000_000_000_000,
        }

        # Act
        result = FundingRateUpdate.from_dict(values)

        # Assert
        assert result.instrument_id == BTCUSDT_PERP_BINANCE
        assert result.rate == Decimal("0.0001")
        assert result.next_funding_ns == 1_640_000_100_000_000_000
        assert result.ts_event == 1_640_000_000_000_000_000
        assert result.ts_init == 1_640_000_000_000_000_000

    def test_roundtrip_dict_conversion_minimal_fields(self):
        # Arrange
        original = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
        )

        # Act
        result = FundingRateUpdate.from_dict(original.to_dict())

        # Assert
        assert result == original

    def test_roundtrip_dict_conversion_all_fields(self):
        # Arrange
        original = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
            next_funding_ns=1_640_000_100_000_000_000,
        )

        # Act
        result = FundingRateUpdate.from_dict(original.to_dict())

        # Assert
        assert result == original

    def test_pickling_round_trip(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
            next_funding_ns=1_640_000_100_000_000_000,
        )

        # Act
        pickled = pickle.dumps(funding_rate)
        unpickled = pickle.loads(pickled)  # noqa: S301 (pickle safe here)

        # Assert
        assert unpickled == funding_rate

    def test_json_serialization_roundtrip(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
            next_funding_ns=1_640_000_100_000_000_000,
        )

        # Act
        json_bytes = funding_rate.to_json()
        result = FundingRateUpdate.from_json(json_bytes)

        # Assert
        assert result == funding_rate

    def test_msgpack_serialization_roundtrip(self):
        # Arrange
        funding_rate = FundingRateUpdate(
            instrument_id=BTCUSDT_PERP_BINANCE,
            rate=Decimal("0.0001"),
            ts_event=1_640_000_000_000_000_000,
            ts_init=1_640_000_000_000_000_000,
            next_funding_ns=1_640_000_100_000_000_000,
        )

        # Act
        msgpack_bytes = funding_rate.to_msgpack()
        result = FundingRateUpdate.from_msgpack(msgpack_bytes)

        # Assert
        assert result == funding_rate

    def test_get_metadata(self):
        # Arrange, Act
        metadata = FundingRateUpdate.get_metadata(BTCUSDT_PERP_BINANCE)

        # Assert
        assert metadata == {"instrument_id": "BTCUSDT-PERP.BINANCE"}

    def test_get_fields(self):
        # Arrange, Act
        fields = FundingRateUpdate.get_fields()

        # Assert
        expected_fields = {
            "rate": "Decimal128",
            "next_funding_ns": "UInt64",
            "ts_event": "UInt64",
            "ts_init": "UInt64",
        }
        assert fields == expected_fields
```


---

## Overview

This file is located at `tests/unit_tests/model/test_funding_rate_pyo3.py` within the repository.

**Classes defined:** TestFundingRateUpdate

**Functions defined:** test_fully_qualified_name, test_funding_rate_update_new_minimal, test_funding_rate_update_new_complete, test_hash_str_and_repr, test_equality, test_to_dict_minimal_fields, test_to_dict_all_fields, test_from_dict_minimal_fields, test_from_dict_all_fields, test_roundtrip_dict_conversion_minimal_fields and 6 more

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `TestFundingRateUpdate`


### Functions

#### `test_fully_qualified_name(self)`


#### `test_funding_rate_update_new_minimal(self)`


#### `test_funding_rate_update_new_complete(self)`


#### `test_hash_str_and_repr(self)`


#### `test_equality(self)`


#### `test_to_dict_minimal_fields(self)`


#### `test_to_dict_all_fields(self)`


#### `test_from_dict_minimal_fields(self)`


#### `test_from_dict_all_fields(self)`


#### `test_roundtrip_dict_conversion_minimal_fields(self)`


#### `test_roundtrip_dict_conversion_all_fields(self)`


#### `test_pickling_round_trip(self)`


#### `test_json_serialization_roundtrip(self)`


#### `test_msgpack_serialization_roundtrip(self)`


#### `test_get_metadata(self)`


#### `test_get_fields(self)`


### Imports

- `import pickle`
- `from decimal import Decimal`
- `from nautilus_trader.core.nautilus_pyo3 import FundingRateUpdate`
- `from nautilus_trader.core.nautilus_pyo3 import InstrumentId`
- `from nautilus_trader.core.nautilus_pyo3 import Symbol`
- `from nautilus_trader.core.nautilus_pyo3 import Venue`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.test_funding_rate_pyo3 import TestFundingRateUpdate
```


---

## Related Files

This file imports from the following modules:

- `import pickle`
- `from decimal import Decimal`
- `from nautilus_trader.core.nautilus_pyo3 import FundingRateUpdate`
- `from nautilus_trader.core.nautilus_pyo3 import InstrumentId`
- `from nautilus_trader.core.nautilus_pyo3 import Symbol`
- `from nautilus_trader.core.nautilus_pyo3 import Venue`

**Directory:** `tests/unit_tests/model`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


