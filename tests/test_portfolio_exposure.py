#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment, mock_env, fetchTestData
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

    @requests_mock.Mocker()
    def test__pf_NetInstrumentsExposureMe(self, mock_req):
        """test the NetInstrumentsExposureMe request."""
        tid = "_v3_NetInstrumentsExposureMe"
        resp, data = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.NetInstrumentsExposureMe()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_NetInstrumentExposureSpecific(self, mock_req):
        """test the NetInstrumentExposureSpecific request."""
        tid = "_v3_NetInstrumentExposureSpecific"
        resp, data, params = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.NetInstrumentExposureSpecific(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_CreateExposureSubscription(self, mock_req):
        """test the CreateExposureSubscription request."""
        tid = "_v3_CreateExposureSubscription"
        resp, data = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.CreateExposureSubscription(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_RemoveExposureSubscriptionsByTag(self, mock_req):
        """test the RemoveExposureSubscriptionsByTag request."""
        tid = "_v3_RemoveExposureSubscriptionsByTag"
        resp, data, params = fetchTestData(pf.exposure.responses, tid)
        ContextId = 'explorer_1552035128308'
        r = pf.exposure.RemoveExposureSubscriptionsByTag(ContextId,
                                                         params=params)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_RemoveExposureSubscription(self, mock_req):
        """test the RemoveExposureSubscription request."""
        tid = "_v3_RemoveExposureSubscription"
        resp, data, params = fetchTestData(pf.exposure.responses, tid)
        ContextId = 'explorer_1552035128308'
        ReferenceId = 'Z_807'
        r = pf.exposure.RemoveExposureSubscription(ContextId, ReferenceId)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_CurrencyExposureMe(self, mock_req):
        """test the CurrencyExposureMe request."""
        tid = "_v3_CurrencyExposureMe"
        resp, data = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.CurrencyExposureMe()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_CurrencyExposureSpecific(self, mock_req):
        """test the CurrencyExposureSpecific request."""
        tid = "_v3_CurrencyExposureSpecific"
        resp, data, params = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.CurrencyExposureSpecific(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_FxSpotExposureMe(self, mock_req):
        """test the FxSpotExposureMe request."""
        tid = "_v3_FxSpotExposureMe"
        resp, data = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.FxSpotExposureMe()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_FxSpotExposureSpecific(self, mock_req):
        """test the FxSpotExposureSpecific request."""
        tid = "_v3_FxSpotExposureSpecific"
        resp, data, params = fetchTestData(pf.exposure.responses, tid)
        r = pf.exposure.FxSpotExposureSpecific(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
