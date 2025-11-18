# Documentation: test_error_handling.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/test_error_handling.py`
- **Size**: 4,258 bytes
- **Lines**: 157
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 13 function(s).

## Detailed Walkthrough

### Functions
- **`retry_error()`**: Function defined in this file
- **`non_retry_error()`**: Function defined in this file
- **`test_should_retry_with_dict_message_containing_code()`**: Function defined in this file
- **`test_should_retry_with_dict_message_missing_code()`**: Function defined in this file
- **`test_should_retry_with_string_message_json_parseable()`**: Function defined in this file
- **`test_should_retry_with_string_message_not_json()`**: Function defined in this file
- **`test_should_retry_with_malformed_json_string()`**: Function defined in this file
- **`test_should_retry_with_none_message()`**: Function defined in this file
- **`test_should_retry_with_non_retry_error_code()`**: Function defined in this file
- **`test_should_retry_with_non_binance_error()`**: Function defined in this file
- **`test_should_retry_with_empty_dict_message()`**: Function defined in this file
- **`test_should_retry_with_string_code_value()`**: Function defined in this file
- **`test_should_retry_with_invalid_code_type()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Functions**: `non_retry_error`, `retry_error`, `test_should_retry_with_dict_message_containing_code`, `test_should_retry_with_dict_message_missing_code`, `test_should_retry_with_empty_dict_message`, `test_should_retry_with_invalid_code_type`, `test_should_retry_with_malformed_json_string`, `test_should_retry_with_non_binance_error`, `test_should_retry_with_non_retry_error_code`, `test_should_retry_with_none_message`, `test_should_retry_with_string_code_value`, `test_should_retry_with_string_message_json_parseable`, `test_should_retry_with_string_message_not_json`
**Imports**: `nautilus_trader.adapters.binance.http.error`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/test_error_handling.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.750549Z*
