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


class TestSaxo_Portfolio_Acctgrps(unittest.TestCase):
    """Tests for `portfolio-accountgroups` endpoints."""

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
    def test__pf_AccountGroupDetails(self, mock_req):
        """test the AccountGroupDetails request."""
        tid = "_v3_AccountGroupDetails"
        resp, data, params = fetchTestData(pf.accountgroups.responses, tid)
        AGK = 'Cf4xZWiYL6W1nMKpygBLLA=='
        r = pf.accountgroups.AccountGroupDetails(AccountGroupKey=AGK,
                                                 params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_AccountGroupsMe(self, mock_req):
        """test the AccountGroupsMe request."""
        tid = "_v3_AccountGroupsMe"
        resp, data, params = fetchTestData(pf.accountgroups.responses, tid)
        r = pf.accountgroups.AccountGroupsMe(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_AccountGroupsList(self, mock_req):
        """test the AccountGroupsList request."""
        tid = "_v3_AccountGroupsList"
        resp, data, params = fetchTestData(pf.accountgroups.responses, tid)
        r = pf.accountgroups.AccountGroupsList(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_accountgrp_update(self, mock_req):
        """test the AccountGroupUpdate request."""
        tid = "_v3_AccountGroupUpdate"
        resp, data, params = fetchTestData(pf.accountgroups.responses, tid)
        AGK = 'Cf4xZWiYL6W1nMKpygBLLA=='
        r = pf.accountgroups.AccountGroupUpdate(AccountGroupKey=AGK,
                                                params=params,
                                                data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
