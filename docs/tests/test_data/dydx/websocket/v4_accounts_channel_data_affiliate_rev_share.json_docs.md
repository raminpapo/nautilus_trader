# Documentation: v4_accounts_channel_data_affiliate_rev_share.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data_affiliate_rev_share.json`
- **Size**: 2,549 bytes
- **Lines**: 78
- **Language**: JSON

## Original Source

```json
{
    "type": "channel_data",
    "connection_id": "72a02287-d522-4485-961d-74d420c52ca3",
    "message_id": 5,
    "id": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5/0",
    "channel": "v4_subaccounts",
    "version": "3.0.0",
    "contents": {
      "fills": [
        {
          "id": "c01a0746-47fe-5773-b0e9-e9e3d3592e78",
          "fee": "0.001219",
          "side": "SELL",
          "size": "0.001",
          "type": "LIMIT",
          "price": "2437",
          "eventId": "01757f260000000200000005",
          "orderId": "af5ca4ec-98ea-54ff-a43c-3555fbc031c2",
          "createdAt": "2024-11-03T16:09:38.395Z",
          "liquidity": "TAKER",
          "clobPairId": "1",
          "quoteAmount": "2.437",
          "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
          "clientMetadata": "1",
          "createdAtHeight": "24477478",
          "transactionHash": "446C1C91B86CE3544500A2395F8BE61923F742A759135B8B7F917BA3879D6E19",
          "affiliateRevShare": "0",
          "ticker": "ETH-USD"
        }
      ],
      "perpetualPositions": [
        {
          "address": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5",
          "subaccountNumber": 0,
          "positionId": "0a7ba1d8-dde9-5390-994f-dd5590ef91d0",
          "market": "ETH-USD",
          "side": "LONG",
          "status": "OPEN",
          "size": "0.013",
          "maxSize": "0.014",
          "netFunding": "0",
          "entryPrice": "1885.328125",
          "exitPrice": "2433.73333333333333333333",
          "sumOpen": "0.02",
          "sumClose": "0.003",
          "realizedPnl": "1.64521562499999999999999",
          "unrealizedPnl": "7.3268871"
        }
      ],
      "blockHeight": "24477478",
      "orders": [
        {
          "id": "af5ca4ec-98ea-54ff-a43c-3555fbc031c2",
          "side": "SELL",
          "size": "0.001",
          "type": "LIMIT",
          "price": "0.1",
          "status": "FILLED",
          "clientId": "1943906971",
          "updatedAt": "2024-11-03T16:09:38.395Z",
          "clobPairId": "1",
          "orderFlags": "0",
          "reduceOnly": true,
          "timeInForce": "IOC",
          "totalFilled": "0.001",
          "goodTilBlock": "24477478",
          "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
          "triggerPrice": null,
          "clientMetadata": "1",
          "createdAtHeight": "24477478",
          "updatedAtHeight": "24477478",
          "goodTilBlockTime": null,
          "postOnly": false,
          "ticker": "ETH-USD"
        }
      ]
    }
  }
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 9


**Identifiers**: `ETH`, `FILLED`, `IOC`, `LIMIT`, `LONG`, `OPEN`, `SELL`, `TAKER`, `USD`

## Related Files

This file is located in `tests/test_data/dydx/websocket/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data_affiliate_rev_share.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.450545Z*
