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


class TestSaxo_Portfolio_Balances(unittest.TestCase):
    """Tests for `portfolio-balances` endpoints."""

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
    def test__pf_AccountBalancesMe(self, mock_req):
        """test the AccountBalancesMe request."""
        tid = "_v3_AccountBalancesMe"
        resp, data = fetchTestData(pf.balances.responses, tid)
        r = pf.balances.AccountBalancesMe()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_AccountBalances(self, mock_req):
        """test the AccountBalances request."""
        tid = "_v3_AccountBalances"
        resp, data, params = fetchTestData(pf.balances.responses, tid)
        r = pf.balances.AccountBalances(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_MarginOverview(self, mock_req):
        """test the MarginOverview request."""
        tid = "_v3_MarginOverview"
        resp, data, params = fetchTestData(pf.balances.responses, tid)
        r = pf.balances.MarginOverview(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_BalanceSubscriptionCreate(self, mock_req):
        """test the BalanceSubscriptionCreate request."""
        tid = "_v3_BalanceSubscriptionCreate"
        resp, data = fetchTestData(pf.balances.responses, tid)
        r = pf.balances.BalanceSubscriptionCreate(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_BalanceSubscriptionRemoveByTag(self, mock_req):
        """test the BalanceSubscriptionRemoveByTag request."""
        tid = "_v3_BalanceSubscriptionRemoveByTag"
        resp, data, params = fetchTestData(pf.balances.responses, tid)
        ContextId = "explorer_1551792578055"
        r = pf.balances.BalanceSubscriptionRemoveByTag(ContextId=ContextId,
                                                       params=params)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_BalanceSubscriptionRemoveById(self, mock_req):
        """test the BalanceSubscriptionRemoveById request."""
        tid = "_v3_BalanceSubscriptionRemoveById"
        resp, data = fetchTestData(pf.balances.responses, tid)
        ContextId = "explorer_1551792578055"
        ReferenceId = "O_697"
        r = pf.balances.BalanceSubscriptionRemoveById(ContextId=ContextId,
                                                      ReferenceId=ReferenceId)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
