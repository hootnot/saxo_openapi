# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_HistoricalPositions": {
        "url": "/openapi/hist/v3/positions/{ClientKey}",
        "params": {
            'FromDate': '2019-03-01',
            'ToDate': '2019-03-10'
        },
        "response": {
            "Data": [
              {
                "AccountId": "112209INET",
                "AccountValueEndOfDay": {
                  "AccountBalance": 7526.17183,
                  "CashTransfers": 0,
                  "Date": "2016-07-19",
                  "PositionsValue": -978.29753,
                  "SecurityTransfers": 0,
                  "TotalValue": 6547.8743
                },
                "Amount": -1,
                "AmountAccountValueCloseRatio": "2:1",
                "AmountAccountValueOpenRatio": "2:1",
                "ClosingAssetType": "CfdOnIndex",
                "ClosingTradeDate": "2016-07-19",
                "ClosingValueDate": "2016-07-19",
                "CopiedFrom": "1",
                "CorrelationType": "None",
                "Decimals": 2,
                "ExecutionTimeClose": "2016-07-19T07:25:37.000000Z",
                "ExecutionTimeOpen": "2016-07-18T10:38:06.000000Z",
                "FigureValue": 1,
                "InstrumentCcyToAccountCcyRateClose": 1.1020982542939,
                "InstrumentCcyToAccountCcyRateOpen": 1.11308229426434,
                "InstrumentSymbol": "GER30.I",
                "LongShort": {
                  "PresentationValue": "Short",
                  "Value": "Short"
                },
                "OpeningAssetType": "CfdOnIndex",
                "OpeningTradeDate": "2016-07-18",
                "OpeningValueDate": "2016-07-18",
                "PriceClose": 9998,
                "PriceGain": 0.004778021102926538,
                "PriceOpen": 10046,
                "PricePct": -0.4778021102926538,
                "ProfitLoss": 52.87,
                "ProfitLossAccountValueFraction": 0.00807437613761156,
                "Uic": "1373",
                "ValueInAccountCurrencyClose": -11018.778346430412,
                "ValueInAccountCurrencyOpen": -11182.02472817956
              }
            ]
        }
    },
}
