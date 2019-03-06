# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_SingleNetPosition": {
        "url": "/openapi/port/v1/netpositions/{NetPositionId}",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
           "NetPositionBase": {
             "AccountId": "9226397",
             "Amount": 100000,
             "AssetType": "FxSpot",
             "CanBeClosed": True,
             "ClientId": "9226397",
             "IsMarketOpen": True,
             "NumberOfRelatedOrders": 0,
             "PositionsAccount": "9226397",
             "SinglePositionId": "212550210",
             "SinglePositionStatus": "Open",
             "Uic": 23,
             "ValueDate": "2019-03-06T00:00:00.000000Z"
           },
           "NetPositionDetails": {
             "CloseCost": {
               "Commission": 8.77
             },
             "CloseCostInBaseCurrency": {
               "Commission": 5.81
             },
             "MarketValue": -508,
             "MarketValueInBaseCurrency": -336.7,
             "OpenCost": {
               "Commission": 8.79
             },
             "OpenCostInBaseCurrency": {
               "Commission": 5.83
             }
           },
           "NetPositionId": "GBPCAD__FxSpot",
           "NetPositionView": {
             "AverageOpenPrice": 1.75824,
             "CalculationReliability": "Ok",
             "CurrentPrice": 1.75316,
             "CurrentPriceDelayMinutes": 0,
             "CurrentPriceType": "Bid",
             "Exposure": 100000,
             "ExposureCurrency": "GBP",
             "ExposureInBaseCurrency": 116226,
             "InstrumentPriceDayPercentChange": -0.17,
             "PositionCount": 1,
             "PositionsNotClosedCount": 1,
             "ProfitLossOnTrade": -508,
             "ProfitLossOnTradeInBaseCurrency": -336.7,
             "Status": "Open",
             "TradeCostsTotal": -17.56,
             "TradeCostsTotalInBaseCurrency": -11.64
           }
        }
    },
    "_v3_SingleNetPositionDetails": {
        "url": "/openapi/port/v1/netpositions/{NetPositionId}/details",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "NetPositionBase": {
              "AccountId": "9226397",
              "Amount": 100000,
              "AssetType": "FxSpot",
              "CanBeClosed": True,
              "ClientId": "9226397",
              "IsMarketOpen": True,
              "NumberOfRelatedOrders": 0,
              "PositionsAccount": "9226397",
              "SinglePositionId": "212550210",
              "SinglePositionStatus": "Open",
              "Uic": 23,
              "ValueDate": "2019-03-06T00:00:00.000000Z"
            },
            "NetPositionDetails": {
              "CloseCost": {
                "Commission": 8.77
              },
              "CloseCostInBaseCurrency": {
                "Commission": 5.81
              },
              "MarketValue": -478,
              "MarketValueInBaseCurrency": -316.77,
              "OpenCost": {
                "Commission": 8.79
              },
              "OpenCostInBaseCurrency": {
                "Commission": 5.83
              }
            },
            "NetPositionId": "GBPCAD__FxSpot",
            "NetPositionView": {
              "AverageOpenPrice": 1.75824,
              "CalculationReliability": "Ok",
              "CurrentPrice": 1.75346,
              "CurrentPriceDelayMinutes": 0,
              "CurrentPriceType": "Bid",
              "Exposure": 100000,
              "ExposureCurrency": "GBP",
              "ExposureInBaseCurrency": 116228,
              "InstrumentPriceDayPercentChange": -0.15,
              "PositionCount": 1,
              "PositionsNotClosedCount": 1,
              "ProfitLossOnTrade": -478,
              "ProfitLossOnTradeInBaseCurrency": -316.77,
              "Status": "Open",
              "TradeCostsTotal": -17.56,
              "TradeCostsTotalInBaseCurrency": -11.64
            }
        }
    },
    "_v3_NetPositionsMe": {
        "url": "/openapi/port/v1/netpositions/me",
        "params": {},
        "response": {
            "__count": 4,
            "Data": [
              {
                "NetPositionBase": {
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "SinglePositionId": "212550210",
                  "SinglePositionStatus": "Open",
                  "Uic": 23,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "GBPCAD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 1.75824,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.75322,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 100000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 116201.5,
                  "InstrumentPriceDayPercentChange": -0.17,
                  "PositionCount": 1,
                  "PositionsNotClosedCount": 1,
                  "ProfitLossOnTrade": -502,
                  "ProfitLossOnTradeInBaseCurrency": -332.64,
                  "Status": "Open",
                  "TradeCostsTotal": -17.56,
                  "TradeCostsTotalInBaseCurrency": -11.64
                }
              },
              {
                "NetPositionBase": {
                  "Amount": 500000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "SinglePositionId": "212550212",
                  "SinglePositionStatus": "Open",
                  "Uic": 22,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "GBPAUD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 1.86391,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.85813,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 500000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 581007.5,
                  "InstrumentPriceDayPercentChange": -0.35,
                  "PositionCount": 1,
                  "PositionsNotClosedCount": 1,
                  "ProfitLossOnTrade": -2890,
                  "ProfitLossOnTradeInBaseCurrency": -1806.86,
                  "Status": "Open",
                  "TradeCostsTotal": -93.05,
                  "TradeCostsTotalInBaseCurrency": -58.18
                }
              },
              {
                "NetPositionBase": {
                  "Amount": 0,
                  "AssetType": "FxSpot",
                  "CanBeClosed": False,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "Uic": 21,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "EURUSD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 0,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.13343,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 0,
                  "ExposureCurrency": "EUR",
                  "ExposureInBaseCurrency": 0,
                  "InstrumentPriceDayPercentChange": -0.26,
                  "PositionCount": 2,
                  "PositionsNotClosedCount": 2,
                  "ProfitLossOnTrade": 5,
                  "ProfitLossOnTradeInBaseCurrency": 4.41,
                  "Status": "Open",
                  "TradeCostsTotal": -11.38,
                  "TradeCostsTotalInBaseCurrency": -10.04
                }
              },
              {
                "NetPositionBase": {
                  "Amount": 10000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "SinglePositionId": "212675868",
                  "SinglePositionStatus": "Open",
                  "Uic": 31,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "GBPUSD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 1.31849,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.31701,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 10000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 11620.15,
                  "InstrumentPriceDayPercentChange": -0.27,
                  "PositionCount": 1,
                  "PositionsNotClosedCount": 1,
                  "ProfitLossOnTrade": -14.8,
                  "ProfitLossOnTradeInBaseCurrency": -13.06,
                  "Status": "Open",
                  "TradeCostsTotal": -6,
                  "TradeCostsTotalInBaseCurrency": -5.29
                }
              }
            ]
        }
    },
    "_v3_NetPositionsQuery": {
        "url": "/openapi/port/v1/netpositions/",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
          "__count": 4,
          "Data": [
              {
                "NetPositionBase": {
                  "AccountId": "9226397",
                  "Amount": 100000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "SinglePositionId": "212550210",
                  "SinglePositionStatus": "Open",
                  "Uic": 23,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "GBPCAD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 1.75824,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.75287,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 100000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 116180.5,
                  "InstrumentPriceDayPercentChange": -0.19,
                  "PositionCount": 1,
                  "PositionsNotClosedCount": 1,
                  "ProfitLossOnTrade": -537,
                  "ProfitLossOnTradeInBaseCurrency": -355.85,
                  "Status": "Open",
                  "TradeCostsTotal": -17.55,
                  "TradeCostsTotalInBaseCurrency": -11.63
                }
              },
              {
                "NetPositionBase": {
                  "AccountId": "9226397",
                  "Amount": 500000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "SinglePositionId": "212550212",
                  "SinglePositionStatus": "Open",
                  "Uic": 22,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "GBPAUD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 1.86391,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.8575,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 500000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 580902.5,
                  "InstrumentPriceDayPercentChange": -0.39,
                  "PositionCount": 1,
                  "PositionsNotClosedCount": 1,
                  "ProfitLossOnTrade": -3205,
                  "ProfitLossOnTradeInBaseCurrency": -2004.09,
                  "Status": "Open",
                  "TradeCostsTotal": -93.04,
                  "TradeCostsTotalInBaseCurrency": -58.18
                }
              },
              {
                "NetPositionBase": {
                  "AccountId": "9226397",
                  "Amount": 0,
                  "AssetType": "FxSpot",
                  "CanBeClosed": False,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "Uic": 21,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "EURUSD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 0,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.13377,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 0,
                  "ExposureCurrency": "EUR",
                  "ExposureInBaseCurrency": 0,
                  "InstrumentPriceDayPercentChange": -0.23,
                  "PositionCount": 2,
                  "PositionsNotClosedCount": 2,
                  "ProfitLossOnTrade": 5,
                  "ProfitLossOnTradeInBaseCurrency": 4.41,
                  "Status": "Open",
                  "TradeCostsTotal": -11.38,
                  "TradeCostsTotalInBaseCurrency": -10.04
                }
              },
              {
                "NetPositionBase": {
                  "AccountId": "9226397",
                  "Amount": 10000,
                  "AssetType": "FxSpot",
                  "CanBeClosed": True,
                  "ClientId": "9226397",
                  "IsMarketOpen": True,
                  "NumberOfRelatedOrders": 0,
                  "PositionsAccount": "9226397",
                  "SinglePositionId": "212675868",
                  "SinglePositionStatus": "Open",
                  "Uic": 31,
                  "ValueDate": "2019-03-06T00:00:00.000000Z"
                },
                "NetPositionId": "GBPUSD__FxSpot",
                "NetPositionView": {
                  "AverageOpenPrice": 1.31849,
                  "CalculationReliability": "Ok",
                  "CurrentPrice": 1.31718,
                  "CurrentPriceDelayMinutes": 0,
                  "CurrentPriceType": "Bid",
                  "Exposure": 10000,
                  "ExposureCurrency": "GBP",
                  "ExposureInBaseCurrency": 11618.05,
                  "InstrumentPriceDayPercentChange": -0.26,
                  "PositionCount": 1,
                  "PositionsNotClosedCount": 1,
                  "ProfitLossOnTrade": -13.1,
                  "ProfitLossOnTradeInBaseCurrency": -11.55,
                  "Status": "Open",
                  "TradeCostsTotal": -6,
                  "TradeCostsTotalInBaseCurrency": -5.29
                }
              }
            ]
        }
    },
    "_v3_NetPositionListSubscription": {
        "url": "/openapi/port/v1/netpositions/subscriptions",
        "body": {
            "Arguments": {
                "ClientKey": "Cf4xZWiYL6W1nMKpygBLLA=="
            },
            "ContextId": "explorer_1551702571343",
            "ReferenceId": "F_20"
        },
        "response": {
            "ContextId": "explorer_1551702571343",
            "Format": "application/json",
            "InactivityTimeout": 30,
            "ReferenceId": "F_20",
            "RefreshRate": 1000,
            "Snapshot": {
              "Data": [
                {
                  "NetPositionBase": {
                    "Amount": 100000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "IsMarketOpen": True,
                    "NumberOfRelatedOrders": 0,
                    "PositionsAccount": "9226397",
                    "SinglePositionId": "212550210",
                    "SinglePositionStatus": "Open",
                    "Uic": 23,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "NetPositionId": "GBPCAD__FxSpot",
                  "NetPositionView": {
                    "AverageOpenPrice": 1.75824,
                    "CalculationReliability": "Ok",
                    "CurrentPrice": 1.75313,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 100000,
                    "ExposureCurrency": "GBP",
                    "ExposureInBaseCurrency": 116179,
                    "InstrumentPriceDayPercentChange": -0.17,
                    "PositionCount": 1,
                    "PositionsNotClosedCount": 1,
                    "ProfitLossOnTrade": -511,
                    "ProfitLossOnTradeInBaseCurrency": -338.57,
                    "Status": "Open",
                    "TradeCostsTotal": -17.56,
                    "TradeCostsTotalInBaseCurrency": -11.63
                  }
                },
                {
                  "NetPositionBase": {
                    "Amount": 500000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "IsMarketOpen": True,
                    "NumberOfRelatedOrders": 0,
                    "PositionsAccount": "9226397",
                    "SinglePositionId": "212550212",
                    "SinglePositionStatus": "Open",
                    "Uic": 22,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "NetPositionId": "GBPAUD__FxSpot",
                  "NetPositionView": {
                    "AverageOpenPrice": 1.86391,
                    "CalculationReliability": "Ok",
                    "CurrentPrice": 1.85805,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 500000,
                    "ExposureCurrency": "GBP",
                    "ExposureInBaseCurrency": 580895,
                    "InstrumentPriceDayPercentChange": -0.36,
                    "PositionCount": 1,
                    "PositionsNotClosedCount": 1,
                    "ProfitLossOnTrade": -2930,
                    "ProfitLossOnTradeInBaseCurrency": -1831.62,
                    "Status": "Open",
                    "TradeCostsTotal": -93.05,
                    "TradeCostsTotalInBaseCurrency": -58.17
                  }
                },
                {
                  "NetPositionBase": {
                    "Amount": 0,
                    "AssetType": "FxSpot",
                    "CanBeClosed": False,
                    "ClientId": "9226397",
                    "IsMarketOpen": True,
                    "NumberOfRelatedOrders": 0,
                    "PositionsAccount": "9226397",
                    "Uic": 21,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "NetPositionId": "EURUSD__FxSpot",
                  "NetPositionView": {
                    "AverageOpenPrice": 0,
                    "CalculationReliability": "Ok",
                    "CurrentPrice": 1.13416,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 0,
                    "ExposureCurrency": "EUR",
                    "ExposureInBaseCurrency": 0,
                    "InstrumentPriceDayPercentChange": -0.2,
                    "PositionCount": 2,
                    "PositionsNotClosedCount": 2,
                    "ProfitLossOnTrade": 5,
                    "ProfitLossOnTradeInBaseCurrency": 4.41,
                    "Status": "Open",
                    "TradeCostsTotal": -11.38,
                    "TradeCostsTotalInBaseCurrency": -10.03
                  }
                },
                {
                  "NetPositionBase": {
                    "Amount": 10000,
                    "AssetType": "FxSpot",
                    "CanBeClosed": True,
                    "ClientId": "9226397",
                    "IsMarketOpen": True,
                    "NumberOfRelatedOrders": 0,
                    "PositionsAccount": "9226397",
                    "SinglePositionId": "212675868",
                    "SinglePositionStatus": "Open",
                    "Uic": 31,
                    "ValueDate": "2019-03-06T00:00:00.000000Z"
                  },
                  "NetPositionId": "GBPUSD__FxSpot",
                  "NetPositionView": {
                    "AverageOpenPrice": 1.31849,
                    "CalculationReliability": "Ok",
                    "CurrentPrice": 1.3176,
                    "CurrentPriceDelayMinutes": 0,
                    "CurrentPriceType": "Bid",
                    "Exposure": 10000,
                    "ExposureCurrency": "GBP",
                    "ExposureInBaseCurrency": 11617.9,
                    "InstrumentPriceDayPercentChange": -0.23,
                    "PositionCount": 1,
                    "PositionsNotClosedCount": 1,
                    "ProfitLossOnTrade": -8.9,
                    "ProfitLossOnTradeInBaseCurrency": -7.85,
                    "Status": "Open",
                    "TradeCostsTotal": -6,
                    "TradeCostsTotalInBaseCurrency": -5.29
                  }
                }
              ]
            },
            "State": "Active"
        }
    },
    "_v3_NetPositionSubscriptionRemoveMultiple": {
        "url": "/openapi/port/v1/netpositions/subscriptions/{ContextId}",
        "params": {
                  "Tag": "..."
        },
        "response": ''
    },
    "_v3_NetPositionSubscriptionRemove": {
        "url": "/openapi/port/v1/netpositions/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "response": ''
    },
}
