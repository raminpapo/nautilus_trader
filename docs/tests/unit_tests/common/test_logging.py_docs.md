# Documentation: test_logging.py

## File Metadata

- **Path**: `tests/unit_tests/common/test_logging.py`
- **Size**: 4,142 bytes
- **Lines**: 140
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

from nautilus_trader.common.component import Logger
from nautilus_trader.common.enums import LogColor
from nautilus_trader.common.enums import LogLevel
from nautilus_trader.common.enums import log_level_from_str
from nautilus_trader.common.enums import log_level_to_str


class TestLogLevel:
    @pytest.mark.parametrize(
        ("enum", "expected"),
        [
            [LogLevel.TRACE, "TRACE"],
            [LogLevel.DEBUG, "DEBUG"],
            [LogLevel.INFO, "INFO"],
            [LogLevel.WARNING, "WARNING"],
            [LogLevel.ERROR, "ERROR"],
        ],
    )
    def test_log_level_to_str(self, enum, expected):
        # Arrange, Act
        result = log_level_to_str(enum)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(
        ("string", "expected"),
        [
            ["TRACE", LogLevel.TRACE],
            ["DEBUG", LogLevel.DEBUG],
            ["INFO", LogLevel.INFO],
            ["WARN", LogLevel.WARNING],
            ["WARNING", LogLevel.WARNING],
            ["ERROR", LogLevel.ERROR],
        ],
    )
    def test_log_level_from_str(self, string, expected):
        # Arrange, Act
        result = log_level_from_str(string)

        # Assert
        assert result == expected


class TestLoggerTests:
    def test_name(self):
        # Arrange
        name = "TEST_LOGGER"
        logger = Logger(name=name)

        # Act, Assert
        assert logger.name == name

    def test_log_debug_messages_to_console(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.debug("This is a DEBUG log message.")

        # Assert
        assert True  # No exceptions raised

    def test_log_info_messages_to_console(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.info("This is an INFO log message.")

        # Assert
        assert True  # No exceptions raised

    def test_log_info_messages_to_console_with_blue_colour(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.info("This is an INFO log message.", color=LogColor.BLUE)

        # Assert
        assert True  # No exceptions raised

    def test_log_info_messages_to_console_with_green_colour(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.info("This is an INFO log message.", color=LogColor.GREEN)

        # Assert
        assert True  # No exceptions raised

    def test_log_warning_messages_to_console(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.warning("This is a WARNING log message.")

        # Assert
        assert True  # No exceptions raised

    def test_log_error_messages_to_console(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.error("This is an ERROR log message.")

        # Assert
        assert True  # No exceptions raised

    def test_log_exception_messages_to_console(self):
        # Arrange
        logger = Logger(name="TEST_LOGGER")

        # Act
        logger.exception("We intentionally divided by zero!", ZeroDivisionError("Oops"))

        # Assert
        assert True  # No exceptions raised

```

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`TestLogLevel`**: Class defined in this file
- **`TestLoggerTests`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `TestLogLevel`, `TestLoggerTests`
**Imports**: `nautilus_trader.common.component`, `nautilus_trader.common.enums`, `pytest`

## Related Files

This file is located in `tests/unit_tests/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/common/test_logging.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.276981Z*
