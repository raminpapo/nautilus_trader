# Documentation: `tests/integration_tests/adapters/binance/test_config_validation.py`
**Generated:** 2025-11-15T19:40:07.681758Z
**File Size:** 4255 bytes
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

- **Path:** `tests/integration_tests/adapters/binance/test_config_validation.py`
- **Size:** 4,255 bytes
- **Lines:** 127
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 8

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

from nautilus_trader.adapters.binance.config import BinanceDataClientConfig
from nautilus_trader.adapters.binance.config import BinanceExecClientConfig


@pytest.fixture
def default_data_config():
    return BinanceDataClientConfig()


@pytest.fixture
def default_exec_config():
    return BinanceExecClientConfig()


def test_data_client_config_documentation_accuracy(default_data_config):
    config = default_data_config

    # Verify default values are as documented
    assert config.api_key is None
    assert config.api_secret is None
    assert config.testnet is False
    assert config.us is False
    assert config.update_instruments_interval_mins == 60
    assert config.use_agg_trade_ticks is False


def test_exec_client_config_documentation_accuracy(default_exec_config):
    config = default_exec_config

    # Verify default values are as documented
    assert config.api_key is None
    assert config.api_secret is None
    assert config.testnet is False
    assert config.us is False
    assert config.use_gtd is True
    assert config.use_reduce_only is True
    assert config.use_position_ids is True
    assert config.use_trade_lite is False
    assert config.treat_expired_as_canceled is False
    assert config.recv_window_ms == 5_000


def test_data_client_config_with_valid_parameters():
    config = BinanceDataClientConfig(
        api_key="test_api_key",
        api_secret="test_api_secret",
        testnet=True,
        us=True,
        update_instruments_interval_mins=30,
        use_agg_trade_ticks=True,
    )

    assert config.api_key == "test_api_key"
    assert config.api_secret == "test_api_secret"
    assert config.testnet is True
    assert config.us is True
    assert config.update_instruments_interval_mins == 30
    assert config.use_agg_trade_ticks is True


def test_exec_client_config_with_valid_parameters():
    config = BinanceExecClientConfig(
        api_key="test_api_key",
        api_secret="test_api_secret",
        testnet=True,
        us=True,
        use_gtd=False,
        use_reduce_only=False,
        use_position_ids=False,
        use_trade_lite=True,
        treat_expired_as_canceled=True,
        recv_window_ms=10_000,
        max_retries=5,
    )

    assert config.api_key == "test_api_key"
    assert config.api_secret == "test_api_secret"
    assert config.testnet is True
    assert config.us is True
    assert config.use_gtd is False
    assert config.use_reduce_only is False
    assert config.use_position_ids is False
    assert config.use_trade_lite is True
    assert config.treat_expired_as_canceled is True
    assert config.recv_window_ms == 10_000
    assert config.max_retries == 5


def test_config_frozen_behavior(default_data_config):
    config = default_data_config

    # Should not be able to modify frozen config
    with pytest.raises(AttributeError):
        config.api_key = "new_key"


def test_exec_config_optional_parameters_none():
    config = BinanceExecClientConfig(
        max_retries=None,
        retry_delay_initial_ms=None,
        retry_delay_max_ms=None,
        futures_leverages=None,
        futures_margin_types=None,
    )

    assert config.max_retries is None
    assert config.retry_delay_initial_ms is None
    assert config.retry_delay_max_ms is None
    assert config.futures_leverages is None
    assert config.futures_margin_types is None
```


---

## Overview

This file is located at `tests/integration_tests/adapters/binance/test_config_validation.py` within the repository.

**Functions defined:** default_data_config, default_exec_config, test_data_client_config_documentation_accuracy, test_exec_client_config_documentation_accuracy, test_data_client_config_with_valid_parameters, test_exec_client_config_with_valid_parameters, test_config_frozen_behavior, test_exec_config_optional_parameters_none

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `default_data_config()`


#### `default_exec_config()`


#### `test_data_client_config_documentation_accuracy(default_data_config)`


#### `test_exec_client_config_documentation_accuracy(default_exec_config)`


#### `test_data_client_config_with_valid_parameters()`


#### `test_exec_client_config_with_valid_parameters()`


#### `test_config_frozen_behavior(default_data_config)`


#### `test_exec_config_optional_parameters_none()`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.binance.config import BinanceDataClientConfig`
- `from nautilus_trader.adapters.binance.config import BinanceExecClientConfig`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.binance.test_config_validation import default_data_config
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.binance.config import BinanceDataClientConfig`
- `from nautilus_trader.adapters.binance.config import BinanceExecClientConfig`

**Directory:** `tests/integration_tests/adapters/binance`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


