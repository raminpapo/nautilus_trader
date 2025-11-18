# Documentation: market_definition_open.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/market_definition_open.json`
- **Size**: 3,401 bytes
- **Lines**: 154
- **Language**: JSON

## Original Source

```json
{
  "bspMarket": true,
  "turnInPlayEnabled": false,
  "persistenceEnabled": false,
  "marketBaseRate": 7.0,
  "eventId": "31873357",
  "eventTypeId": "7",
  "numberOfWinners": 3,
  "bettingType": "ODDS",
  "marketType": "PLACE",
  "marketTime": "2022-11-01T01:49:00.000Z",
  "suspendTime": "2022-11-01T01:49:00.000Z",
  "bspReconciled": false,
  "complete": true,
  "inPlay": false,
  "crossMatching": false,
  "runnersVoidable": false,
  "numberOfActiveRunners": 17,
  "betDelay": 0,
  "status": "OPEN",
  "runners": [
    {
      "adjustmentFactor": 11.53,
      "status": "ACTIVE",
      "sortPriority": 1,
      "id": 49808334,
      "name": "1. Realaide"
    },
    {
      "adjustmentFactor": 1.25,
      "status": "ACTIVE",
      "sortPriority": 2,
      "id": 45368013,
      "name": "2. Legend I Am"
    },
    {
      "adjustmentFactor": 15.98,
      "status": "ACTIVE",
      "sortPriority": 3,
      "id": 19143530,
      "name": "3. Storm Harbour"
    },
    {
      "adjustmentFactor": 27.58,
      "status": "ACTIVE",
      "sortPriority": 4,
      "id": 2329545,
      "name": "4. Gap Year"
    },
    {
      "adjustmentFactor": 11.53,
      "status": "ACTIVE",
      "sortPriority": 5,
      "id": 48672282,
      "name": "6. Unlikelyoccurrence"
    },
    {
      "adjustmentFactor": 1.25,
      "status": "ACTIVE",
      "sortPriority": 6,
      "id": 6159479,
      "name": "7. Winston Blue"
    },
    {
      "adjustmentFactor": 9.84,
      "status": "ACTIVE",
      "sortPriority": 7,
      "id": 10591436,
      "name": "8. Bonnie And Clyde"
    },
    {
      "adjustmentFactor": 4.39,
      "status": "ACTIVE",
      "sortPriority": 8,
      "id": 16206031,
      "name": "9. Herecum Da Drums"
    },
    {
      "adjustmentFactor": 13.87,
      "status": "ACTIVE",
      "sortPriority": 9,
      "id": 25694777,
      "name": "11. Rip City"
    },
    {
      "adjustmentFactor": 2.65,
      "status": "ACTIVE",
      "sortPriority": 10,
      "id": 35672106,
      "name": "12. Who Said So"
    },
    {
      "adjustmentFactor": 2.93,
      "status": "ACTIVE",
      "sortPriority": 11,
      "id": 49808335,
      "name": "13. Daulat Machtigamor"
    },
    {
      "adjustmentFactor": 1.25,
      "status": "ACTIVE",
      "sortPriority": 12,
      "id": 39000334,
      "name": "15. Tallahassee Lassie"
    },
    {
      "adjustmentFactor": 9.84,
      "status": "ACTIVE",
      "sortPriority": 13,
      "id": 49808338,
      "name": "18. Federal Agent"
    },
    {
      "adjustmentFactor": 6.78,
      "status": "ACTIVE",
      "sortPriority": 14,
      "id": 49808340,
      "name": "20. Frozen Prince"
    },
    {
      "adjustmentFactor": 1.69,
      "status": "ACTIVE",
      "sortPriority": 15,
      "id": 42011335,
      "name": "22. Claudius"
    },
    {
      "adjustmentFactor": 11.53,
      "status": "ACTIVE",
      "sortPriority": 16,
      "id": 49808342,
      "name": "23. Birkin Black"
    },
    {
      "adjustmentFactor": 2.65,
      "status": "ACTIVE",
      "sortPriority": 17,
      "id": 49808343,
      "name": "24. Dacxi Kaboom"
    }
  ],
  "regulators": [
    "MR_INT"
  ],
  "venue": "Sunshine Coast",
  "countryCode": "AU",
  "discountAllowed": true,
  "timezone": "Australia/Queensland",
  "openDate": "2022-11-01T01:49:00.000Z",
  "version": 4881874440,
  "name": "To Be Placed",
  "eventName": "Sunshine Coast (AUS) 1st Nov"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 43


**Identifiers**: `ACTIVE`, `AUS`, `Agent`, `And`, `Australia`, `Birkin`, `Black`, `Blue`, `Bonnie`, `City`, `Claudius`, `Clyde`, `Coast`, `Dacxi`, `Daulat`, `Drums`, `Federal`, `Frozen`, `Gap`, `Harbour`, `Herecum`, `Kaboom`, `Lassie`, `Legend`, `MR_INT`, `Machtigamor`, `Nov`, `ODDS`, `OPEN`, `PLACE` *(+13 more)*

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
pytest tests/integration_tests/adapters/betfair/resources/responses/market_definition_open.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.246664Z*
