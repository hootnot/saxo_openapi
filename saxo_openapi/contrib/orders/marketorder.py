# -*- coding: utf-8 -*-

from .baseorder import BaseOrder
from .helper import direction_from_amount
import saxo_openapi.definitions.orders as OD
from .mixin import OnFillHnd


class MarketOrder(BaseOrder, OnFillHnd):
    """create a MarketOrder.

    MarketOrder is used to build the body for a MarketOrder. The body can be
    used to pass to the Order endpoint.
    """

    def __init__(self,
                 Uic,
                 Amount,
                 AssetType,
                 AmountType=OD.AmountType.Quantity,
                 TakeProfitOnFill=None,
                 StopLossOnFill=None,
                 TrailingStopLossOnFill=None):
        """
        Instantiate a MarketOrder.

        Parameters
        ----------

        Uic: int (required)
            the Uic of the instrument to trade

        Amount: decimal (required)
            the number of lots/shares/contracts or a monetary value
            if amountType is set to CashAmount. A value > 0 means 'buy',
            a value < 0 means 'sell'

        AssetType: string (required)
            the assettype for the Uic

        AmountType: AmountType (optional)
            the amountType, defaults to Quantity, see AmountType for
            other options

        TakeProfitOnFill: TakeProfitDetails instance or dict
            the take-profit order specification

        StopLosstOnFill: StopLossDetails instance or dict
            the stoploss order specification

        TrailingStopLosstOnFill: TrailingStopLossDetails instance or dict
            the Trailingstoploss order specification

        Example
        -------

        >>> import json
        >>> from saxo_openapi import API
        >>> import saxo_openapi.endpoints.trading as tr
        >>> from saxo_openapi.contrib.orders import MarketOrder
        >>> # buy 10k EURUSD (Uic=21)
        >>> mo = MarketOrder(Uic=21,
        ...                  AssetType=OD.AssetType.FxSpot,
        ...                  Amount=10000)
        >>> print(json.dumps(mo.data, indent=4))
        {
          "Uic": 21,
          "AssetType": "FxSpot",
          "Amount": 10000,
          "BuySell": "Buy",
          "OrderType": "Market",
          "AmountType": "Quantity",
          "OrderDuration": {
              "DurationType": "DayOrder"
          }
        }
        >>> # now we have the order specification, create the order request
        >>> r = tr.orders.Order(data=mo.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(rv)
        >>> print(json.dumps(rv, indent=4))
        {
           "OrderId": "76697286"
        }
        """

        super(MarketOrder, self).__init__()

        # by default for a Market order
        da = {
             'OrderType': OD.OrderType.Market,
             'AmountType': AmountType,
             'OrderDuration': {   # the default
                 'DurationType': OD.OrderDurationType.DayOrder
             },
        }

        # required
        self._data.update({"Uic": Uic})
        self._data.update({"AssetType": AssetType})
        self._data.update({"Amount": abs(Amount)})
        self._data.update({"BuySell": direction_from_amount(Amount)})
        self._data.update(da)

        self.hndOnFill(TakeProfitOnFill=TakeProfitOnFill,
                       StopLossOnFill=StopLossOnFill,
                       TrailingStopLossOnFill=TrailingStopLossOnFill)

    @property
    def data(self):
        """data property.

        return the JSON body.
        """
        return super(MarketOrder, self).data


class MarketOrderFxSpot(MarketOrder):
    """MarketOrderFxSpot - MarketOrder for FxSpot only.

    The MarketOrderFxSpot lacks the AssetType parameter and only serves
    the AssetType FxSpot.
    """
    def __init__(self,
                 Uic,
                 Amount,
                 AmountType=OD.AmountType.Quantity,
                 TakeProfitOnFill=None,
                 StopLossOnFill=None,
                 TrailingStopLossOnFill=None):
        """
        Instantiate a MarketOrderFxSpot.

        Parameters
        ----------

        Uic: int (required)
            the Uic of the instrument to trade

        Amount: decimal (required)
            the number of lots/shares/contracts or a monetary value
            if amountType is set to CashAmount

        AmountType: AmountType (optional)
            the amountType, defaults to Quantity, see AmountType for
            other options

        TakeProfitOnFill: TakeProfitDetails instance or dict
            the take-profit order specification

        StopLosstOnFill: StopLossDetails instance or dict
            the stoploss order specification

        TrailingStopLosstOnFill: TrailingStopLossDetails instance or dict
            the Trailingstoploss order specification

        Example
        -------

        >>> from saxo_openapi import API
        >>> from saxo_openapi.contrib.orders import (
        ...          tie_account_to_order,
        ...          MarketOrderFxSpot)
        >>> token = "..."
        >>> client = API(access_token=token)
        >>> order = tie_account_to_order(
        ...               AccountKey,
        ...               MarketOrderFxSpot(Uic=21, Amount=25000))
        >>> r = tr.orders.Order(data=req)
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=2))
        {
          "OrderId": "76703544"
        }
        """
        super(MarketOrderFxSpot, self).__init__(
                 Uic=Uic,
                 Amount=Amount,
                 AmountType=AmountType,
                 AssetType=OD.AssetType.FxSpot,
                 TakeProfitOnFill=TakeProfitOnFill,
                 StopLossOnFill=StopLossOnFill,
                 TrailingStopLossOnFill=TrailingStopLossOnFill)


class MarketOrderStock(MarketOrder):
    """MarketOrderStock - MarketOrder for Stock only.

    The MarketOrderStock lacks the AssetType parameter and only serves
    the AssetType Stock.
    """
    def __init__(self,
                 Uic,
                 Amount,
                 AmountType=OD.AmountType.Quantity,
                 TakeProfitOnFill=None,
                 StopLossOnFill=None,
                 TrailingStopLossOnFill=None):
        """
        Instantiate a MarketOrderStock.

        Parameters
        ----------

        Uic: int (required)
            the Uic of the instrument to trade

        Amount: decimal (required)
            the number of lots/shares/contracts or a monetary value
            if amountType is set to CashAmount

        AmountType: AmountType (optional)
            the amountType, defaults to Quantity, see AmountType for
            other options

        TakeProfitOnFill: TakeProfitDetails instance or dict
            the take-profit order specification

        StopLosstOnFill: StopLossDetails instance or dict
            the stoploss order specification

        TrailingStopLosstOnFill: TrailingStopLossDetails instance or dict
            the Trailingstoploss order specification

        Example
        -------

        >>> from saxo_openapi import API
        >>> from saxo_openapi.contrib.orders import (
        ...          tie_account_to_order,
        ...          MarketOrderStock)
        >>> token = "..."
        >>> client = API(access_token=token)
        >>> order = tie_account_to_order(
        ...               AccountKey,
        ...               MarketOrderStock(Uic=16350, Amount=1000))
        >>> r = tr.orders.Order(data=req)
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=2))
        {
          "OrderId": "76703539"
        }
        """
        super(MarketOrderStock, self).__init__(
                 Uic=Uic,
                 Amount=Amount,
                 AmountType=AmountType,
                 AssetType=OD.AssetType.Stock,
                 TakeProfitOnFill=TakeProfitOnFill,
                 StopLossOnFill=StopLossOnFill,
                 TrailingStopLossOnFill=TrailingStopLossOnFill)
