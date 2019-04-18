# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_OptionsChainSubscriptionCreate": {
        "url": "openapi/trade/v1/optionschain/subscriptions"
               "{ContextId}/{ReferenceId}",
        "body": {
           "Arguments": {
             "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
             "AssetType": "StockIndexOption",
             "Expiries": [
               {
                 "Index": 1,
                 "StrikeStartIndex": 0
               }
             ],
             "Identifier": 18,
             "MaxStrikesPerExpiry": 3
           },
           "ContextId": "20190411051355700",
           "ReferenceId": "C0165000",
           "RefreshRate": 1000
        },
        "response": {
              "ContextId": "20190411051355700",
              "InactivityTimeout": 60,
              "ReferenceId": "C0165000",
              "RefreshRate": 1000,
              "Snapshot": {
                "AssetType": "StockIndexOption",
                "Expiries": [
                  {
                    "DisplayDate": "0001-01-01",
                    "DisplayDaysToExpiry": 30,
                    "Expiry": "2017-05-31T11:10:00Z",
                    "Index": 0,
                    "LastTradeDate": "0201-05-31T21:00:00Z",
                    "MidStrikePrice": 0.0,
                    "StrikeCount": 50,
                    "Strikes": [
                      {
                        "Index": 0,
                        "Strike": 97.25
                      },
                      {
                        "Index": 1,
                        "Strike": 97.375
                      },
                      {
                        "Index": 2,
                        "Strike": 97.5
                      },
                      {
                        "Index": 3,
                        "Strike": 97.625
                      },
                      {
                        "Index": 4,
                        "Strike": 97.75
                      },
                      {
                        "Index": 5,
                        "Strike": 97.8125
                      },
                      {
                        "Index": 6,
                        "Strike": 97.875
                      },
                      {
                        "Index": 7,
                        "Strike": 97.9375
                      },
                      {
                        "Index": 8,
                        "Strike": 98.0
                      },
                      {
                        "Index": 9,
                        "Strike": 98.0625
                      },
                      {
                        "Index": 10,
                        "Strike": 98.125
                      },
                      {
                        "Index": 11,
                        "Strike": 98.1875
                      },
                      {
                        "Index": 12,
                        "Strike": 98.25
                      },
                      {
                        "Index": 13,
                        "Strike": 98.3125
                      },
                      {
                        "Index": 14,
                        "Strike": 98.375
                      },
                      {
                        "Index": 15,
                        "Strike": 98.4375
                      },
                      {
                        "Index": 16,
                        "Strike": 98.5
                      },
                      {
                        "Index": 17,
                        "Strike": 98.5625
                      },
                      {
                        "Index": 18,
                        "Strike": 98.625
                      },
                      {
                        "Index": 19,
                        "Strike": 98.6875
                      },
                      {
                        "Index": 20,
                        "Strike": 98.75
                      },
                      {
                        "Index": 21,
                        "Strike": 98.8125
                      },
                      {
                        "Index": 22,
                        "Strike": 98.875
                      },
                      {
                        "Index": 23,
                        "Strike": 98.9375
                      },
                      {
                        "Call": {
                          "High": 0.0,
                          "LastClose": 0.095,
                          "LastTraded": 0.0,
                          "Low": 0.0,
                          "NetChange": -0.095,
                          "Open": 0.0,
                          "OpenInterest": 0.0,
                          "PriceTypeAsk": "NoMarket",
                          "PriceTypeBid": "NoMarket",
                          "Uic": 2485090,
                          "Volume": 0.0
                        },
                        "Index": 24,
                        "Put": {
                          "High": 0.0,
                          "LastClose": 0.0,
                          "LastTraded": 0.0,
                          "Low": 0.0,
                          "NetChange": 0.0,
                          "Open": 0.0,
                          "OpenInterest": 0.0,
                          "PriceTypeAsk": "NoMarket",
                          "PriceTypeBid": "NoMarket",
                          "Uic": 2485130,
                          "Volume": 0.0
                        },
                        "Strike": 99.0
                      },
                      {
                        "Call": {
                          "High": 0.0,
                          "LastClose": 0.035,
                          "LastTraded": 0.0,
                          "Low": 0.0,
                          "NetChange": -0.035,
                          "Open": 0.0,
                          "OpenInterest": 0.0,
                          "PriceTypeAsk": "NoMarket",
                          "PriceTypeBid": "NoMarket",
                          "Uic": 2485091,
                          "Volume": 0.0
                        },
                        "Index": 25,
                        "Put": {
                          "High": 0.0,
                          "LastClose": 0.0025,
                          "LastTraded": 0.0,
                          "Low": 0.0,
                          "NetChange": -0.0025,
                          "Open": 0.0,
                          "OpenInterest": 250.0,
                          "PriceTypeAsk": "NoMarket",
                          "PriceTypeBid": "NoMarket",
                          "Uic": 2485131,
                          "Volume": 0.0
                        },
                        "Strike": 99.0625
                      },
                      {
                        "Call": {
                          "High": 0.0,
                          "LastClose": 0.0025,
                          "LastTraded": 0.0,
                          "Low": 0.0,
                          "NetChange": -0.0025,
                          "Open": 0.0,
                          "OpenInterest": 0.0,
                          "PriceTypeAsk": "NoMarket",
                          "PriceTypeBid": "NoMarket",
                          "Uic": 2485092,
                          "Volume": 0.0
                        },
                        "Index": 26,
                        "Put": {
                          "High": 0.0,
                          "LastClose": 0.0325,
                          "LastTraded": 0.0,
                          "Low": 0.0,
                          "NetChange": -0.0325,
                          "Open": 0.0,
                          "OpenInterest": 250.0,
                          "PriceTypeAsk": "NoMarket",
                          "PriceTypeBid": "NoMarket",
                          "Uic": 2485132,
                          "Volume": 0.0
                        },
                        "Strike": 99.125
                      },
                      {
                        "Index": 27,
                        "Strike": 99.1875
                      },
                      {
                        "Index": 28,
                        "Strike": 99.25
                      },
                      {
                        "Index": 29,
                        "Strike": 99.3125
                      },
                      {
                        "Index": 30,
                        "Strike": 99.375
                      },
                      {
                        "Index": 31,
                        "Strike": 99.4375
                      },
                      {
                        "Index": 32,
                        "Strike": 99.5
                      },
                      {
                        "Index": 33,
                        "Strike": 99.5625
                      },
                      {
                        "Index": 34,
                        "Strike": 99.625
                      },
                      {
                        "Index": 35,
                        "Strike": 99.6875
                      },
                      {
                        "Index": 36,
                        "Strike": 99.75
                      },
                      {
                        "Index": 37,
                        "Strike": 99.8125
                      },
                      {
                        "Index": 38,
                        "Strike": 99.875
                      },
                      {
                        "Index": 39,
                        "Strike": 99.9375
                      },
                      {
                        "Index": 40,
                        "Strike": 100.0
                      },
                      {
                        "Index": 41,
                        "Strike": 100.0625
                      },
                      {
                        "Index": 42,
                        "Strike": 100.125
                      },
                      {
                        "Index": 43,
                        "Strike": 100.1875
                      },
                      {
                        "Index": 44,
                        "Strike": 100.25
                      },
                      {
                        "Index": 45,
                        "Strike": 100.375
                      },
                      {
                        "Index": 46,
                        "Strike": 100.5
                      },
                      {
                        "Index": 47,
                        "Strike": 100.625
                      },
                      {
                        "Index": 48,
                        "Strike": 100.75
                      },
                      {
                        "Index": 49,
                        "Strike": 100.875
                      }
                    ],
                    "StrikeWindowStartIndex": 24,
                    "UnderlyingUic": 2456777
                  }
                ],
                "ExpiryCount": 0,
                "LastUpdated": "0001-01-01T00:00:00Z"
              },
              "State": "Active"
        }
    },
    "_v3_OptionsChainSubscriptionModify": {
        "url": "openapi/trade/v1/optionschain/subscriptions"
               "{ContextId}/{ReferenceId}",
        "route": {
            "ContextId": "8a91b266-1b38-4560-b6bb-d6c343f4736e",
            "ReferenceId": "e7b461b1-56f6-4905-baf9-329f5465d7a9"
        },
        "body": {
            "Expiries": [
              {
                "Index": 129,
                "StrikeStartIndex": 232
              }
            ],
            "MaxStrikesPerExpiry": 157
        },
        "response": ""
    },
    "_v3_OptionsChainSubscriptionRemove": {
        "url": "openapi/trade/v1/optionschain/subscriptions"
               "{ContextId}/{ReferenceId}",
        "route": {
            "ContextId": "29931122",
            "ReferenceId": "0f8fad5b-d9cb-469f-a165-70867728950e"
        },
        "response": ""
    },
    "_v3_OptionsChainSubscriptionResetATM": {
        "url": "openapi/trade/v1/optionschain/subscriptions/"
               "{ContextId}/{ReferenceId}/ResetATM",
        "route": {
            "ContextId": "29931122",
            "ReferenceId": "0f8fad5b-d9cb-469f-a165-70867728950e"
        },
        "response": ""
    },
}
