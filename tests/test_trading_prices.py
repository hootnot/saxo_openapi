# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.trading as tr
from parameterized import parameterized


class TestSaxo_Trading_Prices(ReqMockTest):
    """Tests for `trading-prices` endpoints."""

    def setUp(self):
        super(TestSaxo_Trading_Prices, self).setUp()

    @parameterized.expand([
        (tr.prices, "CreatePriceSubscription", {}),
        (tr.prices, "MarginImpactRequest",
                    {'ContextId': 'ctxt_20190311',
                     'ReferenceId': 'EUR_USD'}),
        (tr.prices, "PriceSubscriptionRemoveByTag",
                    {'ContextId': 'ctxt_20190311'}),
        (tr.prices, "PriceSubscriptionRemove",
                    {'ContextId': 'ctxt_20190311',
                     'ReferenceId': 'EUR_USD'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
