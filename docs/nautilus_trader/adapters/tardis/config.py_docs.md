# Documentation: config.py

## File Metadata

- **Path**: `nautilus_trader/adapters/tardis/config.py`
- **Size**: 2,239 bytes
- **Lines**: 51
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

from nautilus_trader.common.config import PositiveInt
from nautilus_trader.config import LiveDataClientConfig


class TardisDataClientConfig(LiveDataClientConfig, frozen=True):
    """
    Configuration for ``TardisDataClient`` instances.

    Parameters
    ----------
    api_key : str, optional
        The Tardis API secret key.
        If ``None`` then will source the `TARDIS_API_KEY` environment variable.
    base_url_http : str, optional
        The base url for the Tardis HTTP API.
        If ``None`` then will default to https://api.tardis.dev/v1.
    base_url_ws : str, optional
        The base url for the locally running Tardis Machine server.
        If ``None`` then will source the `TARDIS_MACHINE_WS_URL`.
    update_instruments_interval_mins: PositiveInt or None, default 60
        The interval (minutes) between reloading instruments from the venue.
    ws_connection_delay_secs : PositiveInt, default 5
        The delay (seconds) prior to main websocket connection to allow initial subscriptions to arrive.

    References
    ----------
    See the list of Tardis-supported exchanges https://api.tardis.dev/v1/exchanges.

    """

    api_key: str | None = None
    base_url_http: str | None = None
    base_url_ws: str | None = None
    update_instruments_interval_mins: PositiveInt | None = 60
    ws_connection_delay_secs: PositiveInt = 5

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TardisDataClientConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `TardisDataClientConfig`
**Imports**: `nautilus_trader.common.config`, `nautilus_trader.config`

## Related Files

This file is located in `nautilus_trader/adapters/tardis/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:04.999083Z*
