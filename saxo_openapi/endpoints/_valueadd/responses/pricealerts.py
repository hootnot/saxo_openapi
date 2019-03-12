# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_GetAllAlerts": {
        "url": "/openapi/vas/v1/pricealerts/definitions",
        "params": {
           '$top': 12015,
           '$skip': 27782,
           '$inlinecount': 'None',
           'State': 'Enabled',
        },
        "response": {
            "Data": [
              {
                "AccountId": "13457INET",
                "AlertDefinitionId": "30834",
                "AssetType": "FxSpot",
                "Comment": "I believe EURUSD will go up within "
                           "the next few years!",
                "ExpiryDate": "2016-09-30T12:00:00Z",
                "IsRecurring": True,
                "Operator": "GreaterOrEqual",
                "PriceVariable": "AskTick",
                "State": "Enabled",
                "TargetValue": 1.34595,
                "Uic": 21,
                "UserId": "2361528"
              }
            ],
            "MaxRows": 206
        }
    },
    "_v3_GetAlertDefinition": {
        "url": "/openapi/vas/v1/pricealerts/definitions/{AlertDefinitionId}",
        "response": {
            "AccountId": "13457INET",
            "AlertDefinitionId": "30834",
            "AssetType": "FxSpot",
            "Comment": "I believe EURUSD will go up within "
                       "the next few years!",
            "ExpiryDate": "2016-09-30T12:00:00Z",
            "IsRecurring": True,
            "Operator": "GreaterOrEqual",
            "PriceVariable": "AskTick",
            "State": "Enabled",
            "TargetValue": 1.34595,
            "Uic": 21,
            "UserId": "2361528"
        }
    },
    "_v3_CreatePriceAlert": {
        "url": "/openapi/vas/v1/pricealerts/definitions/",
        "body": {
           "AccountId": "13457INET",
           "AssetType": "FxSpot",
           "Comment": "I believe EURUSD will go up within the next few years!",
           "ExpiryDate": "2016-09-30T12:00:00Z",
           "IsRecurring": True,
           "Operator": "GreaterOrEqual",
           "PriceVariable": "AskTick",
           "State": "Enabled",
           "TargetValue": 1.34595,
           "Uic": 21
        },
        "response": {
           "AccountId": "13457INET",
           "AlertDefinitionId": "30834",
           "AssetType": "FxSpot",
           "Comment": "I believe EURUSD will go up within the next few years!",
           "ExpiryDate": "2016-09-30T12:00:00Z",
           "IsRecurring": True,
           "Operator": "GreaterOrEqual",
           "PriceVariable": "AskTick",
           "State": "Enabled",
           "TargetValue": 1.34595,
           "Uic": 21,
           "UserId": "2361528"
        }
    },
    "_v3_UpdatePriceAlert": {
        "url": "/openapi/vas/v1/pricealerts/{AlertDefinitionId}/",
        "body": {
           "AccountId": "13457INET",
           "AssetType": "FxSpot",
           "Comment": "I believe EURUSD will go up within the next few years!",
           "ExpiryDate": "2016-09-30T12:00:00Z",
           "IsRecurring": True,
           "Operator": "GreaterOrEqual",
           "PriceVariable": "AskTick",
           "State": "Enabled",
           "TargetValue": 1.34595,
           "Uic": 21
        },
        "response": ''
    },
    "_v3_DeletePriceAlert": {
        "url": "/openapi/vas/v1/pricealerts/definitions/{AlertDefinitionIds}/",
        "response": ''
    },
    "_v3_GetUserNotificationSettings": {
        "url": "/openapi/vas/v1/pricealerts/usersettings/",
        "response": {
            "EmailAddress": "john.doe@broker.com",
            "EmailAddressValidated": False,
            "NotifyWithMail": True,
            "NotifyWithPopup": True,
            "Sound": "None"
        }
    },
    "_v3_ModifyUserNotificationSettings": {
        "url": "/openapi/vas/v1/pricealerts/usersettings/",
        "body": {
            "EmailAddress": "john.doe@broker.com",
            "EmailAddressValidated": False,
            "NotifyWithMail": True,
            "NotifyWithPopup": True,
            "Sound": "None"
        },
        "response": ''
    },
}
