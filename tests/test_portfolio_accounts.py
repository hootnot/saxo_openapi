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


class TestSaxo_RootServices_Features(unittest.TestCase):
    """Tests for `portfolio-accounts` endpoints."""

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
    def test__pf_accountdetails(self, mock_req):
        """test the AccountDetails request."""
        tid = "_v3_acctdetails"
        resp, data, params = fetchTestData(pf.accounts.responses, tid)
        r = pf.accounts.AccountDetails(**params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_accountlist(self, mock_req):
        """test the AccountList request."""
        tid = "_v3_acctlist"
        resp, data = fetchTestData(pf.accounts.responses, tid)
        r = pf.accounts.AccountList()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_accountlistbyclient(self, mock_req):
        """test the AccountListByClient request."""
        tid = "_v3_acctlistbyclient"
        resp, data, params = fetchTestData(pf.accounts.responses, tid)
        r = pf.accounts.AccountListByClient(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_accountupdate(self, mock_req):
        """test the AccountUpdate request."""
        tid = "_v3_acctupdate"
        AccountKey = "Cf4xZWiYL6W1nMKpygBLLA=="
        resp, data = fetchTestData(pf.accounts.responses, tid)
        r = pf.accounts.AccountUpdate(AccountKey=AccountKey, data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_accountsubscr_create(self, mock_req):
        """test the SubscriptionCreate request."""
        tid = "_v3_acctsubscrcreate"
        resp, data = fetchTestData(pf.accounts.responses, tid)
        r = pf.accounts.SubscriptionCreate(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_accountsubscr_rembytag(self, mock_req):
        """test the SubscriptionRemoveByTag request."""
        # tid = "_v3_acctsubscrrembytag"
        # resp, data = fetchTestData(pf.accounts.responses, tid)
        ContextId = 'explorer_1551455553043'
        params = {'Tag': 'SomeTag'}
        r = pf.accounts.SubscriptionRemoveByTag(ContextId, params=params)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_accountsubscr_rembyid(self, mock_req):
        """test the SubscriptionRemoveById request."""
        # tid = "_v3_acctsubscrrembytag"
        # resp, data = fetchTestData(pf.accounts.responses, tid)
        ContextId = 'explorer_1551455553043'
        ReferenceId = 'Z_721'
        r = pf.accounts.SubscriptionRemoveByTag(ContextId, ReferenceId)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
