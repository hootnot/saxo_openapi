# -*- coding: utf-8 -*-

"""initialization of unittests and data for unittests."""

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


def auth():
    access_token = None
    with open("tests/token.txt") as T:
        access_token = T.read().strip()

    return access_token
