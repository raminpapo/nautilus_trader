# Documentation: streaming_ocm_FULL_IMAGE_STRATEGY.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_FULL_IMAGE_STRATEGY.json`
- **Size**: 2,591 bytes
- **Lines**: 142
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 2,
  "initialClk": "H4alrNUFIZ+RvMkFINaWv80FHvi+lNMFHuak/MkF",
  "clk": "AAAAAAAAAAAAAA==",
  "conflateMs": 0,
  "heartbeatMs": 5000,
  "pt": 1622694738367,
  "ct": "SUB_IMAGE",
  "oc": [
    {
      "fullImage": true,
      "id": "1.184028198",
      "orc": [
        {
          "fullImage": true,
          "id": 6023845,
          "mb": [
            [
              1.44,
              10
            ],
            [
              1.26,
              10
            ],
            [
              1.37,
              10
            ],
            [
              1.55,
              70
            ],
            [
              1.54,
              2.23
            ]
          ],
          "ml": [
            [
              1.33,
              10
            ],
            [
              1.37,
              10
            ],
            [
              1.38,
              10
            ],
            [
              1.43,
              10.15
            ],
            [
              1.45,
              10
            ],
            [
              1.44,
              10
            ],
            [
              1.49,
              10
            ],
            [
              1.47,
              10
            ]
          ],
          "smc": {
            "": {
              "mb": [
                [
                  1.55,
                  70
                ]
              ]
            },
            "Strategy-1": {
              "mb": [
                [
                  1.44,
                  10
                ],
                [
                  1.26,
                  10
                ],
                [
                  1.37,
                  10
                ],
                [
                  1.54,
                  2.23
                ]
              ],
              "ml": [
                [
                  1.33,
                  10
                ],
                [
                  1.37,
                  10
                ],
                [
                  1.38,
                  10
                ],
                [
                  1.43,
                  10.15
                ],
                [
                  1.45,
                  10
                ],
                [
                  1.44,
                  10
                ],
                [
                  1.49,
                  10
                ],
                [
                  1.47,
                  10
                ]
              ]
            }
          }
        }
      ]
    }
  ]
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `AAAAAAAAAAAAAA`, `H4alrNUFIZ`, `MkF`, `RvMkFINaWv80FHvi`, `SUB_IMAGE`, `Strategy`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_FULL_IMAGE_STRATEGY.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.531826Z*
