# Documentation: test_message.py

## File Metadata

- **Path**: `tests/unit_tests/core/test_message.py`
- **Size**: 3,482 bytes
- **Lines**: 119
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

import pickle

from nautilus_trader.core.message import Command
from nautilus_trader.core.message import Document
from nautilus_trader.core.message import Request
from nautilus_trader.core.message import Response
from nautilus_trader.core.uuid import UUID4


class TestMessage:
    def test_command_message_picking(self):
        # Arrange
        command = Command(
            UUID4(),
            0,
        )

        # Act
        pickled = pickle.dumps(command)
        unpickled = pickle.loads(pickled)  # noqa: S301 (pickle is safe here)

        # Assert
        assert command == unpickled

    def test_document_message_picking(self):
        # Arrange
        doc = Document(
            UUID4(),
            0,
        )

        # Act
        pickled = pickle.dumps(doc)
        unpickled = pickle.loads(pickled)  # noqa: S301 (pickle is safe here)

        # Assert
        assert doc == unpickled

    def test_request_message_pickling(self):
        # Arrange
        req = Request(
            print,
            UUID4(),
            0,
        )

        # Act
        pickled = pickle.dumps(req)
        unpickled = pickle.loads(pickled)  # noqa: S301 (pickle is safe here)

        # Assert
        assert req == unpickled

    def test_response_message_pickling(self):
        # Arrange
        res = Response(
            UUID4(),
            UUID4(),
            0,
        )

        # Act
        pickled = pickle.dumps(res)
        unpickled = pickle.loads(pickled)  # noqa: S301 (pickle is safe here)

        # Assert
        assert res == unpickled

    def test_document_message_hash(self):
        # Arrange
        message = Document(
            document_id=UUID4(),
            ts_init=0,
        )

        # Act, Assert
        assert isinstance(hash(message), int)

    def test_document_message_str_and_repr(self):
        # Arrange
        uuid = UUID4()
        message = Document(
            document_id=uuid,
            ts_init=0,
        )

        # Act, Assert
        assert str(message) == f"Document(id={uuid}, ts_init=0)"
        assert str(message) == f"Document(id={uuid}, ts_init=0)"

    def test_response_message_str_and_repr(self):
        # Arrange
        uuid_id = UUID4()
        uuid_corr = UUID4()
        response = Response(
            correlation_id=uuid_corr,
            response_id=uuid_id,
            ts_init=0,
        )

        # Act, Assert
        assert str(response) == f"Response(correlation_id={uuid_corr}, id={uuid_id}, ts_init=0)"
        assert str(response) == f"Response(correlation_id={uuid_corr}, id={uuid_id}, ts_init=0)"

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestMessage`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestMessage`
**Imports**: `nautilus_trader.core.message`, `nautilus_trader.core.uuid`, `pickle`

## Related Files

This file is located in `tests/unit_tests/core/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/core/test_message.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.315795Z*
