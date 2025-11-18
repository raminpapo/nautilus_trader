# Documentation: test_custom_data.py

## File Metadata

- **Path**: `tests/unit_tests/model/test_custom_data.py`
- **Size**: 3,093 bytes
- **Lines**: 114
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


from nautilus_trader.core.data import Data
from nautilus_trader.model.custom import customdataclass
from nautilus_trader.model.identifiers import InstrumentId


@customdataclass
class GreeksTestData(Data):
    instrument_id: InstrumentId = InstrumentId.from_str("ES.GLBX")
    delta: float = 0.0


def test_customdata_decorator_properties() -> None:
    # Arrange, Act
    data = GreeksTestData(ts_event=1, ts_init=2)

    # Assert
    assert data.ts_event == 1
    assert data.ts_init == 2


def test_customdata_decorator_dict() -> None:
    # Arrange
    data = GreeksTestData(1, 2, InstrumentId.from_str("ES.GLBX"), 0.0)

    # Act
    data_dict = data.to_dict()

    # Assert
    assert data_dict == {
        "instrument_id": "ES.GLBX",
        "delta": 0.0,
        "type": "GreeksTestData",
        "ts_event": 1,
        "ts_init": 2,
    }


def test_customdata_repr() -> None:
    # Arrange
    data = GreeksTestData(ts_event=1715248800000000000, ts_init=1715248860000000000)

    # Act
    repr = str(data)

    # Assert
    assert (
        repr
        == "GreeksTestData(instrument_id=InstrumentId('ES.GLBX'), delta=0.0, ts_event=2024-05-09T10:00:00.000000000Z, ts_init=2024-05-09T10:01:00.000000000Z)"
    )


def test_customdata_decorator_dict_identity() -> None:
    # Arrange
    data = GreeksTestData(
        ts_event=1,
        ts_init=2,
        instrument_id=InstrumentId.from_str("CL.GLBX"),
        delta=1000.0,
    )

    # Act
    new_data = GreeksTestData.from_dict(data.to_dict())

    # Assert
    assert new_data == data


def test_customdata_decorator_bytes_identity() -> None:
    # Arrange
    data = GreeksTestData(
        ts_event=1,
        ts_init=2,
        instrument_id=InstrumentId.from_str("CL.GLBX"),
        delta=1000.0,
    )

    # Act
    new_data = GreeksTestData.from_bytes(data.to_bytes())

    # Assert
    assert new_data == data


def test_customdata_decorator_arrow_identity() -> None:
    # Arrange
    data = GreeksTestData(
        ts_event=1,
        ts_init=2,
        instrument_id=InstrumentId.from_str("CL.GLBX"),
        delta=1000.0,
    )

    # Act
    new_data = GreeksTestData.from_arrow(data.to_arrow())[0]

    # Assert
    assert new_data == data

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`test_customdata_decorator_properties()`**: Function defined in this file
- **`test_customdata_decorator_dict()`**: Function defined in this file
- **`test_customdata_repr()`**: Function defined in this file
- **`test_customdata_decorator_dict_identity()`**: Function defined in this file
- **`test_customdata_decorator_bytes_identity()`**: Function defined in this file
- **`test_customdata_decorator_arrow_identity()`**: Function defined in this file

### Classes
- **`GreeksTestData`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Classs**: `GreeksTestData`
**Functions**: `test_customdata_decorator_arrow_identity`, `test_customdata_decorator_bytes_identity`, `test_customdata_decorator_dict`, `test_customdata_decorator_dict_identity`, `test_customdata_decorator_properties`, `test_customdata_repr`
**Imports**: `nautilus_trader.core.data`, `nautilus_trader.model.custom`, `nautilus_trader.model.identifiers`

## Related Files

This file is located in `tests/unit_tests/model/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/model/test_custom_data.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.596584Z*
