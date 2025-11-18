# Documentation: http_get_instruments_BTC-PERP.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/http_get_instruments_BTC-PERP.json`
- **Size**: 1,605 bytes
- **Lines**: 52
- **Language**: JSON

## Original Source

```json
{
  "instrument_id": "149264167780483072",
  "instrument_uuid": "b3469e0b-222c-4f8a-9f68-1f9e44d7e5e0",
  "symbol": "BTC-PERP",
  "type": "PERP",
  "mode": "STANDARD",
  "base_asset_id": "118059611751202816",
  "base_asset_uuid": "5b71fc48-3dd3-540c-809b-f8c94d0e68b5",
  "base_asset_name": "BTC",
  "quote_asset_id": "1",
  "quote_asset_uuid": "2b92315d-eab7-5bef-84fa-089a131333f5",
  "quote_asset_name": "USDC",
  "base_increment": "0.0001",
  "quote_increment": "0.1",
  "price_band_percent": 0.05,
  "market_order_percent": 0.01,
  "qty_24hr": "0.0051",
  "notional_24hr": "499.3577",
  "avg_daily_qty": "2362.797683333333",
  "avg_daily_notional": "237951057.95349997",
  "avg_30day_notional": "7138531738.605",
  "avg_30day_qty": "70883.9305",
  "previous_day_qty": "0.0116",
  "open_interest": "899.6503",
  "position_limit_qty": "2362.7977",
  "position_limit_adq_pct": 1.0,
  "position_notional_limit": "120000000",
  "open_interest_notional_limit": "300000000",
  "replacement_cost": "0.19",
  "base_imf": 0.1,
  "min_notional_value": "10",
  "funding_interval": "3600000000000",
  "trading_state": "TRADING",
  "quote": {
    "best_bid_price": "96785.5",
    "best_bid_size": "0.0005",
    "best_ask_size": "0",
    "trade_price": "97908.8",
    "trade_qty": "0.0005",
    "index_price": "97743.1",
    "mark_price": "97908.8",
    "settlement_price": "97908.8",
    "limit_up": "107517.3",
    "limit_down": "87968.7",
    "predicted_funding": "-0.000044",
    "timestamp": "2025-02-05T06:40:42.399Z"
  },
  "default_imf": 0.2,
  "base_asset_multiplier": "1.0",
  "underlying_type": "SPOT"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `BTC`, `PERP`, `SPOT`, `STANDARD`, `TRADING`, `USDC`

## Related Files

This file is located in `crates/adapters/coinbase_intx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/coinbase_intx/test_data/http_get_instruments_BTC-PERP.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.650440Z*
