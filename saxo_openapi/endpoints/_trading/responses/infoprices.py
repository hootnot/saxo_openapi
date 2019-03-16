# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_InfoPrice": {
        "url": "openapi/trade/v1/infoprices",
        "params": {
            'Uic': 22,
            'AccountKey': '81ef1924-c25f-43fe-90ff-028e3fe249f2',
            'AssetType': '...',
            '<other-parms>': '...',
        },
        "response": {
            "AssetType": "FxSpot",
            "DisplayAndFormat": {
              "Currency": "AUD",
              "Decimals": 4,
              "Description": "British Pound/Australian Dollar",
              "Format": "AllowDecimalPips",
              "OrderDecimals": 4,
              "Symbol": "GBPAUD"
            },
            "HistoricalChanges": {
              "PercentChange1Month": 1.21,
              "PercentChange2Months": 2.95,
              "PercentChange3Months": 1.85,
              "PercentChange6Months": -1.83,
              "PercentChangeWeekly": 1.67
            },
            "InstrumentPriceDetails": {
              "IsMarketOpen": True,
              "ShortTradeDisabled": False,
              "ValueDate": "2017-05-19"
            },
            "LastUpdated": "0001-01-01T00:00:00Z",
            "PriceInfo": {
              "High": 1.09117,
              "Low": 1.08853,
              "NetChange": 0.00048,
              "PercentChange": 0.04
            },
            "PriceInfoDetails": {
              "AskSize": 1000000.0,
              "BidSize": 1000000.0,
              "LastClose": 1.08932,
              "LastTraded": 0.0,
              "LastTradedSize": 0.0,
              "Open": 0.0,
              "Volume": 0.0
            },
            "Quote": {
              "Amount": 100000,
              "Ask": 1.74948,
              "Bid": 1.74858,
              "DelayedByMinutes": 15,
              "ErrorCode": "None",
              "Mid": 1.74903,
              "PriceTypeAsk": "Indicative",
              "PriceTypeBid": "Indicative"
            },
            "Uic": 22
        }
    },
    "_v3_InfoPrices": {
        "url": "openapi/trade/v1/infoprices/list",
        "params": {
            'Uics': '22,23',
            'AccountKey': '1a463418-88d4-4555-92e3-e6004d675245',
            '<other-parms>': '...',
        },
        "response": {
            "Data": [
              {
                "AssetType": "FxSpot",
                "DisplayAndFormat": {
                  "Currency": "AUD",
                  "Decimals": 4,
                  "Description": "British Pound/Australian Dollar",
                  "Format": "AllowDecimalPips",
                  "OrderDecimals": 4,
                  "Symbol": "GBPAUD"
                },
                "HistoricalChanges": {
                  "PercentChange1Month": 1.21,
                  "PercentChange2Months": 2.95,
                  "PercentChange3Months": 1.85,
                  "PercentChange6Months": -1.83,
                  "PercentChangeWeekly": 1.67
                },
                "InstrumentPriceDetails": {
                  "IsMarketOpen": True,
                  "ShortTradeDisabled": False,
                  "ValueDate": "2017-05-19"
                },
                "LastUpdated": "0001-01-01T00:00:00Z",
                "PriceInfo": {
                  "High": 1.09117,
                  "Low": 1.08853,
                  "NetChange": 0.00048,
                  "PercentChange": 0.04
                },
                "PriceInfoDetails": {
                  "AskSize": 1000000.0,
                  "BidSize": 1000000.0,
                  "LastClose": 1.08932,
                  "LastTraded": 0.0,
                  "LastTradedSize": 0.0,
                  "Open": 0.0,
                  "Volume": 0.0
                },
                "Quote": {
                  "Amount": 100000,
                  "Ask": 1.74948,
                  "Bid": 1.74858,
                  "DelayedByMinutes": 15,
                  "ErrorCode": "None",
                  "Mid": 1.74903,
                  "PriceTypeAsk": "Indicative",
                  "PriceTypeBid": "Indicative"
                },
                "Uic": 22
              },
              {
                "AssetType": "FxSpot",
                "DisplayAndFormat": {
                  "Currency": "CAD",
                  "Decimals": 4,
                  "Description": "British Pound/Canadian Dollar",
                  "Format": "AllowDecimalPips",
                  "OrderDecimals": 4,
                  "Symbol": "GBPCAD"
                },
                "InstrumentPriceDetails": {
                  "IsMarketOpen": True,
                  "ShortTradeDisabled": False,
                  "ValueDate": "2017-05-19"
                },
                "LastUpdated": "0001-01-01T00:00:00Z",
                "Quote": {
                  "Amount": 100000,
                  "Ask": 1.76278,
                  "Bid": 1.76198,
                  "DelayedByMinutes": 15,
                  "ErrorCode": "None",
                  "Mid": 1.76238,
                  "PriceTypeAsk": "Indicative",
                  "PriceTypeBid": "Indicative"
                },
                "Uic": 23
              }
            ]
        }
    },
    "_v3_CreateInfoPriceSubscription": {
        "url": "openapi/trade/v1/infoprices/subscriptions",
        "body": {
            "Arguments": {
              "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
              "AssetType": "FxSpot",
              "FieldGroups": [
                "DisplayAndFormat",
                "HistoricalChanges",
                "InstrumentPriceDetails",
                "PriceInfo",
                "PriceInfoDetails",
                "Quote"
              ],
              "Uics": "22,23"
            },
            "ContextId": "20190307094456688",
            "ReferenceId": "IP17820",
            "RefreshRate": 1000
        },
        "response": {
            "ContextId": "20190307094456688",
            "Format": "application/json",
            "InactivityTimeout": 60,
            "ReferenceId": "IP17820",
            "RefreshRate": 1000,
            "Snapshot": {
              "Data": [
                {
                  "AssetType": "FxSpot",
                  "DisplayAndFormat": {
                    "Currency": "AUD",
                    "Decimals": 4,
                    "Description": "British Pound/Australian Dollar",
                    "Format": "AllowDecimalPips",
                    "OrderDecimals": 4,
                    "Symbol": "GBPAUD"
                  },
                  "HistoricalChanges": {
                    "PercentChange1Month": 1.21,
                    "PercentChange2Months": 2.95,
                    "PercentChange3Months": 1.85,
                    "PercentChange6Months": -1.83,
                    "PercentChangeWeekly": 1.67
                  },
                  "InstrumentPriceDetails": {
                    "IsMarketOpen": True,
                    "ShortTradeDisabled": False,
                    "ValueDate": "2017-05-19"
                  },
                  "LastUpdated": "0001-01-01T00:00:00Z",
                  "PriceInfo": {
                    "High": 1.09117,
                    "Low": 1.08853,
                    "NetChange": 0.00048,
                    "PercentChange": 0.04
                  },
                  "PriceInfoDetails": {
                    "AskSize": 1000000.0,
                    "BidSize": 1000000.0,
                    "LastClose": 1.08932,
                    "LastTraded": 0.0,
                    "LastTradedSize": 0.0,
                    "Open": 0.0,
                    "Volume": 0.0
                  },
                  "Quote": {
                    "Amount": 100000,
                    "Ask": 1.74948,
                    "Bid": 1.74858,
                    "DelayedByMinutes": 15,
                    "ErrorCode": "None",
                    "Mid": 1.74903,
                    "PriceTypeAsk": "Indicative",
                    "PriceTypeBid": "Indicative"
                  },
                  "Uic": 22
                },
                {
                  "AssetType": "FxSpot",
                  "DisplayAndFormat": {
                    "Currency": "CAD",
                    "Decimals": 4,
                    "Description": "British Pound/Canadian Dollar",
                    "Format": "AllowDecimalPips",
                    "OrderDecimals": 4,
                    "Symbol": "GBPCAD"
                  },
                  "InstrumentPriceDetails": {
                    "IsMarketOpen": True,
                    "ShortTradeDisabled": False,
                    "ValueDate": "2017-05-19"
                  },
                  "LastUpdated": "0001-01-01T00:00:00Z",
                  "Quote": {
                    "Amount": 100000,
                    "Ask": 1.76278,
                    "Bid": 1.76198,
                    "DelayedByMinutes": 15,
                    "ErrorCode": "None",
                    "Mid": 1.76238,
                    "PriceTypeAsk": "Indicative",
                    "PriceTypeBid": "Indicative"
                  },
                  "Uic": 23
                }
              ]
            },
            "State": "Active"
        }
    },
    "_v3_RemoveInfoPriceSubscriptionsByTag": {
        "url": "openapi/trade/v1/infoprices/subscriptions",
        "route": {
            'ContextId': 'ctxt_20190316',
        },
        "params": {
            "Tag": "IP"
        },
        "response": ''
    },
    "_v3_RemoveInfoPriceSubscriptionById": {
        "url": "openapi/trade/v1/infoprices/subscriptions",
        "route": {
            'ContextId': 'ctxt_20190316',
            'ReferenceId': 'IP_EURUSD'
        },
        "response": ''
    },
}
