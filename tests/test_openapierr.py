# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

from .unittestsetup import ReqMockTest
from saxo_openapi.exceptions import OpenAPIError


class TestSaxo_Exceptions(ReqMockTest):
    """Tests for exceptions."""

    def setUp(self):
        super(TestSaxo_Exceptions, self).setUp()

    def test_openapierr(self):
        err = OpenAPIError(401, "Unauthorized", "xxx")

        self.assertTrue(err.content == 'xxx' and
                        err.code == 401 and
                        err.reason == 'Unauthorized')
