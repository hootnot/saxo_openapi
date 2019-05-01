# -*- coding: utf-8 -*-

from .helper import direction_from_amount, direction_invert


class OnFillHnd(object):

    def hndOnFill(self,
                  TakeProfitOnFill=None,
                  StopLossOnFill=None,
                  TrailingStopLossOnFill=None):

        ospec = None
        for onFillOrder in [TakeProfitOnFill,
                            StopLossOnFill,
                            TrailingStopLossOnFill]:

            if onFillOrder is None:
                continue

            if not isinstance(onFillOrder, dict):
                ospec = onFillOrder.data.copy()
            else:
                ospec = onFillOrder

            if ospec:
                if 'Orders' not in self._data:
                    self._data.update({'Orders': []})

                ospec.update({"Uic": self._data['Uic']})
                ospec.update({'BuySell':
                              direction_invert(self._data['BuySell'])})
                ospec.update({'AssetType': self._data['AssetType']})
                if 'Amount' not in ospec:
                    ospec.update({'Amount': self._data['Amount']})
                self._data['Orders'].append(ospec)
