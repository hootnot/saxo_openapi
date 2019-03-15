#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
from . import unittestsetup
from .unittestsetup import environment, mock_env, test_generic
from saxo_openapi import API
import saxo_openapi.endpoints.valueadd as va
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_Valueadd_PriceAlerts(unittest.TestCase):
    """Tests for `valueadd-pricealerts` endpoints."""

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
        (va.pricealerts, "GetAllAlerts", {}),
        (va.pricealerts, "GetAlertDefinition",
                         {'AlertDefinitionId': 30834}),
        (va.pricealerts, "CreatePriceAlert", {}),
        (va.pricealerts, "UpdatePriceAlert",
                         {'AlertDefinitionId': 30834}),
        (va.pricealerts, "DeletePriceAlert",
                         {'AlertDefinitionIds': "30834,30386"}),
        (va.pricealerts, "GetUserNotificationSettings", {}),
        (va.pricealerts, "ModifyUserNotificationSettings", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test__rd_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, api, _mod, clsNm, route, **kwargs)


if __name__ == "__main__":

    unittest.main()
