# Documentation: market_definition_closed.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/market_definition_closed.json`
- **Size**: 3,854 bytes
- **Lines**: 171
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
  "bspReconciled": true,
  "complete": true,
  "inPlay": false,
  "crossMatching": false,
  "runnersVoidable": false,
  "numberOfActiveRunners": 0,
  "betDelay": 0,
  "status": "CLOSED",
  "settledTime": "2022-11-01T02:02:23.000Z",
  "runners": [
    {
      "adjustmentFactor": 27.58,
      "status": "REMOVED",
      "sortPriority": 1,
      "removalDate": "2022-10-31T07:39:36.000Z",
      "id": 2329545,
      "name": "4. Gap Year"
    },
    {
      "adjustmentFactor": 8.37,
      "status": "REMOVED",
      "sortPriority": 2,
      "removalDate": "2022-10-31T21:18:59.000Z",
      "id": 49808340,
      "name": "20. Frozen Prince"
    },
    {
      "adjustmentFactor": 2.41,
      "status": "REMOVED",
      "sortPriority": 3,
      "removalDate": "2022-10-31T22:52:32.000Z",
      "id": 42011335,
      "name": "22. Claudius"
    },
    {
      "adjustmentFactor": 11.78,
      "status": "WINNER",
      "sortPriority": 4,
      "bsp": 4.2,
      "id": 49808334,
      "name": "1. Realaide"
    },
    {
      "adjustmentFactor": 1.58,
      "status": "LOSER",
      "sortPriority": 5,
      "bsp": 16.17,
      "id": 45368013,
      "name": "2. Legend I Am"
    },
    {
      "adjustmentFactor": 14.46,
      "status": "LOSER",
      "sortPriority": 6,
      "bsp": 5.27,
      "id": 19143530,
      "name": "3. Storm Harbour"
    },
    {
      "adjustmentFactor": 12.65,
      "status": "LOSER",
      "sortPriority": 7,
      "bsp": 3.45,
      "id": 48672282,
      "name": "6. Unlikelyoccurrence"
    },
    {
      "adjustmentFactor": 1.27,
      "status": "LOSER",
      "sortPriority": 8,
      "bsp": 16.0,
      "id": 6159479,
      "name": "7. Winston Blue"
    },
    {
      "adjustmentFactor": 11.64,
      "status": "LOSER",
      "sortPriority": 9,
      "bsp": 4.5,
      "id": 10591436,
      "name": "8. Bonnie And Clyde"
    },
    {
      "adjustmentFactor": 6.06,
      "status": "LOSER",
      "sortPriority": 10,
      "bsp": 10.1,
      "id": 16206031,
      "name": "9. Herecum Da Drums"
    },
    {
      "adjustmentFactor": 12.24,
      "status": "LOSER",
      "sortPriority": 11,
      "bsp": 3.98,
      "id": 25694777,
      "name": "11. Rip City"
    },
    {
      "adjustmentFactor": 3.88,
      "status": "LOSER",
      "sortPriority": 12,
      "bsp": 14.37,
      "id": 35672106,
      "name": "12. Who Said So"
    },
    {
      "adjustmentFactor": 12.65,
      "status": "WINNER",
      "sortPriority": 13,
      "bsp": 3.58,
      "id": 49808335,
      "name": "13. Daulat Machtigamor"
    },
    {
      "adjustmentFactor": 3.61,
      "status": "LOSER",
      "sortPriority": 14,
      "bsp": 9.13,
      "id": 39000334,
      "name": "15. Tallahassee Lassie"
    },
    {
      "adjustmentFactor": 19.61,
      "status": "LOSER",
      "sortPriority": 15,
      "bsp": 1.76,
      "id": 49808338,
      "name": "18. Federal Agent"
    },
    {
      "adjustmentFactor": 21.79,
      "status": "WINNER",
      "sortPriority": 16,
      "bsp": 1.86,
      "id": 49808342,
      "name": "23. Birkin Black"
    },
    {
      "adjustmentFactor": 2.87,
      "status": "LOSER",
      "sortPriority": 17,
      "bsp": 15.04,
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
  "version": 4883105963,
  "name": "To Be Placed",
  "eventName": "Sunshine Coast (AUS) 1st Nov"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 45


**Identifiers**: `AUS`, `Agent`, `And`, `Australia`, `Birkin`, `Black`, `Blue`, `Bonnie`, `CLOSED`, `City`, `Claudius`, `Clyde`, `Coast`, `Dacxi`, `Daulat`, `Drums`, `Federal`, `Frozen`, `Gap`, `Harbour`, `Herecum`, `Kaboom`, `LOSER`, `Lassie`, `Legend`, `MR_INT`, `Machtigamor`, `Nov`, `ODDS`, `PLACE` *(+15 more)*

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
pytest tests/integration_tests/adapters/betfair/resources/responses/market_definition_closed.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.244537Z*
