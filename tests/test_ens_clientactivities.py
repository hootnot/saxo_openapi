# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.eventnotificationservices as ens
from parameterized import parameterized


class TestSaxo_Trading_Orders(ReqMockTest):
    """Tests for `ens-clientactivities` endpoints."""

    def setUp(self):
        super(TestSaxo_Trading_Orders, self).setUp()

    @parameterized.expand([
        (ens.clientactivities, "CreateSubscriptionForClientEvents", {}),
        (ens.clientactivities, "RemoveSubscription", {}),
        (ens.clientactivities, "RemoveSubscriptions", {}),
        (ens.clientactivities, "GetActivities", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
