# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_NetInstrumentsExposureMe": {
        "url": "/openapi/port/v1/exposure/instruments/me",
        "response": [
            {
              "Amount": 60000,
              "AssetType": "FxSpot",
              "AverageOpenPrice": 1.13071,
              "CalculationReliability": "Ok",
              "CanBeClosed": True,
              "DisplayAndFormat": {
                "Currency": "USD",
                "Decimals": 4,
                "Description": "Euro/US Dollar",
                "Format": "AllowDecimalPips",
                "Symbol": "EURUSD"
              },
              "InstrumentPriceDayPercentChange": 0.42,
              "NetPositionId": "EURUSD__FxSpot",
              "ProfitLossOnTrade": -408.6,
              "Uic": 21
            },
            {
              "Amount": -50000,
              "AssetType": "FxSpot",
              "AverageOpenPrice": 8.6839,
              "CalculationReliability": "Ok",
              "CanBeClosed": True,
              "DisplayAndFormat": {
                "Currency": "DKK",
                "Decimals": 4,
                "Description": "British Pound/Danish Krone",
                "Format": "Normal",
                "Symbol": "GBPDKK"
              },
              "InstrumentPriceDayPercentChange": -1,
              "NetPositionId": "GBPDKK__FxSpot",
              "ProfitLossOnTrade": 2530,
              "Uic": 25
            }
        ]
    },
    "_v3_NetInstrumentExposureSpecific": {
        "url": "/openapi/port/v1/exposure/instruments",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": [
            {
              "Amount": 60000,
              "AssetType": "FxSpot",
              "AverageOpenPrice": 1.13071,
              "CalculationReliability": "Ok",
              "CanBeClosed": True,
              "DisplayAndFormat": {
                "Currency": "USD",
                "Decimals": 4,
                "Description": "Euro/US Dollar",
                "Format": "AllowDecimalPips",
                "Symbol": "EURUSD"
              },
              "InstrumentPriceDayPercentChange": 0.42,
              "NetPositionId": "EURUSD__FxSpot",
              "ProfitLossOnTrade": -405,
              "Uic": 21
            },
            {
              "Amount": -50000,
              "AssetType": "FxSpot",
              "AverageOpenPrice": 8.6839,
              "CalculationReliability": "Ok",
              "CanBeClosed": True,
              "DisplayAndFormat": {
                "Currency": "DKK",
                "Decimals": 4,
                "Description": "British Pound/Danish Krone",
                "Format": "Normal",
                "Symbol": "GBPDKK"
              },
              "InstrumentPriceDayPercentChange": -1.02,
              "NetPositionId": "GBPDKK__FxSpot",
              "ProfitLossOnTrade": 2600,
              "Uic": 25
            }
        ]
    },
    "_v3_CreateExposureSubscription": {
        "url": "/openapi/port/v1/exposure/instruments/subscriptions",
        "body": {
            "Arguments": {
               "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
            },
            "ContextId": "explorer_1552035128308",
            "ReferenceId": "Z_807"
        },
        "response": {
            "ContextId": "explorer_1552035128308",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "Z_807",
            "RefreshRate": 1000,
            "Snapshot": {
              "Data": [
                {
                  "Amount": 60000,
                  "AssetType": "FxSpot",
                  "AverageOpenPrice": 1.13071,
                  "CalculationReliability": "Ok",
                  "CanBeClosed": True,
                  "DisplayAndFormat": {
                    "Currency": "USD",
                    "Decimals": 4,
                    "Description": "Euro/US Dollar",
                    "Format": "AllowDecimalPips",
                    "Symbol": "EURUSD"
                  },
                  "InstrumentPriceDayPercentChange": 0.44,
                  "NetPositionId": "EURUSD__FxSpot",
                  "ProfitLossOnTrade": -396.6,
                  "Uic": 21
                },
                {
                  "Amount": -50000,
                  "AssetType": "FxSpot",
                  "AverageOpenPrice": 8.6839,
                  "CalculationReliability": "Ok",
                  "CanBeClosed": True,
                  "DisplayAndFormat": {
                    "Currency": "DKK",
                    "Decimals": 4,
                    "Description": "British Pound/Danish Krone",
                    "Format": "Normal",
                    "Symbol": "GBPDKK"
                  },
                  "InstrumentPriceDayPercentChange": -0.98,
                  "NetPositionId": "GBPDKK__FxSpot",
                  "ProfitLossOnTrade": 2420,
                  "Uic": 25
                }
              ]
            },
            "State": "Active"
        }
    },
    "_v3_RemoveExposureSubscriptionsByTag": {
        "url": "/openapi/port/v1/exposure/instruments/"
               "subscriptions/{ContextId}",
        "params": {},
        "response": ''
    },
    "_v3_RemoveExposureSubscription": {
        "url": "/openapi/port/v1/exposure/instruments/"
               "subscriptions/{ContextId}/{ReferenceId}",
        "params": {},
        "response": ''
    },
    "_v3_CurrencyExposureMe": {
        "url": "/openapi/port/v1/exposure/currency/me",
        "response": [
            {
              "Amount": 1057573.99,
              "Currency": "EUR"
            },
            {
              "Amount": -67842.6,
              "Currency": "USD"
            },
            {
              "Amount": -50000,
              "Currency": "GBP"
            },
            {
              "Amount": 434195,
              "Currency": "DKK"
            }
        ]
    },
    "_v3_CurrencyExposureSpecific": {
        "url": "/openapi/port/v1/exposure/currency/me",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": [
            {
              "Amount": 1057573.99,
              "Currency": "EUR"
            },
            {
              "Amount": -67842.6,
              "Currency": "USD"
            },
            {
              "Amount": -50000,
              "Currency": "GBP"
            },
            {
              "Amount": 434195,
              "Currency": "DKK"
            }
        ]
    },
    "_v3_FxSpotExposureMe": {
        "url": "/openapi/port/v1/exposure/fxspot/me",
        "response": [
          {
            "Amount": 431950,
            "AmountInCalculationEntityCurrency": 57878,
            "Currency": "DKK"
          },
          {
            "Amount": 60000,
            "AmountInCalculationEntityCurrency": 60000,
            "Currency": "EUR"
          },
          {
            "Amount": -50000,
            "AmountInCalculationEntityCurrency": -57878,
            "Currency": "GBP"
          },
          {
            "Amount": -67402.2,
            "AmountInCalculationEntityCurrency": -60000,
            "Currency": "USD"
          }
        ]
    },
    "_v3_FxSpotExposureSpecific": {
        "url": "/openapi/port/v1/exposure/fxspot/me",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": [
          {
            "Amount": 432350,
            "AmountInCalculationEntityCurrency": 57929,
            "Currency": "DKK"
          },
          {
            "Amount": 60000,
            "AmountInCalculationEntityCurrency": 60000,
            "Currency": "EUR"
          },
          {
            "Amount": -50000,
            "AmountInCalculationEntityCurrency": -57929,
            "Currency": "GBP"
          },
          {
            "Amount": -67398,
            "AmountInCalculationEntityCurrency": -60000,
            "Currency": "USD"
          }
        ]
    },
}
