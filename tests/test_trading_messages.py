# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.trading as tr
from parameterized import parameterized


class TestSaxo_Trading_Messages(ReqMockTest):
    """Tests for `trading-messages` endpoints."""

    def setUp(self):
        super(TestSaxo_Trading_Messages, self).setUp()

    @parameterized.expand([
        (tr.messages, "GetTradeMessages", {}),
        (tr.messages, "MarkMessageAsSeen",
                      {'MessageId': '345322'}),
        (tr.messages, "CreateTradeMessageSubscription", {}),
        (tr.messages, "RemoveTradeMessageSubscriptionById",
                      {
                       "ContextId": "ctxt_20190318",
                       "ReferenceId": "M452"
                      }),
        (tr.messages, "RemoveTradeMessageSubscriptions",
                      {
                       "ContextId": "ctxt_20190318",
                      })
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
