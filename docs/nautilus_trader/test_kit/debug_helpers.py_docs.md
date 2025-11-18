# Documentation: debug_helpers.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/debug_helpers.py`
- **Size**: 3,737 bytes
- **Lines**: 108
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
import json
import os
import sys

import debugpy  # noqa: T100

from nautilus_trader import PACKAGE_ROOT


def setup_debugging(vs_code_path=PACKAGE_ROOT.parent, enable_python_debugging=True, port=5678):
    # By default the directory containing the .vscode folder is assumed to be
    # one folder above the root nautilus_trader folder
    if enable_python_debugging:
        debugpy.listen(port)  # noqa: T100

    # Get current process info
    pid = os.getpid()
    python_path = sys.executable

    # Essential configurations for mixed debugging only
    config = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Rust Debugger (for Jupyter)",
                "type": "lldb",
                "request": "attach",
                "program": python_path,
                "pid": pid,
                "sourceLanguages": ["rust"],
                "env": {
                    "RUST_BACKTRACE": "1",
                },
            },
            {
                "name": "Python Debugger (for Jupyter)",
                "type": "debugpy",
                "request": "attach",
                "connect": {
                    "host": "localhost",
                    "port": port,
                },
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}/nautilus_trader",
                        "remoteRoot": "${workspaceFolder}/nautilus_trader",
                    },
                ],
                "env": {
                    "RUST_BACKTRACE": "1",
                    "PYTHONPATH": "${workspaceFolder}/nautilus_trader",
                },
            },
        ],
        "compounds": [
            {
                "name": "Python + Rust Debugger (for Jupyter)",
                "configurations": [
                    "Python Debugger (for Jupyter)",
                    "Rust Debugger (for Jupyter)",
                ],
                "stopAll": True,
                "presentation": {
                    "hidden": False,
                    "group": "mixed",
                    "order": 2,
                },
            },
        ],
    }

    # Determine path
    launch_json_path = vs_code_path / ".vscode" / "launch.json"
    print(f"{launch_json_path=}")

    # Create .vscode directory if it doesn't exist
    launch_json_path.parent.mkdir(exist_ok=True)

    # Write the configuration
    with open(launch_json_path, "w") as f:
        json.dump(config, f, indent=4)

    print("✓ VS Code configuration updated")
    print(
        f"Created {len(config['configurations'])} configurations and {len(config['compounds'])} compound configurations",
    )
    print("1. In VS Code: Select 'Python + Rust Debugger (for Jupyter)' → Start Debugging (F5)")


def print_stack():
    import traceback

    print("".join(traceback.format_stack()))

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`setup_debugging()`**: Function defined in this file
- **`print_stack()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `print_stack`, `setup_debugging`
**Imports**: `debugpy`, `json`, `nautilus_trader`, `os`, `sys`

## Related Files

This file is located in `nautilus_trader/test_kit/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/debug_helpers.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.947084Z*
