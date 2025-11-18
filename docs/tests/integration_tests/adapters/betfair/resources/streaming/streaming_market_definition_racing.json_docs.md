# Documentation: streaming_market_definition_racing.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition_racing.json`
- **Size**: 6,999 bytes
- **Lines**: 315
- **Language**: JSON

## Original Source

```json
{
  "op": "mcm",
  "id": 1,
  "initialClk": "mBzWkfrZC6Yci8vz5QudHPKO1d0L",
  "clk": "AAAAAAAA",
  "conflateMs": 0,
  "heartbeatMs": 5000,
  "pt": 1617253902641,
  "ct": "SUB_IMAGE",
  "mc": [
    {
      "id": "1.180737206",
      "rc": [
        {
          "id": 19248890,
          "atb": [
            [
              46.0,
              3.0
            ]
          ],
          "atl": null,
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 38848248,
          "atb": [
            [
              2.54,
              7.95
            ]
          ],
          "atl": [
            [
              2.72,
              8.8
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 10921178,
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              980.0,
              22.72
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 3601619,
          "atb": [
            [
              5.8,
              3.44
            ]
          ],
          "atl": [
            [
              980.0,
              22.72
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 13388439,
          "atb": [
            [
              1.8,
              21.32
            ]
          ],
          "atl": [
            [
              2.18,
              48.28
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 35510787,
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              130.0,
              22.72
            ]
          ],
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        },
        {
          "id": 10147870,
          "atb": [
            [
              42.0,
              3.0
            ]
          ],
          "atl": null,
          "batb": null,
          "batl": null,
          "bdatb": null,
          "bdatl": null,
          "spb": null,
          "spl": null,
          "spn": null,
          "spf": null,
          "trd": null,
          "ltp": 0.0,
          "tv": 0.0,
          "hc": null
        }
      ],
      "con": null,
      "img": true,
      "marketDefinition": {
        "betDelay": 0,
        "bettingType": "ODDS",
        "bspMarket": true,
        "bspReconciled": false,
        "competitionId": null,
        "competitionName": "",
        "complete": true,
        "countryCode": "GB",
        "crossMatching": false,
        "discountAllowed": true,
        "eachWayDivisor": null,
        "eventId": "30361178",
        "eventName": "",
        "eventTypeId": 7,
        "inPlay": false,
        "keyLineDefinition": null,
        "lineInterval": null,
        "lineMaxUnit": null,
        "lineMinUnit": null,
        "marketBaseRate": 5.0,
        "marketId": "",
        "marketName": "",
        "marketTime": "2021-03-19T12:07:00+10:00",
        "marketType": "WIN",
        "name": null,
        "numberOfActiveRunners": 7,
        "numberOfWinners": 1,
        "openDate": "2021-03-19T12:07:00+10:00",
        "persistenceEnabled": true,
        "priceLadderDefinition": null,
        "raceType": null,
        "regulators": [
          "MR_INT"
        ],
        "runners": [
          {
            "sortPriority": 1,
            "id": 19248890,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 44.323,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 2,
            "id": 38848248,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 41.972,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 3,
            "id": 10921178,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 6.006,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 4,
            "id": 3601619,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 3.635,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 5,
            "id": 13388439,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 3.129,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 6,
            "id": 35510787,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 0.468,
            "bsp": null,
            "removalDate": null
          },
          {
            "sortPriority": 7,
            "id": 10147870,
            "name": null,
            "hc": null,
            "status": "ACTIVE",
            "adjustmentFactor": 0.468,
            "bsp": null,
            "removalDate": null
          }
        ],
        "runnersVoidable": false,
        "settledTime": null,
        "status": "OPEN",
        "suspendTime": "2021-03-19T12:07:00+10:00",
        "timezone": "Europe/London",
        "turnInPlayEnabled": true,
        "venue": "Kempton",
        "version": 1400311331
      },
      "tv": 0.0
    }
  ]
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Identifiers**: `AAAAAAAA`, `ACTIVE`, `Europe`, `Kempton`, `London`, `MR_INT`, `ODDS`, `OPEN`, `SUB_IMAGE`, `WIN`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_market_definition_racing.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.460360Z*
