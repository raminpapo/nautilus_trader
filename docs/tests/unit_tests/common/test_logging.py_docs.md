# Documentation: `tests/unit_tests/common/test_logging.py`
**Generated:** 2025-11-15T19:40:09.056720Z
**File Size:** 4142 bytes
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

- **Path:** `tests/unit_tests/common/test_logging.py`
- **Size:** 4,142 bytes
- **Lines:** 139
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6
- **Classes:** 2
- **Functions:** 10

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


---

## Overview

This file is located at `tests/unit_tests/common/test_logging.py` within the repository.

**Classes defined:** TestLogLevel, TestLoggerTests

**Functions defined:** test_log_level_to_str, test_log_level_from_str, test_name, test_log_debug_messages_to_console, test_log_info_messages_to_console, test_log_info_messages_to_console_with_blue_colour, test_log_info_messages_to_console_with_green_colour, test_log_warning_messages_to_console, test_log_error_messages_to_console, test_log_exception_messages_to_console

**Import statements:** 6


---

## Detailed Analysis

### Classes

#### `TestLogLevel`


#### `TestLoggerTests`


### Functions

#### `test_log_level_to_str(self, enum, expected)`


#### `test_log_level_from_str(self, string, expected)`


#### `test_name(self)`


#### `test_log_debug_messages_to_console(self)`


#### `test_log_info_messages_to_console(self)`


#### `test_log_info_messages_to_console_with_blue_colour(self)`


#### `test_log_info_messages_to_console_with_green_colour(self)`


#### `test_log_warning_messages_to_console(self)`


#### `test_log_error_messages_to_console(self)`


#### `test_log_exception_messages_to_console(self)`


### Imports

- `import pytest`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.enums import LogColor`
- `from nautilus_trader.common.enums import LogLevel`
- `from nautilus_trader.common.enums import log_level_from_str`
- `from nautilus_trader.common.enums import log_level_to_str`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_logging import TestLogLevel
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.enums import LogColor`
- `from nautilus_trader.common.enums import LogLevel`
- `from nautilus_trader.common.enums import log_level_from_str`
- `from nautilus_trader.common.enums import log_level_to_str`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


