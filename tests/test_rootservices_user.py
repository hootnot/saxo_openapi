#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import unittest
import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.rootservices as rs
from parameterized import parameterized


class TestSaxo_RootServices_User(ReqMockTest):

    def setUp(self):
        super(TestSaxo_RootServices_User, self).setUp()

    @parameterized.expand([
        (rs.user, "User", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test__ft_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)


if __name__ == "__main__":

    unittest.main()
