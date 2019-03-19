# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_GetSessionCapabilities": {
        "url": "/openapi/root/v1/sessions/capabilities",
        "response": {
            "DataLevel": "Standard",
            "TradeLevel": "OrdersOnly"
        }
    },
    "_v3_ChangeSessionCapabilities": {
        "url": "/openapi/root/v1/sessions/capabilities",
        "body": {
           "TradeLevel": "OrdersOnly"
        },
        "response": ''
    },
    #    "_v3_ChangeSessionCapabilities": {
    #        "url": "/openapi/root/v1/sessions/capabilities",
    #        "body": {
    #           "TradeLevel": "OrdersOnly"
    #        },
    #        "response": ''
    #    },
    "_v3_CreateSessionCapabilitiesSubscription": {
        "url": "openapi/root/v1/sessions/events/subscriptions",
        "body": {
            "ContextId": "20190314053019906",
            "ReferenceId": "S56886",
            "RefreshRate": 1000,
            "Tag": "PAGE1"
        },
        "response": {
            "ContextId": "20190314053019906",
            "Format": "application/json",
            "InactivityTimeout": 120,
            "ReferenceId": "S56886",
            "RefreshRate": 1000,
            "Snapshot": {
              "DataLevel": "Standard",
              "TradeLevel": "OrdersOnly"
            },
            "State": "Active"
        }
    },
    "_v3_RemoveSessionCapabilitiesSubscription": {
        "url": "/openapi/root/v1/sessions/events/subscriptions"
               "/{ContextId}/{ReferenceId}",
        "route": {
            "ContextId": "20180204125301453",
            "ReferenceId": "C04",
        },
        "response": ''
    }
}
