# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.portfolio as pf
from parameterized import parameterized


class TestSaxo_Portfolio_Positions(ReqMockTest):
    """Tests for `portfolio-positions` endpoints."""

    def setUp(self):
        super(TestSaxo_Portfolio_Positions, self).setUp()

    @parameterized.expand([
        (pf.positions, "SinglePosition", {'PositionId': 212561926}),
        (pf.positions, "SinglePositionDetails", {'PositionId': 212561926}),
        (pf.positions, "PositionsMe", {}),
        (pf.positions, "PositionsQuery", {}),
        (pf.positions, "PositionListSubscription", {}),
        (pf.positions, "PositionSubscriptionPageSize",
                       {'ContextId': 'explorer_1551702571343',
                        'ReferenceId': 'C_702'}),
        (pf.positions, "PositionSubscriptionRemoveMultiple",
                       {'ContextId': 'explorer_1551702571343'}),
        (pf.positions, "PositionSubscriptionRemove",
                       {'ContextId': 'explorer_1551702571343',
                        'ReferenceId': 'C_702'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
