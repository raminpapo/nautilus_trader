# Documentation: `tests/integration_tests/adapters/binance/test_error_handling.py`
**Generated:** 2025-11-15T19:40:07.686796Z
**File Size:** 4258 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/test_error_handling.py`
- **Size:** 4,258 bytes
- **Lines:** 156
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 13

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

import pytest

from nautilus_trader.adapters.binance.http.error import BinanceError
from nautilus_trader.adapters.binance.http.error import should_retry


@pytest.fixture
def retry_error():
    """
    Create a BinanceError with a retryable error code.
    """
    return BinanceError(
        status=400,
        message={"code": -1021, "msg": "Timestamp for this request is outside of the recvWindow."},
        headers={},
    )


@pytest.fixture
def non_retry_error():
    """
    Create a BinanceError with a non-retryable error code.
    """
    return BinanceError(
        status=400,
        message={"code": -1000, "msg": "Unknown error"},
        headers={},
    )


def test_should_retry_with_dict_message_containing_code(retry_error):
    result = should_retry(retry_error)
    # -1021 is in BINANCE_RETRY_ERRORS, so should return True
    assert result is True


def test_should_retry_with_dict_message_missing_code():
    error = BinanceError(
        status=400,
        message={"msg": "Some error message without code"},
        headers={},
    )

    result = should_retry(error)
    # Should not crash and return False
    assert result is False


def test_should_retry_with_string_message_json_parseable():
    error = BinanceError(
        status=400,
        message='{"code": -1021, "msg": "Timestamp error"}',
        headers={},
    )

    result = should_retry(error)
    # Should parse JSON and find code -1021
    assert result is True


def test_should_retry_with_string_message_not_json():
    error = BinanceError(
        status=400,
        message="This is just a plain string error message",
        headers={},
    )

    result = should_retry(error)
    # Should not crash and return False
    assert result is False


def test_should_retry_with_malformed_json_string():
    error = BinanceError(
        status=400,
        message='{"code": -1021, "msg": "Malformed JSON',  # Missing closing brace
        headers={},
    )

    result = should_retry(error)
    # Should not crash and return False
    assert result is False


def test_should_retry_with_none_message():
    error = BinanceError(
        status=400,
        message=None,
        headers={},
    )

    result = should_retry(error)
    # Should not crash and return False
    assert result is False


def test_should_retry_with_non_retry_error_code(non_retry_error):
    result = should_retry(non_retry_error)
    assert result is False


def test_should_retry_with_non_binance_error():
    error = ValueError("Some other error")

    result = should_retry(error)
    assert result is False


def test_should_retry_with_empty_dict_message():
    error = BinanceError(
        status=400,
        message={},
        headers={},
    )

    result = should_retry(error)
    assert result is False


def test_should_retry_with_string_code_value():
    error = BinanceError(
        status=400,
        message={"code": "-1021", "msg": "String code value"},
        headers={},
    )

    result = should_retry(error)
    # Should handle string to int conversion
    assert result is True


def test_should_retry_with_invalid_code_type():
    error = BinanceError(
        status=400,
        message={"code": "invalid", "msg": "Invalid code type"},
        headers={},
    )

    result = should_retry(error)
    # Should not crash on invalid int conversion
    assert result is False
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/test_error_handling.py` within the repository.

**Functions defined:** retry_error, non_retry_error, test_should_retry_with_dict_message_containing_code, test_should_retry_with_dict_message_missing_code, test_should_retry_with_string_message_json_parseable, test_should_retry_with_string_message_not_json, test_should_retry_with_malformed_json_string, test_should_retry_with_none_message, test_should_retry_with_non_retry_error_code, test_should_retry_with_non_binance_error and 3 more

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `retry_error()`


#### `non_retry_error()`


#### `test_should_retry_with_dict_message_containing_code(retry_error)`


#### `test_should_retry_with_dict_message_missing_code()`


#### `test_should_retry_with_string_message_json_parseable()`


#### `test_should_retry_with_string_message_not_json()`


#### `test_should_retry_with_malformed_json_string()`


#### `test_should_retry_with_none_message()`


#### `test_should_retry_with_non_retry_error_code(non_retry_error)`


#### `test_should_retry_with_non_binance_error()`


#### `test_should_retry_with_empty_dict_message()`


#### `test_should_retry_with_string_code_value()`


#### `test_should_retry_with_invalid_code_type()`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.binance.http.error import BinanceError`
- `from nautilus_trader.adapters.binance.http.error import should_retry`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.binance.test_error_handling import retry_error
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.binance.http.error import BinanceError`
- `from nautilus_trader.adapters.binance.http.error import should_retry`

**Directory:** `tests/integration_tests/adapters/binance`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


