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
    def test__rd_AlgoStrategies(self, mock_req):
        """test the AlgoStrategies request."""
        tid = "_v3_AlgoStrategies"
        resp, data, params = fetchTestData(rd.algostrategies.responses, tid)
        r = rd.algostrategies.AlgoStrategies(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_AlgoStrategyDetails(self, mock_req):
        """test the AlgoStrategyDetails request."""
        tid = "_v3_AlgoStrategyDetails"
        resp, data = fetchTestData(rd.algostrategies.responses, tid)
        Name = "Implementation%20Shortfall"
        r = rd.algostrategies.AlgoStrategyDetails(Name=Name)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_Countries(self, mock_req):
        """test the Countries request."""
        tid = "_v3_Countries"
        resp, data = fetchTestData(rd.countries.responses, tid)
        r = rd.countries.Countries()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_Cultures(self, mock_req):
        """test the Cultures request."""
        tid = "_v3_Cultures"
        resp, data = fetchTestData(rd.cultures.responses, tid)
        r = rd.cultures.Cultures()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_Currencies(self, mock_req):
        """test the Currencies request."""
        tid = "_v3_Currencies"
        resp, data = fetchTestData(rd.currencies.responses, tid)
        r = rd.currencies.Currencies()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_ExchangeList(self, mock_req):
        """test the ExchangeList request."""
        tid = "_v3_ExchangeList"
        resp, data = fetchTestData(rd.exchanges.responses, tid)
        r = rd.exchanges.ExchangeList()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_ExchangeDetails(self, mock_req):
        """test the ExchangeDetails request."""
        tid = "_v3_ExchangeDetails"
        resp, data = fetchTestData(rd.exchanges.responses, tid)
        r = rd.exchanges.ExchangeDetails(ExchangeId="NYSE_ARCA")
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_Languages(self, mock_req):
        """test the Languages request."""
        tid = "_v3_Languages"
        resp, data = fetchTestData(rd.languages.responses, tid)
        r = rd.languages.Languages()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_ForwardTenorDates(self, mock_req):
        """test the ForwardTenorDates request."""
        tid = "_v3_ForwardTenorDates"
        resp, data, params = fetchTestData(rd.standarddates.responses, tid)
        r = rd.standarddates.ForwardTenorDates(Uic=22, params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_FXOptionExpiryDates(self, mock_req):
        """test the FXOptionExpiryDates request."""
        tid = "_v3_FXOptionExpiryDates"
        resp, data = fetchTestData(rd.standarddates.responses, tid)
        r = rd.standarddates.FXOptionExpiryDates(Uic=22)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_Timezones(self, mock_req):
        """test the TimeZones request."""
        tid = "_v3_Timezones"
        resp, data = fetchTestData(rd.timezones.responses, tid)
        r = rd.timezones.TimeZones()
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_Instruments(self, mock_req):
        """test the Instruments request."""
        tid = "_v3_Instruments"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.Instruments(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_InstrumentsDetails(self, mock_req):
        """test the InstrumentsDetails request."""
        tid = "_v3_InstrumentsDetails"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.InstrumentsDetails(params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_InstrumentDetails(self, mock_req):
        """test the InstrumentDetails request."""
        tid = "_v3_InstrumentDetails"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.InstrumentDetails(Uic=23,
                                             AssetType="FxForwards",
                                             params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_ContractoptionSpaces(self, mock_req):
        """test the ContractoptionSpaces request."""
        tid = "_v3_ContractoptionSpaces"
        resp, data, params = fetchTestData(rd.instruments.responses, tid)
        OptionRootId = 231
        r = rd.instruments.ContractoptionSpaces(OptionRootId=OptionRootId,
                                                params=params)
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__rd_TradingSchedule(self, mock_req):
        """test the TradingSchedule request."""
        tid = "_v3_TradingSchedule"
        resp, data = fetchTestData(rd.instruments.responses, tid)
        r = rd.instruments.TradingSchedule(Uic=21,
                                           AssetType="FxSpot")
        mock_req.register_uri('GET',
                              "{}/sim/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
