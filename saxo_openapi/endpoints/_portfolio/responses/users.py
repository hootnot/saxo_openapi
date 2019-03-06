# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_UsersMe": {
        "url": "/openapi/port/v1/users/me",
        "response": {
            "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Culture": "en-GB",
            "Language": "en",
            "LastLoginStatus": "Successful",
            "LastLoginTime": "2019-03-05T13:22:22.123000Z",
            "LegalAssetTypes": [
              "FxSpot",
              "FxForwards",
              "FxVanillaOption",
              "FxKnockInOption",
              "FxKnockOutOption",
              "FxOneTouchOption",
              "FxNoTouchOption"
            ],
            "MarketDataViaOpenApiTermsAccepted": False,
            "Name": "F. Brekeveld",
            "TimeZoneId": 26,
            "UserId": "9226397",
            "UserKey": "Cf4xZWiYL6W1nMKpygBLLA=="
        }
    },
    "_v3_Users": {
        "url": "/openapi/port/v1/users",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "Data": [
              {
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "Culture": "en-GB",
                "Language": "en",
                "LastLoginStatus": "Successful",
                "LastLoginTime": "2019-03-05T13:22:22.123000Z",
                "LegalAssetTypes": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption",
                  "FxOneTouchOption",
                  "FxNoTouchOption"
                ],
                "MarketDataViaOpenApiTermsAccepted": False,
                "Name": "F. Brekeveld",
                "TimeZoneId": 26,
                "UserId": "9226397",
                "UserKey": "Cf4xZWiYL6W1nMKpygBLLA=="
              }
            ]
        }
    },
    "_v3_UserDetails": {
        "url": "/openapi/port/v1/users/{UserKey}",
        "response": {
            "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Culture": "en-GB",
            "Language": "en",
            "LastLoginStatus": "Successful",
            "LastLoginTime": "2019-03-05T13:22:22.123000Z",
            "LegalAssetTypes": [
              "FxSpot",
              "FxForwards",
              "FxVanillaOption",
              "FxKnockInOption",
              "FxKnockOutOption",
              "FxOneTouchOption",
              "FxNoTouchOption"
            ],
            "MarketDataViaOpenApiTermsAccepted": False,
            "Name": "F. Brekeveld",
            "TimeZoneId": 26,
            "UserId": "9226397",
            "UserKey": "Cf4xZWiYL6W1nMKpygBLLA=="
        }
    },
    "_v3_UserUpdate": {
        "url": "/openapi/port/v1/users/me}",
        "body": {"Language": "nl"},
        "response": ''
    }
}
