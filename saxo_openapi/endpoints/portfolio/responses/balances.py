# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_AccountBalancesMe": {
        "url": "/port/v1/balances/me",
        "response": {
            "CalculationReliability": "Ok",
            "CashBalance": 999956.74,
            "ChangesScheduled": False,
            "ClosedPositionsCount": 0,
            "CollateralCreditValue": {
              "Line": 978723.62,
              "UtilzationPct": 0
            },
            "CostToClosePositions": -37.39,
            "Currency": "EUR",
            "CurrencyDecimals": 2,
            "InitialMargin": {
              "MarginAvailable": 978723.61,
              "MarginUsedByCurrentPositions": -17662.4,
              "MarginUtilizationPct": 1.77,
              "NetEquityForMargin": 996386.01
            },
            "IsPortfolioMarginModelSimple": True,
            "MarginAvailableForTrading": 978723.61,
            "MarginCollateralNotAvailable": 0,
            "MarginExposureCoveragePct": 141.03,
            "MarginNetExposure": 706507.11,
            "MarginUsedByCurrentPositions": -17662.4,
            "MarginUtilizationPct": 1.77,
            "NetEquityForMargin": 996386.01,
            "NetPositionsCount": 3,
            "NonMarginPositionsValue": 0,
            "OpenPositionsCount": 3,
            "OptionPremiumsMarketValue": 0,
            "OrdersCount": 1,
            "OtherCollateral": 0,
            "TotalValue": 996386.01,
            "TransactionsNotBooked": 0,
            "UnrealizedMarginClosedProfitLoss": 0,
            "UnrealizedMarginOpenProfitLoss": -3533.34,
            "UnrealizedMarginProfitLoss": -3533.34,
            "UnrealizedPositionsValue": -3570.73
        }
    },
    "_v3_AccountBalances": {
        "url": "/port/v1/balances",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "CalculationReliability": "Ok",
            "CashBalance": 999956.74,
            "ChangesScheduled": False,
            "ClosedPositionsCount": 0,
            "CollateralCreditValue": {
              "Line": 979022.6,
              "UtilzationPct": 0
            },
            "CostToClosePositions": -37.46,
            "Currency": "EUR",
            "CurrencyDecimals": 2,
            "InitialMargin": {
              "MarginAvailable": 979022.6,
              "MarginUsedByCurrentPositions": -17692.44,
              "MarginUtilizationPct": 1.78,
              "NetEquityForMargin": 996715.04
            },
            "IsPortfolioMarginModelSimple": True,
            "MarginAvailableForTrading": 979022.6,
            "MarginCollateralNotAvailable": 0,
            "MarginExposureCoveragePct": 140.84,
            "MarginNetExposure": 707697.6,
            "MarginUsedByCurrentPositions": -17692.44,
            "MarginUtilizationPct": 1.78,
            "NetEquityForMargin": 996715.04,
            "NetPositionsCount": 3,
            "NonMarginPositionsValue": 0,
            "OpenPositionsCount": 3,
            "OptionPremiumsMarketValue": 0,
            "OrdersCount": 1,
            "OtherCollateral": 0,
            "TotalValue": 996715.04,
            "TransactionsNotBooked": 0,
            "UnrealizedMarginClosedProfitLoss": 0,
            "UnrealizedMarginOpenProfitLoss": -3204.24,
            "UnrealizedMarginProfitLoss": -3204.24,
            "UnrealizedPositionsValue": -3241.7
        }
    },
    "_v3_MarginOverview": {
        "url": "/port/v1/balances/marginoverview",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "Groups": [
              {
                "Contributors": [
                  {
                    "AssetTypes": [
                      "FxSpot"
                    ],
                    "InstrumentDescription": "British Pound/Canadian Dollar",
                    "InstrumentSpecifier": "GBPCAD",
                    "Margin": 2908,
                    "Uic": 23
                  },
                  {
                    "AssetTypes": [
                      "FxSpot"
                    ],
                    "InstrumentDescription": "British Pound/Australian Dollar",
                    "InstrumentSpecifier": "GBPAUD",
                    "Margin": 14540,
                    "Uic": 22
                  },
                  {
                    "AssetTypes": [
                      "FxSpot"
                    ],
                    "InstrumentDescription": "British Pound/US Dollar",
                    "InstrumentSpecifier": "GBPUSD",
                    "Margin": 291,
                    "Uic": 31
                  }
                ],
                "GroupType": "FX",
                "TotalMargin": 17739
              }
            ]
        }
    },
    "_v3_BalanceSubscriptionCreate": {
        "url": "/port/v1/balances/subscriptions",
        "body": {
            "Arguments": {
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
            },
            "ContextId": "explorer_1551792578055",
            "ReferenceId": "U_452"
        },
        "response": {
            "ContextId": "explorer_1551792578055",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "U_452",
            "RefreshRate": 1000,
            "Snapshot": {
              "CalculationReliability": "Ok",
              "CashBalance": 999956.74,
              "ChangesScheduled": False,
              "ClosedPositionsCount": 0,
              "CollateralCreditValue": {
                "Line": 979847,
                "UtilzationPct": 0
              },
              "CostToClosePositions": -37.54,
              "Currency": "EUR",
              "CurrencyDecimals": 2,
              "InitialMargin": {
                "MarginAvailable": 979847,
                "MarginUsedByCurrentPositions": -17733.77,
                "MarginUtilizationPct": 1.78,
                "NetEquityForMargin": 997580.77
              },
              "IsPortfolioMarginModelSimple": True,
              "MarginAvailableForTrading": 979847,
              "MarginCollateralNotAvailable": 0,
              "MarginExposureCoveragePct": 140.63,
              "MarginNetExposure": 709350.7,
              "MarginUsedByCurrentPositions": -17733.77,
              "MarginUtilizationPct": 1.78,
              "NetEquityForMargin": 997580.77,
              "NetPositionsCount": 3,
              "NonMarginPositionsValue": 0,
              "OpenPositionsCount": 3,
              "OptionPremiumsMarketValue": 0,
              "OrdersCount": 1,
              "OtherCollateral": 0,
              "TotalValue": 997580.77,
              "TransactionsNotBooked": 0,
              "UnrealizedMarginClosedProfitLoss": 0,
              "UnrealizedMarginOpenProfitLoss": -2338.43,
              "UnrealizedMarginProfitLoss": -2338.43,
              "UnrealizedPositionsValue": -2375.97
            },
            "State": "Active"
        }
    },
    "_v3_BalanceSubscriptionRemoveByTag": {
        "url": "/port/v1/balances/subscriptions/{ContextId}",
        "params": {'Tag': 'PAGE1'},
        "response": ''
    },
    "_v3_BalanceSubscriptionRemoveById": {
        "url": "/port/v1/balances/subscriptions/{ContextId}/ReferenceId}",
        "response": ''
    },
}
