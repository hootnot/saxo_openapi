# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_algostrategies": {
        "url": "/openapi/ref/v1/algostrategies",
        "params": {'$top': '...', '$skip': '...'},
        "response": {
            "__count": 4,
            "Data": [
              {
                "Description": "Group of VWAP",
                "MinAmountUSD": 0,
                "Name": "VWAP",
                "Parameters": [],
                "SupportedDurationTypes": [
                  "DayOrder"
                ],
                "TradableInstrumentTypes": []
              },
              {
                "Description": "Groups of Iceberg Strategies",
                "MinAmountUSD": 0,
                "Name": "Iceberg",
                "Parameters": [],
                "SupportedDurationTypes": [
                  "DayOrder"
                ],
                "TradableInstrumentTypes": []
              },
              {
                "Description": "Group of With Volume strategies",
                "MinAmountUSD": 0,
                "Name": "With Volume",
                "Parameters": [],
                "SupportedDurationTypes": [
                  "DayOrder"
                ],
                "TradableInstrumentTypes": []
              },
              {
                "Description": "Group of IS strategies",
                "MinAmountUSD": 0,
                "Name": "Implementation Shortfall",
                "Parameters": [],
                "SupportedDurationTypes": [
                  "DayOrder"
                ],
                "TradableInstrumentTypes": []
              }
            ]
        }
    },
    "_v3_algostrategybyname": {
        "url": "/openapi/ref/v1/algostrategies/{Name}",
        "response": {
            "Description": "Group of IS strategies",
            "MinAmountUSD": 0,
            "Name": "Implementation Shortfall",
            "Parameters": [],
            "SupportedDurationTypes": [
                "DayOrder"
            ],
            "TradableInstrumentTypes": []
        }
    },
}
