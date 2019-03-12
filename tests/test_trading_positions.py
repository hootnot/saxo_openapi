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


class TestSaxo_Trading_Positions(unittest.TestCase):
    """Tests for `trading-positions` endpoints."""

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
    def test__tr_PositionByQuote(self, mock_req):
        """test the PositionByQuote request."""
        tid = "_v3_PositionByQuote"
        resp, data = fetchTestData(tr.positions.responses, tid)
        r = tr.positions.PositionByQuote(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__tr_UpdatePosition(self, mock_req):
        """test the UpdatePosition request."""
        tid = "_v3_UpdatePosition"
        resp, data = fetchTestData(tr.positions.responses, tid)
        PositionId = 1019942426
        r = tr.positions.UpdatePosition(PositionId=PositionId, data=data)
        mock_req.register_uri('PATCH',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__tr_ExercisePosition(self, mock_req):
        """test the ExercisePosition request."""
        tid = "_v3_ExercisePosition"
        resp, data = fetchTestData(tr.positions.responses, tid)
        PositionId = 1019942426
        r = tr.positions.ExercisePosition(PositionId=PositionId, data=data)
        mock_req.register_uri('PUT',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__tr_ExerciseAmount(self, mock_req):
        """test the ExerciseAmount request."""
        tid = "_v3_ExerciseAmount"
        resp, data = fetchTestData(tr.positions.responses, tid)
        PositionId = 1019942426
        r = tr.positions.ExerciseAmount(data=data)
        mock_req.register_uri('PUT',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)


if __name__ == "__main__":

    unittest.main()
