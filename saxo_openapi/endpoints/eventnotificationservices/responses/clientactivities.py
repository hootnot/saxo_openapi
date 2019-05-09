# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_CreateSubscriptionForClientEvents": {
        "url": "/openapi/ens/v1/activities/subscriptions",
        "body": {
          "Arguments": {
            "AccountKey": "mroYddvgiGqqudzBPn8daA==",
            "Activities": [
              "AccountFundings",
              "MarginCalls",
              "Orders",
              "Positions"
            ],
            "ClientKey": "URpoxLBgX2I33Af3IhCvHg==",
            "FieldGroups": [
              "DisplayAndFormat",
              "ExchangeInfo"
            ],
            "FromDateTime": "2015-02-02T01:02:03Z",
            "IncludeSubAccounts": False,
            "SequenceId": "37456"
          },
          "ContextId": "Context_20190503051756665",
          "ReferenceId": "M_344",
          "RefreshRate": 0
        },
        "response": {
          "ContextId": "Context_20190503051756665",
          "InactivityTimeout": 30,
          "ReferenceId": "M_344",
          "RefreshRate": 0,
          "Snapshot": {
            "Data": []
          },
          "State": "Active"
        }
    },
    "_v3_RemoveSubscription": {
        "url": "/openapi/ens/v1/activities/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "route": {
            "ContextId": "29931122",
            "ReferenceId": "NP6783",
        },
        "response": ''
    },
    "_v3_RemoveSubscriptions": {
        "url": "/openapi/ens/v1/activities/subscriptions/{ContextId}",
        "route": {
            "ContextId": "29931122",
        },
        "params": {
            "Tag": "PAGE2"
        },
        "response": ''
    },
    "_v3_GetActivities": {
        "url": "/openapi/ens/v1/activities",
        "params": {
            "Activities": "Positions",
            "AccountKey": "fOA0tvOyQqW2aHpWi9P5bw==",
            "ClientKey": "fOA0tvOyQqW2aHpWi9P5bw==",
        },
        "response": {
          "__count": 7,
          "Data": [
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:04.346666Z",
              "ActivityType": "Positions",
              "Amount": 89000,
              "AssetType": "FxSpot",
              "BuySell": "Buy",
              "ClientId": "9300675",
              "Commission": 5.08,
              "ConversionRate": 0.876035,
              "CorrelationKey": "290088ee-c30b-43e0-bb31-f54379950c25",
              "CurrencyCode": "CHF",
              "ExecutionTime": "2019-05-07T11:52:04.344981Z",
              "OpenPrice": 1.14166,
              "OpenSpot": 1.14166,
              "PositionEvent": "New",
              "PositionId": "219378806",
              "PriceType": "Amount",
              "SequenceId": "840526",
              "SourceOrderId": "77283801",
              "SpotDate": "2019-05-09",
              "Symbol": "EURCHF",
              "TotalCost": 5.08,
              "Uic": 14,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            },
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:04.836666Z",
              "ActivityType": "Positions",
              "Amount": 142000,
              "AssetType": "FxSpot",
              "BuySell": "Buy",
              "ClientId": "9300675",
              "Commission": 5.09,
              "ConversionRate": 0.876035,
              "CorrelationKey": "2f3b72b6-4bc8-4d35-a4bc-8ca092586f81",
              "CurrencyCode": "CHF",
              "ExecutionTime": "2019-05-07T11:52:04.833449Z",
              "OpenPrice": 0.71691,
              "OpenSpot": 0.71691,
              "PositionEvent": "New",
              "PositionId": "219378808",
              "PriceType": "Amount",
              "SequenceId": "840529",
              "SourceOrderId": "77283802",
              "SpotDate": "2019-05-09",
              "Symbol": "AUDCHF",
              "TotalCost": 5.09,
              "Uic": 5027,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            },
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:06.470000Z",
              "ActivityType": "Positions",
              "Amount": 76000,
              "AssetType": "FxSpot",
              "BuySell": "Buy",
              "ClientId": "9300675",
              "Commission": 5.07,
              "ConversionRate": 0.876035,
              "CorrelationKey": "f77bf761-380c-49b9-8027-93281f3fa321",
              "CurrencyCode": "CHF",
              "ExecutionTime": "2019-05-07T11:52:06.469006Z",
              "OpenPrice": 1.33438,
              "OpenSpot": 1.33438,
              "PositionEvent": "New",
              "PositionId": "219378812",
              "PriceType": "Amount",
              "SequenceId": "840532",
              "SourceOrderId": "77283803",
              "SpotDate": "2019-05-09",
              "Symbol": "GBPCHF",
              "TotalCost": 5.07,
              "Uic": 24,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            },
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:06.930000Z",
              "ActivityType": "Positions",
              "Amount": 152000,
              "AssetType": "FxSpot",
              "BuySell": "Buy",
              "ClientId": "9300675",
              "Commission": 5.12,
              "ConversionRate": 0.876035,
              "CorrelationKey": "f9cc8f67-b48e-490d-bc0e-811d2cd2dc8a",
              "CurrencyCode": "CHF",
              "ExecutionTime": "2019-05-07T11:52:06.929444Z",
              "OpenPrice": 0.67363,
              "OpenSpot": 0.67363,
              "PositionEvent": "New",
              "PositionId": "219378814",
              "PriceType": "Amount",
              "SequenceId": "840535",
              "SourceOrderId": "77283804",
              "SpotDate": "2019-05-09",
              "Symbol": "NZDCHF",
              "TotalCost": 5.12,
              "Uic": 34,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            },
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:07.273333Z",
              "ActivityType": "Positions",
              "Amount": 102000,
              "AssetType": "FxSpot",
              "BuySell": "Sell",
              "ClientId": "9300675",
              "Commission": 553,
              "ConversionRate": 0.0080785,
              "CorrelationKey": "0f0ee8ff-da82-4945-911c-5e232749d8a0",
              "CurrencyCode": "JPY",
              "ExecutionTime": "2019-05-07T11:52:07.271770Z",
              "OpenPrice": 108.419,
              "OpenSpot": 108.419,
              "PositionEvent": "New",
              "PositionId": "219378816",
              "PriceType": "Amount",
              "SequenceId": "840538",
              "SourceOrderId": "77283805",
              "SpotDate": "2019-05-09",
              "Symbol": "CHFJPY",
              "TotalCost": 553,
              "Uic": 8,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            },
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:09.190000Z",
              "ActivityType": "Positions",
              "Amount": 135000,
              "AssetType": "FxSpot",
              "BuySell": "Buy",
              "ClientId": "9300675",
              "Commission": 5.12,
              "ConversionRate": 0.876085,
              "CorrelationKey": "9b29a7b7-8e5f-4b53-b9d0-91dbeb881a95",
              "CurrencyCode": "CHF",
              "ExecutionTime": "2019-05-07T11:52:09.187595Z",
              "OpenPrice": 0.75825,
              "OpenSpot": 0.75825,
              "PositionEvent": "New",
              "PositionId": "219378832",
              "PriceType": "Amount",
              "SequenceId": "840541",
              "SourceOrderId": "77283806",
              "SpotDate": "2019-05-09",
              "Symbol": "CADCHF",
              "TotalCost": 5.12,
              "Uic": 5,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            },
            {
              "AccountId": "9300675",
              "ActivityTime": "2019-05-07T11:52:12.400000Z",
              "ActivityType": "Positions",
              "Amount": 100000,
              "AssetType": "FxSpot",
              "BuySell": "Buy",
              "ClientId": "9300675",
              "Commission": 5.1,
              "ConversionRate": 0.876065,
              "CorrelationKey": "4eeb4738-b1b9-4b36-bd14-31113fa77a2d",
              "CurrencyCode": "CHF",
              "ExecutionTime": "2019-05-07T11:52:12.398657Z",
              "OpenPrice": 1.0205,
              "OpenSpot": 1.0205,
              "PositionEvent": "New",
              "PositionId": "219379050",
              "PriceType": "Amount",
              "SequenceId": "840544",
              "SourceOrderId": "77283807",
              "SpotDate": "2019-05-09",
              "Symbol": "USDCHF",
              "TotalCost": 5.1,
              "Uic": 39,
              "UserId": 9300675,
              "ValueDate": "2019-05-09"
            }
          ]
        }
    },
}
