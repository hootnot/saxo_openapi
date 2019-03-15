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
from nose_parameterized import parameterized


access_token = None
api = None


class TestSaxo_Portfolio_Exposure(unittest.TestCase):
    """Tests for `portfolio-exposure` endpoints."""

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
        (pf.exposure, "NetInstrumentsExposureMe", {}),
        (pf.exposure, "NetInstrumentExposureSpecific", {}),
        (pf.exposure, "CreateExposureSubscription", {}),
        (pf.exposure, "RemoveExposureSubscriptionsByTag",
                      {'ContextId': 'explorer_1552035128308'}),
        (pf.exposure, "RemoveExposureSubscription",
                      {'ContextId': 'explorer_1552035128308',
                       'ReferenceId': 'Z_807'}),
        (pf.exposure, "CurrencyExposureMe", {}),
        (pf.exposure, "CurrencyExposureSpecific", {}),
        (pf.exposure, "FxSpotExposureMe", {}),
        (pf.exposure, "FxSpotExposureSpecific", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test__rd_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, api, _mod, clsNm, route, **kwargs)


if __name__ == "__main__":

    unittest.main()
