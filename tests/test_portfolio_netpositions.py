# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_NetPositions(ReqMockTest):
    """Tests for `portfolio-netpositions` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_NetPositions, self).setUp()

    @parameterized.expand([
        (pf.netpositions, "SingleNetPosition",
                          {'NetPositionId': 'GBPCAD__FxSpot'}),
        (pf.netpositions, "SingleNetPositionDetails",
                          {'NetPositionId': 'GBPCAD__FxSpot'}),
        (pf.netpositions, "NetPositionsMe", {}),
        (pf.netpositions, "NetPositionsQuery", {}),
        (pf.netpositions, "NetPositionListSubscription", {}),
        (pf.netpositions, "NetPositionSubscriptionRemoveMultiple",
                          {'ContextId': 'explorer_1551702571343'}),
        (pf.netpositions, "NetPositionSubscriptionRemove",
                          {'ContextId': 'explorer_1551702571343',
                           'ReferenceId': 'C_702'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
