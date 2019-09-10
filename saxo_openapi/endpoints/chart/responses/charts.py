# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""
responses = {
    "_v3_GetChartData": {
        "url": "/openapi/chart/v1/charts",
        "params": {
            "AssetType": "FxSpot",
            "Horizon": 60,
            "Count": 24,
            "Uic": 23
        },
        "response": {
              "Data": [
                {
                  "CloseAsk": 1.6321,
                  "CloseBid": 1.6302,
                  "HighAsk": 1.633,
                  "HighBid": 1.63091,
                  "LowAsk": 1.6316,
                  "LowBid": 1.62974,
                  "OpenAsk": 1.63237,
                  "OpenBid": 1.6306,
                  "Time": "2019-09-05T21:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.63115,
                  "CloseBid": 1.63035,
                  "HighAsk": 1.63353,
                  "HighBid": 1.63219,
                  "LowAsk": 1.63092,
                  "LowBid": 1.62988,
                  "OpenAsk": 1.6321,
                  "OpenBid": 1.6303,
                  "Time": "2019-09-05T22:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.63103,
                  "CloseBid": 1.63023,
                  "HighAsk": 1.63146,
                  "HighBid": 1.63066,
                  "LowAsk": 1.63049,
                  "LowBid": 1.62969,
                  "OpenAsk": 1.63114,
                  "OpenBid": 1.63034,
                  "Time": "2019-09-05T23:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.63072,
                  "CloseBid": 1.62992,
                  "HighAsk": 1.63148,
                  "HighBid": 1.63068,
                  "LowAsk": 1.63056,
                  "LowBid": 1.62976,
                  "OpenAsk": 1.63103,
                  "OpenBid": 1.63023,
                  "Time": "2019-09-06T00:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.63125,
                  "CloseBid": 1.63045,
                  "HighAsk": 1.63157,
                  "HighBid": 1.63077,
                  "LowAsk": 1.63063,
                  "LowBid": 1.62983,
                  "OpenAsk": 1.6307,
                  "OpenBid": 1.6299,
                  "Time": "2019-09-06T01:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.63176,
                  "CloseBid": 1.63096,
                  "HighAsk": 1.63211,
                  "HighBid": 1.63131,
                  "LowAsk": 1.63072,
                  "LowBid": 1.62992,
                  "OpenAsk": 1.63125,
                  "OpenBid": 1.63045,
                  "Time": "2019-09-06T02:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62897,
                  "CloseBid": 1.62817,
                  "HighAsk": 1.63182,
                  "HighBid": 1.63102,
                  "LowAsk": 1.62897,
                  "LowBid": 1.62817,
                  "OpenAsk": 1.63178,
                  "OpenBid": 1.63098,
                  "Time": "2019-09-06T03:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62973,
                  "CloseBid": 1.62893,
                  "HighAsk": 1.62981,
                  "HighBid": 1.62901,
                  "LowAsk": 1.62854,
                  "LowBid": 1.62774,
                  "OpenAsk": 1.62896,
                  "OpenBid": 1.62816,
                  "Time": "2019-09-06T04:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62998,
                  "CloseBid": 1.62918,
                  "HighAsk": 1.63058,
                  "HighBid": 1.62978,
                  "LowAsk": 1.62831,
                  "LowBid": 1.62751,
                  "OpenAsk": 1.62974,
                  "OpenBid": 1.62894,
                  "Time": "2019-09-06T05:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62696,
                  "CloseBid": 1.62616,
                  "HighAsk": 1.63084,
                  "HighBid": 1.63004,
                  "LowAsk": 1.62695,
                  "LowBid": 1.62614,
                  "OpenAsk": 1.62999,
                  "OpenBid": 1.62919,
                  "Time": "2019-09-06T06:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62529,
                  "CloseBid": 1.62449,
                  "HighAsk": 1.62772,
                  "HighBid": 1.62692,
                  "LowAsk": 1.62403,
                  "LowBid": 1.62323,
                  "OpenAsk": 1.62695,
                  "OpenBid": 1.62615,
                  "Time": "2019-09-06T07:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.6244,
                  "CloseBid": 1.6236,
                  "HighAsk": 1.62576,
                  "HighBid": 1.62496,
                  "LowAsk": 1.62252,
                  "LowBid": 1.62172,
                  "OpenAsk": 1.62528,
                  "OpenBid": 1.62448,
                  "Time": "2019-09-06T08:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62616,
                  "CloseBid": 1.62536,
                  "HighAsk": 1.62839,
                  "HighBid": 1.62759,
                  "LowAsk": 1.62362,
                  "LowBid": 1.62282,
                  "OpenAsk": 1.62436,
                  "OpenBid": 1.62356,
                  "Time": "2019-09-06T09:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62682,
                  "CloseBid": 1.62602,
                  "HighAsk": 1.62782,
                  "HighBid": 1.62702,
                  "LowAsk": 1.62557,
                  "LowBid": 1.62477,
                  "OpenAsk": 1.62616,
                  "OpenBid": 1.62536,
                  "Time": "2019-09-06T10:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62839,
                  "CloseBid": 1.62759,
                  "HighAsk": 1.62898,
                  "HighBid": 1.62818,
                  "LowAsk": 1.62582,
                  "LowBid": 1.62502,
                  "OpenAsk": 1.6268,
                  "OpenBid": 1.626,
                  "Time": "2019-09-06T11:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62347,
                  "CloseBid": 1.62267,
                  "HighAsk": 1.63078,
                  "HighBid": 1.62894,
                  "LowAsk": 1.6222,
                  "LowBid": 1.62079,
                  "OpenAsk": 1.62839,
                  "OpenBid": 1.62759,
                  "Time": "2019-09-06T12:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62287,
                  "CloseBid": 1.62207,
                  "HighAsk": 1.62688,
                  "HighBid": 1.62607,
                  "LowAsk": 1.62234,
                  "LowBid": 1.62155,
                  "OpenAsk": 1.62346,
                  "OpenBid": 1.62266,
                  "Time": "2019-09-06T13:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62272,
                  "CloseBid": 1.62192,
                  "HighAsk": 1.62351,
                  "HighBid": 1.6227,
                  "LowAsk": 1.62093,
                  "LowBid": 1.62012,
                  "OpenAsk": 1.62287,
                  "OpenBid": 1.62207,
                  "Time": "2019-09-06T14:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62005,
                  "CloseBid": 1.61925,
                  "HighAsk": 1.62339,
                  "HighBid": 1.62259,
                  "LowAsk": 1.61979,
                  "LowBid": 1.619,
                  "OpenAsk": 1.62271,
                  "OpenBid": 1.62191,
                  "Time": "2019-09-06T15:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.61863,
                  "CloseBid": 1.61783,
                  "HighAsk": 1.62038,
                  "HighBid": 1.61958,
                  "LowAsk": 1.61848,
                  "LowBid": 1.61767,
                  "OpenAsk": 1.62005,
                  "OpenBid": 1.61925,
                  "Time": "2019-09-06T16:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.61971,
                  "CloseBid": 1.61891,
                  "HighAsk": 1.62004,
                  "HighBid": 1.61924,
                  "LowAsk": 1.6174,
                  "LowBid": 1.6166,
                  "OpenAsk": 1.6186,
                  "OpenBid": 1.6178,
                  "Time": "2019-09-06T17:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.61992,
                  "CloseBid": 1.61912,
                  "HighAsk": 1.62017,
                  "HighBid": 1.61937,
                  "LowAsk": 1.61818,
                  "LowBid": 1.61738,
                  "OpenAsk": 1.61971,
                  "OpenBid": 1.61891,
                  "Time": "2019-09-06T18:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.62072,
                  "CloseBid": 1.61992,
                  "HighAsk": 1.62083,
                  "HighBid": 1.62005,
                  "LowAsk": 1.61969,
                  "LowBid": 1.61889,
                  "OpenAsk": 1.61993,
                  "OpenBid": 1.61913,
                  "Time": "2019-09-06T19:00:00.000000Z"
                },
                {
                  "CloseAsk": 1.61933,
                  "CloseBid": 1.61732,
                  "HighAsk": 1.6212,
                  "HighBid": 1.62041,
                  "LowAsk": 1.61861,
                  "LowBid": 1.61683,
                  "OpenAsk": 1.62073,
                  "OpenBid": 1.61993,
                  "Time": "2019-09-06T20:00:00.000000Z"
                }
              ],
              "DataVersion": 1715815481
         }
    },
    "_v3_CreateChartDataSubscription": {
        "url": "/openapi/chart/v1/charts/subscriptions",
        "params": {
        },
        "body": {
          "Arguments": {
            "AssetType": "FxSpot",
            "Count": 2,
            "Horizon": 1,
            "Uic": 21
          },
          "ContextId": "20190830035501020",
          "Format": "application/json",
          "ReferenceId": "UIC_21",
          "RefreshRate": 1000
        },
        "response": {
           "ContextId": "20190830035501020",
           "Format": "application/json",
           "InactivityTimeout": 30,
           "ReferenceId": "UIC_21",
           "RefreshRate": 1000,
           "Snapshot": {
             "Data": [
               {
                 "CloseAsk": 1.10631,
                 "CloseBid": 1.10611,
                 "HighAsk": 1.10636,
                 "HighBid": 1.10616,
                 "LowAsk": 1.10631,
                 "LowBid": 1.10611,
                 "OpenAsk": 1.10632,
                 "OpenBid": 1.10612,
                 "Time": "2019-09-09T16:54:00.000000Z"
               },
               {
                 "CloseAsk": 1.10631,
                 "CloseBid": 1.10611,
                 "HighAsk": 1.10632,
                 "HighBid": 1.10612,
                 "LowAsk": 1.10631,
                 "LowBid": 1.10611,
                 "OpenAsk": 1.10632,
                 "OpenBid": 1.10612,
                 "Time": "2019-09-09T16:55:00.000000Z"
               }
             ],
             "DataVersion": 1592272523
           },
           "State": "Active"
        }
    },
    "_v3_ChartDataRemoveSubscriptions": {
        "url": "/openapi/chart/v1/charts/subscriptions/{ContextId}",
        "params": {},
        "response": ''
    },
    "_v3_ChartDataRemoveSubscription": {
        "url": "/openapi/chart/v1/charts/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "params": {},
        "response": ''
    }
}
