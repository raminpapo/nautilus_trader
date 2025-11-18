# Documentation: streaming_mcm_UPDATE_md.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_UPDATE_md.json`
- **Size**: 1,289 bytes
- **Lines**: 53
- **Language**: JSON

## Original Source

```json
{
  "op": "mcm",
  "id": 12345,
  "clk": "AKEIANcNANkP",
  "pt": 1478717720756,
  "mc": [
    {
      "id": "1.180770798",
      "marketDefinition": {
        "bspMarket": false,
        "turnInPlayEnabled": true,
        "persistenceEnabled": true,
        "marketBaseRate": 5,
        "eventId": "30363344",
        "eventTypeId": "2",
        "numberOfWinners": 1,
        "bettingType": "ODDS",
        "marketType": "GAME_BY_GAME_01_07",
        "marketTime": "2021-03-19T04:00:00+00:00",
        "suspendTime": "2021-03-19T04:00:00+00:00",
        "bspReconciled": false,
        "complete": true,
        "inPlay": true,
        "crossMatching": true,
        "runnersVoidable": false,
        "numberOfActiveRunners": 2,
        "betDelay": 5,
        "status": "SUSPENDED",
        "runners": [
          {
            "status": "ACTIVE",
            "sortPriority": 1,
            "id": "13834991"
          },
          {
            "status": "ACTIVE",
            "sortPriority": 2,
            "id": "3120169"
          }
        ],
        "regulators": [
          "MR_INT"
        ],
        "countryCode": "CO",
        "discountAllowed": true,
        "timezone": "UTC",
        "openDate": "2021-03-19T04:00:00+00:00",
        "version": 1488624717
      }
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `ACTIVE`, `AKEIANcNANkP`, `GAME_BY_GAME_01_07`, `MR_INT`, `ODDS`, `SUSPENDED`, `UTC`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_UPDATE_md.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.517794Z*
