# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Acctgrps(ReqMockTest):
    """Tests for `portfolio-accountgroups` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Acctgrps, self).setUp()

    @parameterized.expand([
        (pf.accountgroups, "AccountGroupDetails",
                           {'AccountGroupKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
        (pf.accountgroups, "AccountGroupsMe", {}),
        (pf.accountgroups, "AccountGroupsList", {}),
        (pf.accountgroups, "AccountGroupUpdate",
                           {'AccountGroupKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
