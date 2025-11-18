# Documentation: streaming_mcm_SUB_IMAGE.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_SUB_IMAGE.json`
- **Size**: 4,090 bytes
- **Lines**: 201
- **Language**: JSON

## Original Source

```json
{
  "op": "mcm",
  "id": 2,
  "initialClk": "ab34r43r",
  "clk": "AAAAAAAA",
  "conflateMs": 0,
  "heartbeatMs": 5000,
  "pt": 1471370159007,
  "ct": "SUB_IMAGE",
  "mc": [
    {
      "id": "1.180737206",
      "marketDefinition": {
        "bspMarket": true,
        "turnInPlayEnabled": true,
        "persistenceEnabled": true,
        "marketBaseRate": 5,
        "eventId": "30361178",
        "eventTypeId": "7",
        "numberOfWinners": 1,
        "bettingType": "ODDS",
        "marketType": "WIN",
        "marketTime": "2021-03-19T12:07:00+10:00",
        "suspendTime": "2021-03-19T12:07:00+10:00",
        "bspReconciled": false,
        "complete": true,
        "inPlay": false,
        "crossMatching": false,
        "runnersVoidable": false,
        "numberOfActiveRunners": 7,
        "betDelay": 0,
        "status": "OPEN",
        "runners": [
          {
            "adjustmentFactor": 44.323,
            "status": "ACTIVE",
            "sortPriority": 1,
            "id": "19248890"
          },
          {
            "adjustmentFactor": 41.972,
            "status": "ACTIVE",
            "sortPriority": 2,
            "id": "38848248"
          },
          {
            "adjustmentFactor": 6.006,
            "status": "ACTIVE",
            "sortPriority": 3,
            "id": "10921178"
          },
          {
            "adjustmentFactor": 3.635,
            "status": "ACTIVE",
            "sortPriority": 4,
            "id": "3601619"
          },
          {
            "adjustmentFactor": 3.129,
            "status": "ACTIVE",
            "sortPriority": 5,
            "id": "13388439"
          },
          {
            "adjustmentFactor": 0.468,
            "status": "ACTIVE",
            "sortPriority": 6,
            "id": "35510787"
          },
          {
            "adjustmentFactor": 0.468,
            "status": "ACTIVE",
            "sortPriority": 7,
            "id": "10147870"
          }
        ],
        "regulators": [
          "MR_INT"
        ],
        "venue": "Kempton",
        "countryCode": "GB",
        "discountAllowed": true,
        "timezone": "Europe/London",
        "openDate": "2021-03-19T12:07:00+10:00",
        "version": 1400311331
      },
      "rc": [
        {
          "atb": [
            [
              46,
              3
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "19248890"
        },
        {
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
          "ltp": 0,
          "tv": 0,
          "id": "38848248"
        },
        {
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              980,
              22.72
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "10921178"
        },
        {
          "atb": [
            [
              5.8,
              3.44
            ]
          ],
          "atl": [
            [
              980,
              22.72
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "3601619"
        },
        {
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
          "ltp": 0,
          "tv": 0,
          "id": "13388439"
        },
        {
          "atb": [
            [
              4.6,
              3.69
            ]
          ],
          "atl": [
            [
              130,
              22.72
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "35510787"
        },
        {
          "atb": [
            [
              42,
              3
            ]
          ],
          "ltp": 0,
          "tv": 0,
          "id": "10147870"
        }
      ],
      "img": true,
      "tv": 0
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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_mcm_SUB_IMAGE.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.480256Z*
