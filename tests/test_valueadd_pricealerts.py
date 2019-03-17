# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.valueadd as va
from parameterized import parameterized


class TestSaxo_Valueadd_PriceAlerts(ReqMockTest):
    """Tests for `valueadd-pricealerts` endpoints."""

    def setUp(self):
        super(TestSaxo_Valueadd_PriceAlerts, self).setUp()

    @parameterized.expand([
        (va.pricealerts, "GetAllAlerts", {}),
        (va.pricealerts, "GetAlertDefinition",
                         {'AlertDefinitionId': 30834}),
        (va.pricealerts, "CreatePriceAlert", {}),
        (va.pricealerts, "UpdatePriceAlert",
                         {'AlertDefinitionId': 30834}),
        (va.pricealerts, "DeletePriceAlert",
                         {'AlertDefinitionIds': "30834,30386"}),
        (va.pricealerts, "GetUserNotificationSettings", {}),
        (va.pricealerts, "ModifyUserNotificationSettings", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
