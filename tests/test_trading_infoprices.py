# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.trading as tr
from parameterized import parameterized


class TestSaxo_Trading_InfoPrices(ReqMockTest):
    """Tests for `trading-prices` endpoints."""

    def setUp(self):
        super(TestSaxo_Trading_InfoPrices, self).setUp()

    @parameterized.expand([
        (tr.infoprices, "InfoPrice", {}),
        (tr.infoprices, "InfoPrices", {}),
        (tr.infoprices, "CreateInfoPriceSubscription", {}),
        (tr.infoprices, "RemoveInfoPriceSubscriptionsByTag",
                        {'ContextId': 'ctxt_20190316'}),
        (tr.infoprices, "RemoveInfoPriceSubscriptionById",
                        {'ContextId': 'ctxt_20190316',
                         'ReferenceId': 'pri_EURUSD'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
