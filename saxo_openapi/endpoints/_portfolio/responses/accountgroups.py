# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_acctgrpdetails": {
        "url": "/openapi/port/v1/accountgroups/{AccountGroupKey}",
        "params": {'AccountKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "Data": []
        }
    },
    "_v3_acctgrpmelist": {
        "url": "/openapi/port/v1/accountgroups/me",
        "params": {},
        "response": {
            "Data": []
        }
    },
    "_v3_acctgrplist": {
        "url": "/openapi/port/v1/accountgroups",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "response": {
            "Data": []
        }
    },
    "_v3_acctgrpupdate": {
        "url": "/openapi/port/v1/accountgroups/{AccountGroupKey}",
        "params": {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='},
        "body": {"AccountValueProtectionLimit": 100000.00},
        "response": {
            "Data": []
        }
    },
}
