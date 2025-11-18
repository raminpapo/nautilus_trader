# Documentation: example_config.json

## File Metadata

- **Path**: `crates/adapters/tardis/bin/example_config.json`
- **Size**: 516 bytes
- **Lines**: 31
- **Language**: JSON

## Original Source

```json
{
  "tardis_ws_url": "ws://localhost:8001",
  "normalize_symbols": true,
  "output_path": null,
  "options": [
    {
      "exchange": "binance-futures",
      "symbols": [
        "btcusdt"
      ],
      "data_types": [
        "trade"
      ],
      "from": "2023-10-01",
      "to": "2023-10-02"
    },
    {
      "exchange": "bitmex",
      "symbols": [
        "xbtusd",
        "ethusd"
      ],
      "data_types": [
        "trade"
      ],
      "from": "2019-10-01",
      "to": "2019-10-02"
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/adapters/tardis/bin/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.637635Z*
