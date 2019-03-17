# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Orders(ReqMockTest):
    """Tests for `portfolio-orders` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Orders, self).setUp()

    @parameterized.expand([
        (pf.orders, "GetOpenOrder", {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA==',
                                     'OrderId': '76332324'}),
        (pf.orders, "GetOpenOrdersMe", {}),
        (pf.orders, "OrderDetails", {'OrderId': '76332324'}),
        (pf.orders, "GetAllOpenOrders", {}),
        (pf.orders, "CreateOpenOrdersSubscription", {}),
        (pf.orders, "RemoveOpenOrderSubscriptionsByTag",
         {'ContextId': 'explorer_1552035128308'}),
        (pf.orders, "RemoveOpenOrderSubscription",
                    {'ContextId': 'explorer_1552035128308',
                     'ReferenceId': 'C_582'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
