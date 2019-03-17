# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Clients(ReqMockTest):
    """Tests for `portfolio-clients` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Clients, self).setUp()

    @parameterized.expand([
        (pf.clients, "ClientDetailsMe", {}),
        (pf.clients, "ClientDetails",
                     {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
        (pf.clients, "ClientDetailsUpdate", {}),
        (pf.clients, "ClientDetailsByOwner", {}),
        (pf.clients, "ClientSwitchPosNettingMode", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
