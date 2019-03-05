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


class TestSaxo_Portfolio_Clients(unittest.TestCase):
    """Tests for `portfolio-clients` endpoints."""

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
    def test__pf_ClientDetailsMe(self, mock_req):
        """test the ClientDetailsMe request."""
        tid = "_v3_ClientDetailsMe"
        resp, data = fetchTestData(pf.clients.responses, tid)
        r = pf.clients.ClientDetailsMe()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClientDetails(self, mock_req):
        """test the ClientDetails request."""
        tid = "_v3_ClientDetails"
        resp, data = fetchTestData(pf.clients.responses, tid)
        ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        r = pf.clients.ClientDetails(ClientKey=ClientKey)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClientDetailsUpdate(self, mock_req):
        """test the ClientDetailsUpdate request."""
        tid = "_v3_ClientDetailsUpdate"
        resp, data = fetchTestData(pf.clients.responses, tid)
        r = pf.clients.ClientDetailsUpdate(data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_ClientDetailsByOwner(self, mock_req):
        """test the ClientDetailsByOwner request."""
        tid = "_v3_ClientDetailsByOwner"
        resp, data, params = fetchTestData(pf.clients.responses, tid)
        r = pf.clients.ClientDetailsByOwner(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClientSwitchPosNettingMode(self, mock_req):
        """test the ClientSwitchPosNettingMode request."""
        tid = "_v3_ClientSwitchPosNettingMode"
        resp, data, params = fetchTestData(pf.clients.responses, tid)
        r = pf.clients.ClientSwitchPosNettingMode(params=params, data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
