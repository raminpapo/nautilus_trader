# Documentation: market.capnp

## File Metadata

- **Path**: `crates/serialization/schemas/capnp/data/market.capnp`
- **Size**: 4,352 bytes
- **Lines**: 167
- **Language**: Unknown

## Original Source

```
@0xe9ad557eba0125dc;
# Cap'n Proto schema for Nautilus market data types

using Identifiers = import "../common/identifiers.capnp";
using Types = import "../common/types.capnp";
using Enums = import "../common/enums.capnp";
using Base = import "../common/base.capnp";

# Quote tick - top-of-book bid/ask
struct QuoteTick {
    instrumentId @0 :Identifiers.InstrumentId;
    bidPrice @1 :Types.Price;
    askPrice @2 :Types.Price;
    bidSize @3 :Types.Quantity;
    askSize @4 :Types.Quantity;
    tsEvent @5 :Base.UnixNanos;
    tsInit @6 :Base.UnixNanos;
}

# Trade tick - individual trade
struct TradeTick {
    instrumentId @0 :Identifiers.InstrumentId;
    price @1 :Types.Price;
    size @2 :Types.Quantity;
    aggressorSide @3 :Enums.AggressorSide;
    tradeId @4 :Identifiers.TradeId;
    tsEvent @5 :Base.UnixNanos;
    tsInit @6 :Base.UnixNanos;
}

# Bar specification
struct BarSpec {
    step @0 :UInt32;
    aggregation @1 :Enums.BarAggregation;
    priceType @2 :Enums.PriceType;
}

# Bar type
struct BarType {
    instrumentId @0 :Identifiers.InstrumentId;
    spec @1 :BarSpec;
    aggregationSource @2 :Enums.AggregationSource;
}

# Bar/Candlestick
struct Bar {
    barType @0 :BarType;
    open @1 :Types.Price;
    high @2 :Types.Price;
    low @3 :Types.Price;
    close @4 :Types.Price;
    volume @5 :Types.Quantity;
    tsEvent @6 :Base.UnixNanos;
    tsInit @7 :Base.UnixNanos;
}

# Mark price update
struct MarkPriceUpdate {
    instrumentId @0 :Identifiers.InstrumentId;
    markPrice @1 :Types.Price;
    tsEvent @2 :Base.UnixNanos;
    tsInit @3 :Base.UnixNanos;
}

# Index price update
struct IndexPriceUpdate {
    instrumentId @0 :Identifiers.InstrumentId;
    indexPrice @1 :Types.Price;
    tsEvent @2 :Base.UnixNanos;
    tsInit @3 :Base.UnixNanos;
}

# Instrument close
struct InstrumentClose {
    instrumentId @0 :Identifiers.InstrumentId;
    closePrice @1 :Types.Price;
    closeType @2 :Enums.InstrumentCloseType;
    tsEvent @3 :Base.UnixNanos;
    tsInit @4 :Base.UnixNanos;
}

struct InstrumentStatus {
    instrumentId @0 :Identifiers.InstrumentId;
    action @1 :Enums.MarketStatusAction;
    reason @2 :Text;  # Optional explanation (empty if not provided)
    tradingEvent @3 :Text;  # Optional venue-specific trading event description
    isTrading @4 :Bool;
    isQuoting @5 :Bool;
    isShortSellRestricted @6 :Bool;
    tsEvent @7 :Base.UnixNanos;
    tsInit @8 :Base.UnixNanos;
}

# Funding rate update
struct FundingRateUpdate {
    instrumentId @0 :Identifiers.InstrumentId;
    rate @1 :Types.Decimal;  # Decimal as binary (optimized)
    nextFundingTime @2 :Base.UnixNanos;  # Optional - 0 means None
    tsEvent @3 :Base.UnixNanos;
    tsInit @4 :Base.UnixNanos;
}

# Market data enum union
struct DataAny {
    union {
        quote @0 :QuoteTick;
        trade @1 :TradeTick;
        bar @2 :Bar;
        markPrice @3 :MarkPriceUpdate;
        indexPrice @4 :IndexPriceUpdate;
        instrumentClose @5 :InstrumentClose;
        instrumentStatus @6 :InstrumentStatus;
        fundingRate @7 :FundingRateUpdate;
        orderBookDelta @8 :OrderBookDelta;
        orderBookDeltas @9 :OrderBookDeltas;
        orderBookDepth10 @10 :OrderBookDepth10;
    }
}

# Book order
struct BookOrder {
    price @0 :Types.Price;
    size @1 :Types.Quantity;
    side @2 :Enums.OrderSide;
    orderId @3 :UInt64;
}

# Order book delta (single)
struct OrderBookDelta {
    instrumentId @0 :Identifiers.InstrumentId;
    action @1 :Enums.BookAction;
    order @2 :BookOrder;
    flags @3 :UInt8;
    sequence @4 :UInt64;
    tsEvent @5 :Base.UnixNanos;
    tsInit @6 :Base.UnixNanos;
}

# Order book deltas (batch)
struct OrderBookDeltas {
    instrumentId @0 :Identifiers.InstrumentId;
    deltas @1 :List(OrderBookDelta);
    flags @2 :UInt8;
    sequence @3 :UInt64;
    tsEvent @4 :Base.UnixNanos;
    tsInit @5 :Base.UnixNanos;
}

# Book level
struct BookLevel {
    price @0 :Types.Price;
    size @1 :Types.Quantity;
}

# Order book depth (top 10 levels)
struct OrderBookDepth10 {
    instrumentId @0 :Identifiers.InstrumentId;
    bids @1 :List(BookLevel);  # Up to 10 levels
    asks @2 :List(BookLevel);  # Up to 10 levels
    bidCounts @3 :List(UInt32);
    askCounts @4 :List(UInt32);
    flags @5 :UInt8;
    sequence @6 :UInt64;
    tsEvent @7 :Base.UnixNanos;
    tsInit @8 :Base.UnixNanos;
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 55


**Identifiers**: `AggregationSource`, `AggressorSide`, `Bar`, `BarAggregation`, `BarSpec`, `BarType`, `Base`, `Book`, `BookAction`, `BookLevel`, `BookOrder`, `Bool`, `Candlestick`, `Cap`, `DataAny`, `Decimal`, `Enums`, `Funding`, `FundingRateUpdate`, `Identifiers`, `Index`, `IndexPriceUpdate`, `Instrument`, `InstrumentClose`, `InstrumentCloseType`, `InstrumentId`, `InstrumentStatus`, `List`, `Mark`, `MarkPriceUpdate` *(+25 more)*

## Related Files

This file is located in `crates/serialization/schemas/capnp/data/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.065502Z*
