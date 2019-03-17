# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.trading as tr
from parameterized import parameterized


class TestSaxo_Trading_Positions(ReqMockTest):
    """Tests for `trading-positions` endpoints."""

    def setUp(self):
        super(TestSaxo_Trading_Positions, self).setUp()

    @parameterized.expand([
        (tr.positions, "PositionByQuote", {}),
        (tr.positions, "UpdatePosition", {'PositionId': '1019942426'}),
        (tr.positions, "ExercisePosition", {'PositionId': '1019942426'}),
        (tr.positions, "ExerciseAmount", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
