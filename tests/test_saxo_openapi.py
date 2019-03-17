# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
from .unittestsetup import environment as environment, ReqMockTest
from saxo_openapi import API


class Test__saxo_openapi(ReqMockTest):
    """Tests for `saxo_openapi` package."""

    def setUp(self):
        super(Test__saxo_openapi, self).setUp()

    def test__saxo_environment(self):
        """test the exception on a faulty environment."""
        with self.assertRaises(KeyError) as envErr:
            API(environment="faulty", access_token=self.access_token)

        self.assertTrue("Unknown environment" in "{}".format(envErr.exception))

    def test__requests_params(self):
        """request parameters."""
        request_params = {"timeout": 10}
        api = API(environment=environment,
                  access_token=self.access_token,
                  request_params=request_params)
        self.assertTrue(api.request_params == request_params)

    def test__requests_exception(self):
        """force a requests exception."""
        from requests.exceptions import RequestException
        import saxo_openapi.endpoints.portfolio as pf
        setattr(sys.modules["saxo_openapi.saxo_openapi"],
                "TRADING_ENVIRONMENTS",
                {"simulation": {
                 "stream": "ttps://test.com",
                 "api": "ttps://test.com",
                 "prefix": "sim"
                 }})
        api = API(environment=environment, access_token=self.access_token)
        text = "No connection " \
               "adapters were found for " \
               "'ttps://test.com/sim/openapi/port/v1/accounts/me'"
        r = pf.accounts.AccountsMe()
        with self.assertRaises(RequestException) as oErr:
            api.request(r)

        self.assertEqual("{}".format(oErr.exception), text)
