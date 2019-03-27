# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_PositionByQuote": {
        "url": "/openapi/trade/v1/positions",
        "body": {
            "AppHint": 12,
            "BuySell": "Buy",
            "PriceReferenceId": "P57629",
            "QuoteId": "1232145",
            "UserPrice": 234.1
        },
        "response": {
            "PositionId": "1019942426"
        }
    },
    "_v3_UpdatePosition": {
        "url": "/openapi/trade/v1/positions/{PositionId}",
        "body": {
            "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
            "ExerciseMethod": "Spot"
        },
        "response": {
            "PositionId": "1019942426"
        }
    },
    "_v3_ExercisePosition": {
        "url": "/openapi/trade/v1/positions/{PositionId}/exercise",
        "body": {
            "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
            "Amount": 100,
            "AssetType": "StockOption",
            "Uic": 5455848
        },
        "response": {
            "PositionId": "1019942426"
        }
    },
    "_v3_ExerciseAmount": {
        "url": "/openapi/trade/v1/positions/exercise",
        "body": {
            "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
            "Amount": 100,
            "AssetType": "StockOption",
            "Uic": 5455848
        },
        "response": {
            "PositionId": "1019942426"
        }
    },
}
