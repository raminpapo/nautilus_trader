# Documentation: filters.py

## File Metadata

- **Path**: `nautilus_trader/trading/filters.py`
- **Size**: 7,868 bytes
- **Lines**: 288
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

from datetime import datetime
from enum import Enum
from enum import unique

import pandas as pd

from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.core.data import Data
from nautilus_trader.core.datetime import is_datetime_utc
from nautilus_trader.model.objects import Currency


@unique
class NewsImpact(Enum):
    NONE = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4


class NewsEvent(Data):
    """
    Represents an economic news event.

    Parameters
    ----------
    impact : NewsImpact
        The expected impact for the economic news event.
    name : str
        The name of the economic news event.
    currency : Currency
        The currency the economic news event is expected to affect.
    ts_event : int
        UNIX timestamp (nanoseconds) when the news event occurred.
    ts_init : int
        UNIX timestamp (nanoseconds) when the data object was initialized.

    """

    def __init__(
        self,
        impact: NewsImpact,
        name: str,
        currency: Currency,
        ts_event: int,
        ts_init: int,
    ):
        self._impact = impact
        self._name = name
        self._currency = currency
        self._ts_event = ts_event
        self._ts_init = ts_init

    @property
    def impact(self) -> NewsImpact:
        return self._impact

    @property
    def name(self) -> str:
        return self._name

    @property
    def currency(self) -> Currency:
        return self._currency

    @property
    def ts_event(self) -> int:
        return self._ts_event

    @property
    def ts_init(self) -> int:
        return self._ts_init

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"impact={self.impact}, "
            f"name={self.name}, "
            f"currency={self.currency}, "
            f"ts_event={self.ts_event}, "
            f"ts_init={self.ts_init})"
        )


class EconomicNewsEventFilter:
    """
    Provides methods to help filter trading strategy rules based on economic news
    events.

    Parameters
    ----------
    currencies : list[str]
        The list of three letter currency codes to filter.
    impacts : list[str]
        The list of impact levels to filter ('LOW', 'MEDIUM', 'HIGH').
    news_data : pd.DataFrame
        The economic news data.

    """

    def __init__(
        self,
        currencies: list[str],
        impacts: list[str],
        news_data: pd.DataFrame,
    ):
        self._currencies = currencies
        self._impacts = impacts

        self._unfiltered_data_start = news_data.index[0]
        self._unfiltered_data_end = news_data.index[-1]

        self._news_data = news_data[
            news_data["Currency"].isin(currencies) & news_data["Impact"].isin(impacts)
        ]

    @property
    def unfiltered_data_start(self):
        """
        Return the start of the raw data.

        Returns
        -------
        datetime

        """
        return self._unfiltered_data_start

    @property
    def unfiltered_data_end(self):
        """
        Return the end of the raw data.

        Returns
        -------
        datetime

        """
        return self._unfiltered_data_end

    @property
    def currencies(self):
        """
        Return the currencies the data is filtered on.

        Returns
        -------
        list[str]

        """
        return self._currencies

    @property
    def impacts(self):
        """
        Return the news impacts the data is filtered on.

        Returns
        -------
        list[str]

        """
        return self._impacts

    def next_event(self, time_now: datetime) -> NewsEvent | None:
        """
        Return the next news event matching the filter conditions. Will return None if
        no news events match the filter conditions.

        Parameters
        ----------
        time_now : datetime
            The current time.

        Returns
        -------
        NewsEvent or ``None``
            The next news event in the filtered data if any.

        Raises
        ------
        ValueError
            The `time_now` < `self.unfiltered_data_start`.
        ValueError
            The `time_now` > `self.unfiltered_data_end`.
        ValueError
            If `time_now` is not tz aware UTC.

        """
        PyCondition.is_true(is_datetime_utc(time_now), "time_now was not tz aware UTC")

        if time_now < self._unfiltered_data_start:
            raise ValueError(
                f"The given time_now at {time_now} was prior to the "
                f"available news data start at {self._unfiltered_data_start}",
            )

        if time_now > self._unfiltered_data_end:
            raise ValueError(
                f"The given time_now at {time_now} was after the "
                f"available news data end at {self._unfiltered_data_end}",
            )

        events = self._news_data[self._news_data.index >= time_now]

        if events.empty:
            return None

        index = 0
        row = events.iloc[index]
        ts_event = pd.Timestamp(events.index[index]).value
        return NewsEvent(
            NewsImpact[row["Impact"]],
            row["Name"],
            Currency.from_str(row["Currency"]),
            ts_event,
            ts_event,
        )

    def prev_event(self, time_now: datetime) -> NewsEvent | None:
        """
        Return the previous news event matching the initial filter conditions. Will
        return None if no news events match the filter conditions.

        Parameters
        ----------
        time_now : datetime
            The current time.

        Returns
        -------
        NewsEvent or ``None``
            The previous news event in the filtered data if any.

        Raises
        ------
        ValueError
            The `time_now` < `self.unfiltered_data_start`.
        ValueError
            The `time_now` > `self.unfiltered_data_end`.
        ValueError
            If `time_now` is not tz aware UTC.

        """
        PyCondition.is_true(is_datetime_utc(time_now), "time_now was not tz aware UTC")

        if time_now < self._unfiltered_data_start:
            raise ValueError(
                f"The given time_now at {time_now} was prior to the "
                f"available news data start at {self._unfiltered_data_start}",
            )

        if time_now > self._unfiltered_data_end:
            raise ValueError(
                f"The given time_now at {time_now} was after the "
                f"available news data end at {self._unfiltered_data_end}",
            )

        events = self._news_data[self._news_data.index <= time_now]
        if events.empty:
            return None

        index = -1
        row = events.iloc[index]
        ts_event = pd.Timestamp(events.index[index]).value
        return NewsEvent(
            NewsImpact[row["Impact"]],
            row["Name"],
            Currency.from_str(row["Currency"]),
            ts_event,
            ts_event,
        )

```

## High-Level Overview

This file is part of the NautilusTrader repository. 3 class(es).

## Detailed Walkthrough


### Classes
- **`NewsImpact`**: Class defined in this file
- **`NewsEvent`**: Class defined in this file
- **`EconomicNewsEventFilter`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Classs**: `EconomicNewsEventFilter`, `NewsEvent`, `NewsImpact`
**Imports**: `datetime`, `enum`, `nautilus_trader.core.correctness`, `nautilus_trader.core.data`, `nautilus_trader.core.datetime`, `nautilus_trader.model.objects`, `pandas`

## Related Files

This file is located in `nautilus_trader/trading/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.023620Z*
