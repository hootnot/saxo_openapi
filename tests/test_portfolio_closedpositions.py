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


class TestSaxo_Portfolio_ClosedPositions(unittest.TestCase):
    """Tests for `portfolio-closedpositions` endpoints."""

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
    def test__pf_ClosedPositionList(self, mock_req):
        """test the ClosedPositionList request."""
        tid = "_v3_ClosedPositionList"
        resp, data, params = fetchTestData(pf.closedpositions.responses, tid)
        r = pf.closedpositions.ClosedPositionList(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClosedPositionById(self, mock_req):
        """test the ClosedPositionById request."""
        tid = "_v3_ClosedPositionById"
        resp, data, params = fetchTestData(pf.closedpositions.responses, tid)
        ClosedPositionId = '212702698-212702774'
        r = pf.closedpositions.ClosedPositionById(
                ClosedPositionId=ClosedPositionId,
                params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClosedPositionDetails(self, mock_req):
        """test the ClosedPositionDetails request."""
        tid = "_v3_ClosedPositionDetails"
        resp, data, params = fetchTestData(pf.closedpositions.responses, tid)
        ClosedPositionId = '212702698-212702774'
        r = pf.closedpositions.ClosedPositionDetails(
                ClosedPositionId=ClosedPositionId,
                params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClosedPositionsMe(self, mock_req):
        """test the ClosedPositionsMe request."""
        tid = "_v3_ClosedPositionsMe"
        resp, data, params = fetchTestData(pf.closedpositions.responses, tid)
        r = pf.closedpositions.ClosedPositionsMe(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClosedPositionSubscription(self, mock_req):
        """test the ClosedPositionSubscription request."""
        tid = "_v3_ClosedPositionSubscription"
        resp, data, params = fetchTestData(pf.closedpositions.responses, tid)
        r = pf.closedpositions.ClosedPositionSubscription(data=data, params=params)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code= r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_ClosedPositionSubscriptionUpdate(self, mock_req):
        """test the ClosedPositionSubscriptionUpdate request."""
        tid = "_v3_ClosedPositionSubscriptionUpdate"
        resp, data = fetchTestData(pf.closedpositions.responses, tid)
        ContextId = 'explorer_1551913039211'
        ReferenceId = 'D_975'
        r = pf.closedpositions.ClosedPositionSubscriptionUpdate(
                      ContextId=ContextId,
                      ReferenceId=ReferenceId,
                      data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code= r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
