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


class TestSaxo_Portfolio_Orders(unittest.TestCase):
    """Tests for `portfolio-orders` endpoints."""

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
    def test__pf_GetOpenOrder(self, mock_req):
        """test the GetOpenOrder request."""
        tid = "_v3_GetOpenOrder"
        resp, data, params = fetchTestData(pf.orders.responses, tid)
        ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        OrderId = '76332324'
        r = pf.orders.GetOpenOrder(ClientKey, OrderId, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_GetOpenOrdersMe(self, mock_req):
        """test the GetOpenOrdersMe request."""
        tid = "_v3_GetOpenOrdersMe"
        resp, data, params = fetchTestData(pf.orders.responses, tid)
        r = pf.orders.GetOpenOrdersMe(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_OrderDetails(self, mock_req):
        """test the OrderDetails request."""
        tid = "_v3_OrderDetails"
        resp, data, params = fetchTestData(pf.orders.responses, tid)
        OrderId = '76332324'
        r = pf.orders.OrderDetails(OrderId=OrderId, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_GetAllOpenOrders(self, mock_req):
        """test the GetAllOpenOrders request."""
        tid = "_v3_GetAllOpenOrders"
        resp, data, params = fetchTestData(pf.orders.responses, tid)
        r = pf.orders.GetAllOpenOrders(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_CreateOpenOrdersSubscription(self, mock_req):
        """test the CreateOpenOrdersSubscription request."""
        tid = "_v3_CreateOpenOrdersSubscription"
        resp, data = fetchTestData(pf.orders.responses, tid)
        r = pf.orders.CreateOpenOrdersSubscription(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_RemoveOpenOrderSubscriptionsByTag(self, mock_req):
        """test the RemoveOpenOrderSubscriptionsByTag request."""
        tid = "_v3_RemoveOpenOrderSubscriptionsByTag"
        resp, data, params = fetchTestData(pf.orders.responses, tid)
        ContextId = 'explorer_1552035128308'
        r = pf.orders.RemoveOpenOrderSubscriptionsByTag(
            ContextId=ContextId,
            params=params)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_RemoveOpenOrderSubscription(self, mock_req):
        """test the RemoveOpenOrderSubscription request."""
        tid = "_v3_RemoveOpenOrderSubscription"
        resp, data = fetchTestData(pf.orders.responses, tid)
        ContextId = 'explorer_1552035128308'
        ReferenceId = 'C_582'
        r = pf.orders.RemoveOpenOrderSubscription(ContextId=ContextId,
                                                  ReferenceId=ReferenceId)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
