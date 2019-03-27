# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_GetTradeMessages": {
        "url": "openapi/trade/v1/messages",
        "response": {
          "Data": [
            {
              "DateTime": "2014-12-12T09:17:12Z",
              "DisplayName": "Price Alert",
              "DisplayType": "Default",
              "IsDiscardable": False,
              "MessageBody": "Price alert was triggered on EURUSD",
              "MessageHeader": "Price Alert",
              "MessageId": "345322",
              "MessageType": "PriceAlert"
            }
          ]
        }
    },
    "_v3_MarkMessageAsSeen": {
        "url": "openapi/trade/v1/messages/seen/{MessageId}",
        "route": {
            "MessageId": 345322
        },
        "response": ''
    },
    "_v3_CreateTradeMessageSubscription": {
        "url": "openapi/trade/v1/messages/subscriptions/",
        "body": {
            "ContextId": "20190307094456781",
            "Format": "application/json",
            "ReferenceId": "TM90172",
            "RefreshRate": 5,
            "Tag": "PAGE1"
        },
        "response": {
            "ContextId": "20190307094456781",
            "Format": "application/json",
            "InactivityTimeout": 120,
            "ReferenceId": "TM90172",
            "RefreshRate": 800,
            "Snapshot": {
              "Data": [
                {
                  "DateTime": "2014-12-12T09:17:12Z",
                  "DisplayName": "Price Alert",
                  "DisplayType": "Default",
                  "IsDiscardable": False,
                  "MessageBody": "Price alert was triggered on EURUSD",
                  "MessageHeader": "Price Alert",
                  "MessageId": "345322",
                  "MessageType": "PriceAlert"
                }
              ]
            },
            "State": "Active",
            "Tag": "PAGE1"
          }
    },
    "_v3_RemoveTradeMessageSubscriptionById": {
        "url": "openapi/trade/v1/messages/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "route": {
            "ContextId": "ctxt_20190318",
            "ReferenceId": "M452"
        },
        "response": ""
    },
    "_v3_RemoveTradeMessageSubscriptions": {
        "url": "openapi/trade/v1/messages/subscriptions/{ContextId}/",
        "route": {
            "ContextId": "ctxt_20190318",
        },
        "params": {
            "Tag": "CORE"
        },
        "response": ""
    },
}
