# Documentation: `tests/integration_tests/adapters/tardis/test_enums.py`
**Generated:** 2025-11-15T19:40:07.980956Z
**File Size:** 4798 bytes
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

- **Path:** `tests/integration_tests/adapters/tardis/test_enums.py`
- **Size:** 4,798 bytes
- **Lines:** 129
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Functions:** 2

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

from nautilus_trader.core.nautilus_pyo3 import tardis_exchange_from_venue_str
from nautilus_trader.core.nautilus_pyo3 import tardis_exchange_to_venue_str
from nautilus_trader.core.nautilus_pyo3 import tardis_exchanges
from nautilus_trader.model.identifiers import Venue


_EXPECTED_VENUE_MAPPINGS = {
    "ascendex": "ASCENDEX",
    "binance": "BINANCE",
    "binance-delivery": "BINANCE_DELIVERY",
    "binance-dex": "BINANCE",
    "binance-european-options": "BINANCE",
    "binance-futures": "BINANCE",
    "binance-jersey": "BINANCE",
    "binance-options": "BINANCE",
    "binance-us": "BINANCE_US",
    "bitfinex": "BITFINEX",
    "bitfinex-derivatives": "BITFINEX",
    "bitflyer": "BITFLYER",
    "bitget": "BITGET",
    "bitget-futures": "BITGET",
    "bitmex": "BITMEX",
    "bitnomial": "BITNOMIAL",
    "bitstamp": "BITSTAMP",
    "blockchain-com": "BLOCKCHAIN_COM",
    "bybit": "BYBIT",
    "bybit-options": "BYBIT",
    "bybit-spot": "BYBIT",
    "coinbase": "COINBASE",
    "coinbase-international": "COINBASE_INTX",
    "coinflex": "COINFLEX",
    "crypto-com": "CRYPTO_COM",
    "crypto-com-derivatives": "CRYPTO_COM",
    "cryptofacilities": "CRYPTOFACILITIES",
    "delta": "DELTA",
    "deribit": "DERIBIT",
    "dydx": "DYDX",
    "dydx-v4": "DYDX_V4",
    "ftx": "FTX",
    "ftx-us": "FTX",
    "gate-io": "GATE_IO",
    "gate-io-futures": "GATE_IO",
    "gemini": "GEMINI",
    "hitbtc": "HITBTC",
    "huobi": "HUOBI",
    "huobi-dm": "HUOBI",
    "huobi-dm-linear-swap": "HUOBI",
    "huobi-dm-options": "HUOBI",
    "huobi-dm-swap": "HUOBI_DELIVERY",
    "hyperliquid": "HYPERLIQUID",
    "kraken": "KRAKEN",
    "kucoin": "KUCOIN",
    "kucoin-futures": "KUCOIN",
    "mango": "MANGO",
    "okcoin": "OKCOIN",
    "okex": "OKEX",
    "okex-futures": "OKEX",
    "okex-options": "OKEX",
    "okex-spreads": "OKEX",
    "okex-swap": "OKEX",
    "phemex": "PHEMEX",
    "poloniex": "POLONIEX",
    "serum": "SERUM",
    "star-atlas": "STAR_ATLAS",
    "upbit": "UPBIT",
    "woo-x": "WOO_X",
}


def test_exchange_to_venue_mapping():
    """
    Test that all Tardis exchanges map to valid Nautilus venues.
    """
    exchanges = tardis_exchanges()
    for exchange_str in exchanges:
        venue_str = tardis_exchange_to_venue_str(exchange_str)
        try:
            # Verify the venue string is what we expect
            if exchange_str in _EXPECTED_VENUE_MAPPINGS:
                expected_venue = _EXPECTED_VENUE_MAPPINGS[exchange_str]
                assert venue_str == expected_venue, (
                    f"Tardis exchange '{exchange_str}' maps to '{venue_str}' "
                    f"but expected '{expected_venue}'"
                )
        except ValueError:
            raise AssertionError(f"Tardis exchange '{exchange_str}' maps to invalid Nautilus venue '{venue_str}'")


def test_venue_to_exchange_mapping_bidirectional():
    """
    Test bidirectional mapping between venues and exchanges.
    """
    # Get all unique venue strings from expected mappings
    expected_venues = set(_EXPECTED_VENUE_MAPPINGS.values())

    for venue_str in expected_venues:
        try:
            venue = Venue(venue_str)
            exchanges = tardis_exchange_from_venue_str(venue.value)

            # Some venues might not map to exchanges (this is acceptable)
            if not exchanges:
                continue

            # Test bidirectional mapping for venues that do map
            for exchange_str in exchanges:
                mapped_venue_str = tardis_exchange_to_venue_str(exchange_str)
                assert mapped_venue_str == venue.value, (
                    f"Bidirectional mapping failed: Nautilus venue '{venue.value}' -> "
                    f"Tardis exchange '{exchange_str}' -> Nautilus venue '{mapped_venue_str}'"
                )
        except ValueError:
            # Some venue strings might not be valid Venue instances, skip them
            continue
```


---

## Overview

This file is located at `tests/integration_tests/adapters/tardis/test_enums.py` within the repository.

**Functions defined:** test_exchange_to_venue_mapping, test_venue_to_exchange_mapping_bidirectional

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `test_exchange_to_venue_mapping()`


#### `test_venue_to_exchange_mapping_bidirectional()`


### Imports

- `from nautilus_trader.core.nautilus_pyo3 import tardis_exchange_from_venue_str`
- `from nautilus_trader.core.nautilus_pyo3 import tardis_exchange_to_venue_str`
- `from nautilus_trader.core.nautilus_pyo3 import tardis_exchanges`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.tardis.test_enums import test_exchange_to_venue_mapping
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.nautilus_pyo3 import tardis_exchange_from_venue_str`
- `from nautilus_trader.core.nautilus_pyo3 import tardis_exchange_to_venue_str`
- `from nautilus_trader.core.nautilus_pyo3 import tardis_exchanges`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `tests/integration_tests/adapters/tardis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


