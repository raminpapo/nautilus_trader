# Documentation: `tests/unit_tests/core/test_message.py`
**Generated:** 2025-11-15T19:40:09.084457Z
**File Size:** 3482 bytes
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

- **Path:** `tests/unit_tests/core/test_message.py`
- **Size:** 3,482 bytes
- **Lines:** 118
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 1
- **Functions:** 7

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


---

## Overview

This file is located at `tests/unit_tests/core/test_message.py` within the repository.

**Classes defined:** TestMessage

**Functions defined:** test_command_message_picking, test_document_message_picking, test_request_message_pickling, test_response_message_pickling, test_document_message_hash, test_document_message_str_and_repr, test_response_message_str_and_repr

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `TestMessage`


### Functions

#### `test_command_message_picking(self)`


#### `test_document_message_picking(self)`


#### `test_request_message_pickling(self)`


#### `test_response_message_pickling(self)`


#### `test_document_message_hash(self)`


#### `test_document_message_str_and_repr(self)`


#### `test_response_message_str_and_repr(self)`


### Imports

- `import pickle`
- `from nautilus_trader.core.message import Command`
- `from nautilus_trader.core.message import Document`
- `from nautilus_trader.core.message import Request`
- `from nautilus_trader.core.message import Response`
- `from nautilus_trader.core.uuid import UUID4`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.core.test_message import TestMessage
```


---

## Related Files

This file imports from the following modules:

- `import pickle`
- `from nautilus_trader.core.message import Command`
- `from nautilus_trader.core.message import Document`
- `from nautilus_trader.core.message import Request`
- `from nautilus_trader.core.message import Response`
- `from nautilus_trader.core.uuid import UUID4`

**Directory:** `tests/unit_tests/core`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


