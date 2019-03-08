# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_GetOpenOrder": {
        "url": "/openapi/port/v1/orders/{ClientKey}/{OrderId}",
        "params": {},
        "response": {
            "__count": 1,
            "Data": [
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 100000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "925ab7aa-998b-4f4b-af26-7c1b3f4eee27",
                "CurrentPrice": 7.46175,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.46175,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": True,
                "MarketPrice": 7.46175,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76332324",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-07T14:54:17.423333Z",
                "Price": 7,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 16
              }
            ]
        }
    },
    "_v3_GetOpenOrdersMe": {
        "url": "/openapi/port/v1/orders/me",
        "params": {},
        "response": {
            "__count": 3,
            "Data": [
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 100000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "925ab7aa-998b-4f4b-af26-7c1b3f4eee27",
                "CurrentPrice": 7.46175,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.46175,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": True,
                "MarketPrice": 7.46175,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76332324",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-07T14:54:17.423333Z",
                "Price": 7,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 16
              },
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 100000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "e684a2e2-f9f9-4b10-91ad-a50e2f8b80ae",
                "CurrentPrice": 7.46175,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.46175,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": True,
                "MarketPrice": 7.46175,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76328908",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-07T12:04:13.493333Z",
                "Price": 7,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 16
              },
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 10000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "ec6ca0f4-8380-4068-a32d-538b7b06208e",
                "CurrentPrice": 1.30195,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.20195,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": True,
                "MarketPrice": 1.30195,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76289260",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-04T17:55:59.503333Z",
                "Price": 1.1,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 31
              }
            ]
        }
    },
    "_v3_OrderDetails": {
        "url": "/openapi/port/v1/orders/{OrderId}/details",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "AccountId": "9226397",
            "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Amount": 100000,
            "AssetType": "FxSpot",
            "BuySell": "Buy",
            "CalculationReliability": "Ok",
            "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "CorrelationKey": "925ab7aa-998b-4f4b-af26-7c1b3f4eee27",
            "CurrentPrice": 7.46175,
            "CurrentPriceDelayMinutes": 0,
            "CurrentPriceType": "Ask",
            "DisplayAndFormat": {
              "Currency": "DKK",
              "Decimals": 4,
              "Description": "Euro/Danish Krone",
              "Format": "AllowDecimalPips",
              "Symbol": "EURDKK"
            },
            "DistanceToMarket": 0.46175,
            "Duration": {
              "DurationType": "GoodTillCancel"
            },
            "Exchange": {
              "Description": "Inter Bank",
              "ExchangeId": "SBFX",
              "IsOpen": False
            },
            "IsMarketOpen": False,
            "MarketPrice": 7.46175,
            "OpenOrderType": "Limit",
            "OrderAmountType": "Quantity",
            "OrderId": "76332324",
            "OrderRelation": "StandAlone",
            "OrderTime": "2019-03-07T14:54:17.423333Z",
            "Price": 7,
            "RelatedOpenOrders": [],
            "Status": "Working",
            "Uic": 16
        }
    },
    "_v3_GetAllOpenOrders": {
        "url": "/openapi/port/v1/orders",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "__count": 3,
            "Data": [
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 100000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "925ab7aa-998b-4f4b-af26-7c1b3f4eee27",
                "CurrentPrice": 7.46175,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.46175,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": False,
                "MarketPrice": 7.46175,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76332324",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-07T14:54:17.423333Z",
                "Price": 7,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 16
              },
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 100000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "e684a2e2-f9f9-4b10-91ad-a50e2f8b80ae",
                "CurrentPrice": 7.46175,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.46175,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": False,
                "MarketPrice": 7.46175,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76328908",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-07T12:04:13.493333Z",
                "Price": 7,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 16
              },
              {
                "AccountId": "9226397",
                "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Amount": 10000,
                "AssetType": "FxSpot",
                "BuySell": "Buy",
                "CalculationReliability": "Ok",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CorrelationKey": "ec6ca0f4-8380-4068-a32d-538b7b06208e",
                "CurrentPrice": 1.30179,
                "CurrentPriceDelayMinutes": 0,
                "CurrentPriceType": "Ask",
                "DistanceToMarket": 0.20179,
                "Duration": {
                  "DurationType": "GoodTillCancel"
                },
                "IsMarketOpen": False,
                "MarketPrice": 1.30179,
                "OpenOrderType": "Limit",
                "OrderAmountType": "Quantity",
                "OrderId": "76289260",
                "OrderRelation": "StandAlone",
                "OrderTime": "2019-03-04T17:55:59.503333Z",
                "Price": 1.1,
                "RelatedOpenOrders": [],
                "Status": "Working",
                "Uic": 31
              }
            ]
        }
    },
    "_v3_CreateOpenOrdersSubscription": {
        "url": "/openapi/port/v1/orders/subscriptions",
        "body": {
                "Arguments": {
                    "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
                },
                "ContextId": "explorer_1552035128308",
                "ReferenceId": "C_582"
        },
        "response": {
            "ContextId": "explorer_1552035128308",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "C_582",
            "RefreshRate": 1000,
            "Snapshot": {
              "Data": [
                {
                  "AccountId": "9226397",
                  "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "BuySell": "Buy",
                  "CalculationReliability": "Ok",
                  "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                  "CorrelationKey": "925ab7aa-998b-4f4b-af26-7c1b3f4eee27",
                  "CurrentPrice": 7.46175,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Ask",
                  "DistanceToMarket": 0.46175,
                  "Duration": {
                    "DurationType": "GoodTillCancel"
                  },
                  "IsMarketOpen": False,
                  "MarketPrice": 7.46175,
                  "OpenOrderType": "Limit",
                  "OrderAmountType": "Quantity",
                  "OrderId": "76332324",
                  "OrderRelation": "StandAlone",
                  "OrderTime": "2019-03-07T14:54:17.423333Z",
                  "Price": 7,
                  "RelatedOpenOrders": [],
                  "Status": "Working",
                  "Uic": 16
                },
                {
                  "AccountId": "9226397",
                  "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "BuySell": "Buy",
                  "CalculationReliability": "Ok",
                  "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                  "CorrelationKey": "e684a2e2-f9f9-4b10-91ad-a50e2f8b80ae",
                  "CurrentPrice": 7.46175,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Ask",
                  "DistanceToMarket": 0.46175,
                  "Duration": {
                    "DurationType": "GoodTillCancel"
                  },
                  "IsMarketOpen": False,
                  "MarketPrice": 7.46175,
                  "OpenOrderType": "Limit",
                  "OrderAmountType": "Quantity",
                  "OrderId": "76328908",
                  "OrderRelation": "StandAlone",
                  "OrderTime": "2019-03-07T12:04:13.493333Z",
                  "Price": 7,
                  "RelatedOpenOrders": [],
                  "Status": "Working",
                  "Uic": 16
                },
                {
                  "AccountId": "9226397",
                  "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                  "Amount": 10000,
                  "AssetType": "FxSpot",
                  "BuySell": "Buy",
                  "CalculationReliability": "Ok",
                  "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                  "CorrelationKey": "ec6ca0f4-8380-4068-a32d-538b7b06208e",
                  "CurrentPrice": 1.30179,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Ask",
                  "DistanceToMarket": 0.20179,
                  "Duration": {
                    "DurationType": "GoodTillCancel"
                  },
                  "IsMarketOpen": False,
                  "MarketPrice": 1.30179,
                  "OpenOrderType": "Limit",
                  "OrderAmountType": "Quantity",
                  "OrderId": "76289260",
                  "OrderRelation": "StandAlone",
                  "OrderTime": "2019-03-04T17:55:59.503333Z",
                  "Price": 1.1,
                  "RelatedOpenOrders": [],
                  "Status": "Working",
                  "Uic": 31
                }
              ]
            },
            "State": "Active"
        }
    },
    "_v3_RemoveOpenOrderSubscriptionsByTag": {
        "url": "/openapi/port/v1/orders/subscriptions/{ContextId}",
        "params": {},
        "response": ''
    },
    "_v3_RemoveOpenOrderSubscription": {
        "url": "/openapi/port/v1/orders/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "response": ''
    }
}
