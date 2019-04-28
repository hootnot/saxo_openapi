# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Users(ReqMockTest):
    """Tests for `portfolio-users` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Users, self).setUp()

    @parameterized.expand([
        (pf.users, "UsersMe", {}),
        (pf.users, "Users", {}),
        (pf.users, "UserDetails", {'UserKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
        (pf.users, "UserUpdate", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
