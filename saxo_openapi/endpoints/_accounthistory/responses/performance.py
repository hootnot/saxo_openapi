# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_AccountPerformance": {
        "url": "/openapi/hist/v3/perf/{ClientKey}",
        "params": {
            'FromDate': '2019-03-01',
            'ToDate': '2019-03-10'
        },
        "response": {
            "AccountSummary": {
              "AverageTradeDurationInMinutes": 34260,
              "AverageTradesPerWeek": 48.2325728770595,
              "NumberOfDaysTraded": 1589,
              "NumberOfLongTrades": 5434,
              "NumberOfShortTrades": 5263,
              "TopTradedInstruments": [
                "DAX.I",
                "DJI.I",
                "EURUSD",
                "GBPUSD",
                "NAS100.I",
                "NOKSEK",
                "EURNOK",
                "SP500.I"
              ],
              "TotalReturnFraction": -0.9999963956455,
              "TradedInstruments": [
                "FxSpot",
                "Stock",
                "FxVanillaOption",
                "ContractFutures"
              ],
              "TradesTotalCount": 10697,
              "TradesWonCount": 6499,
              "WinFraction": 0.61
            },
            "Allocation": {
              "TradesPerAssetType": {
                "ClosedTradesAllocations": [
                  {
                    "AssetClassType": "Equity",
                    "ReturnAttribution": 1,
                    "TradeCount": 168,
                    "TradePercent": 0.38009049773755654
                  },
                  {
                    "AssetClassType": "Currency",
                    "ReturnAttribution": 0.249937016456527,
                    "TradeCount": 112,
                    "TradePercent": 0.25339366515837103
                  },
                  {
                    "AssetClassType": "Commodity",
                    "ReturnAttribution": 0.5628789450009563,
                    "TradeCount": 105,
                    "TradePercent": 0.23755656108597284
                  },
                  {
                    "AssetClassType": "Fixed Income",
                    "ReturnAttribution": -0.013150856136249162,
                    "TradeCount": 57,
                    "TradePercent": 0.12895927601809956
                  }
                ]
              },
              "TradesPerInstrument": {
                "ClosedTradesAllocations": [
                  {
                    "AssetType": "ContractFutures",
                    "InstrumentDescription": "30-Year U.S. Treasury Bond - Sep 2016",
                    "InstrumentSymbol": "ZBU6",
                    "InstrumentUic": 3626018,
                    "ReturnAttribution": -0.15987101005684304,
                    "TradeCount": 40,
                    "TradePercent": 0.09049773755656108
                  },
                  {
                    "AssetType": "FxSpot",
                    "InstrumentDescription": "British Pound/US Dollar",
                    "InstrumentSymbol": "GBPUSD",
                    "InstrumentUic": 31,
                    "ReturnAttribution": 0.14685155225185834,
                    "TradeCount": 37,
                    "TradePercent": 0.083710407239819
                  }
                ]
              }
            },
            "BalancePerformance": {
              "AccountBalanceTimeSeries": [
                {
                  "Date": "2016-03-28",
                  "Value": 0
                },
                {
                  "Date": "2016-03-29",
                  "Value": 0
                }
              ],
              "AccountValueTimeSeries": [
                {
                  "Date": "2016-03-28",
                  "Value": 0
                },
                {
                  "Date": "2016-03-29",
                  "Value": 0
                }
              ],
              "MonthlyProfitLossTimeSeries": [
                {
                  "Date": "2015-11-30",
                  "Value": 0
                },
                {
                  "Date": "2015-12-31",
                  "Value": 0
                }
              ],
              "SecurityTransferTimeSeries": [
                {
                  "Date": "2016-03-28",
                  "Value": 0
                },
                {
                  "Date": "2016-03-29",
                  "Value": 0
                }
              ],
              "YearlyProfitLossTimeSeries": [
                {
                  "Date": "2015-12-31",
                  "Value": 0
                },
                {
                  "Date": "2016-12-31",
                  "Value": 0
                },
                {
                  "Date": "2017-12-31",
                  "Value": 0
                }
              ]
            },
            "From": "2016-03-28",
            "InceptionDay": "2015-11-24",
            "LastTradeDay": "2017-03-27",
            "Thru": "2017-03-27",
            "TimeWeightedPerformance": {
              "AccumulatedTimeWeightedTimeSeries": [
                {
                  "Date": "2016-03-25",
                  "Value": 0
                }
              ],
              "MonthlyReturnTimeSeries": [
                {
                  "Date": "2016-03-25",
                  "Value": 0
                }
              ],
              "PerformanceFraction": -1,
              "PerformanceKeyFigures": {
                "ClosedTradesCount": 0,
                "DrawdownReport": {
                  "Drawdowns": [
                    {
                      "DaysCount": 3,
                      "DepthInPercent": 1,
                      "FromDate": "2016-08-05",
                      "ThruDate": "2016-08-08"
                    }
                  ],
                  "MaxDaysInDrawdownFromTop10Drawdowns": 3
                },
                "LosingDaysFraction": 0.03,
                "MaxDrawDownFraction": 1,
                "ReturnFraction": -1,
                "SampledStandardDeviation": 0.0618018874919214,
                "SharpeRatio": -0.952069751000777,
                "SortinoRatio": -0.0591710418985739
              },
              "YearlyReturnTimeSeries": [
                {
                  "Date": "2016-03-25",
                  "Value": 0
                }
              ]
            },
            "TotalCashBalance": 20226.02,
            "TotalCashBalancePerCurrency": [
              {
                "StringValue": "CAD",
                "Value": -491.707122366824
              }
            ],
            "TotalOpenPositionsValue": 29571.057,
            "TotalPositionsValuePerCurrency": [
              {
                "StringValue": "CAD",
                "Value": -491.707122366824
              }
            ],
            "TotalPositionsValuePerProductPerSecurity": [
              {
                "Description": "Abengoa SA - Warrants",
                "ProductName": "Shares",
                "Symbol": "LOCK - 1496:xxxx",
                "Value": 0
              }
            ]
        }
    },
}
