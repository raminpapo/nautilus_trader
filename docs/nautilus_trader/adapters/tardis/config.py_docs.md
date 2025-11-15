# Documentation: `nautilus_trader/adapters/tardis/config.py`
**Generated:** 2025-11-15T19:40:04.500965Z
**File Size:** 2239 bytes
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

- **Path:** `nautilus_trader/adapters/tardis/config.py`
- **Size:** 2,239 bytes
- **Lines:** 50
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Classes:** 1

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


---

## Overview

This file is located at `nautilus_trader/adapters/tardis/config.py` within the repository.

**Classes defined:** TardisDataClientConfig

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `TardisDataClientConfig`

**Inherits from:** LiveDataClientConfig, frozen=True


### Imports

- `from nautilus_trader.common.config import PositiveInt`
- `from nautilus_trader.config import LiveDataClientConfig`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.tardis.config import TardisDataClientConfig
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.config import PositiveInt`
- `from nautilus_trader.config import LiveDataClientConfig`

**Directory:** `nautilus_trader/adapters/tardis`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.


