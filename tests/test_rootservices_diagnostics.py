# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.rootservices as rs
from parameterized import parameterized


class TestSaxo_RootServices_Diagnostics(ReqMockTest):
    """Tests for `rootservices-diagnostics` endpoints."""

    def setUp(self):
        super(TestSaxo_RootServices_Diagnostics, self).setUp()

    @parameterized.expand([
        (rs.diagnostics, "Get", {}),
        (rs.diagnostics, "Post", {}),
        (rs.diagnostics, "Put", {}),
        (rs.diagnostics, "Delete", {}),
        (rs.diagnostics, "Patch", {}),
        (rs.diagnostics, "Head", {}),
        (rs.diagnostics, "Options", {}),
        (rs.diagnostics, "Echo", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
