# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_ClosedPositions(ReqMockTest):
    """Tests for `portfolio-closedpositions` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_ClosedPositions, self).setUp()

    @parameterized.expand([
        (pf.closedpositions, "ClosedPositionList", {}),
        (pf.closedpositions, "ClosedPositionById",
                             {'ClosedPositionId': '212702698-212702774'}),
        (pf.closedpositions, "ClosedPositionDetails",
                             {'ClosedPositionId': '212702698-212702774'}),
        (pf.closedpositions, "ClosedPositionsMe", {}),
        (pf.closedpositions, "ClosedPositionSubscription", {}),
        (pf.closedpositions, "ClosedPositionSubscriptionUpdate",
                             {'ContextId': 'explorer_1551913039211',
                              'ReferenceId': 'D_975'}),
        (pf.closedpositions, "ClosedPositionSubscriptionsRemove",
                             {'ContextId': 29931122,
                              'params': {'Tag': 2345223}}),
        (pf.closedpositions, "ClosedPositionSubscriptionRemoveById",
         {'ContextId': 29931122,
          'ReferenceId': '0f8fad5b-d9cb-469f-a165-70867728950e'}),

      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
