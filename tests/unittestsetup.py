# -*- coding: utf-8 -*-

"""initialization of unittests and data for unittests."""

import sys
import json
import unittest
from saxo_openapi import API

environment = "simulation"

mock_env = {
    "simulation": {
        "stream": "https://test.com",
        "api": "https://test.com",
        "prefix": "sim"
    }
}


def fetchTestData(responses, k):
    resp = responses[k]['response']
    params, data = None, None
    if 'body' in responses[k]:
        data = responses[k]['body']

    if "params" in responses[k]:
        params = responses[k]['params']

    if params is not None:
        return (resp, data, params)

    return (resp, data)


class TestData(object):

    def __init__(self, responses, tid):
        self._responses = responses[tid]

    @property
    def resp(self):
        if 'resp' in self._responses:
            return self._responses['response']
        return None

    @property
    def body(self):
        if 'body' in self._responses:
            return self._responses['body']
        return None

    @property
    def params(self):
        if 'params' in self._responses:
            return self._responses['params']
        return None

    @property
    def route(self):
        if 'route' in self._responses:
            return self._responses['route']
        return None


def test_generic(self, _mod, clsNm, route, **kwargs):
    if hasattr(_mod, "responses"):
        tdata = TestData(getattr(_mod, "responses"), "_v3_"+clsNm)
    else:
        tdata = TestData(dict({"_v3_"+clsNm: {}}), "_v3_"+clsNm)

    cls = getattr(_mod, clsNm)

    stuf = dict()
    out = dict()
    if tdata.params:
        stuf.update({'params': tdata.params})
    if tdata.body:
        stuf.update({'data': tdata.body})
    if tdata.route:
        stuf.update(tdata.route)
    elif route:
        stuf.update(route)

    try:
        r = cls(**stuf)
    except Exception as e:
        raise ValueError("{}: FAILURE instantiating {}: {}".format(
            e, clsNm, stuf))

    if hasattr(r, "RESPONSE_DATA"):
        if r.RESPONSE_DATA is not None:
            out.update({'text': tdata.resp})

    else:
        out.update({'text': json.dumps(tdata.resp)})

    out.update({'status_code': r.expected_status})

    kwargs['mock'].register_uri(r.method,
                                "{}/sim/{}".format(self.api.api_url, r),
                                **out)
    self.api.request(r)
    if 'text' in out:
        self.assertTrue(r.response == tdata.resp and
                        r.status_code == r.expected_status)
    else:
        self.assertTrue(r.status_code == r.expected_status)


def auth():
    access_token = None
    with open("tests/token.txt") as T:
        access_token = T.read().strip()

    return access_token


class ReqMockTest(unittest.TestCase):
    """Class to test the request-classes that represent the endpoints."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.access_token = None
        self.api = None

        try:
            self.access_token = auth()
            setattr(sys.modules["saxo_openapi.saxo_openapi"],
                    "TRADING_ENVIRONMENTS",
                    mock_env)
            self.api = API(environment=environment,
                           access_token=self.access_token)
            self.api.api_url = 'https://test.com'

        except Exception as e:
            print(e)
            exit(0)

    def tearDown(self):
        """Tear down test fixtures, if any."""
