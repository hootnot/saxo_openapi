#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
from . import unittestsetup
from .unittestsetup import environment, mock_env, test_generic
from saxo_openapi import API
import saxo_openapi.endpoints.portfolio as pf
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_Portfolio_Positions(unittest.TestCase):
    """Tests for `portfolio-positions` endpoints."""

    def setUp(self):
        """Set up test fixtures, if any."""
        global access_token
        global api

        try:
            access_token = unittestsetup.auth()
            setattr(sys.modules["saxo_openapi.saxo_openapi"],
                    "TRADING_ENVIRONMENTS",
                    mock_env)
            api = API(environment=environment, access_token=access_token)
            api.api_url = 'https://test.com'

        except Exception as e:
            print(e)
            exit(0)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @parameterized.expand([
        (pf.positions, "SinglePosition", {'PositionId': 212561926}),
        (pf.positions, "SinglePositionDetails", {'PositionId': 212561926}),
        (pf.positions, "PositionsMe", {}),
        (pf.positions, "PositionsQuery", {}),
        (pf.positions, "PositionListSubscription", {}),
        (pf.positions, "PositionSubscriptionPageSize",
                       {'ContextId': 'explorer_1551702571343',
                        'ReferenceId': 'C_702'}),
        (pf.positions, "PositionSubscriptionRemoveMultiple",
                       {'ContextId': 'explorer_1551702571343'}),
        (pf.positions, "PositionSubscriptionRemove",
                       {'ContextId': 'explorer_1551702571343',
                        'ReferenceId': 'C_702'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test__rd_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, api, _mod, clsNm, route, **kwargs)


if __name__ == "__main__":

    unittest.main()
