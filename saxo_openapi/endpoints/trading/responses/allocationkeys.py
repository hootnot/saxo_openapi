# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_GetAllocationKeys": {
        "url": "openapi/trade/v1/allocationkeys",
        "params": {
             '$top': 601,
             '$skip': 22968,
             'AccountKey': '...',
             'ClientKey': '...',
             'Statuses': 'Active,OneTime'
        },
        "response": {
           "Data": [
             {
               "AllocationKeyId": "227",
               "AllocationKeyName": "MyAllocation_Key",
               "OwnerAccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
               "Status": "Active"
             },
             {
               "AllocationKeyId": "227_2",
               "AllocationKeyName": "MyAllocation_Key_2",
               "OwnerAccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
               "Status": "OneTime"
             }
           ]
        }
    },
    "_v3_GetAllocationKeyDetails": {
        "url": "openapi/trade/v1/allocationkeys/{AllocationKeyId}",
        "route": {
            'AllocationKeyId': 227
        },
        "response": {
            "AllocationKeyId": "227",
            "AllocationKeyName": "MyAllocation_Key",
            "AllocationUnitType": "Percentage",
            "MarginHandling": "Reduce",
            "OwnerAccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
            "ParticipatingAccountsInfo": [
              {
                "AcceptRemainderAmount": True,
                "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
                "Priority": 1,
                "UnitValue": 10.0
              },
              {
                "AcceptRemainderAmount": False,
                "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
                "Priority": 1,
                "UnitValue": 90.0
              }
            ],
            "Status": "Active"
        }
    },
    "_v3_CreateAllocationKey": {
        "url": "openapi/trade/v1/allocationkeys",
        "body": {
              "AllocationKeyName": "MyAllocation_Key",
              "AllocationUnitType": "Percentage",
              "MarginHandling": "Reduce",
              "OneTime": True,
              "OwnerAccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
              "ParticipatingAccountsInfo": [
                {
                  "AcceptRemainderAmount": True,
                  "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
                  "Priority": 1,
                  "UnitValue": 10.0
                },
                {
                  "AcceptRemainderAmount": False,
                  "AccountKey": "LZTc7DdejXODf-WSl2aCyQ==",
                  "Priority": 1,
                  "UnitValue": 90.0
                }
              ]
        },
        "response": {
            "AllocationKeyId": "227"
        }
    },
    "_v3_DeleteAllocationKey": {
        "url": "openapi/trade/v1/allocationkeys/{AllocationKeyId}",
        "route": {
            'AllocationKeyId': 227
        },
        "response": ''
    },
}
