# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_ClientDetailsMe": {
        "url": "/openapi/port/v1/clients/me",
        "response": {
            "AccountValueProtectionLimit": 0,
            "ClientId": "9226397",
            "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "CurrencyDecimals": 2,
            "DefaultAccountId": "9226397",
            "DefaultAccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "DefaultCurrency": "EUR",
            "IsMarginTradingAllowed": True,
            "IsVariationMarginEligible": False,
            "LegalAssetTypes": [
              "FxSpot",
              "FxForwards",
              "FxVanillaOption",
              "FxKnockInOption",
              "FxKnockOutOption",
              "FxOneTouchOption",
              "FxNoTouchOption"
            ],
            "LegalAssetTypesAreIndicative": False,
            "Name": "F. Brekeveld",
            "PositionNettingMode": "EndOfDay",
            "SupportsAccountValueProtectionLimit": True
        }
    },
    "_v3_ClientDetails": {
        "url": "/openapi/port/v1/clients/{ClientKey}",
        "response": {
            "AccountValueProtectionLimit": 0,
            "ClientId": "9226397",
            "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "CurrencyDecimals": 2,
            "DefaultAccountId": "9226397",
            "DefaultAccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "DefaultCurrency": "EUR",
            "IsMarginTradingAllowed": True,
            "IsVariationMarginEligible": False,
            "LegalAssetTypes": [
              "FxSpot",
              "FxForwards",
              "FxVanillaOption",
              "FxKnockInOption",
              "FxKnockOutOption",
              "FxOneTouchOption",
              "FxNoTouchOption"
            ],
            "LegalAssetTypesAreIndicative": False,
            "Name": "F. Brekeveld",
            "PositionNettingMode": "EndOfDay",
            "SupportsAccountValueProtectionLimit": True
        }
    },
    "_v3_ClientDetailsUpdate": {
        "url": "/openapi/port/v1/clients/me",
        "body": {
           "AccountValueProtectionLimit": 10000,
           "NewPositionNettingMode": "EndOfDay"
        },
        "response": ''
    },
    "_v3_ClientDetailsByOwner": {
        "url": "/openapi/port/v1/clients",
        "params": {'OwnerKey': "Cf4xZWiYL6W1nMKpygBLLA=="},
        "response": {
            "Data": [
              {
                "AccountValueProtectionLimit": 10000,
                "ClientId": "9226397",
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "CurrencyDecimals": 2,
                "DefaultAccountId": "9226397",
                "DefaultAccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                "DefaultCurrency": "EUR",
                "IsMarginTradingAllowed": True,
                "IsVariationMarginEligible": False,
                "LegalAssetTypes": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption",
                  "FxOneTouchOption",
                  "FxNoTouchOption"
                ],
                "LegalAssetTypesAreIndicative": False,
                "Name": "F. Brekeveld",
                "PositionNettingMode": "EndOfDay",
                "SupportsAccountValueProtectionLimit": True
              }
            ]
        }
    },
    "_v3_ClientSwitchPosNettingMode": {
        "url": "/openapi/port/v1/clients",
        "params": {'ClientKey': "Cf4xZWiYL6W1nMKpygBLLA=="},
        "body": {
           "AccountValueProtectionLimit": 100000,
           "NewPositionNettingMode": "EndOfDay"
        },
        "response": ''
    }
}
