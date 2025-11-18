# Documentation: ws_instruments.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/ws_instruments.json`
- **Size**: 927 bytes
- **Lines**: 30
- **Language**: JSON

## Original Source

```json
{
  "channel": "INSTRUMENTS",
  "type": "SNAPSHOT",
  "product_id": "ETH-PERP",
  "sequence": 0,
  "time": "2025-03-14T22:59:53.373Z",
  "instrument_type": "PERP",
  "instrument_mode": "standard",
  "base_asset_name": "ETH",
  "quote_asset_name": "USDC",
  "base_increment": "0.0001",
  "quote_increment": "0.01",
  "avg_daily_quantity": "229061.15400333333",
  "avg_daily_volume": "5.33931093731498E8",
  "total30_day_quantity": "6871834.6201",
  "total30_day_volume": "1.601793281194494E10",
  "total24_hour_quantity": "116705.0261",
  "total24_hour_volume": "2.22252453944151E8",
  "base_imf": "0.05",
  "min_quantity": "0.0001",
  "position_size_limit": "5841.0594",
  "position_notional_limit": "70000000",
  "funding_interval": "3600000000000",
  "trading_state": "trading",
  "last_updated_time": "2025-03-14T22:00:00Z",
  "default_initial_margin": "0.2",
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


**Identifiers**: `ETH`, `INSTRUMENTS`, `PERP`, `SNAPSHOT`, `SPOT`, `USDC`

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
pytest crates/adapters/coinbase_intx/test_data/ws_instruments.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.666991Z*
