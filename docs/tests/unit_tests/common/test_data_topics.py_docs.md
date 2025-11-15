# Documentation: `tests/unit_tests/common/test_data_topics.py`
**Generated:** 2025-11-15T19:40:09.047783Z
**File Size:** 6294 bytes
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

- **Path:** `tests/unit_tests/common/test_data_topics.py`
- **Size:** 6,294 bytes
- **Lines:** 171
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9
- **Classes:** 1
- **Functions:** 15

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


from nautilus_trader.common.data_topics import TopicCache
from nautilus_trader.model.data import DataType
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import OrderBookDepth10
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs


class TestTopicCache:
    def setup(self):
        self.cache = TopicCache()
        self.instrument_id = TestInstrumentProvider.default_fx_ccy("AUD/USD").id
        self.venue = Venue("BINANCE")

    def test_get_instruments_topic_non_historical(self):
        # Arrange, Act
        topic = self.cache.get_instrument_topic(self.instrument_id, historical=False)

        # Assert
        assert topic == f"data.instrument.{self.instrument_id.venue}.{self.instrument_id.symbol}"

    def test_get_instruments_topic_historical(self):
        # Arrange, Act
        topic = self.cache.get_instrument_topic(self.instrument_id, historical=True)

        # Assert
        assert (
            topic
            == f"historical.data.instrument.{self.instrument_id.venue}.{self.instrument_id.symbol}"
        )

    def test_get_instruments_topic_caching(self):
        # Arrange, Act
        topic1 = self.cache.get_instrument_topic(self.instrument_id, historical=False)
        topic2 = self.cache.get_instrument_topic(self.instrument_id, historical=False)

        # Assert - should return same cached instance
        assert topic1 is topic2

    def test_get_instruments_topic_pattern(self):
        # Arrange, Act
        topic = self.cache.get_instruments_topic(self.venue)

        # Assert
        assert topic == f"data.instrument.{self.venue}.*"

    def test_get_book_topic_deltas(self):
        # Arrange, Act
        topic = self.cache.get_book_topic(OrderBookDelta, self.instrument_id, historical=False)

        # Assert
        assert (
            topic
            == f"data.book.deltas.{self.instrument_id.venue}.{self.instrument_id.symbol.topic()}"
        )

    def test_get_book_topic_depth(self):
        # Arrange, Act
        topic = self.cache.get_book_topic(OrderBookDepth10, self.instrument_id, historical=False)

        # Assert
        assert (
            topic
            == f"data.book.depth.{self.instrument_id.venue}.{self.instrument_id.symbol.topic()}"
        )

    def test_get_quotes_topic_historical(self):
        # Arrange, Act
        topic = self.cache.get_quotes_topic(self.instrument_id, historical=True)

        # Assert
        assert (
            topic
            == f"historical.data.quotes.{self.instrument_id.venue}.{self.instrument_id.symbol}"
        )

    def test_get_trades_topic_historical(self):
        # Arrange, Act
        topic = self.cache.get_trades_topic(self.instrument_id, historical=True)

        # Assert
        assert (
            topic
            == f"historical.data.trades.{self.instrument_id.venue}.{self.instrument_id.symbol}"
        )

    def test_get_bars_topic_non_historical(self):
        # Arrange
        bar_type = TestDataStubs.bartype_audusd_1min_bid()

        # Act
        topic = self.cache.get_bars_topic(bar_type, historical=False)

        # Assert
        assert topic == f"data.bars.{bar_type}"

    def test_get_bars_topic_historical(self):
        # Arrange
        bar_type = TestDataStubs.bartype_audusd_1min_bid()

        # Act
        topic = self.cache.get_bars_topic(bar_type, historical=True)

        # Assert
        assert topic == f"historical.data.bars.{bar_type}"

    def test_get_custom_data_topic_with_metadata(self):
        # Arrange
        from nautilus_trader.model.data import QuoteTick

        data_type = DataType(QuoteTick, metadata={"topic": "custom.data.topic"})

        # Act
        topic = self.cache.get_custom_data_topic(data_type, self.instrument_id, historical=False)

        # Assert - when metadata has 'topic' key, it uses data_type.topic which includes the metadata
        assert topic == "data.QuoteTick.topic=custom.data.topic"

    def test_get_custom_data_topic_without_metadata(self):
        # Arrange
        from nautilus_trader.model.data import QuoteTick

        data_type = DataType(QuoteTick)

        # Act
        topic = self.cache.get_custom_data_topic(data_type, self.instrument_id, historical=False)

        # Assert
        assert (
            topic
            == f"data.QuoteTick.{self.instrument_id.venue}.{self.instrument_id.symbol.topic()}"
        )

    def test_get_signal_topic(self):
        # Arrange, Act
        topic = self.cache.get_signal_topic("test")

        # Assert
        assert topic == "data.SignalTest*"

    def test_clear_cache(self):
        # Arrange - populate some caches
        self.cache.get_instrument_topic(self.instrument_id, historical=False)
        self.cache.get_quotes_topic(self.instrument_id, historical=False)
        bar_type = TestDataStubs.bartype_audusd_1min_bid()
        self.cache.get_bars_topic(bar_type, historical=False)

        # Act
        self.cache.clear_cache()

        # Assert - verify caches are cleared by checking new topics are created
        topic1 = self.cache.get_instrument_topic(self.instrument_id, historical=False)
        topic2 = self.cache.get_instrument_topic(self.instrument_id, historical=False)
        assert topic1 is topic2  # Should be cached again after clear
```


---

## Overview

This file is located at `tests/unit_tests/common/test_data_topics.py` within the repository.

**Classes defined:** TestTopicCache

**Functions defined:** setup, test_get_instruments_topic_non_historical, test_get_instruments_topic_historical, test_get_instruments_topic_caching, test_get_instruments_topic_pattern, test_get_book_topic_deltas, test_get_book_topic_depth, test_get_quotes_topic_historical, test_get_trades_topic_historical, test_get_bars_topic_non_historical and 5 more

**Import statements:** 9


---

## Detailed Analysis

### Classes

#### `TestTopicCache`


### Functions

#### `setup(self)`


#### `test_get_instruments_topic_non_historical(self)`


#### `test_get_instruments_topic_historical(self)`


#### `test_get_instruments_topic_caching(self)`


#### `test_get_instruments_topic_pattern(self)`


#### `test_get_book_topic_deltas(self)`


#### `test_get_book_topic_depth(self)`


#### `test_get_quotes_topic_historical(self)`


#### `test_get_trades_topic_historical(self)`


#### `test_get_bars_topic_non_historical(self)`


#### `test_get_bars_topic_historical(self)`


#### `test_get_custom_data_topic_with_metadata(self)`


#### `test_get_custom_data_topic_without_metadata(self)`


#### `test_get_signal_topic(self)`


#### `test_clear_cache(self)`


### Imports

- `from nautilus_trader.common.data_topics import TopicCache`
- `from nautilus_trader.model.data import DataType`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import OrderBookDepth10`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import QuoteTick`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_data_topics import TestTopicCache
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.data_topics import TopicCache`
- `from nautilus_trader.model.data import DataType`
- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.model.data import OrderBookDepth10`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import QuoteTick`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


