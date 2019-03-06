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


class TestSaxo_Portfolio_NetPositions(unittest.TestCase):
    """Tests for `portfolio-netpositions` endpoints."""

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
    def test__pf_SingleNetPosition(self, mock_req):
        """test the SingleNetPosition request."""
        tid = "_v3_SingleNetPosition"
        resp, data, params = fetchTestData(pf.netpositions.responses, tid)
        NetPositionId = "GBPCAD__FxSpot"
        r = pf.netpositions.SingleNetPosition(NetPositionId=NetPositionId,
                                              params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_SingleNetPositionDetails(self, mock_req):
        """test the SingleNetPositionDetails request."""
        tid = "_v3_SingleNetPositionDetails"
        resp, data, params = fetchTestData(pf.netpositions.responses, tid)
        NetPositionId = "GBPCAD__FxSpot"
        r = pf.netpositions.SingleNetPositionDetails(
               NetPositionId=NetPositionId,
               params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_NetPositionsMe(self, mock_req):
        """test the NetPositionsMe request."""
        tid = "_v3_NetPositionsMe"
        resp, data, params = fetchTestData(pf.netpositions.responses, tid)
        r = pf.netpositions.NetPositionsMe(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_NetPositionsQuery(self, mock_req):
        """test the NetPositionsQuery request."""
        tid = "_v3_NetPositionsQuery"
        resp, data, params = fetchTestData(pf.netpositions.responses, tid)
        r = pf.netpositions.NetPositionsQuery(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_NetPositionListSubscription(self, mock_req):
        """test the NetPositionListSubscription request."""
        tid = "_v3_NetPositionListSubscription"
        resp, data = fetchTestData(pf.netpositions.responses, tid)
        r = pf.netpositions.NetPositionListSubscription(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_positionsubscriptionremovemultiple(self, mock_req):
        """test the NetPositionSubscriptionRemoveMultiple request."""
        tid = "_v3_NetPositionSubscriptionRemoveMultiple"
        resp, data, params = fetchTestData(pf.netpositions.responses, tid)
        ContextId = 'explorer_1551702571343'
        r = pf.netpositions.NetPositionSubscriptionRemoveMultiple(
            ContextId=ContextId,
            params=params)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_positionsubscriptionremove(self, mock_req):
        """test the NetPositionSubscriptionRemove request."""
        tid = "_v3_NetPositionSubscriptionRemove"
        resp, data = fetchTestData(pf.netpositions.responses, tid)
        ContextId = 'explorer_1551702571343'
        ReferenceId = 'C_702'
        r = pf.netpositions.NetPositionSubscriptionRemove(
           ContextId=ContextId,
           ReferenceId=ReferenceId)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
