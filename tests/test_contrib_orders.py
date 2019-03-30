# -*- coding: utf-8 -*-

"""Tests for saxo_openapi.contrib.orders."""

import unittest

from parameterized import parameterized


import saxo_openapi.contrib.orders as order
import saxo_openapi.contrib.orders.onfill as onfill
import saxo_openapi.definitions.orders as OD


class TestContribOrders(unittest.TestCase):
    """Tests regarding contrib orders.

    The reference is created using the second dict parameter. The
    first dict parameter is merge with this, but only for the keys
    that do NOT exist. That allows us to override parameters.
    The result should reflect the data constructed by the class

    """

    @parameterized.expand([
       # TakeProfitDetails
       (onfill.TakeProfitDetails,
           {"price": 1.10},
           {'OrderDurationType': 'GoodTillCancel',    # the default
            'OrderType': 'Limit',
            'OrderPrice': 1.10}
        ),
       # .. raises ValueError because GTD requires gtd-datetime
       (onfill.TakeProfitDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.GoodTillDate},
           {'OrderDurationType': 'GoodTillDate',
            'OrderType': 'Limit',
            'OrderPrice': 1.10},
           ValueError
        ),
       # .. raises ValueError because OrderDurationType must be GTC/GTD/GFD
       (onfill.TakeProfitDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.FillOrKill},
           {'OrderDurationType': 'FillOrKill',
            'OrderPrice': 1.10},
           ValueError
        ),
       # StopLossDetails
       (onfill.StopLossDetails,
           {"price": 1.10},
           {'OrderDurationType': 'GoodTillCancel',
            'OrderType': 'Stop',
            'OrderPrice': 1.10}
        ),
       # .. raises ValueError because GTD requires gtd-datetime
       (onfill.StopLossDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.GoodTillDate},
           {'OrderDurationType': 'GoodTillDate',
            'OrderPrice': 1.10},
           ValueError
        ),
       # .. raises ValueError because OrderDurationType must be GTC/GTD/GFD
       (onfill.StopLossDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.FillOrKill},
           {'OrderDurationType': 'FOK',
            'OrderPrice': 1.10},
           ValueError
        ),
       # MO
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "Amount": 10000},         # integer!
           {'Uic': 21,
            'OrderDurationType': 'FillOrKill',    # the default
            'Amount': 10000,
            'AmountType': 'Quantity',
            'BuySell': 'Buy',
            'AssetType': 'FxSpot',
            'OrderType': 'Market'}
        ),
       # test BuySell as dep. on sign of amount
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "Amount": -10000},         # integer!
           {'Uic': 21,
            'OrderDurationType': 'FillOrKill',    # the default
            'Amount': 10000,
            'AmountType': 'Quantity',
            'BuySell': 'Sell',
            'AssetType': 'FxSpot',
            'OrderType': 'Market'}
        ),
       # test GTD without a date, should result in a ValueError
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "OrderDurationType": OD.OrderDurationType.GoodTillDate,
            "Amount": -10000},
           {'Uic': 21,
            'OrderDurationType': 'FillOrKill',    # the default
            'Amount': 10000,
            'AmountType': 'Quantity',
            'BuySell': 'Sell',
            'AssetType': 'FxSpot',
            'OrderType': 'Market'},
           ValueError
        ),
       # test validity of OrderDurationType, should result in a ValueError
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "OrderDurationType": "WRONG",
            "Amount": -10000},
           {'Uic': 21,
            'OrderDurationType': 'WRONG',
            'Amount': 10000,
            'AmountType': 'Quantity',
            'BuySell': 'Sell',
            'AssetType': 'FxSpot',
            'OrderType': 'Market'},
           ValueError
        ),
    ])
    def test_all(self, cls, inpar, refpar, exc=None):

        if not exc:
            r = cls(**inpar) if inpar else cls()
            self.assertTrue(r.data == refpar)
        else:
            with self.assertRaises(exc):
                r = cls(**inpar)
