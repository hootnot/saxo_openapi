# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.rootservices as rs
from parameterized import parameterized


class TestSaxo_RootServices_Sessions(ReqMockTest):

    def setUp(self):
        super(TestSaxo_RootServices_Sessions, self).setUp()

    @parameterized.expand([
        (rs.sessions, "GetSessionCapabilities", {}),
        (rs.sessions, "ChangeSessionCapabilities", {}),
        (rs.sessions, "CreateSessionCapabilitiesSubscription", {}),
        (rs.sessions, "RemoveSessionCapabilitiesSubscription",
                      {'ContextId': '20180204125301453',
                       'ReferenceId': 'C03'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test__ft_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
