# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_User": {
        "url": "/openapi/root/v1/user",
        "response": {
            "AccessRights": {
              "CanManageCashTransfers": True,
              "CanTakePriceSession": True,
              "CanTakeTradeSession": True,
              "CanTrade": True,
              "CanViewAnyClient": True
            },
            "ClientId": 467989277,
            "EmployeeId": "472298225",
            "Roles": [
              "OAPI.Roles.RetailClient"
            ],
            "UserId": 983293960
          }
    },
}
