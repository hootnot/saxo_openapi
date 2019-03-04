# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_Order": {
        "url": "/openapi/trade/v2/orders",
        "body": {
            "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Amount": "10000",
            "AssetType": "FxSpot",
            "BuySell": "Buy",
            "OrderType": "Market",
            "Uic": 31
        },
        "response": {
            "OrderId": "76288494"
        }
    },
    "_v3_ChangeOrder": {
        "url": "/openapi/trade/v2/orders",
        "body": {
            "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Amount": 40000.0,
            "AssetType": "FxSpot",
            "OrderId": "76289286",
            "OrderType": "Limit",
            "OrderDuration": {
                "DurationType": "DayOrder"
            }
        },
        "response": {
            "OrderId": "76289286"
        }
    },
    "_v3_CancelOrders": {
        "url": "/openapi/trade/v2/orders/{OrderIds}/",
        "params": {"AccountKey": "Cf4xZWiYL6W1nMKpygBLLA=="},
        "response": {
            "Orders": [
                {
                   "OrderId": "76289286"
                }
            ]
        }
    },
    "_v3_PrecheckOrder": {
        "url": "/openapi/trade/v2/orders/precheck",
        "body": {
            "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Amount": "10000",
            "AssetType": "FxSpot",
            "BuySell": "Buy",
            "OrderType": "Market",
            "Uic": 31
        },
        "response": {
            "EstimatedCashRequired": 296.275,
            "EstimatedCashRequiredCurrency": "EUR",
            "InstrumentToAccountConversionRate": 0.88239,
            "PreCheckResult": "Ok"
        }
    },
}
