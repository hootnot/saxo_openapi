# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""
responses = {
    "_v3_CreatePriceSubscription": {
        "url": "/openapi/trade/v1/prices/subscriptions",
        "body": {
            "Arguments": {
                "Uic": 45,
                "AssetType": "FxSpot"
            },
            "ContextId": "explorer_1552305379377",
            "ReferenceId": "USDSGD"
        },
        "response": {
           "ContextId": "explorer_1552305379377",
           "Format": "application/json",
           "InactivityTimeout": 30,
           "ReferenceId": "N_935",
           "RefreshRate": 1000,
           "Snapshot": {
             "AssetType": "FxSpot",
             "LastUpdated": "2019-03-11T21:14:00.578000Z",
             "PriceSource": "SBFX",
             "Quote": {
               "Amount": 100000,
               "Ask": 1.35827,
               "Bid": 1.35754,
               "DelayedByMinutes": 0,
               "ErrorCode": "None",
               "Mid": 1.357905,
               "PriceTypeAsk": "Tradable",
               "PriceTypeBid": "Tradable",
               "RFQState": "None"
             },
             "Uic": 45
           },
           "State": "Active"
        }
    },
    "_v3_MarginImpactRequest": {
        "url": "/openapi/trade/v1/prices/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "response": ''
    },
    "_v3_PriceSubscriptionRemoveByTag": {
        "url": "/openapi/trade/v1/prices/subscriptions/{ContextId}",
        "params": {},
        "response": ''
    },
    "_v3_PriceSubscriptionRemove": {
        "url": "/openapi/trade/v1/prices/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "response": ''
    }
}
