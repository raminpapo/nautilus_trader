# Documentation: list_current_orders_execution_complete.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/list_current_orders_execution_complete.json`
- **Size**: 2,230 bytes
- **Lines**: 80
- **Language**: JSON

## Original Source

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "currentOrders": [
      {
        "betId": "228059754671",
        "marketId": "1.180575118",
        "selectionId": 39980,
        "handicap": 0.0,
        "priceSize": {
          "price": 5.0,
          "size": 10.0
        },
        "bspLiability": 0.0,
        "side": "BACK",
        "status": "EXECUTABLE",
        "persistenceType": "LAPSE",
        "orderType": "LIMIT",
        "placedDate": "2021-03-24T06:47:02.000Z",
        "averagePriceMatched": 0.0,
        "sizeMatched": 0.0,
        "sizeRemaining": 10.0,
        "sizeLapsed": 0.0,
        "sizeCancelled": 0.0,
        "sizeVoided": 0.0,
        "regulatorCode": "MALTA LOTTERIES AND GAMBLING AUTHORITY"
      },
      {
        "betId": "228059821049",
        "marketId": "1.180575118",
        "selectionId": 217709,
        "handicap": 0.0,
        "priceSize": {
          "price": 1.9,
          "size": 10.0
        },
        "bspLiability": 0.0,
        "side": "BACK",
        "status": "EXECUTION_COMPLETE",
        "persistenceType": "LAPSE",
        "orderType": "LIMIT",
        "placedDate": "2021-03-24T06:49:41.000Z",
        "matchedDate": "2021-03-24T06:49:41.000Z",
        "averagePriceMatched": 1.9,
        "sizeMatched": 10.0,
        "sizeRemaining": 0.0,
        "sizeLapsed": 0.0,
        "sizeCancelled": 0.0,
        "sizeVoided": 0.0,
        "regulatorCode": "MALTA LOTTERIES AND GAMBLING AUTHORITY"
      },
      {
        "betId": "228059869313",
        "marketId": "1.180575118",
        "selectionId": 217709,
        "handicap": 0.0,
        "priceSize": {
          "price": 1.92,
          "size": 10.0
        },
        "bspLiability": 0.0,
        "side": "LAY",
        "status": "EXECUTION_COMPLETE",
        "persistenceType": "LAPSE",
        "orderType": "LIMIT",
        "placedDate": "2021-03-24T06:51:50.000Z",
        "matchedDate": "2021-03-24T06:51:50.000Z",
        "averagePriceMatched": 1.92,
        "sizeMatched": 10.0,
        "sizeRemaining": 0.0,
        "sizeLapsed": 0.0,
        "sizeCancelled": 0.0,
        "sizeVoided": 0.0,
        "regulatorCode": "MALTA LOTTERIES AND GAMBLING AUTHORITY"
      }
    ],
    "moreAvailable": false
  }
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 11


**Identifiers**: `AND`, `AUTHORITY`, `BACK`, `EXECUTABLE`, `EXECUTION_COMPLETE`, `GAMBLING`, `LAPSE`, `LAY`, `LIMIT`, `LOTTERIES`, `MALTA`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/responses/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/responses/list_current_orders_execution_complete.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.233605Z*
