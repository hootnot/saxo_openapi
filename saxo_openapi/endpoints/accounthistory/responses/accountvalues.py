# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_AccountSummary": {
        "url": "/openapi/hist/v3/accountvalues/{ClientKey}",
        "params": {},
        "response": {
            "Data": [
              {
                "AccountValue": 5028322.26953125,
                "AccountValueMonth": 1510.67004394531,
                "AccountValueYear": 0,
                "Key": "WMhrJRysCuCFlMbcGFvPVA==",
                "KeyType": "Account"
              },
              {
                "AccountValue": 1000,
                "AccountValueMonth": 0,
                "AccountValueYear": 0,
                "Key": "076n7v5YfRys3|tNojPVcA==",
                "KeyType": "Account"
              },
              {
                "AccountValue": 5028469.04129028,
                "AccountValueMonth": 1510.670043945311,
                "AccountValueYear": 0,
                "Key": "xwhUCDYh8X|pIwV|og2Qag==",
                "KeyType": "Client"
              }
            ]
        }
    },
}
