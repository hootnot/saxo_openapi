# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Exposure(ReqMockTest):
    """Tests for `portfolio-exposure` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Exposure, self).setUp()

    @parameterized.expand([
        (pf.exposure, "NetInstrumentsExposureMe", {}),
        (pf.exposure, "NetInstrumentExposureSpecific", {}),
        (pf.exposure, "CreateExposureSubscription", {}),
        (pf.exposure, "RemoveExposureSubscriptionsByTag",
                      {'ContextId': 'explorer_1552035128308'}),
        (pf.exposure, "RemoveExposureSubscription",
                      {'ContextId': 'explorer_1552035128308',
                       'ReferenceId': 'Z_807'}),
        (pf.exposure, "CurrencyExposureMe", {}),
        (pf.exposure, "CurrencyExposureSpecific", {}),
        (pf.exposure, "FxSpotExposureMe", {}),
        (pf.exposure, "FxSpotExposureSpecific", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
