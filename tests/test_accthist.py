#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment, mock_env, fetchTestData
from saxo_openapi import API
import saxo_openapi.endpoints.accounthistory as ah
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_AcctHist(unittest.TestCase):
    """Tests for `accounthistory` endpoints."""

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
    def test__ah_AccountSummary(self, mock_req):
        """test the AccountSummary request."""
        tid = "_v3_AccountSummary"
        resp, data, params = fetchTestData(ah.accountvalues.responses, tid)
        ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        r = ah.accountvalues.AccountSummary(ClientKey, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__ah_HistoricalPositions(self, mock_req):
        """test the HistoricalPositions request."""
        tid = "_v3_HistoricalPositions"
        resp, data, params = fetchTestData(ah.historicalpositions.responses,
                                           tid)
        ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        r = ah.historicalpositions.HistoricalPositions(ClientKey,
                                                       params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__ah_AccountPerformance(self, mock_req):
        """test the AccountPerformance request."""
        tid = "_v3_AccountPerformance"
        resp, data, params = fetchTestData(ah.performance.responses, tid)
        ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        r = ah.performance.AccountPerformance(ClientKey, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
