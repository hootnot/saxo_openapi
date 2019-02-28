#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
from . import unittestsetup
from .unittestsetup import environment as environment, mock_env
from saxo_openapi import API

access_token = None
api = None


class TestSaxo_openapi(unittest.TestCase):
    """Tests for `saxo_openapi` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        global access_token
        global api

        try:
            access_token = unittestsetup.auth()
            setattr(sys.modules["saxo_openapi.saxo_openapi"],
                    "TRADING_ENVIRONMENTS",
                    mock_env)
            api = API(environment=environment, access_token=access_token)

        except Exception as e:
            print(e)
            exit(0)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test__saxo_environment(self):
        """test the exception on a faulty environment."""
        with self.assertRaises(KeyError) as envErr:
            API(environment="faulty", access_token=access_token)

        self.assertTrue("Unknown environment" in "{}".format(envErr.exception))

    def test__requests_params(self):
        """request parameters."""
        request_params = {"timeout": 10}
        api = API(environment=environment,
                  access_token=access_token,
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
        api = API(environment=environment, access_token=access_token)
        text = "No connection " \
               "adapters were found for " \
               "'ttps://test.com/sim/openapi/port/v1/accounts/me'"
        r = pf.AccountList()
        with self.assertRaises(RequestException) as oErr:
            api.request(r)

        self.assertEqual("{}".format(oErr.exception), text)


if __name__ == "__main__":

    unittest.main()
