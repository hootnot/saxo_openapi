#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment, mock_env, fetchTestData
from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_RootServices_Features(unittest.TestCase):
    """Tests for `rootservices-features` endpoints."""

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
    def test__ft_Availability(self, mock_req):
        """test the Availability request."""
        r = rs.features.Availability()
        tid = "_v3_Availability"
        resp, data = fetchTestData(rs.features.responses, tid)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__ft_CreateAvailabilitySubscription(self, mock_req):
        """test the CreateAvailabilitySubscription Subscription request."""
        tid = "_v3_CreateAvailabilitySubscription"
        resp, data = fetchTestData(rs.features.responses, tid)
        r = rs.features.CreateAvailabilitySubscription(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__ft_RemoveAvailabilitySubscription(self, mock_req):
        """test the RemoveAvailabilitySubscription request."""
        tid = "_v3_RemoveAvailabilitySubscription"
        resp, data, params = fetchTestData(rs.features.responses, tid)
        r = rs.features.RemoveAvailabilitySubscription(**params)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
