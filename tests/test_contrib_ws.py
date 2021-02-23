# -*- coding: utf-8 -*-

"""Tests for saxo_openapi.contrib.ws"""

import unittest


import saxo_openapi.contrib.ws.stream as wsstr


class TestContribWS(unittest.TestCase):
    """Tests regarding contrib ws."""

    def test_stream_decode_ws_msg(self):
        raw = b'e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04' \
              + b'H_47\x00z\x00\x00\x00[{"PositionId":"212710174",' \
              + b'"PositionView":{"ConversionRateCurrent":0.89127500,' \
              + b'"ProfitLossOnTradeInBaseCurrency":-466.32}}]'
        res = {'refid': b'H_47',
               'msgId': 101,
               'msg': [
                  {'PositionId': '212710174',
                   'PositionView': {
                       'ConversionRateCurrent': 0.891275,
                       'ProfitLossOnTradeInBaseCurrency': -466.32
                    }
                   }
               ]
               }
        decmsg = wsstr.decode_ws_msg(raw)
        self.assertTrue(decmsg, res)

    def test_stream_decode_ws_msg1(self):
        raw = b'\x8b\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'AUDJPY\x00\\\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.971000Z","Quote":{"Ask":83.27,"Bid":83.22,"Mid":83.245}}' \
            + b'\x8c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'GBPCAD\x00a\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.976000Z","Quote":{"Ask":1.77132,"Bid":1.77052,"Mid":1.77092}}' \
            + b'\x8d\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'GBPNZD\x00a\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.979000Z","Quote":{"Ask":1.91672,"Bid":1.91552,"Mid":1.91612}}' \
            + b'\x8e\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'NZDCHF\x00a\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.979000Z","Quote":{"Ask":0.65704,"Bid":0.65634,"Mid":0.65669}}' \
            + b'\x8f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'GBPUSD\x00a\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.976000Z","Quote":{"Ask":1.40218,"Bid":1.40188,"Mid":1.40203}}' \
            + b'\x90\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'NZDCAD\x00a\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.979000Z","Quote":{"Ask":0.92462,"Bid":0.92382,"Mid":0.92422}}' \
            + b'\x91\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'NZDUSD\x00^\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.979000Z","Quote":{"Ask":0.7319,"Bid":0.7315,"Mid":0.7317}}' \
            + b'\x92\x03\x00\x00\x00\x00\x00\x00\x00\x00\x06' \
            + b'GBPAUD\x00a\x00\x00\x00{"LastUpdated":"2021-02-22T12:45:52.976000Z","Quote":{"Ask":1.77906,"Bid":1.77816,"Mid":1.77861}}'  # noqa E501

        res = [{
                "refid": "AUDJPY",
                "msgId": 907,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.971000Z",
                  "Quote": {
                    "Ask": 83.27,
                    "Bid": 83.22,
                    "Mid": 83.245
                  }
                }
              },
              {
                "refid": "GBPCAD",
                "msgId": 908,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.976000Z",
                  "Quote": {
                    "Ask": 1.77132,
                    "Bid": 1.77052,
                    "Mid": 1.77092
                  }
                }
              },
              {
                "refid": "GBPNZD",
                "msgId": 909,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.979000Z",
                  "Quote": {
                    "Ask": 1.91672,
                    "Bid": 1.91552,
                    "Mid": 1.91612
                  }
                }
              },
              {
                "refid": "NZDCHF",
                "msgId": 910,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.979000Z",
                  "Quote": {
                    "Ask": 0.65704,
                    "Bid": 0.65634,
                    "Mid": 0.65669
                  }
                }
              },
              {
                "refid": "GBPUSD",
                "msgId": 911,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.976000Z",
                  "Quote": {
                    "Ask": 1.40218,
                    "Bid": 1.40188,
                    "Mid": 1.40203
                  }
                }
              },
              {
                "refid": "NZDCAD",
                "msgId": 912,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.979000Z",
                  "Quote": {
                    "Ask": 0.92462,
                    "Bid": 0.92382,
                    "Mid": 0.92422
                  }
                }
              },
              {
                "refid": "NZDUSD",
                "msgId": 913,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.979000Z",
                  "Quote": {
                    "Ask": 0.7319,
                    "Bid": 0.7315,
                    "Mid": 0.7317
                  }
                }
              },
              {
                "refid": "GBPAUD",
                "msgId": 914,
                "msg": {
                  "LastUpdated": "2021-02-22T12:45:52.976000Z",
                  "Quote": {
                    "Ask": 1.77906,
                    "Bid": 1.77816,
                    "Mid": 1.77861
                  }
                }
              }]
        decmsgs = [m for m in wsstr.decode_ws_msg(raw)]
        self.assertTrue(decmsgs, res)
