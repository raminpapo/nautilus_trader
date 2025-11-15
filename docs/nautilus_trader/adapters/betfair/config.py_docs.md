# Documentation: `nautilus_trader/adapters/betfair/config.py`
**Generated:** 2025-11-15T19:40:04.021389Z
**File Size:** 4964 bytes
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

- **Path:** `nautilus_trader/adapters/betfair/config.py`
- **Size:** 4,964 bytes
- **Lines:** 112
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Classes:** 2

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

from nautilus_trader.adapters.betfair.providers import BetfairInstrumentProviderConfig
from nautilus_trader.common.config import NonNegativeInt
from nautilus_trader.common.config import PositiveInt
from nautilus_trader.config import LiveDataClientConfig
from nautilus_trader.config import LiveExecClientConfig


class BetfairDataClientConfig(LiveDataClientConfig, kw_only=True, frozen=True):
    """
    Configuration for ``BetfairDataClient`` instances.

    Parameters
    ----------
    account_currency : str
        The currency for the Betfair account.
    username : str, optional
        The Betfair account username.
    password : str, optional
        The Betfair account password.
    app_key : str, optional
        The Betfair application key.
    cert_dir : str, optional
        The local directory that contains the Betfair certificates.
    instrument_config : BetfairInstrumentProviderConfig, None
        The Betfair instrument provider config.
    subscription_delay_secs : PositiveInt, default 3
        The delay (seconds) before sending the *initial* subscription message.
    keep_alive_secs : PositiveInt, default 36_000 (10 hours)
        The keep alive interval (seconds) for the HTTP client.
    stream_conflate_ms : PositiveInt, optional
        The Betfair data stream conflation setting. Default of `None` means no explicit value is
        set for the conflation interval. Betfair interprets this as using its default behaviour for
        conflation. The default typically applies conflation, so you need to ensure
        stream_conflate_ms=0 is explicitly set to guarantee no conflation.
    proxy_url : str, optional
        The proxy URL for HTTP requests.

    """

    account_currency: str
    username: str | None = None
    password: str | None = None
    app_key: str | None = None
    certs_dir: str | None = None
    instrument_config: BetfairInstrumentProviderConfig | None = None
    subscription_delay_secs: PositiveInt | None = 3
    keep_alive_secs: PositiveInt = 36_000  # 10 hours
    stream_conflate_ms: PositiveInt | None = None
    proxy_url: str | None = None


class BetfairExecClientConfig(LiveExecClientConfig, kw_only=True, frozen=True):
    """
    Configuration for ``BetfairExecClient`` instances.

    Parameters
    ----------
    account_currency : str
        The currency for the Betfair account.
    username : str, optional
        The Betfair account username.
    password : str, optional
        The Betfair account password.
    app_key : str, optional
        The Betfair application key.
    certs_dir : str, optional
        The local directory that contains the Betfair certificates.
    instrument_config : BetfairInstrumentProviderConfig, None
        The Betfair instrument provider config.
    calculate_account_state : bool, default True
        If the Betfair account state should be calculated from events.
    request_account_state_secs : NonNegativeInt, default 300 (5 minutes)
        The request interval (seconds) for account state checks.
        If zero, then will not request account state from Betfair.
    reconcile_market_ids_only : bool, default False
        If True, reconciliation only requests orders matching the market IDs listed
        in the `instrument_config`. If False, all orders are reconciled.
    ignore_external_orders : bool, default False
        If True, orders received over the stream that aren't found in the cache
        will be silently ignored. This is useful when multiple trading nodes
        share the same Betfair account across different markets.
    proxy_url : str, optional
        The proxy URL for HTTP requests.

    """

    account_currency: str
    username: str | None = None
    password: str | None = None
    app_key: str | None = None
    certs_dir: str | None = None
    instrument_config: BetfairInstrumentProviderConfig | None = None
    calculate_account_state: bool = True
    request_account_state_secs: NonNegativeInt = 300
    reconcile_market_ids_only: bool = False
    ignore_external_orders: bool = False
    proxy_url: str | None = None
```


---

## Overview

This file is located at `nautilus_trader/adapters/betfair/config.py` within the repository.

**Classes defined:** BetfairDataClientConfig, BetfairExecClientConfig

**Import statements:** 5


---

## Detailed Analysis

### Classes

#### `BetfairDataClientConfig`

**Inherits from:** LiveDataClientConfig, kw_only=True, frozen=True


#### `BetfairExecClientConfig`

**Inherits from:** LiveExecClientConfig, kw_only=True, frozen=True


### Imports

- `from nautilus_trader.adapters.betfair.providers import BetfairInstrumentProviderConfig`
- `from nautilus_trader.common.config import NonNegativeInt`
- `from nautilus_trader.common.config import PositiveInt`
- `from nautilus_trader.config import LiveDataClientConfig`
- `from nautilus_trader.config import LiveExecClientConfig`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.betfair.config import BetfairDataClientConfig
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.betfair.providers import BetfairInstrumentProviderConfig`
- `from nautilus_trader.common.config import NonNegativeInt`
- `from nautilus_trader.common.config import PositiveInt`
- `from nautilus_trader.config import LiveDataClientConfig`
- `from nautilus_trader.config import LiveExecClientConfig`

**Directory:** `nautilus_trader/adapters/betfair`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password. Ensure proper handling of secrets.


