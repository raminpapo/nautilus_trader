# Documentation: `tests/performance_tests/test_perf_msgbus.py`
**Generated:** 2025-11-15T19:40:08.048459Z
**File Size:** 1808 bytes
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

- **Path:** `tests/performance_tests/test_perf_msgbus.py`
- **Size:** 1,808 bytes
- **Lines:** 49
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 3

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

import random

from nautilus_trader.common.component import is_matching_py


def generate_topics(n: int, seed: int) -> list[str]:
    random.seed(seed)

    cat = ["data", "info", "order"]
    model = ["quotes", "trades", "orderbooks", "depths"]
    venue = ["BINANCE", "BYBIT", "OKX", "FTX", "KRAKEN"]
    instrument = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT"]

    topics: list[str] = []

    for _ in range(n):
        c = random.choice(cat)  # noqa: S311
        m = random.choice(model)  # noqa: S311
        v = random.choice(venue)  # noqa: S311
        i = random.choice(instrument)  # noqa: S311
        topics.append(f"{c}.{m}.{v}.{i}")

    return topics


def test_topic_pattern_matching(benchmark) -> None:
    topics = generate_topics(1000, 42)
    pattern = "data.*.BINANCE.ETH???"

    def match_topics():
        for topic in topics:
            is_matching_py(pattern, topic)

    benchmark(match_topics)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_msgbus.py` within the repository.

**Functions defined:** generate_topics, test_topic_pattern_matching, match_topics

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `generate_topics(n: int, seed: int)`


#### `test_topic_pattern_matching(benchmark)`


#### `match_topics()`


### Imports

- `import random`
- `from nautilus_trader.common.component import is_matching_py`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_msgbus import generate_topics
```


---

## Related Files

This file imports from the following modules:

- `import random`
- `from nautilus_trader.common.component import is_matching_py`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


