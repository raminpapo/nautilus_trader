# Documentation: types.sql

## File Metadata

- **Path**: `schema/sql/types.sql`
- **Size**: 2,243 bytes
- **Lines**: 38
- **Language**: SQL

## Original Source

```sql
------------------- ENUMS -------------------

CREATE TYPE ACCOUNT_TYPE AS ENUM ('Cash', 'Margin', 'Betting');
CREATE TYPE AGGREGATION_SOURCE AS ENUM ('EXTERNAL', 'INTERNAL');
CREATE TYPE AGGRESSOR_SIDE AS ENUM ('NO_AGGRESSOR','BUYER','SELLER');
CREATE TYPE ASSET_CLASS AS ENUM ('FX', 'EQUITY', 'COMMODITY', 'DEBT', 'INDEX', 'CRYPTOCURRENCY', 'ALTERNATIVE');
CREATE TYPE INSTRUMENT_CLASS AS ENUM ('Spot', 'Swap', 'Future', 'FutureSpread', 'Forward', 'Cfg', 'Bond', 'Option', 'OptionSpread', 'Warrant', 'SportsBetting');
CREATE TYPE BAR_AGGREGATION AS ENUM ('TICK', 'TICK_IMBALANCE', 'TICK_RUNS', 'VOLUME', 'VOLUME_IMBALANCE', 'VOLUME_RUNS', 'VALUE', 'VALUE_IMBALANCE', 'VALUE_RUNS', 'MILLISECOND', 'SECOND', 'MINUTE', 'HOUR', 'DAY', 'WEEK', 'MONTH');
CREATE TYPE BOOK_ACTION AS ENUM ('Add', 'Update', 'Delete','Clear');
CREATE TYPE ORDER_STATUS AS ENUM ('Initialized', 'Denied', 'Emulated', 'Released', 'Submitted', 'Accepted', 'Rejected', 'Canceled', 'Expired', 'Triggered', 'PendingUpdate', 'PendingCancel', 'PartiallyFilled', 'Filled');
CREATE TYPE CURRENCY_TYPE AS ENUM('CRYPTO', 'FIAT', 'COMMODITY_BACKED');
CREATE TYPE TRAILING_OFFSET_TYPE AS ENUM('NO_TRAILING_OFFSET', 'PRICE', 'BASIS_POINTS', 'TICKS', 'PRICE_TIER');
CREATE TYPE PRICE_TYPE AS ENUM('BID','ASK','MID','LAST');

------------------- DOMAIN TYPES -------------------

CREATE DOMAIN I256 AS NUMERIC(78, 0) CONSTRAINT i256_range CHECK (
    VALUE >= -57896044618658097711785492504343953926634992332820282019728792003956564819968
    AND VALUE <= 57896044618658097711785492504343953926634992332820282019728792003956564819967
);

CREATE DOMAIN U256 AS NUMERIC(78, 0) CONSTRAINT u256_range CHECK (
    VALUE >= 0 AND VALUE <= 115792089237316195423570985008687907853269984665640564039457584007913129639935
);

CREATE DOMAIN U128 AS NUMERIC(39, 0) CONSTRAINT u128_range CHECK (
    VALUE >= 0 AND VALUE <= 340282366920938463463374607431768211455
);

CREATE DOMAIN U160 AS NUMERIC(49, 0) CONSTRAINT u160_range CHECK (
    VALUE >= 0 AND VALUE <= 1461501637330902918203684832716283019655932542975
);

CREATE DOMAIN I128 AS NUMERIC(39, 0) CONSTRAINT i128_range CHECK (
    VALUE >= -170141183460469231731687303715884105728
    AND VALUE <= 170141183460469231731687303715884105727
);

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 97


**Identifiers**: `ACCOUNT_TYPE`, `AGGREGATION_SOURCE`, `AGGRESSOR_SIDE`, `ALTERNATIVE`, `AND`, `ASK`, `ASSET_CLASS`, `Accepted`, `Add`, `BAR_AGGREGATION`, `BASIS_POINTS`, `BID`, `BOOK_ACTION`, `BUYER`, `Betting`, `Bond`, `CHECK`, `COMMODITY`, `COMMODITY_BACKED`, `CONSTRAINT`, `CREATE`, `CRYPTO`, `CRYPTOCURRENCY`, `CURRENCY_TYPE`, `Canceled`, `Cash`, `Cfg`, `Clear`, `DAY`, `DEBT` *(+67 more)*

## Related Files

This file is located in `schema/sql/`. Related files may include:
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
*Generated on 2025-11-18T21:55:06.123222Z*
