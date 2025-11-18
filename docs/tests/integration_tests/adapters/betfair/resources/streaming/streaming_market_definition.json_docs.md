# Documentation: streaming_market_definition.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition.json`
- **Size**: 1,712 bytes
- **Lines**: 87
- **Language**: JSON

## Original Source

```json
{
  "bspMarket": true,
  "turnInPlayEnabled": true,
  "persistenceEnabled": true,
  "marketBaseRate": 5,
  "eventId": "27890558",
  "eventTypeId": "7",
  "numberOfWinners": 1,
  "bettingType": "ODDS",
  "marketType": "WIN",
  "marketTime": "2016-08-17T18:10:00.000Z",
  "suspendTime": "2016-08-17T18:10:00.000Z",
  "bspReconciled": false,
  "complete": true,
  "inPlay": false,
  "crossMatching": false,
  "runnersVoidable": false,
  "numberOfActiveRunners": 7,
  "betDelay": 0,
  "status": "OPEN",
  "keyLineDefinition": {
    "kl": [
      {
        "hc": -2,
        "id": 11131804
      },
      {
        "hc": 2,
        "id": 11064886
      }
    ]
  },
  "runners": [
    {
      "adjustmentFactor": 44.323,
      "status": "ACTIVE",
      "sortPriority": 1,
      "id": 11131804
    },
    {
      "adjustmentFactor": 41.972,
      "status": "ACTIVE",
      "sortPriority": 2,
      "id": 11064886
    },
    {
      "adjustmentFactor": 6.006,
      "status": "ACTIVE",
      "sortPriority": 3,
      "id": 11404390
    },
    {
      "adjustmentFactor": 3.635,
      "status": "ACTIVE",
      "sortPriority": 4,
      "id": 11527192
    },
    {
      "adjustmentFactor": 3.129,
      "status": "ACTIVE",
      "sortPriority": 5,
      "id": 14341
    },
    {
      "adjustmentFactor": 0.468,
      "status": "ACTIVE",
      "sortPriority": 6,
      "id": 11530194
    },
    {
      "adjustmentFactor": 0.468,
      "status": "ACTIVE",
      "sortPriority": 7,
      "id": 10257411
    }
  ],
  "regulators": [
    "MR_INT"
  ],
  "venue": "Kempton",
  "countryCode": "GB",
  "discountAllowed": true,
  "timezone": "Europe/London",
  "openDate": "2016-08-17T17:40:00.000Z",
  "version": 1400311331
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `ACTIVE`, `Europe`, `Kempton`, `London`, `MR_INT`, `ODDS`, `OPEN`, `WIN`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/streaming/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.458607Z*
