# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_SinglePosition": {
        "url": "/openapi/port/v1/positions/{PositionId}",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "NetPositionId": "EURUSD__FxSpot",
            "PositionBase": {
              "AccountId": "9226397",
              "Amount": -100000,
              "AssetType": "FxSpot",
              "CanBeClosed": True,
              "ClientId": "9226397",
              "CloseConversionRateSettled": False,
              "CorrelationKey": "46dc6b2a-5b6f-43c8-b747-6b530da9110e",
              "ExecutionTimeOpen": "2019-03-04T00:10:23.040641Z",
              "IsMarketOpen": True,
              "OpenPrice": 1.13715,
              "RelatedOpenOrders": [],
              "SourceOrderId": "76271915",
              "SpotDate": "2019-03-06",
              "Status": "Open",
              "Uic": 21,
              "ValueDate": "2019-03-06T00:00:00.000000Z"
            },
            "PositionId": "212561926",
            "PositionView": {
              "CalculationReliability": "Ok",
              "ConversionRateCurrent": 0.88199,
              "ConversionRateOpen": 0.88199,
              "CurrentPrice": 1.1339,
              "CurrentPriceDelayMinutes": 0,
              "CurrentPriceType": "Ask",
              "Exposure": -100000,
              "ExposureCurrency": "EUR",
              "ExposureInBaseCurrency": -100000,
              "InstrumentPriceDayPercentChange": -0.24,
              "ProfitLossOnTrade": 325,
              "ProfitLossOnTradeInBaseCurrency": 286.65,
              "TradeCostsTotal": -11.36,
              "TradeCostsTotalInBaseCurrency": -10.02
            }
        }
    },
    "_v3_SinglePositionDetails": {
        "url": "/openapi/port/v1/positions/{PositionId}/details",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA==',
                   'AccountKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "DisplayAndFormat": {
              "Currency": "USD",
              "Decimals": 4,
              "Description": "Euro/US Dollar",
              "Format": "AllowDecimalPips",
              "Symbol": "EURUSD"
            },
            "Exchange": {
              "Description": "Inter Bank",
              "ExchangeId": "SBFX",
              "IsOpen": True
            },
            "NetPositionId": "EURUSD__FxSpot",
            "PositionBase": {
              "AccountId": "9226397",
              "Amount": -100000,
              "AssetType": "FxSpot",
              "CanBeClosed": True,
              "ClientId": "9226397",
              "CloseConversionRateSettled": False,
              "CorrelationKey": "46dc6b2a-5b6f-43c8-b747-6b530da9110e",
              "ExecutionTimeOpen": "2019-03-04T00:10:23.040641Z",
              "IsMarketOpen": True,
              "OpenPrice": 1.13715,
              "RelatedOpenOrders": [],
              "SourceOrderId": "76271915",
              "SpotDate": "2019-03-06",
              "Status": "Open",
              "Uic": 21,
              "ValueDate": "2019-03-06T00:00:00.000000Z"
            },
            "PositionDetails": {
              "CloseCost": {
                "Commission": 5.67
              },
              "CloseCostInBaseCurrency": {
                "Commission": 5
              },
              "CorrelationKey": "46dc6b2a-5b6f-43c8-b747-6b530da9110e",
              "LockedByBackOffice": False,
              "MarketValue": 351,
              "OpenCost": {
                "Commission": 5.69
              },
              "OpenCostInBaseCurrency": {
                "Commission": 5.02
              },
              "SourceOrderId": "76271915"
            },
            "PositionId": "212561926",
            "PositionView": {
              "CalculationReliability": "Ok",
              "ConversionRateCurrent": 0.882195,
              "ConversionRateOpen": 0.882195,
              "CurrentPrice": 1.13364,
              "CurrentPriceDelayMinutes": 0,
              "CurrentPriceType": "Ask",
              "Exposure": -100000,
              "ExposureCurrency": "EUR",
              "ExposureInBaseCurrency": -100000,
              "InsTrumentPriceDayPercentChange": -0.26,
              "ProfitLossOnTrade": 351,
              "ProfitLossOnTradeInBaseCurrency": 309.65,
              "TradeCostsTotal": -11.36,
              "TradeCostsTotalInBaseCurrency": -10.02
            }
        }
    },
    "_v3_PositionsMe": {
        "url": "/openapi/port/v1/positions/me",
        "params": {},
        "response": {
            "__count": 4,
            "Data": [
              {
                "NetPositionId": "EURUSD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": -100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "46dc6b2a-5b6f-43c8-b747-6b530da9110e",
                  "ExecutionTimeOpen": "2019-03-04T00:10:23.040641Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.13715,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271915",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 21,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212561926",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.882595,
                  "ConversionRateOpen": 0.882595,
                  "CurrentPrice": 1.13312,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Ask",
                  "Exposure": -100000,
                  "ExposureCurrency": "EUR",
                  "ExposureInBaseCurrency": -100000,
                  "InstrumentPriceDayPercentChange": -0.31,
                  "ProfitLossOnTrade": 403,
                  "ProfitLossOnTradeInBaseCurrency": 355.69,
                  "TradeCostsTotal": -11.36,
                  "TradeCostsTotalInBaseCurrency": -10.03
                }
              },
              {
                "NetPositionId": "EURUSD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "50fae087-b7d4-49ab-afa2-5145cd56a7c5",
                  "ExecutionTimeOpen": "2019-03-04T00:04:11.340151Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.1371,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271912",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 21,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212561892",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.882595,
                  "ConversionRateOpen": 0.882595,
                  "CurrentPrice": 1.13292,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 100000,
                  "ExposureCurrency": "EUR",
                  "ExposureInBaseCurrency": 100000,
                  "InstrumentPriceDayPercentChange": -0.31,
                  "ProfitLossOnTrade": -418,
                  "ProfitLossOnTradeInBaseCurrency": -368.92,
                  "TradeCostsTotal": -11.35,
                  "TradeCostsTotalInBaseCurrency": -10.02
                }
              },
              {
                "NetPositionId": "GBPAUD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": 500000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "206cceed-2240-43f8-8c46-840e8b722549",
                  "ExecutionTimeOpen": "2019-03-03T23:35:08.243690Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.86391,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271862",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 22,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212550212",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.6254,
                  "ConversionRateOpen": 0.6254,
                  "CurrentPrice": 1.85999,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 500000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 581757.5,
                  "InstrumentPriceDayPercentChange": -0.25,
                  "ProfitLossOnTrade": -1960,
                  "ProfitLossOnTradeInBaseCurrency": -1225.78,
                  "TradeCostsTotal": -93.1,
                  "TradeCostsTotalInBaseCurrency": -58.22
                }
              },
              {
                "NetPositionId": "GBPCAD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "19c44107-6858-4191-805c-764a69d27491",
                  "ExecutionTimeOpen": "2019-03-03T23:34:51.823660Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.75824,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271861",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 23,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212550210",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.663595,
                  "ConversionRateOpen": 0.663595,
                  "CurrentPrice": 1.75294,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 100000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 116351.5,
                  "InstrumentPriceDayPercentChange": -0.18,
                  "ProfitLossOnTrade": -530,
                  "ProfitLossOnTradeInBaseCurrency": -351.71,
                  "TradeCostsTotal": -17.55,
                  "TradeCostsTotalInBaseCurrency": -11.65
                }
              }
            ]
        }
    },
    "_v3_PositionsQuery": {
        "url": "/openapi/port/v1/positions/",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
           "__count": 4,
           "Data": [
              {
                "NetPositionId": "EURUSD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": -100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "46dc6b2a-5b6f-43c8-b747-6b530da9110e",
                  "ExecutionTimeOpen": "2019-03-04T00:10:23.040641Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.13715,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271915",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 21,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212561926",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.882905,
                  "ConversionRateOpen": 0.882905,
                  "CurrentPrice": 1.13273,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Ask",
                  "Exposure": -100000,
                  "ExposureCurrency": "EUR",
                  "ExposureInBaseCurrency": -100000,
                  "InstrumentPriceDayPercentChange": -0.34,
                  "ProfitLossOnTrade": 442,
                  "ProfitLossOnTradeInBaseCurrency": 390.24,
                  "TradeCostsTotal": -11.35,
                  "TradeCostsTotalInBaseCurrency": -10.02
                }
              },
              {
                "NetPositionId": "EURUSD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "50fae087-b7d4-49ab-afa2-5145cd56a7c5",
                  "ExecutionTimeOpen": "2019-03-04T00:04:11.340151Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.1371,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271912",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 21,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212561892",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.882905,
                  "ConversionRateOpen": 0.882905,
                  "CurrentPrice": 1.13253,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 100000,
                  "ExposureCurrency": "EUR",
                  "ExposureInBaseCurrency": 100000,
                  "InstrumentPriceDayPercentChange": -0.34,
                  "ProfitLossOnTrade": -457,
                  "ProfitLossOnTradeInBaseCurrency": -403.49,
                  "TradeCostsTotal": -11.35,
                  "TradeCostsTotalInBaseCurrency": -10.02
                }
              },
              {
                "NetPositionId": "GBPAUD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": 500000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "206cceed-2240-43f8-8c46-840e8b722549",
                  "ExecutionTimeOpen": "2019-03-03T23:35:08.243690Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.86391,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271862",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 22,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212550212",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.62534,
                  "ConversionRateOpen": 0.62534,
                  "CurrentPrice": 1.86127,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 500000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 582115,
                  "InstrumentPriceDayPercentChange": -0.19,
                  "ProfitLossOnTrade": -1320,
                  "ProfitLossOnTradeInBaseCurrency": -825.45,
                  "TradeCostsTotal": -93.13,
                  "TradeCostsTotalInBaseCurrency": -58.24
                }
              },
              {
                "NetPositionId": "GBPCAD__FxSpot",
                "PositionBase": {
                  "AccountId": "9226397",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "CloseConversionRateSettled": False,
                  "CorrelationKey": "19c44107-6858-4191-805c-764a69d27491",
                  "ExecutionTimeOpen": "2019-03-03T23:34:51.823660Z",
                  "IsMarketOpen": True,
                  "OpenPrice": 1.75824,
                  "RelatedOpenOrders": [],
                  "SourceOrderId": "76271861",
                  "SpotDate": "2019-03-06",
                  "Status": "Open",
                  "Uic": 23,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "PositionId": "212550210",
                "PositionView": {
                  "CalculationReliability": "Ok",
                  "ConversionRateCurrent": 0.66389,
                  "ConversionRateOpen": 0.66389,
                  "CurrentPrice": 1.75321,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 100000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 116423,
                  "InstrumentPriceDayPercentChange": -0.17,
                  "ProfitLossOnTrade": -503,
                  "ProfitLossOnTradeInBaseCurrency": -333.94,
                  "TradeCostsTotal": -17.56,
                  "TradeCostsTotalInBaseCurrency": -11.66
                }
              }
            ]
        }
    },
    "_v3_PositionListSubscription": {
        "url": "/openapi/port/v1/positions/subscriptions",
        "params": {},
        "body": {
            "Arguments": {
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
            },
            "ContextId": "explorer_1551702571343",
            "ReferenceId": "C_702"
        },
        "response": {
            "ContextId": "explorer_1551702571343",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "C_702",
            "RefreshRate": 1000,
            "Snapshot": {
              "Data": [
                {
                  "NetPositionId": "EURUSD__FxSpot",
                  "PositionBase": {
                    "AccountId": "9226397",
                    "Amount": -100000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "CloseConversionRateSettled": False,
                    "CorrelationKey": "46dc6b2a-5b6f-43c8-b747-6b530da9110e",
                    "ExecutionTimeOpen": "2019-03-04T00:10:23.040641Z",
                    "IsMarketOpen": True,
                    "OpenPrice": 1.13715,
                    "RelatedOpenOrders": [],
                    "SourceOrderId": "76271915",
                    "SpotDate": "2019-03-06",
                    "Status": "Open",
                    "Uic": 21,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "PositionId": "212561926",
                  "PositionView": {
                    "CalculationReliability": "Ok",
                    "ConversionRateCurrent": 0.883135,
                    "ConversionRateOpen": 0.883135,
                    "CurrentPrice": 1.13243,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Ask",
                    "Exposure": -100000,
                    "ExposureCurrency": "EUR",
                    "ExposureInBaseCurrency": -100000,
                    "InstrumentPriceDayPercentChange": -0.37,
                    "ProfitLossOnTrade": 472,
                    "ProfitLossOnTradeInBaseCurrency": 416.84,
                    "TradeCostsTotal": -11.35,
                    "TradeCostsTotalInBaseCurrency": -10.02
                  }
                },
                {
                  "NetPositionId": "EURUSD__FxSpot",
                  "PositionBase": {
                    "AccountId": "9226397",
                    "Amount": 100000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "CloseConversionRateSettled": False,
                    "CorrelationKey": "50fae087-b7d4-49ab-afa2-5145cd56a7c5",
                    "ExecutionTimeOpen": "2019-03-04T00:04:11.340151Z",
                    "IsMarketOpen": True,
                    "OpenPrice": 1.1371,
                    "RelatedOpenOrders": [],
                    "SourceOrderId": "76271912",
                    "SpotDate": "2019-03-06",
                    "Status": "Open",
                    "Uic": 21,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "PositionId": "212561892",
                  "PositionView": {
                    "CalculationReliability": "Ok",
                    "ConversionRateCurrent": 0.883135,
                    "ConversionRateOpen": 0.883135,
                    "CurrentPrice": 1.13223,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 100000,
                    "ExposureCurrency": "EUR",
                    "ExposureInBaseCurrency": 100000,
                    "InstrumentPriceDayPercentChange": -0.37,
                    "ProfitLossOnTrade": -487,
                    "ProfitLossOnTradeInBaseCurrency": -430.09,
                    "TradeCostsTotal": -11.35,
                    "TradeCostsTotalInBaseCurrency": -10.02
                  }
                },
                {
                  "NetPositionId": "GBPAUD__FxSpot",
                  "PositionBase": {
                    "AccountId": "9226397",
                    "Amount": 500000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "CloseConversionRateSettled": False,
                    "CorrelationKey": "206cceed-2240-43f8-8c46-840e8b722549",
                    "ExecutionTimeOpen": "2019-03-03T23:35:08.243690Z",
                    "IsMarketOpen": True,
                    "OpenPrice": 1.86391,
                    "RelatedOpenOrders": [],
                    "SourceOrderId": "76271862",
                    "SpotDate": "2019-03-06",
                    "Status": "Open",
                    "Uic": 22,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "PositionId": "212550212",
                  "PositionView": {
                    "CalculationReliability": "Ok",
                    "ConversionRateCurrent": 0.625415,
                    "ConversionRateOpen": 0.625415,
                    "CurrentPrice": 1.86215,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 500000,
                    "ExposureCurrency": "GBP",
                    "ExposureInBaseCurrency": 582455,
                    "InstrumentPriceDayPercentChange": -0.14,
                    "ProfitLossOnTrade": -880,
                    "ProfitLossOnTradeInBaseCurrency": -550.37,
                    "TradeCostsTotal": -93.15,
                    "TradeCostsTotalInBaseCurrency": -58.26
                  }
                },
                {
                  "NetPositionId": "GBPCAD__FxSpot",
                  "PositionBase": {
                    "AccountId": "9226397",
                    "Amount": 100000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "CloseConversionRateSettled": False,
                    "CorrelationKey": "19c44107-6858-4191-805c-764a69d27491",
                    "ExecutionTimeOpen": "2019-03-03T23:34:51.823660Z",
                    "IsMarketOpen": True,
                    "OpenPrice": 1.75824,
                    "RelatedOpenOrders": [],
                    "SourceOrderId": "76271861",
                    "SpotDate": "2019-03-06",
                    "Status": "Open",
                    "Uic": 23,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "PositionId": "212550210",
                  "PositionView": {
                    "CalculationReliability": "Ok",
                    "ConversionRateCurrent": 0.66362,
                    "ConversionRateOpen": 0.66362,
                    "CurrentPrice": 1.75496,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 100000,
                    "ExposureCurrency": "GBP",
                    "ExposureInBaseCurrency": 116491,
                    "InstrumentPriceDayPercentChange": -0.07,
                    "ProfitLossOnTrade": -328,
                    "ProfitLossOnTradeInBaseCurrency": -217.67,
                    "TradeCostsTotal": -17.56,
                    "TradeCostsTotalInBaseCurrency": -11.65
                  }
                }
              ],
              "MaxRows": 100000
            },
            "State": "Active"
        }
    },
    "_v3_PositionSubscriptionPageSize": {
        "url": "/openapi/port/v1/positions/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "body": {
                  "NewPageSize": 25630
        },
        "response": ''
    },
    "_v3_PositionSubscriptionRemoveMultiple": {
        "url": "/openapi/port/v1/positions/subscriptions/{ContextId}",
        "params": {
                  "Tag": "..."
        },
        "response": ''
    },
    "_v3_PositionSubscriptionRemove": {
        "url": "/openapi/port/v1/positions/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "response": ''
    },
}
