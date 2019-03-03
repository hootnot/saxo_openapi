# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_instruments": {
        "url": "/openapi/ref/v1/instruments",
        "params": {'AccountKey': 'Cf4xZWiYL6W1nMKpygBLLA==',
                   'Uics': '12,22,23'},
        "response": {
            "Data": [
              {
                "AssetType": "FxSpot",
                "CurrencyCode": "AUD",
                "Description": "Euro/Australian Dollar",
                "ExchangeId": "SBFX",
                "GroupId": 28784,
                "Identifier": 12,
                "SummaryType": "Instrument",
                "Symbol": "EURAUD",
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ]
              },
              {
                "AssetType": "FxSpot",
                "CurrencyCode": "AUD",
                "Description": "British Pound/Australian Dollar",
                "ExchangeId": "SBFX",
                "GroupId": 28867,
                "Identifier": 22,
                "SummaryType": "Instrument",
                "Symbol": "GBPAUD",
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ]
              },
              {
                "AssetType": "FxSpot",
                "CurrencyCode": "CAD",
                "Description": "British Pound/Canadian Dollar",
                "ExchangeId": "SBFX",
                "GroupId": 28871,
                "Identifier": 23,
                "SummaryType": "Instrument",
                "Symbol": "GBPCAD",
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ]
              }
            ]
        }
    },
    "_v3_instrumentsdetails": {
        "url": "/openapi/ref/v1/instruments/details",
        "params": {'AccountKey': 'Cf4xZWiYL6W1nMKpygBLLA==', 'Uics': '23'},
        "response": {
            "__count": 6,
            "Data": [
              {
                "AmountDecimals": 6,
                "AssetType": "FxSwap",
                "CurrencyCode": "CAD",
                "DefaultAmount": 100000,
                "DefaultSlippage": 0.01,
                "DefaultSlippageType": "Percentage",
                "Description": "British Pound/Canadian Dollar",
                "Exchange": {
                  "CountryCode": "DK",
                  "ExchangeId": "SBFX",
                  "Name": "Inter Bank"
                },
                "Format": {
                  "Decimals": 4,
                  "Format": "AllowTwoDecimalPips",
                  "OrderDecimals": 4
                },
                "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
                "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
                "FxSpotDate": "2019-03-06T00:00:00.000000Z",
                "GroupId": 0,
                "IncrementSize": 5000,
                "IsTradable": True,
                "MinimumTradeSize": 1000,
                "OrderDistances": {
                  "EntryDefaultDistance": 0.5,
                  "EntryDefaultDistanceType": "Percentage",
                  "StopLimitDefaultDistance": 5,
                  "StopLimitDefaultDistanceType": "Pips",
                  "StopLossDefaultDistance": 50,
                  "StopLossDefaultDistanceType": "Pips",
                  "StopLossDefaultEnabled": False,
                  "StopLossDefaultOrderType": "Stop",
                  "TakeProfitDefaultDistance": 50,
                  "TakeProfitDefaultDistanceType": "Pips",
                  "TakeProfitDefaultEnabled": False
                },
                "StandardAmounts": [
                  10000,
                  50000,
                  100000,
                  250000,
                  500000,
                  1000000,
                  2000000,
                  5000000,
                  10000000,
                  20000000
                ],
                "SupportedOrderTypes": [
                  "Market",
                  "Limit"
                ],
                "Symbol": "GBPCAD",
                "TickSize": 0.0001,
                "TickSizeLimitOrder": 0.0001,
                "TickSizeStopOrder": 0.00005,
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ],
                "TradableOn": [],
                "TradingSignals": "NotAllowed",
                "Uic": 23
              },
              {
                "AmountDecimals": 6,
                "AssetType": "FxKnockOutOption",
                "CurrencyCode": "CAD",
                "DefaultAmount": 100,
                "Description": "British Pound/Canadian Dollar",
                "Exchange": {
                  "CountryCode": "DK",
                  "ExchangeId": "SBFX",
                  "Name": "Inter Bank"
                },
                "Format": {
                  "Decimals": 4,
                  "OrderDecimals": 4,
                  "StrikeDecimals": 4
                },
                "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
                "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
                "GroupId": 0,
                "IncrementSize": 100,
                "IsTradable": True,
                "MinimumTradeSize": 1000,
                "OptionsChainSubscriptionAllowed": True,
                "OrderDistances": {
                  "EntryDefaultDistance": 0.25,
                  "EntryDefaultDistanceType": "Percentage",
                  "StopLimitDefaultDistance": 5,
                  "StopLimitDefaultDistanceType": "Pips",
                  "StopLossDefaultDistance": 0.5,
                  "StopLossDefaultDistanceType": "Percentage",
                  "StopLossDefaultEnabled": False,
                  "StopLossDefaultOrderType": "Stop",
                  "TakeProfitDefaultDistance": 0.5,
                  "TakeProfitDefaultDistanceType": "Percentage",
                  "TakeProfitDefaultEnabled": False
                },
                "StandardAmounts": [
                  10000,
                  30000,
                  50000,
                  80000,
                  100000
                ],
                "SupportedOrderTypes": [
                  "Market",
                  "Limit",
                  "Stop",
                  "TrailingStop",
                  "StopLimit"
                ],
                "Symbol": "GBPCAD",
                "TickSize": 0.0001,
                "TickSizeLimitOrder": 0.0001,
                "TickSizeStopOrder": 0.00005,
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ],
                "TradableOn": [
                  "9226397"
                ],
                "TradingSignals": "NotAllowed",
                "Uic": 23
              },
              {
                "AmountDecimals": 6,
                "AssetType": "FxKnockInOption",
                "CurrencyCode": "CAD",
                "DefaultAmount": 100,
                "Description": "British Pound/Canadian Dollar",
                "Exchange": {
                  "CountryCode": "DK",
                  "ExchangeId": "SBFX",
                  "Name": "Inter Bank"
                },
                "Format": {
                  "Decimals": 4,
                  "OrderDecimals": 4,
                  "StrikeDecimals": 4
                },
                "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
                "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
                "GroupId": 0,
                "IncrementSize": 100,
                "IsTradable": True,
                "MinimumTradeSize": 1000,
                "OptionsChainSubscriptionAllowed": True,
                "OrderDistances": {
                  "EntryDefaultDistance": 0.25,
                  "EntryDefaultDistanceType": "Percentage",
                  "StopLimitDefaultDistance": 5,
                  "StopLimitDefaultDistanceType": "Pips",
                  "StopLossDefaultDistance": 0.5,
                  "StopLossDefaultDistanceType": "Percentage",
                  "StopLossDefaultEnabled": False,
                  "StopLossDefaultOrderType": "Stop",
                  "TakeProfitDefaultDistance": 0.5,
                  "TakeProfitDefaultDistanceType": "Percentage",
                  "TakeProfitDefaultEnabled": False
                },
                "StandardAmounts": [
                  10000,
                  30000,
                  50000,
                  80000,
                  100000
                ],
                "SupportedOrderTypes": [
                  "Market",
                  "Limit",
                  "Stop",
                  "TrailingStop",
                  "StopLimit"
                ],
                "Symbol": "GBPCAD",
                "TickSize": 0.0001,
                "TickSizeLimitOrder": 0.0001,
                "TickSizeStopOrder": 0.00005,
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ],
                "TradableOn": [
                  "9226397"
                ],
                "TradingSignals": "NotAllowed",
                "Uic": 23
              },
              {
                "AmountDecimals": 6,
                "AssetType": "FxVanillaOption",
                "CurrencyCode": "CAD",
                "DefaultAmount": 100000,
                "Description": "British Pound/Canadian Dollar",
                "Exchange": {
                  "CountryCode": "DK",
                  "ExchangeId": "SBFX",
                  "Name": "Inter Bank"
                },
                "Format": {
                  "Decimals": 4,
                  "Format": "AllowDecimalPips",
                  "StrikeDecimals": 4
                },
                "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
                "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
                "GroupId": 0,
                "IncrementSize": 10000,
                "IsTradable": True,
                "MinimumTradeSize": 1000,
                "OptionsChainSubscriptionAllowed": True,
                "OrderDistances": {
                  "EntryDefaultDistance": 0.5,
                  "EntryDefaultDistanceType": "Percentage",
                  "StopLimitDefaultDistance": 5,
                  "StopLimitDefaultDistanceType": "Pips",
                  "StopLossDefaultDistance": 50,
                  "StopLossDefaultDistanceType": "Pips",
                  "StopLossDefaultEnabled": False,
                  "StopLossDefaultOrderType": "Stop",
                  "TakeProfitDefaultDistance": 50,
                  "TakeProfitDefaultDistanceType": "Pips",
                  "TakeProfitDefaultEnabled": False
                },
                "StandardAmounts": [
                  100000,
                  250000,
                  500000,
                  1000000,
                  2000000,
                  3000000,
                  4000000,
                  5000000,
                  10000000,
                  20000000
                ],
                "SupportedOrderTypes": [
                  "Market",
                  "Limit",
                  "Stop",
                  "TrailingStop",
                  "StopLimit"
                ],
                "Symbol": "GBPCAD",
                "TickSize": 0.0005,
                "TickSizeLimitOrder": 0.0001,
                "TickSizeStopOrder": 0.00005,
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ],
                "TradableOn": [
                  "9226397"
                ],
                "TradingSignals": "NotAllowed",
                "Uic": 23
              },
              {
                "AmountDecimals": 6,
                "AssetType": "FxSpot",
                "CurrencyCode": "CAD",
                "DefaultAmount": 100000,
                "DefaultSlippage": 0.01,
                "DefaultSlippageType": "Percentage",
                "Description": "British Pound/Canadian Dollar",
                "Exchange": {
                  "CountryCode": "DK",
                  "ExchangeId": "SBFX",
                  "Name": "Inter Bank"
                },
                "Format": {
                  "Decimals": 4,
                  "Format": "AllowDecimalPips",
                  "OrderDecimals": 4
                },
                "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
                "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
                "FxSpotDate": "2019-03-06T00:00:00.000000Z",
                "GroupId": 0,
                "IncrementSize": 5000,
                "IsTradable": True,
                "MinimumTradeSize": 1000,
                "OrderDistances": {
                  "EntryDefaultDistance": 0.5,
                  "EntryDefaultDistanceType": "Percentage",
                  "StopLimitDefaultDistance": 5,
                  "StopLimitDefaultDistanceType": "Pips",
                  "StopLossDefaultDistance": 50,
                  "StopLossDefaultDistanceType": "Pips",
                  "StopLossDefaultEnabled": False,
                  "StopLossDefaultOrderType": "Stop",
                  "TakeProfitDefaultDistance": 50,
                  "TakeProfitDefaultDistanceType": "Pips",
                  "TakeProfitDefaultEnabled": False
                },
                "StandardAmounts": [
                  10000,
                  50000,
                  100000,
                  250000,
                  500000,
                  1000000,
                  2000000,
                  5000000,
                  10000000,
                  20000000
                ],
                "SupportedOrderTypes": [
                  "Market",
                  "Limit",
                  "Stop",
                  "TrailingStop",
                  "StopLimit"
                ],
                "Symbol": "GBPCAD",
                "TickSize": 0.00005,
                "TickSizeLimitOrder": 0.0001,
                "TickSizeStopOrder": 0.00005,
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ],
                "TradableOn": [
                  "9226397"
                ],
                "TradingSignals": "Allowed",
                "Uic": 23
              },
              {
                "AmountDecimals": 6,
                "AssetType": "FxForwards",
                "CurrencyCode": "CAD",
                "DefaultAmount": 100000,
                "DefaultSlippage": 0.01,
                "DefaultSlippageType": "Percentage",
                "Description": "British Pound/Canadian Dollar",
                "Exchange": {
                  "CountryCode": "DK",
                  "ExchangeId": "SBFX",
                  "Name": "Inter Bank"
                },
                "Format": {
                  "Decimals": 4,
                  "Format": "AllowDecimalPips",
                  "OrderDecimals": 4
                },
                "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
                "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
                "FxSpotDate": "2019-03-06T00:00:00.000000Z",
                "GroupId": 0,
                "IncrementSize": 5000,
                "IsTradable": True,
                "MinimumTradeSize": 1000,
                "OrderDistances": {
                  "EntryDefaultDistance": 0.5,
                  "EntryDefaultDistanceType": "Percentage",
                  "StopLimitDefaultDistance": 5,
                  "StopLimitDefaultDistanceType": "Pips",
                  "StopLossDefaultDistance": 50,
                  "StopLossDefaultDistanceType": "Pips",
                  "StopLossDefaultEnabled": False,
                  "StopLossDefaultOrderType": "Stop",
                  "TakeProfitDefaultDistance": 50,
                  "TakeProfitDefaultDistanceType": "Pips",
                  "TakeProfitDefaultEnabled": False
                },
                "StandardAmounts": [
                  10000,
                  50000,
                  100000,
                  250000,
                  500000,
                  1000000,
                  2000000,
                  5000000,
                  10000000,
                  20000000
                ],
                "SupportedOrderTypes": [
                  "Market",
                  "Limit",
                  "Stop",
                  "TrailingStop",
                  "StopLimit"
                ],
                "Symbol": "GBPCAD",
                "TickSize": 0.0001,
                "TickSizeLimitOrder": 0.0001,
                "TickSizeStopOrder": 0.00005,
                "TradableAs": [
                  "FxSpot",
                  "FxForwards",
                  "FxVanillaOption",
                  "FxKnockInOption",
                  "FxKnockOutOption"
                ],
                "TradableOn": [
                  "9226397"
                ],
                "TradingSignals": "NotAllowed",
                "Uic": 23
              }
            ]
          }
    },
    "_v3_instrumentdetails": {
        "url": "/openapi/ref/v1/instruments/details/{Uic}/{AssetType}",
        "params": {'AccountKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "AmountDecimals": 6,
            "AssetType": "FxForwards",
            "CurrencyCode": "CAD",
            "DefaultAmount": 100000,
            "DefaultSlippage": 0.01,
            "DefaultSlippageType": "Percentage",
            "Description": "British Pound/Canadian Dollar",
            "Exchange": {
              "CountryCode": "DK",
              "ExchangeId": "SBFX",
              "Name": "Inter Bank"
            },
            "Format": {
              "Decimals": 4,
              "Format": "AllowDecimalPips",
              "OrderDecimals": 4
            },
            "FxForwardMaxForwardDate": "2020-03-10T00:00:00.000000Z",
            "FxForwardMinForwardDate": "2019-03-06T00:00:00.000000Z",
            "FxSpotDate": "2019-03-06T00:00:00.000000Z",
            "GroupId": 0,
            "IncrementSize": 5000,
            "IsTradable": True,
            "MinimumTradeSize": 1000,
            "OrderDistances": {
              "EntryDefaultDistance": 0.5,
              "EntryDefaultDistanceType": "Percentage",
              "StopLimitDefaultDistance": 5,
              "StopLimitDefaultDistanceType": "Pips",
              "StopLossDefaultDistance": 50,
              "StopLossDefaultDistanceType": "Pips",
              "StopLossDefaultEnabled": False,
              "StopLossDefaultOrderType": "Stop",
              "TakeProfitDefaultDistance": 50,
              "TakeProfitDefaultDistanceType": "Pips",
              "TakeProfitDefaultEnabled": False
            },
            "StandardAmounts": [
              10000,
              50000,
              100000,
              250000,
              500000,
              1000000,
              2000000,
              5000000,
              10000000,
              20000000
            ],
            "SupportedOrderTypes": [
              "Market",
              "Limit",
              "Stop",
              "TrailingStop",
              "StopLimit"
            ],
            "Symbol": "GBPCAD",
            "TickSize": 0.0001,
            "TickSizeLimitOrder": 0.0001,
            "TickSizeStopOrder": 0.00005,
            "TradableAs": [
              "FxSpot",
              "FxForwards",
              "FxVanillaOption",
              "FxKnockInOption",
              "FxKnockOutOption"
            ],
            "TradableOn": [
              "9226397"
            ],
            "TradingSignals": "NotAllowed",
            "Uic": 23
        }
    }
}
