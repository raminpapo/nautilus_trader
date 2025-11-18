# Documentation: http_get_instruments_BTC-USDC.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/http_get_instruments_BTC-USDC.json`
- **Size**: 1,490 bytes
- **Lines**: 50
- **Language**: JSON

## Original Source

```json
{
  "instrument_id": "252572044003115008",
  "instrument_uuid": "cf8dee38-6d4e-4658-a5ff-70c19201c485",
  "symbol": "BTC-USDC",
  "type": "SPOT",
  "mode": "STANDARD",
  "base_asset_id": "118059611751202816",
  "base_asset_uuid": "5b71fc48-3dd3-540c-809b-f8c94d0e68b5",
  "base_asset_name": "BTC",
  "quote_asset_id": "1",
  "quote_asset_uuid": "2b92315d-eab7-5bef-84fa-089a131333f5",
  "quote_asset_name": "USDC",
  "base_increment": "0.00001",
  "quote_increment": "0.01",
  "price_band_percent": 0.02,
  "market_order_percent": 0.0075,
  "qty_24hr": "0",
  "notional_24hr": "0",
  "avg_daily_qty": "1241.5042833333332",
  "avg_daily_notional": "125201028.9956107",
  "avg_30day_notional": "3756030869.868321",
  "avg_30day_qty": "37245.1285",
  "previous_day_qty": "0",
  "open_interest": "0",
  "position_limit_qty": "0",
  "position_limit_adq_pct": 0.0,
  "position_notional_limit": "5000000",
  "open_interest_notional_limit": "26000000",
  "replacement_cost": "0",
  "base_imf": 1.0,
  "min_notional_value": "10",
  "funding_interval": "0",
  "trading_state": "TRADING",
  "quote": {
    "best_bid_size": "0",
    "best_ask_size": "0",
    "trade_price": "101761.64",
    "trade_qty": "3",
    "index_price": "97728.02",
    "mark_price": "101761.64",
    "settlement_price": "101761.64",
    "limit_up": "102614.41",
    "limit_down": "92841.61",
    "timestamp": "2025-02-05T06:40:23.040Z"
  },
  "default_imf": 1.0,
  "base_asset_multiplier": "1.0",
  "underlying_type": "SPOT"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BTC`, `SPOT`, `STANDARD`, `TRADING`, `USDC`

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
pytest crates/adapters/coinbase_intx/test_data/http_get_instruments_BTC-USDC.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.651720Z*
