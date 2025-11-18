# Documentation: web.py

## File Metadata

- **Path**: `nautilus_trader/adapters/interactive_brokers/web.py`
- **Size**: 4,977 bytes
- **Lines**: 199
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 3 class(es).

## Detailed Walkthrough

### Functions
- **`_parse_products()`**: Function defined in this file
- **`load_product_list()`**: Function defined in this file

### Classes
- **`ProductClass`**: Class defined in this file
- **`Exchange`**: Class defined in this file
- **`Product`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Classs**: `Exchange`, `Product`, `ProductClass`
**Functions**: `_parse_products`, `load_product_list`
**Imports**: `collections.abc`, `enum`, `lxml.etree`, `lxml.html`, `nautilus_trader.core.nautilus_pyo3.network`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/interactive_brokers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.881882Z*
