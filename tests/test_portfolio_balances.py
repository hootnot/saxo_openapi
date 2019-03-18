# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Balances(ReqMockTest):
    """Tests for `portfolio-balances` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Balances, self).setUp()

    @parameterized.expand([
        (pf.balances, "AccountBalancesMe", {}),
        (pf.balances, "AccountBalances", {}),
        (pf.balances, "MarginOverview", {}),
        (pf.balances, "BalanceSubscriptionCreate", {}),
        (pf.balances, "BalanceSubscriptionRemoveByTag",
                      {'ContextId': 'explorer_1551792578055'}),
        (pf.balances, "BalanceSubscriptionRemoveById",
                      {'ContextId': 'explorer_1551792578055',
                       'ReferenceId': 'O_697'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
