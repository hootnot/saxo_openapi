#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment, mock_env, fetchTestData
from saxo_openapi import API
import saxo_openapi.endpoints.referencedata as rd
import requests_mock

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

access_token = None
api = None


class TestSaxo_Referencedata(unittest.TestCase):
    """Tests for `referencedata` endpoints."""

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
    def test__rd_algostrategies(self, mock_req):
        """test the AlgoStrategies request."""
        tid = "_v3_algostrategies"
        resp, data, params = fetchTestData(rd.algostrategies.responses, tid)
        r = rd.algostrategies.AlgoStrategies(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_algostrategydetails(self, mock_req):
        """test the AlgoStrategyDetails request."""
        tid = "_v3_algostrategybyname"
        resp, data = fetchTestData(rd.algostrategies.responses, tid)
        Name = "Implementation%20Shortfall"
        r = rd.algostrategies.AlgoStrategyDetails(Name=Name)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_countries(self, mock_req):
        """test the Countries request."""
        tid = "_v3_countries"
        resp, data = fetchTestData(rd.countries.responses, tid)
        r = rd.countries.Countries()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_cultures(self, mock_req):
        """test the Cultures request."""
        tid = "_v3_cultures"
        resp, data = fetchTestData(rd.cultures.responses, tid)
        r = rd.cultures.Cultures()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_currencies(self, mock_req):
        """test the Currencies request."""
        tid = "_v3_currencies"
        resp, data = fetchTestData(rd.currencies.responses, tid)
        r = rd.currencies.Currencies()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_exchangelist(self, mock_req):
        """test the ExchangeList request."""
        tid = "_v3_exchangelist"
        resp, data = fetchTestData(rd.exchanges.responses, tid)
        r = rd.exchanges.ExchangeList()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_exchangedetails(self, mock_req):
        """test the ExchangeDetails request."""
        tid = "_v3_exchangedetails"
        resp, data = fetchTestData(rd.exchanges.responses, tid)
        r = rd.exchanges.ExchangeDetails(ExchangeId="NYSE_ARCA")
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_languages(self, mock_req):
        """test the Languages request."""
        tid = "_v3_languages"
        resp, data = fetchTestData(rd.languages.responses, tid)
        r = rd.languages.Languages()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_forwardtenordates(self, mock_req):
        """test the ForwardTenorDates request."""
        tid = "_v3_forwardtenordt"
        resp, data, params = fetchTestData(rd.standarddates.responses, tid)
        r = rd.standarddates.ForwardTenorDates(Uic=22, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_fxoptionexpirydt(self, mock_req):
        """test the FXOptionExpiryDates request."""
        tid = "_v3_fxoptionexpirydt"
        resp, data = fetchTestData(rd.standarddates.responses, tid)
        r = rd.standarddates.FXOptionExpiryDates(Uic=22)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_timezones(self, mock_req):
        """test the TimeZones request."""
        tid = "_v3_timezones"
        resp, data = fetchTestData(rd.timezones.responses, tid)
        r = rd.timezones.TimeZones()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_instruments(self, mock_req):
        """test the Instruments request."""
        tid = "_v3_instruments"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.Instruments(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_instrumentsdetails(self, mock_req):
        """test the InstrumentsDetails request."""
        tid = "_v3_instrumentsdetails"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.InstrumentsDetails(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_instrumentdetails(self, mock_req):
        """test the InstrumentDetails request."""
        tid = "_v3_instrumentdetails"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.InstrumentDetails(Uic=23,
                                             AssetType="FxForwards",
                                             params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
