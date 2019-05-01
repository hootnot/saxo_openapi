# -*- coding: utf-8 -*-

"""Tests for saxo_openapi.contrib.orders.helper"""

import unittest


import saxo_openapi.contrib.orders.helper as hlp


class TestContribOrdersHelper(unittest.TestCase):
    """Tests regarding contrib.orders.helper."""

    def test_hlp_direction_from_amount(self):
        # a negative amount should give Sell, positive: Buy
        bs = hlp.direction_from_amount(-100) + hlp.direction_from_amount(100)
        self.assertTrue(bs, "SellBuy")

    def test_hlp_direction_invert(self):
        # invert Buy should give Sell, Sell -> Buy
        bs = hlp.direction_invert("Buy") + hlp.direction_invert("Sell")
        self.assertTrue(bs, "SellBuy")

    def test_hlp_direction_invert_exc(self):
        # anything else than Buy or Sell should raise a ValueError
        with self.assertRaises(ValueError) as err:
            hlp.direction_invert("Neutral")
        self.assertTrue("wrong value for direction:" in str(err.exception))

    def test_hlp_tie_account_to_order(self):
        # inject the AccountKey in an order specification dict
        order = {
           'Amount': 1000,
           'AssetType': 'FxSpot',
           'Uic': 21,
           'Orders': [
              {'Amount': 1000,
               'etc': None}
           ]
        }
        AccountKey = 'ABCDE'
        reforder = order.copy()
        reforder.update({'AccountKey': AccountKey})
        reforder['Orders'][0].update({'AccountKey': AccountKey})
        o = hlp.tie_account_to_order(AccountKey, order)
        self.assertTrue(o, reforder)

    def test_hlp_order_duration_spec(self):
        r1 = {
           "DurationType": "GoodTillDate",
           "ExpirationDateContainsTime": True,
           "ExpirationDateTime": "2017-12-12T00:00"
        }
        r2 = {
           "DurationType": "DO",
           "ExpirationDateContainsTime": True,
           "ExpirationDateTime": "2017-12-12T14:00"
        }
        o1 = hlp.order_duration_spec("GoodTillDate",
                                     ["GoodTillDate"], "2017-12-12")
        o2 = hlp.order_duration_spec("GoodTillDate",
                                     ["GoodTillDate"], "2017-12-12T14:00")
        self.assertTrue([r1, r2], [o1, o2])

    def test_hlp_order_duration_spec_excep(self):
        with self.assertRaises(ValueError) as err:
            hlp.order_duration_spec("GoodTillDat",
                                    ["GoodTillDate"], "2017-12-12")
        errval = err.exception
        self.assertTrue("GoodTillDat is not supported" in str(errval))
