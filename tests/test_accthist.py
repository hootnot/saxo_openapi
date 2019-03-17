#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from parameterized import parameterized
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.accounthistory as ah


class TestSaxo_AcctHist(ReqMockTest):
    """Tests for `accounthistory` endpoints."""

    def setUp(self):
        super(TestSaxo_AcctHist, self).setUp()

    @parameterized.expand([
        (ah.accountvalues, "AccountSummary",
         {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
        (ah.historicalpositions, "HistoricalPositions",
         {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
        (ah.performance, "AccountPerformance",
         {'ClientKey': 'Cf4xZWiYL6W1nMKpygBLLA=='}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
