# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.referencedata as rd
from parameterized import parameterized


class TestSaxo_Referencedata(ReqMockTest):
    """Tests for `referencedata` endpoints."""

    def setUp(self):
        super(TestSaxo_Referencedata, self).setUp()

    @parameterized.expand([
        (rd.algostrategies, "AlgoStrategies", {}),
        (rd.algostrategies, "AlgoStrategyDetails",
         {'Name': 'Implementation%20Shortfall'}),
        (rd.countries, "Countries", {}),
        (rd.cultures, "Cultures", {}),
        (rd.currencies, "Currencies", {}),
        (rd.exchanges, "ExchangeList", {}),
        (rd.exchanges, "ExchangeDetails", {'ExchangeId': 'NYSE_ARCA'}),
        (rd.languages, "Languages", {}),
        (rd.standarddates, "ForwardTenorDates", {'Uic': 22}),
        (rd.standarddates, "FXOptionExpiryDates", {'Uic': 22}),
        (rd.timezones, "TimeZones", {}),
        (rd.instruments, "Instruments", {}),
        (rd.instruments, "InstrumentsDetails", {}),
        (rd.instruments, "InstrumentDetails", {'Uic': 23,
                                               'AssetType': 'FxForwards'}),
        (rd.instruments, "ContractoptionSpaces", {'OptionRootId': 231}),
        (rd.instruments, "FuturesSpaces", {'ContinuousFuturesUic': 28016}),
        (rd.instruments, "TradingSchedule", {'Uic': 21, 'AssetType': 'Spot'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
