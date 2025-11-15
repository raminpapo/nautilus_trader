# Documentation: `nautilus_trader/adapters/interactive_brokers/web.py`
**Generated:** 2025-11-15T19:40:04.402745Z
**File Size:** 4977 bytes
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

- **Path:** `nautilus_trader/adapters/interactive_brokers/web.py`
- **Size:** 4,977 bytes
- **Lines:** 198
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Classes:** 3
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

import enum
from collections.abc import Generator
from typing import Any
from typing import NamedTuple

from lxml.etree import _Element
from lxml.html import fromstring

from nautilus_trader.core.nautilus_pyo3.network import http_get


class ProductClass(enum.Enum):
    """
    Interactive Brokers Web ProductClass.
    """

    ETFS = "ETF"
    INDICES = "IND"
    STOCKS = "STK"
    OPTIONS = "OPTGRP"
    WARRANTS = "WANT"


class Exchange(enum.Enum):
    """
    Interactive Brokers Exchange.
    """

    AEB = "aeb"
    ALPHA = "alpha"
    AMEX = "amex"
    ARCA = "arca"
    ARCAEDGE = "arcaedge"
    ASX = "asx"
    BATECH = "batech"
    BATEDE = "batede"
    BATEEN = "bateen"
    BATEEN_BE = "bateen-be"
    BATEEN_FR = "bateen-fr"
    BATEES = "batees"
    BATEUK = "bateuk"
    BATS = "bats"
    BEX = "bex"
    BM = "bm"
    BUX = "bux"
    BVL = "bvl"
    BVME = "bvme"
    BYX = "byx"
    CHIX_CA = "chix_ca"
    CHIXAU = "chixau"
    CHIXCH = "chixch"
    CHIXDE = "chixde"
    CHIXEN = "chixen"
    CHIXEN_BE = "chixen-be"
    CHIXEN_FR = "chixen-fr"
    CHIXES = "chixes"
    CHIXJ = "chixj"
    CHIXUK = "chixuk"
    CHX = "chx"
    DRCTEDGE = "drctedge"
    DXEDE = "dxede"
    EBS = "ebs"
    EDGEA = "edgea"
    ENEXT_BE = "enext.be"
    FWB = "fwb"
    GETTEX = "gettex"
    IBIS = "ibis"
    IEX = "iex"
    ISLAND = "island"
    JPNNEXT = "jpnnext"
    LSE = "lse"
    LSEIOB1 = "lseiob1"
    LTSE = "ltse"
    MEMX = "memx"
    MEXI = "mexi"
    MOEX = "moex"
    N_RIGA = "n.riga"
    N_TALLINN = "n.tallinn"
    N_VILNIUS = "n.vilnius"
    NASDAQ = "nasdaq"
    NITE = "nite"
    NSE = "nse"
    NYSE = "nyse"
    NYSENAT = "nysenat"
    OMEGA = "omega"
    OMXNO = "omxno"
    PEARL = "pearl"
    PINK = "pink"
    PSX = "psx"
    SBF = "sbf"
    SEHK = "sehk"
    SEHKNTL = "sehkntl"
    SEHKSTAR = "sehkstar"
    SEHKSZSE = "sehkszse"
    SFB = "sfb"
    SGX = "sgx"
    SWB = "swb"
    TASE = "tase"
    TGATE = "tgate"
    TRQX_BE = "trqx-be"
    TRQX_FR = "trqx-fr"
    TRQXCH = "trqxch"
    TRQXDE = "trqxde"
    TRQXEN = "trqxen"
    TSE = "tse"
    TSEJ = "tsej"
    VENTURE = "venture"
    VIRTX = "virtx"
    VSE = "vse"
    WSE = "wse"


class Product(NamedTuple):
    """
    Interactive Brokers Web Product.
    """

    ib_symbol: Any  # TODO: More specific type
    description: Any  # TODO: More specific type
    native_symbol: Any  # TODO: More specific type
    currency: Any  # TODO: More specific type


def _parse_products(table: _Element) -> Generator:
    for row in table.xpath(".//tr")[1:]:
        ib_symbol, desc, symbol, currency = list(
            filter(None, map(str.strip, row.xpath(".//text()"))),
        )
        yield Product(
            ib_symbol=ib_symbol,
            description=desc,
            native_symbol=symbol,
            currency=currency,
        )


def load_product_list(
    exchange: Exchange,
    product_class: ProductClass,
    limit: int = 500,
    debug: bool = False,
) -> Generator:
    """
    Load all instruments for a given `exchange` and `product_class` via the Interactive
    Brokers web interface.

    >>> products = load_product_list(exchange=Exchange.NYSE, product_class=ProductClass.STOCKS)

    """
    url = "https://www.interactivebrokers.com/en/index.php"
    params = {
        "f": "2222",
        "exch": exchange.value,
        "showcategories": product_class.value,
        "limit": str(limit),
    }
    page = 0

    while True:
        page += 1
        params.update({"page": str(page)})

        if debug:
            print(f"Requesting instruments using {params=}")

        response = http_get(url, params=params, timeout_secs=30)
        tree = fromstring(response.body)
        tables = tree.xpath('//table[@class="table table-striped table-bordered"]')

        if not tables:
            break
        try:
            symbol_table = tables[2]
        except IndexError:
            break

        products = list(_parse_products(symbol_table))

        if not products:
            break

        print(f"Found {len(products)} products for {page=}")
        yield from products
```


---

## Overview

This file is located at `nautilus_trader/adapters/interactive_brokers/web.py` within the repository.

**Classes defined:** ProductClass, Exchange, Product

**Functions defined:** _parse_products, load_product_list

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `ProductClass`

**Inherits from:** enum.Enum


#### `Exchange`

**Inherits from:** enum.Enum


#### `Product`

**Inherits from:** NamedTuple


### Functions

#### `_parse_products(table: _Element)`


#### `load_product_list(
    exchange: Exchange,
    product_class: ProductClass,
    limit: int = 500,
    debug: bool = False,
)`


### Imports

- `import enum`
- `from collections.abc import Generator`
- `from typing import Any`
- `from typing import NamedTuple`
- `from lxml.etree import _Element`
- `from lxml.html import fromstring`
- `from nautilus_trader.core.nautilus_pyo3.network import http_get`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.interactive_brokers.web import ProductClass
```


---

## Related Files

This file imports from the following modules:

- `import enum`
- `from collections.abc import Generator`
- `from typing import Any`
- `from typing import NamedTuple`
- `from lxml.etree import _Element`
- `from lxml.html import fromstring`
- `from nautilus_trader.core.nautilus_pyo3.network import http_get`

**Directory:** `nautilus_trader/adapters/interactive_brokers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


