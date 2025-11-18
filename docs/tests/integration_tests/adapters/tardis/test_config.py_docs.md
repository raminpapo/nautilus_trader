# Documentation: test_config.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/tardis/test_config.py`
- **Size**: 2,483 bytes
- **Lines**: 79
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

import pkgutil

from nautilus_trader.core import nautilus_pyo3


def test_tardis_config_replay_options():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "replay_options.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.ReplayNormalizedRequestOptions.from_json(data)

    # Assert
    assert isinstance(options, nautilus_pyo3.ReplayNormalizedRequestOptions)


def test_tardis_config_replay_options_array():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "replay_options_array.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.ReplayNormalizedRequestOptions.from_json_array(data)

    # Assert
    assert isinstance(options[0], nautilus_pyo3.ReplayNormalizedRequestOptions)


def test_tardis_config_stream_options():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "stream_options.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.StreamNormalizedRequestOptions.from_json(data)

    # Assert
    assert isinstance(options, nautilus_pyo3.StreamNormalizedRequestOptions)


def test_tardis_config_stream_options_array():
    # Arrange
    data = pkgutil.get_data(
        "tests.integration_tests.adapters.tardis.resources",
        "stream_options_array.json",
    )
    assert data

    # Act
    options = nautilus_pyo3.StreamNormalizedRequestOptions.from_json_array(data)

    # Assert
    assert isinstance(options[0], nautilus_pyo3.StreamNormalizedRequestOptions)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`test_tardis_config_replay_options()`**: Function defined in this file
- **`test_tardis_config_replay_options_array()`**: Function defined in this file
- **`test_tardis_config_stream_options()`**: Function defined in this file
- **`test_tardis_config_stream_options_array()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `test_tardis_config_replay_options`, `test_tardis_config_replay_options_array`, `test_tardis_config_stream_options`, `test_tardis_config_stream_options_array`
**Imports**: `nautilus_trader.core`, `pkgutil`

## Related Files

This file is located in `tests/integration_tests/adapters/tardis/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/tardis/test_config.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.214857Z*
