# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.chart as ch
from parameterized import parameterized


class TestSaxo_Chart_Charts(ReqMockTest):
    """Tests for `chart-charts` endpoints."""

    def setUp(self):
        super(TestSaxo_Chart_Charts, self).setUp()

    @parameterized.expand([
        (ch.charts, "GetChartData", {}),
        (ch.charts, "CreateChartDataSubscription",
            {"data": {
               "Arguments": {
                   "AssetType": "FxSpot",
                   "Count": 2,
                   "Horizon": 1,
                   "Uic": 21
               },
               "ContextId": "20190830035501020",
               "Format": "application/json",
               "ReferenceId": "UIC_21",
               "RefreshRate": 1000
            }}),
        (ch.charts, "ChartDataRemoveSubscriptions",
            {'ContextId': 'ctxt_20190311'}),
        (ch.charts, "ChartDataRemoveSubscription",
            {'ContextId': 'ctxt_20190311',
             'ReferenceId': 'UIC_21'})
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
