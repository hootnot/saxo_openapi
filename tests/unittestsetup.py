# -*- coding: utf-8 -*-

"""initialization of unittests and data for unittests."""

import json


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


def test_generic(self, api, _mod, clsNm, route, **kwargs):
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
        raise ValueError("FAILURE instantiating {}: {}".format(clsNm, stuf))

    if hasattr(r, "RESPONSE_DATA"):
        if r.RESPONSE_DATA is not None:
            out.update({'text': tdata.resp})

    else:
        out.update({'text': json.dumps(tdata.resp)})

    out.update({'status_code': r.expected_status})

    kwargs['mock'].register_uri(r.method,
                                "{}/sim/{}".format(api.api_url, r),
                                **out)
    api.request(r)
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
