# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_ClosedPositionList": {
        "url": "/openapi/port/v1/closedpositions/",
        "params": {},
        "response": {
            "__count": 5,
            "Data": [
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": 80000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Buy",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": -260,
                  "ClosedProfitLossInBaseCurrency": -171.1138,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212702774",
                  "ClosingPrice": 1.75612,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": False,
                  "CostClosing": -7.02,
                  "CostClosingInBaseCurrency": -4.62,
                  "CostOpening": -7.04,
                  "CostOpeningInBaseCurrency": -4.63,
                  "ExecutionTimeClose": "2019-03-05T22:57:51.935866Z",
                  "ExecutionTimeOpen": "2019-03-05T22:39:43.738721Z",
                  "OpeningPositionId": "212702698",
                  "OpenPrice": 1.75937,
                  "Uic": 23
                },
                "ClosedPositionUniqueId": "212702698-212702774",
                "NetPositionId": "GBPCAD__FxSpot"
              },
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": -100000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Sell",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": 29,
                  "ClosedProfitLossInBaseCurrency": 25.6447,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212702772",
                  "ClosingPrice": 1.13025,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": False,
                  "CostClosing": -5.65,
                  "CostClosingInBaseCurrency": -5,
                  "CostOpening": -5.65,
                  "CostOpeningInBaseCurrency": -5,
                  "ExecutionTimeClose": "2019-03-05T22:57:51.776721Z",
                  "ExecutionTimeOpen": "2019-03-05T22:39:43.546536Z",
                  "OpeningPositionId": "212702696",
                  "OpenPrice": 1.13054,
                  "Uic": 21
                },
                "ClosedPositionUniqueId": "212702696-212702772",
                "NetPositionId": "EURUSD__FxSpot"
              },
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": 10000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Buy",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": -13.2,
                  "ClosedProfitLossInBaseCurrency": -11.67276,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212702680",
                  "ClosingPrice": 1.31731,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": True,
                  "CostClosing": -3,
                  "CostClosingInBaseCurrency": -2.65,
                  "CostOpening": -3,
                  "CostOpeningInBaseCurrency": -2.65,
                  "ExecutionTimeClose": "2019-03-05T22:23:38.888231Z",
                  "ExecutionTimeOpen": "2019-03-04T17:11:39.129241Z",
                  "OpeningPositionId": "212675868",
                  "OpenPrice": 1.31863,
                  "Uic": 31
                },
                "ClosedPositionUniqueId": "212675868-212702680",
                "NetPositionId": "GBPUSD__FxSpot"
              },
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Buy",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": 50,
                  "ClosedProfitLossInBaseCurrency": 32.9065,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212702664",
                  "ClosingPrice": 1.75878,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": True,
                  "CostClosing": -8.79,
                  "CostClosingInBaseCurrency": -5.78,
                  "CostOpening": -8.79,
                  "CostOpeningInBaseCurrency": -5.82,
                  "ExecutionTimeClose": "2019-03-05T22:22:51.922693Z",
                  "ExecutionTimeOpen": "2019-03-03T23:34:51.823660Z",
                  "OpeningPositionId": "212550210",
                  "OpenPrice": 1.75828,
                  "Uic": 23
                },
                "ClosedPositionUniqueId": "212550210-212702664",
                "NetPositionId": "GBPCAD__FxSpot"
              },
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": 400000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Buy",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": -1800,
                  "ClosedProfitLossInBaseCurrency": -1118.124,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212702660",
                  "ClosingPrice": 1.85952,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": True,
                  "CostClosing": -37.19,
                  "CostClosingInBaseCurrency": -23.1,
                  "CostOpening": -29.824,
                  "CostOpeningInBaseCurrency": -18.62,
                  "ExecutionTimeClose": "2019-03-05T22:22:07.523028Z",
                  "ExecutionTimeOpen": "2019-03-03T23:35:08.243690Z",
                  "OpeningPositionId": "212550212",
                  "OpenPrice": 1.86402,
                  "Uic": 22
                },
                "ClosedPositionUniqueId": "212550212-212702660",
                "NetPositionId": "GBPAUD__FxSpot"
              }
            ]
        }
    },
    "_v3_ClosedPositionById": {
        "url": "/openapi/port/v1/closedpositions/{ClosedPositionId}",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "ClosedPosition": {
              "AccountId": "9226397",
              "Amount": 80000,
              "AssetType": "FxSpot",
              "BuyOrSell": "Buy",
              "ClientId": "9226397",
              "ClosedProfitLoss": -260,
              "ClosedProfitLossInBaseCurrency": -171.0969,
              "ClosingMarketValue": 0,
              "ClosingMarketValueInBaseCurrency": 0,
              "ClosingMethod": "Fifo",
              "ClosingPositionId": "212702774",
              "ClosingPrice": 1.75612,
              "ConversionRateInstrumentToBaseSettledClosing": False,
              "ConversionRateInstrumentToBaseSettledOpening": False,
              "CostClosing": -7.02,
              "CostClosingInBaseCurrency": -4.62,
              "CostOpening": -7.04,
              "CostOpeningInBaseCurrency": -4.63,
              "ExecutionTimeClose": "2019-03-05T22:57:51.935866Z",
              "ExecutionTimeOpen": "2019-03-05T22:39:43.738721Z",
              "OpeningPositionId": "212702698",
              "OpenPrice": 1.75937,
              "Uic": 23
            },
            "ClosedPositionUniqueId": "212702698-212702774",
            "NetPositionId": "GBPCAD__FxSpot"
        }
    },
    "_v3_ClosedPositionDetails": {
        "url": "/openapi/port/v1/closedpositions/{ClosedPositionId}/details",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "ClosedPosition": {
              "AccountId": "9226397",
              "Amount": 80000,
              "AssetType": "FxSpot",
              "BuyOrSell": "Buy",
              "ClientId": "9226397",
              "ClosedProfitLoss": -260,
              "ClosedProfitLossInBaseCurrency": -171.1385,
              "ClosingMarketValue": 0,
              "ClosingMarketValueInBaseCurrency": 0,
              "ClosingMethod": "Fifo",
              "ClosingPositionId": "212702774",
              "ClosingPrice": 1.75612,
              "ConversionRateInstrumentToBaseSettledClosing": False,
              "ConversionRateInstrumentToBaseSettledOpening": False,
              "CostClosing": -7.02,
              "CostClosingInBaseCurrency": -4.62,
              "CostOpening": -7.04,
              "CostOpeningInBaseCurrency": -4.63,
              "ExecutionTimeClose": "2019-03-05T22:57:51.935866Z",
              "ExecutionTimeOpen": "2019-03-05T22:39:43.738721Z",
              "OpeningPositionId": "212702698",
              "OpenPrice": 1.75937,
              "Uic": 23
            },
            "ClosedPositionDetails": {
              "CostClosing": {
                "Commission": -7.02
              },
              "CostClosingInBaseCurrency": {
                "Commission": -4.62
              },
              "CostOpening": {
                "Commission": -7.04
              },
              "CostOpeningInBaseCurrency": {
                "Commission": -4.63
              },
              "CurrencyConversionRateInstrumentToBaseClosing": 0.658225,
              "CurrencyConversionRateInstrumentToBaseOpening": 0.658225,
              "ValueDateClose": "2019-03-08T00:00:00.000000Z",
              "ValueDateOpen": "2019-03-08T00:00:00.000000Z"
            },
            "ClosedPositionUniqueId": "212702698-212702774",
            "DisplayAndFormat": {
              "Currency": "CAD",
              "Decimals": 4,
              "Description": "British Pound/Canadian Dollar",
              "Format": "AllowDecimalPips",
              "Symbol": "GBPCAD"
            },
            "Exchange": {
              "Description": "Inter Bank",
              "ExchangeId": "SBFX",
              "IsOpen": True
            },
            "NetPositionId": "GBPCAD__FxSpot"
        }
    },
    "_v3_ClosedPositionsMe": {
        "url": "/openapi/port/v1/closedpositions/me",
        "params": {},
        "response": {
            "__count": 3,
            "Data": [
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": -40000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Sell",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": -582.8,
                  "ClosedProfitLossInBaseCurrency": -383.377496,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212725160",
                  "ClosingPrice": 1.77074,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": True,
                  "CostClosing": -4.03,
                  "CostClosingInBaseCurrency": -2.65,
                  "CostOpening": -3.51,
                  "CostOpeningInBaseCurrency": -2.32,
                  "ExecutionTimeClose": "2019-03-06T23:07:47.040598Z",
                  "ExecutionTimeOpen": "2019-03-06T10:24:50.635259Z",
                  "OpeningPositionId": "212710176",
                  "OpenPrice": 1.75617,
                  "Uic": 23
                },
                "ClosedPositionUniqueId": "212710176-212725160",
                "NetPositionId": "GBPCAD__FxSpot"
              },
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": -40000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Sell",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": -590.8,
                  "ClosedProfitLossInBaseCurrency": -388.640056,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212725128",
                  "ClosingPrice": 1.77094,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": True,
                  "CostClosing": -4.03,
                  "CostClosingInBaseCurrency": -2.65,
                  "CostOpening": -3.51,
                  "CostOpeningInBaseCurrency": -2.32,
                  "ExecutionTimeClose": "2019-03-06T23:02:56.295679Z",
                  "ExecutionTimeOpen": "2019-03-06T10:24:50.635259Z",
                  "OpeningPositionId": "212710176",
                  "OpenPrice": 1.75617,
                  "Uic": 23
                },
                "ClosedPositionUniqueId": "212710176-212725128",
                "NetPositionId": "GBPCAD__FxSpot"
              },
              {
                "ClosedPosition": {
                  "AccountId": "9226397",
                  "Amount": 40000,
                  "AssetType": "FxSpot",
                  "BuyOrSell": "Buy",
                  "ClientId": "9226397",
                  "ClosedProfitLoss": 6,
                  "ClosedProfitLossInBaseCurrency": 5.30466,
                  "ClosingMarketValue": 0,
                  "ClosingMarketValueInBaseCurrency": 0,
                  "ClosingMethod": "Fifo",
                  "ClosingPositionId": "212724952",
                  "ClosingPrice": 1.13076,
                  "ConversionRateInstrumentToBaseSettledClosing": False,
                  "ConversionRateInstrumentToBaseSettledOpening": True,
                  "CostClosing": -3,
                  "CostClosingInBaseCurrency": -2.65,
                  "CostOpening": -2.26,
                  "CostOpeningInBaseCurrency": -2,
                  "ExecutionTimeClose": "2019-03-06T22:55:59.228387Z",
                  "ExecutionTimeOpen": "2019-03-06T10:24:50.460091Z",
                  "OpeningPositionId": "212710174",
                  "OpenPrice": 1.13061,
                  "Uic": 21
                },
                "ClosedPositionUniqueId": "212710174-212724952",
                "NetPositionId": "EURUSD__FxSpot"
              }
            ]
        }
    },
    "_v3_ClosedPositionSubscription": {
        "url": "/openapi/port/v1/closedpositions/subscriptions",
        "params": {},
        "body": {
            "Arguments": {
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
            },
            "ContextId": "explorer_1551913039211",
            "ReferenceId": "D_975"
        },
        "response": {
            "ContextId": "explorer_1551913039211",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "D_975",
            "RefreshRate": 1000,
            "Snapshot": {
              "Data": [
                {
                  "ClosedPosition": {
                    "AccountId": "9226397",
                    "Amount": -40000,
                    "AssetType": "FxSpot",
                    "BuyOrSell": "Sell",
                    "ClientId": "9226397",
                    "ClosedProfitLoss": -582.8,
                    "ClosedProfitLossInBaseCurrency": -383.389152,
                    "ClosingMarketValue": 0,
                    "ClosingMarketValueInBaseCurrency": 0,
                    "ClosingMethod": "Fifo",
                    "ClosingPositionId": "212725160",
                    "ClosingPrice": 1.77074,
                    "ConversionRateInstrumentToBaseSettledClosing": False,
                    "ConversionRateInstrumentToBaseSettledOpening": True,
                    "CostClosing": -4.03,
                    "CostClosingInBaseCurrency": -2.65,
                    "CostOpening": -3.51,
                    "CostOpeningInBaseCurrency": -2.32,
                    "ExecutionTimeClose": "2019-03-06T23:07:47.040598Z",
                    "ExecutionTimeOpen": "2019-03-06T10:24:50.635259Z",
                    "OpeningPositionId": "212710176",
                    "OpenPrice": 1.75617,
                    "Uic": 23
                  },
                  "ClosedPositionUniqueId": "212710176-212725160",
                  "NetPositionId": "GBPCAD__FxSpot"
                },
                {
                  "ClosedPosition": {
                    "AccountId": "9226397",
                    "Amount": -40000,
                    "AssetType": "FxSpot",
                    "BuyOrSell": "Sell",
                    "ClientId": "9226397",
                    "ClosedProfitLoss": -590.8,
                    "ClosedProfitLossInBaseCurrency": -388.651872,
                    "ClosingMarketValue": 0,
                    "ClosingMarketValueInBaseCurrency": 0,
                    "ClosingMethod": "Fifo",
                    "ClosingPositionId": "212725128",
                    "ClosingPrice": 1.77094,
                    "ConversionRateInstrumentToBaseSettledClosing": False,
                    "ConversionRateInstrumentToBaseSettledOpening": True,
                    "CostClosing": -4.03,
                    "CostClosingInBaseCurrency": -2.65,
                    "CostOpening": -3.51,
                    "CostOpeningInBaseCurrency": -2.32,
                    "ExecutionTimeClose": "2019-03-06T23:02:56.295679Z",
                    "ExecutionTimeOpen": "2019-03-06T10:24:50.635259Z",
                    "OpeningPositionId": "212710176",
                    "OpenPrice": 1.75617,
                    "Uic": 23
                  },
                  "ClosedPositionUniqueId": "212710176-212725128",
                  "NetPositionId": "GBPCAD__FxSpot"
                },
                {
                  "ClosedPosition": {
                    "AccountId": "9226397",
                    "Amount": 40000,
                    "AssetType": "FxSpot",
                    "BuyOrSell": "Buy",
                    "ClientId": "9226397",
                    "ClosedProfitLoss": 6,
                    "ClosedProfitLossInBaseCurrency": 5.30445,
                    "ClosingMarketValue": 0,
                    "ClosingMarketValueInBaseCurrency": 0,
                    "ClosingMethod": "Fifo",
                    "ClosingPositionId": "212724952",
                    "ClosingPrice": 1.13076,
                    "ConversionRateInstrumentToBaseSettledClosing": False,
                    "ConversionRateInstrumentToBaseSettledOpening": True,
                    "CostClosing": -3,
                    "CostClosingInBaseCurrency": -2.65,
                    "CostOpening": -2.26,
                    "CostOpeningInBaseCurrency": -2,
                    "ExecutionTimeClose": "2019-03-06T22:55:59.228387Z",
                    "ExecutionTimeOpen": "2019-03-06T10:24:50.460091Z",
                    "OpeningPositionId": "212710174",
                    "OpenPrice": 1.13061,
                    "Uic": 21
                  },
                  "ClosedPositionUniqueId": "212710174-212724952",
                  "NetPositionId": "EURUSD__FxSpot"
                }
              ],
              "MaxRows": 100000
            },
            "State": "Active"
        }
    },
    "_v3_ClosedPositionSubscriptionUpdate": {
        "url": "/openapi/port/v1/closedpositions/subscriptions/{ContextId}/{ReferenceId}/",
        "body": {'NewPageSize': 25630},
        "response": ''
    },
    "_v3_ClosedPositionSubscriptionsRemove": {
        "url": "/openapi/port/v1/closedpositions/subscriptions/{ContextId}/",
        "route": {
            'ContextId': 29931122,
        },
        "params": {'Tag': 2345223},
        "response": ''
    },
    "_v3_ClosedPositionSubscriptionRemoveById": {
        "url": "/openapi/port/v1/closedpositions/subscriptions/{ContextId}/{ReferenceId}/",
        "route": {
            'ContextId': 29931122,
            'ReferenceId': '0f8fad5b-d9cb-469f-a165-70867728950e',
        },
        "response": ''
    }
}
