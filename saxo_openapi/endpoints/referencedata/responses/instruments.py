# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_Instruments": {
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
    "_v3_InstrumentsDetails": {
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
    "_v3_InstrumentDetails": {
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
    },
    "_v3_ContractoptionSpaces": {
        "url": "/openapi/ref/v1/instruments/contractoptionspaces/"
               "{OptionRootID}/",
        "params": {
            "ExpiryDates": "2019-05-01",
            "OptionSpaceSegment": "SpecificDates",
        },
        "response": {
            "AmountDecimals": 0,
            "AssetType": "StockOption",
            "CanParticipateInMultiLegOrder": False,
            "ContractSize": 100,
            "CurrencyCode": "EUR",
            "DefaultAmount": 1,
            "DefaultExpiry": "2019-04-18T00:00:00Z",
            "DefaultOption": {
              "PutCall": "Call",
              "StrikePrice": 27,
              "Uic": 11897720,
              "UnderlyingUic": 16350
            },
            "Description": "Royal Dutch Shell Plc A",
            "Exchange": {
              "CountryCode": "NL",
              "ExchangeId": "EUR_AMS2",
              "Name": "Euronext Equity & Index Derivatives - AMS"
            },
            "ExerciseStyle": "American",
            "Format": {
              "Decimals": 2,
              "OrderDecimals": 2,
              "StrikeDecimals": 3
            },
            "GroupId": 0,
            "IncrementSize": 1,
            "IsTradable": True,
            "LotSize": 1,
            "LotSizeType": "OddLotsNotAllowed",
            "OptionRootId": 231,
            "OptionSpace": [
              {
                "DisplayDaysToExpiry": 0,
                "DisplayExpiry": "2019-03-01",
                "Expiry": "2019-03-15",
                "LastTradeDate": "2019-03-15T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 24,
                "DisplayExpiry": "2019-04-01",
                "Expiry": "2019-04-18",
                "LastTradeDate": "2019-04-18T15:30:00.000000Z",
                "SpecificOptions": [
                  {
                    "PutCall": "Call",
                    "StrikePrice": 24,
                    "Uic": 11897711,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 25,
                    "Uic": 11897712,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 26.5,
                    "Uic": 11897717,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 26,
                    "Uic": 11897719,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 27,
                    "Uic": 11897720,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 25,
                    "Uic": 11897721,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 24,
                    "Uic": 11897722,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 26,
                    "Uic": 11897723,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 28,
                    "Uic": 11897724,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 30,
                    "Uic": 11897725,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 27.5,
                    "Uic": 11897728,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 29,
                    "Uic": 11897729,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 26.5,
                    "Uic": 11897730,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 27,
                    "Uic": 11897731,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 27.5,
                    "Uic": 11897732,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 28,
                    "Uic": 11897733,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 30,
                    "Uic": 11897734,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 29,
                    "Uic": 11897735,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 23,
                    "Uic": 11900544,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 23,
                    "Uic": 11900558,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 25.5,
                    "Uic": 11903077,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 25.5,
                    "Uic": 11903078,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 22,
                    "Uic": 11949922,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 22,
                    "Uic": 11949924,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 32,
                    "Uic": 12003078,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 32,
                    "Uic": 12003081,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Call",
                    "StrikePrice": 28.5,
                    "Uic": 12007474,
                    "UnderlyingUic": 16350
                  },
                  {
                    "PutCall": "Put",
                    "StrikePrice": 28.5,
                    "Uic": 12007478,
                    "UnderlyingUic": 16350
                  }
                ],
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 54,
                "DisplayExpiry": "2019-05-01",
                "Expiry": "2019-05-17",
                "LastTradeDate": "2019-05-17T15:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 85,
                "DisplayExpiry": "2019-06-01",
                "Expiry": "2019-06-21",
                "LastTradeDate": "2019-06-21T15:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 177,
                "DisplayExpiry": "2019-09-01",
                "Expiry": "2019-09-20",
                "LastTradeDate": "2019-09-20T15:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 268,
                "DisplayExpiry": "2019-12-01",
                "Expiry": "2019-12-20",
                "LastTradeDate": "2019-12-20T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 451,
                "DisplayExpiry": "2020-06-01",
                "Expiry": "2020-06-19",
                "LastTradeDate": "2020-06-19T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 634,
                "DisplayExpiry": "2020-12-01",
                "Expiry": "2020-12-18",
                "LastTradeDate": "2020-12-18T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 999,
                "DisplayExpiry": "2021-12-01",
                "Expiry": "2021-12-17",
                "LastTradeDate": "2021-12-17T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 1364,
                "DisplayExpiry": "2022-12-01",
                "Expiry": "2022-12-16",
                "LastTradeDate": "2022-12-16T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              },
              {
                "DisplayDaysToExpiry": 1729,
                "DisplayExpiry": "2023-12-01",
                "Expiry": "2023-12-15",
                "LastTradeDate": "2023-12-15T16:30:00.000000Z",
                "TickSizeScheme": {
                  "DefaultTickSize": 0.05,
                  "Elements": [
                    {
                      "HighPrice": 5,
                      "TickSize": 0.01
                    }
                  ]
                }
              }
            ],
            "OrderDistances": {
              "EntryDefaultDistance": 0,
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
            "PriceToContractFactor": 100,
            "RelatedInstruments": [
              {
                "AssetType": "CfdOnStock",
                "Uic": 16350
              },
              {
                "AssetType": "Stock",
                "Uic": 16350
              }
            ],
            "RelatedOptionRoots": [],
            "SettlementStyle": "PhysicalDelivery",
            "StandardAmounts": [
              1,
              5,
              10,
              25,
              50,
              100,
              500,
              1000
            ],
            "SupportedOrderTypes": [
              "Limit"
            ],
            "Symbol": "RDSA:xams",
            "TickSize": 0.01,
            "TradableOn": [
              "9300675"
            ],
            "UnderlyingAssetType": "Stock"
        }
    },
    "_v3_FuturesSpaces": {
        "url": "/openapi/ref/v1/instruments/futuresspaces/"
               "{ContinuousFuturesUic}",
        "route": {'ContinuousFuturesUic': 28016},
        "response": {
            "BaseIdentifier": "W",
            "Elements": [
              {
                "DaysToExpiry": 64,
                "ExpiryDate": "2017-07-14",
                "Symbol": "WQ7",
                "Uic": 3406797
              },
              {
                "DaysToExpiry": 127,
                "ExpiryDate": "2017-09-15",
                "Symbol": "WV7",
                "Uic": 3844782
              },
              {
                "DaysToExpiry": 188,
                "ExpiryDate": "2017-11-15",
                "Symbol": "WZ7",
                "Uic": 4239352
              },
              {
                "DaysToExpiry": 278,
                "ExpiryDate": "2018-02-13",
                "Symbol": "WH8",
                "Uic": 4895721
              },
              {
                "DaysToExpiry": 337,
                "ExpiryDate": "2018-04-13",
                "Symbol": "WK8",
                "Uic": 5352847
              },
              {
                "DaysToExpiry": 431,
                "ExpiryDate": "2018-07-16",
                "Symbol": "WQ8",
                "Uic": 6112156
              },
              {
                "DaysToExpiry": 491,
                "ExpiryDate": "2018-09-14",
                "Symbol": "WV8",
                "Uic": 6609171
              }
            ]
        }
    },
    "_v3_TradingSchedule": {
        "url": "/openapi/ref/v1/instruments/tradingschedule/{Uic}/{AssetType}",
        "response": {
           "Sessions": [
             {
               "EndTime": "2019-03-08T21:59:00.000000Z",
               "StartTime": "2019-03-07T22:04:00.000000Z",
               "State": "AutomatedTrading"
             },
             {
               "EndTime": "2019-03-10T18:04:00.000000Z",
               "StartTime": "2019-03-08T21:59:00.000000Z",
               "State": "Closed"
             },
             {
               "EndTime": "2019-03-11T20:59:00.000000Z",
               "StartTime": "2019-03-10T18:04:00.000000Z",
               "State": "AutomatedTrading"
             }
           ],
           "TimeZone": 3,
           "TimeZoneAbbreviation": "EST",
           "TimeZoneOffset": "-05:00:00"
        }
    }
}
