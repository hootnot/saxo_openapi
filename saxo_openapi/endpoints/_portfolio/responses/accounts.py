# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_AccountDetails": {
        "url": "/openapi/port/v1/accounts/{AccountKey}",
        "response": {
            "CreationDate": "2019-02-02T10:47:42.313000Z",
            "CanUseCashPositionsAsMarginCollateral": True,
            "AccountType": "Normal",
            "CurrencyDecimals": 2,
            "IsCurrencyConversionAtSettlementTime": True,
            "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "IsShareable": False,
            "IndividualMargining": False,
            "DirectMarketAccess": False,
            "LegalAssetTypes": [
                "FxSpot",
                "FxForwards",
                "FxVanillaOption",
                "FxKnockInOption",
                "FxKnockOutOption",
                "FxOneTouchOption",
                "FxNoTouchOption"
            ],
            "AccountGroupKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Active": True,
            "Sharing": [
                "NoSharing"
            ],
            "IsMarginTradingAllowed": True,
            "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "SupportsAccountValueProtectionLimit": False,
            "UseCashPositionsAsMarginCollateral": True,
            "ClientId": "9226397",
            "IsTrialAccount": True,
            "AccountId": "9226397",
            "Currency": "EUR"
        }
    },
    "_v3_AccountsMe": {
        "url": "/openapi/port/v1/accounts/me",
        "params": {},
        "response": {
            "Data": [
                {
                    "ClientId": "9226397",
                    "DirectMarketAccess": False,
                    "IsTrialAccount": True,
                    "AccountType": "Normal",
                    "UseCashPositionsAsMarginCollateral": True,
                    "CanUseCashPositionsAsMarginCollateral": True,
                    "LegalAssetTypes": [
                        "FxSpot",
                        "FxForwards",
                        "FxVanillaOption",
                        "FxKnockInOption",
                        "FxKnockOutOption",
                        "FxOneTouchOption",
                        "FxNoTouchOption"
                    ],
                    "SupportsAccountValueProtectionLimit": False,
                    "IndividualMargining": False,
                    "IsShareable": False,
                    "Sharing": [
                        "NoSharing"
                    ],
                    "CreationDate": "2019-02-02T10:47:42.313000Z",
                    "IsCurrencyConversionAtSettlementTime": True,
                    "Active": True,
                    "CurrencyDecimals": 2,
                    "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "AccountGroupKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "AccountId": "9226397",
                    "Currency": "EUR",
                    "IsMarginTradingAllowed": True
                }
            ]
        }
    },
    "_v3_AccountListByClient": {
        "url": "/openapi/port/v1/accounts/me",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "Data": [
                {
                    "IsMarginTradingAllowed": True,
                    "DirectMarketAccess": False,
                    "AccountId": "9226397",
                    "ClientId": "9226397",
                    "CreationDate": "2019-02-02T10:47:42.313000Z",
                    "SupportsAccountValueProtectionLimit": False,
                    "CurrencyDecimals": 2,
                    "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "IsTrialAccount": True,
                    "Sharing": [
                        "NoSharing"
                    ],
                    "IsCurrencyConversionAtSettlementTime": True,
                    "AccountType": "Normal",
                    "Active": True,
                    "IndividualMargining": False,
                    "CanUseCashPositionsAsMarginCollateral": True,
                    "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "AccountGroupKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "Currency": "EUR",
                    "IsShareable": False,
                    "UseCashPositionsAsMarginCollateral": True,
                    "LegalAssetTypes": [
                        "FxSpot",
                        "FxForwards",
                        "FxVanillaOption",
                        "FxKnockInOption",
                        "FxKnockOutOption",
                        "FxOneTouchOption",
                        "FxNoTouchOption"
                    ]
                }
            ]
        }
    },
    "_v3_AccountUpdate": {
        "url": "/openapi/port/v1/accounts/{AccountKey}",
        "body": {'DisplayName': 'MyTestName'},
        "response": ''
    },
    "_v3_SubscriptionCreate": {
        "url": "/openapi/port/v1/accounts/subscriptions",
        "body": {
            "Arguments": {
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
            },
            "ContextId": "explorer_1551455553043",
            "ReferenceId": "I_213"
        },
        "response": {
            "ContextId": "explorer_1551455553043",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "I_213",
            "RefreshRate": 5000,
            "Snapshot": {
                "Data": [{
                    "AccountGroupKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "AccountId": "9226397",
                    "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "AccountType": "Normal",
                    "Active": True,
                    "CanUseCashPositionsAsMarginCollateral": True,
                    "ClientId": "9226397",
                    "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA==",
                    "CreationDate": "2019-02-02T10:47:42.313000Z",
                    "Currency": "EUR",
                    "CurrencyDecimals": 2,
                    "DirectMarketAccess": False,
                    "DisplayName": "bram",
                    "IndividualMargining": False,
                    "IsCurrencyConversionAtSettlementTime": True,
                    "IsMarginTradingAllowed": True,
                    "IsShareable": False,
                    "IsTrialAccount": True,
                    "LegalAssetTypes": [
                        "FxSpot",
                        "FxForwards",
                        "FxVanillaOption",
                        "FxKnockInOption",
                        "FxKnockOutOption",
                        "FxOneTouchOption",
                        "FxNoTouchOption"
                    ],
                    "Sharing": [
                        "NoSharing"
                    ],
                    "SupportsAccountValueProtectionLimit": False,
                    "UseCashPositionsAsMarginCollateral": True
                }]
            },
            "State": "Active"
        }
    },
    "_v3_SubscriptionRemoveByTag": {
        "url": "/openapi/port/v1/accounts/subscriptions/{ContextId}",
        "params": {'ClientKey': "Cf4xZWiYL6W1nMKpygBLLA=="},
        "response": '',
    },
    "_v3_SubscriptionRemoveById": {
        "url": "/openapi/port/v1/accounts/subscriptions/{ContextId}/{ReferenceId}",
        "response": '',
    },
}
