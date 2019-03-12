#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment, mock_env, fetchTestData
from saxo_openapi import API
import saxo_openapi.endpoints.valueadd as va
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_Valueadd_PriceAlerts(unittest.TestCase):
    """Tests for `valueadd-pricealerts` endpoints."""

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
    def test__va_GetAllAlerts(self, mock_req):
        """test the GetAllAlerts request."""
        tid = "_v3_GetAllAlerts"
        resp, data, params = fetchTestData(va.pricealerts.responses, tid)
        r = va.pricealerts.GetAllAlerts(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__va_GetAlertDefinition(self, mock_req):
        """test the GetAlertDefinition request."""
        tid = "_v3_GetAlertDefinition"
        resp, data = fetchTestData(va.pricealerts.responses, tid)
        AlertDefinitionId = 30834
        r = va.pricealerts.GetAlertDefinition(AlertDefinitionId)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__va_CreatePriceAlert(self, mock_req):
        """test the CreatePriceAlert request."""
        tid = "_v3_CreatePriceAlert"
        resp, data = fetchTestData(va.pricealerts.responses, tid)
        r = va.pricealerts.CreatePriceAlert(data=data)
        mock_req.register_uri('POST',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__va_UpdatePriceAlert(self, mock_req):
        """test the UpdatePriceAlert request."""
        tid = "_v3_UpdatePriceAlert"
        resp, data = fetchTestData(va.pricealerts.responses, tid)
        AlertDefinitionId = 30834
        r = va.pricealerts.UpdatePriceAlert(AlertDefinitionId, data=data)
        mock_req.register_uri('PUT',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__va_DeletePriceAlert(self, mock_req):
        """test the DeletePriceAlert request."""
        tid = "_v3_DeletePriceAlert"
        resp, data = fetchTestData(va.pricealerts.responses, tid)
        AlertDefinitionIds = "30834,30386"
        r = va.pricealerts.DeletePriceAlert(AlertDefinitionIds)
        mock_req.register_uri('DELETE',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)

    @requests_mock.Mocker()
    def test__va_GetUserNotificationSettings(self, mock_req):
        """test the GetUserNotificationSettings request."""
        tid = "_v3_GetUserNotificationSettings"
        resp, data = fetchTestData(va.pricealerts.responses, tid)
        r = va.pricealerts.GetUserNotificationSettings()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        rv = api.request(r)
        self.assertTrue(rv == resp)

    @requests_mock.Mocker()
    def test__va_ModifyUserNotificationSettings(self, mock_req):
        """test the ModifyUserNotificationSettings request."""
        tid = "_v3_ModifyUserNotificationSettings"
        resp, data = fetchTestData(va.pricealerts.responses, tid)
        r = va.pricealerts.ModifyUserNotificationSettings(data=data)
        mock_req.register_uri('PUT',
                              "{}/sim/{}".format(api.api_url, r),
                              status_code=r.expected_status)
        api.request(r)
        self.assertTrue(r.status_code == r.expected_status)


if __name__ == "__main__":

    unittest.main()
