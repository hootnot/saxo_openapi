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


class TestSaxo_Trading_Orders(unittest.TestCase):
    """Tests for `trading-orders` endpoints."""

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
    def test__tr_Order(self, mock_req):
        """test the Order request."""
        tid = "_v3_Order"
        resp, data = fetchTestData(tr.orders.responses, tid)
        r = tr.orders.Order(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__tr_ChangeOrder(self, mock_req):
        """test the ChangeOrder request."""
        tid = "_v3_ChangeOrder"
        resp, data = fetchTestData(tr.orders.responses, tid)
        r = tr.orders.ChangeOrder(data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__tr_CancelOrders(self, mock_req):
        """test the CancelOrders request."""
        tid = "_v3_CancelOrders"
        resp, data, params = fetchTestData(tr.orders.responses, tid)
        r = tr.orders.CancelOrders(OrderIds="76289286", params=params)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__tr_PrecheckOrder(self, mock_req):
        """test the PrecheckOrder request."""
        tid = "_v3_PrecheckOrder"
        resp, data = fetchTestData(tr.orders.responses, tid)
        r = tr.orders.PrecheckOrder(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
