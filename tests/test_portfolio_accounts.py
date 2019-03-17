# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from nose_parameterized import parameterized


class TestSaxo_Portfolio_Accounts(ReqMockTest):
    """Tests for `portfolio-accounts` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Accounts, self).setUp()

    @parameterized.expand([
        (pf.accounts, "AccountDetails",
                      {'AccountKey': 'f4xZWiYL6W1nMKpygBLLA=='}),
        (pf.accounts, "AccountsMe", {}),
        (pf.accounts, "AccountListByClient", {}),
        (pf.accounts, "AccountUpdate",
                      {'AccountKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
        (pf.accounts, "SubscriptionCreate", {}),
        (pf.accounts, "SubscriptionRemoveByTag",
                      {'ContextId': 'explorer_1551455553043'}),
        (pf.accounts, "SubscriptionRemoveById",
                      {'ContextId': 'explorer_1551455553043',
                       'ReferenceId': 'Z_721'})
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
