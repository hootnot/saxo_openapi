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
