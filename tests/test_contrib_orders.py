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
           {'OrderDuration': {
               'DurationType': 'GoodTillCancel'    # the default
            },
            'OrderType': 'Limit',
            'OrderPrice': 1.10}
        ),
       # .. raises ValueError because GTD requires gtd-datetime
       (onfill.TakeProfitDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.GoodTillDate},
           {'OrderDuration': {
                'DurationType': 'GoodTillDate'
            },
            'OrderType': 'Limit',
            'OrderPrice': 1.10},
           {'exception': ValueError, 'msg': 'Missing GTDDate'}
        ),
       # .. raises ValueError because OrderDurationType must be GTC/GTD/GFD
       (onfill.TakeProfitDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.FillOrKill},
           {'OrderDuration': {
               'DurationType': 'FillOrKill'
            },
            'OrderPrice': 1.10},
           {'exception': ValueError,
            'msg': 'OrderDurationType: FillOrKill invalid'}
        ),
       # StopLossDetails
       (onfill.StopLossDetails,
           {"price": 1.10},
           {'OrderDuration': {
               'DurationType': 'GoodTillCancel'
            },
            'OrderType': 'Stop',
            'OrderPrice': 1.10}
        ),
       # .. raises ValueError because GTD requires gtd-datetime
       (onfill.StopLossDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.GoodTillDate},
           {'OrderDuration': {
               'DurationType': 'GoodTillDate'
            },
            'OrderPrice': 1.10},
           {'exception': ValueError, 'msg': 'Missing GTDDate'}
        ),
       # .. raises ValueError because OrderDurationType must be GTC/GTD/GFD
       (onfill.StopLossDetails,
           {"price": 1.10,
            "OrderDurationType": OD.OrderDurationType.FillOrKill},
           {'OrderDuration': {
                'DurationType': 'FOK'
            },
            'OrderPrice': 1.10},
           {'exception': ValueError,
            'msg': 'OrderDurationType: FillOrKill invalid'}
        ),
       # MO
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "Amount": 10000},         # integer!
           {'Uic': 21,
            'OrderDuration': {   # the default
                'DurationType': 'DayOrder'
            },
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
            'OrderDuration': {   # the default
                'DurationType': 'DayOrder'
            },
            'Amount': 10000,
            'AmountType': 'Quantity',
            'BuySell': 'Sell',
            'AssetType': 'FxSpot',
            'OrderType': 'Market'}
        ),
       # test MarketOrder with ...OnFill parameters
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "Amount": -10000,
            "TakeProfitOnFill": onfill.TakeProfitDetails(price=1.13),
            },
           {
             "Uic": 21,
             "AssetType": "FxSpot",
             "Amount": 10000,
             "BuySell": "Sell",
             "OrderType": "Market",
             "AmountType": "Quantity",
             "OrderDuration": {
               "DurationType": "DayOrder"
             },
             "Orders": [
               {
                 "OrderDuration": {
                   "DurationType": "GoodTillCancel"
                 },
                 "OrderType": "Limit",
                 "OrderPrice": 1.13,
                 "AssetType": "FxSpot",
                 "Amount": 10000,
                 "BuySell": "Buy"
               }
             ]
           }
        ),
       # the same, but onFill passed as a dict instead of an instance
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "Amount": -10000,
            "TakeProfitOnFill": onfill.TakeProfitDetails(price=1.13).data,
            },
           {
             "Uic": 21,
             "AssetType": "FxSpot",
             "Amount": 10000,
             "BuySell": "Sell",
             "OrderType": "Market",
             "AmountType": "Quantity",
             "OrderDuration": {
               "DurationType": "DayOrder"
             },
             "Orders": [
               {
                 "OrderDuration": {
                   "DurationType": "GoodTillCancel"
                 },
                 "OrderType": "Limit",
                 "OrderPrice": 1.13,
                 "AssetType": "FxSpot",
                 "Amount": 10000,
                 "BuySell": "Buy"
               }
             ]
           }
        ),
       (order.MarketOrder,
           {"Uic": 21,
            "AssetType": 'FxSpot',
            "Amount":  10000,
            "StopLossOnFill": onfill.StopLossDetails(price=1.1045),
            },
           {
             "Uic": 21,
             "AssetType": "FxSpot",
             "Amount": 10000,
             "BuySell": "Buy",
             "OrderType": "Market",
             "AmountType": "Quantity",
             "OrderDuration": {
               "DurationType": "DayOrder"
             },
             "Orders": [
               {
                 "OrderDuration": {
                   "DurationType": "GoodTillCancel"
                 },
                 "OrderType": "Stop",
                 "OrderPrice": 1.1045,
                 "AssetType": "FxSpot",
                 "Amount": 10000,
                 "BuySell": "Sell"
               }
             ]
           }
        ),
       (order.MarketOrderFxSpot,
           {"Uic": 21,
            "Amount":  10000,
            "StopLossOnFill": onfill.StopLossDetails(price=1.1045),
            },
           {
             "Uic": 21,
             "AssetType": "FxSpot",
             "Amount": 10000,
             "BuySell": "Buy",
             "OrderType": "Market",
             "AmountType": "Quantity",
             "OrderDuration": {
               "DurationType": "DayOrder"
             },
             "Orders": [
               {
                 "OrderDuration": {
                   "DurationType": "GoodTillCancel"
                 },
                 "OrderType": "Stop",
                 "OrderPrice": 1.1045,
                 "AssetType": "FxSpot",
                 "Amount": 10000,
                 "BuySell": "Sell"
               }
             ]
           }
        ),
       (order.MarketOrderStock,
           {"Uic": 16350,  # Royal Dutch Shell Plc A Amsterdam (RDSa:xams)
            "Amount":  1000,
            },
           {
             "Uic": 16350,
             "AssetType": "Stock",
             "Amount": 1000,
             "BuySell": "Buy",
             "OrderType": "Market",
             "AmountType": "Quantity",
             "OrderDuration": {
               "DurationType": "DayOrder"
             },
           }
        ),
    ])
    def test_all(self, cls, inpar, refpar, excpar=None):

        if not excpar:
            r = cls(**inpar) if inpar else cls()
            self.assertTrue(r.data == refpar)
        else:
            with self.assertRaises(excpar['exception']) as err:
                r = cls(**inpar)

            errval = err.exception
            if excpar['msg']:
                self.assertTrue(excpar['msg'] in str(errval))
            else:
                self.assertTrue(1 == 0)
