# Documentation: signal.py

## File Metadata

- **Path**: `nautilus_trader/common/signal.py`
- **Size**: 4,501 bytes
- **Lines**: 147
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

from contextlib import suppress

import pyarrow as pa

from nautilus_trader.core.data import Data
from nautilus_trader.serialization.arrow.serializer import register_arrow
from nautilus_trader.serialization.base import register_serializable_type


def generate_signal_class(name: str, value_type: type) -> type:
    """
    Dynamically create a Data subclass for this signal.

    Parameters
    ----------
    name : str
        The name of the signal data.
    value_type : type
        The type for the signal data value.

    Returns
    -------
    SignalData

    """

    class SignalData(Data):
        """
        Represents generic signal data.
        """

        def __init__(self, value: object, ts_event: int, ts_init: int) -> None:
            self.value = value
            self._ts_event = ts_event
            self._ts_init = ts_init

        @property
        def ts_event(self) -> int:
            """
            UNIX timestamp (nanoseconds) when the data event occurred.

            Returns
            -------
            int

            """
            return self._ts_event

        @property
        def ts_init(self) -> int:
            """
            UNIX timestamp (nanoseconds) when the object was initialized.

            Returns
            -------
            int

            """
            return self._ts_init

    SignalData.__name__ = f"Signal{name.title()}"

    # Dictionary serialization for message bus and Redis
    def to_dict_c(obj: SignalData) -> dict[str, object]:
        return {
            "type": type(obj).__name__,
            "value": obj.value,
            "ts_event": obj.ts_event,
            "ts_init": obj.ts_init,
        }

    def from_dict_c(values: dict[str, object]) -> SignalData:
        return SignalData(
            value=values["value"],
            ts_event=int(values["ts_event"]),  # type: ignore
            ts_init=int(values["ts_init"]),  # type: ignore
        )

    # Add serialization methods to the class
    SignalData.to_dict_c = to_dict_c
    SignalData.from_dict_c = from_dict_c
    SignalData.to_dict = lambda obj: SignalData.to_dict_c(obj)
    SignalData.from_dict = lambda values: SignalData.from_dict_c(values)

    # Parquet serialization
    def serialize_signal(data: SignalData) -> pa.RecordBatch:
        return pa.RecordBatch.from_pylist(
            [
                {
                    "ts_init": data.ts_init,
                    "ts_event": data.ts_event,
                    "value": data.value,
                },
            ],
            schema=schema,
        )

    def deserialize_signal(table: pa.Table) -> list[SignalData]:
        return [SignalData(**d) for d in table.to_pylist()]

    schema = pa.schema(
        {
            "ts_event": pa.uint64(),
            "ts_init": pa.uint64(),
            "value": {
                int: pa.int64(),
                float: pa.float64(),
                str: pa.string(),
                bool: pa.bool_(),
                bytes: pa.binary(),
            }[value_type],
        },
    )
    # Register for arrow serialization (only if not already registered)
    with suppress(KeyError, ValueError):
        register_arrow(
            data_cls=SignalData,
            encoder=serialize_signal,
            decoder=deserialize_signal,
            schema=schema,
        )

    # Register for message bus serialization (only if not already registered)
    with suppress(KeyError):
        register_serializable_type(
            cls=SignalData,
            to_dict=SignalData.to_dict_c,
            from_dict=SignalData.from_dict_c,
        )

    return SignalData

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`generate_signal_class()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `generate_signal_class`
**Imports**: `contextlib`, `nautilus_trader.core.data`, `nautilus_trader.serialization.arrow.serializer`, `nautilus_trader.serialization.base`, `pyarrow`

## Related Files

This file is located in `nautilus_trader/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.268949Z*
