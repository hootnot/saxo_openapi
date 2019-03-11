#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment, mock_env, fetchTestData
from saxo_openapi import API
import saxo_openapi.endpoints.trading as tr
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_Trading_Prices(unittest.TestCase):
    """Tests for `trading-prices` endpoints."""

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
    def test__tr_CreatePriceSubscription(self, mock_req):
        """test the CreatePriceSubscription request."""
        tid = "_v3_CreatePriceSubscription"
        resp, data = fetchTestData(tr.prices.responses, tid)
        r = tr.prices.CreatePriceSubscription(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__tr_MarginImpactRequest(self, mock_req):
        """test the MarginImpactRequest request."""
        tid = "_v3_MarginImpactRequest"
        resp, data = fetchTestData(tr.prices.responses, tid)
        ContextId = "ctxt_20190311"
        ReferenceId = "EUR_USD"
        r = tr.prices.MarginImpactRequest(ContextId=ContextId,
                                          ReferenceId=ReferenceId)
        mock_req.register_uri('PUT',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__tr_PriceSubscriptionRemoveByTag(self, mock_req):
        """test the PriceSubscriptionRemoveByTag request."""
        tid = "_v3_PriceSubscriptionRemoveByTag"
        resp, data, params = fetchTestData(tr.prices.responses, tid)
        ContextId = 'ctxt_20190311'
        r = tr.prices.PriceSubscriptionRemoveByTag(
            ContextId=ContextId,
            params=params)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__tr_PriceSubscriptionRemove(self, mock_req):
        """test the PriceSubscriptionRemove request."""
        tid = "_v3_PriceSubscriptionRemove"
        resp, data = fetchTestData(tr.prices.responses, tid)
        ContextId = 'ctxt_20190311'
        ReferenceId = 'EUR_USD'
        r = tr.prices.PriceSubscriptionRemove(ContextId=ContextId,
                                              ReferenceId=ReferenceId)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()



