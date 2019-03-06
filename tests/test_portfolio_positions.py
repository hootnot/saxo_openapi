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


class TestSaxo_Portfolio_Positions(unittest.TestCase):
    """Tests for `portfolio-positions` endpoints."""

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
    def test__pf_SinglePosition(self, mock_req):
        """test the SinglePosition request."""
        tid = "_v3_SinglePosition"
        resp, data, params = fetchTestData(pf.positions.responses, tid)
        PositionId = 212561926
        r = pf.positions.SinglePosition(PositionId=PositionId, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_SinglePositionDetails(self, mock_req):
        """test the SinglePositionDetails request."""
        tid = "_v3_SinglePositionDetails"
        resp, data, params = fetchTestData(pf.positions.responses, tid)
        PositionId = 212561926
        r = pf.positions.SinglePositionDetails(PositionId=PositionId,
                                               params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_PositionsMe(self, mock_req):
        """test the PositionsMe request."""
        tid = "_v3_PositionsMe"
        resp, data, params = fetchTestData(pf.positions.responses, tid)
        r = pf.positions.PositionsMe(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_PositionsQuery(self, mock_req):
        """test the PositionsQuery request."""
        tid = "_v3_PositionsQuery"
        resp, data, params = fetchTestData(pf.positions.responses, tid)
        r = pf.positions.PositionsQuery(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_PositionListSubscription(self, mock_req):
        """test the PositionListSubscription request."""
        tid = "_v3_PositionListSubscription"
        resp, data, params = fetchTestData(pf.positions.responses, tid)
        r = pf.positions.PositionListSubscription(data=data, params=params)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__pf_PositionSubscriptionPageSize(self, mock_req):
        """test the PositionSubscriptionPageSize request."""
        tid = "_v3_PositionSubscriptionPageSize"
        resp, data = fetchTestData(pf.positions.responses, tid)
        ContextId = 'explorer_1551702571343'
        ReferenceId = 'C_702'
        r = pf.positions.PositionSubscriptionPageSize(ContextId=ContextId,
                                                      ReferenceId=ReferenceId,
                                                      data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_PositionSubscriptionRemoveMultiple(self, mock_req):
        """test the PositionSubscriptionRemoveMultiple request."""
        tid = "_v3_PositionSubscriptionRemoveMultiple"
        resp, data, params = fetchTestData(pf.positions.responses, tid)
        ContextId = 'explorer_1551702571343'
        r = pf.positions.PositionSubscriptionRemoveMultiple(
            ContextId=ContextId,
            params=params)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__pf_PositionSubscriptionRemove(self, mock_req):
        """test the PositionSubscriptionRemove request."""
        tid = "_v3_PositionSubscriptionRemove"
        resp, data = fetchTestData(pf.positions.responses, tid)
        ContextId = 'explorer_1551702571343'
        ReferenceId = 'C_702'
        r = pf.positions.PositionSubscriptionRemove(ContextId=ContextId,
                                                    ReferenceId=ReferenceId)

        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
