# Documentation: env.py

## File Metadata

- **Path**: `nautilus_trader/adapters/env.py`
- **Size**: 1,202 bytes
- **Lines**: 31
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

import os


def get_env_key(key: str) -> str:
    if key not in os.environ:
        raise RuntimeError(f"Environment variable '{key}' not set")
    else:
        return os.environ[key]


def get_env_key_or(key: str, default: str) -> str:
    if key not in os.environ:
        return default
    else:
        return os.environ[key]

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`get_env_key()`**: Function defined in this file
- **`get_env_key_or()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `get_env_key`, `get_env_key_or`
**Imports**: `os`

## Related Files

This file is located in `nautilus_trader/adapters/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.790894Z*
