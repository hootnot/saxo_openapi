# -*- coding: utf-8 -*-

"""
The saxo_openapi.contrib.orders.onfill module offers some classes to simplify
the creation of TakeProfit, StopLoss and TrailingStopLoss OCO-orders.

The next example shows how to create a marketorder for FX:

   go LONG 10000 EURUSD
   place a take profit order after fill, to take profit @1.14
   place a stoploss order after fill, to sell in case price drops below 1.12

>>> import json
>>> from saxo_openapi import API
>>> import saxo_openapi.endpoints.trading as tr
>>> import saxo_openapi.endpoints.portfolio as pf
>>> from saxo_openapi.contrib.orders import (
...     tie_account_to_order,
...     MarketOrderFxSpot,
...     TakeProfitDetails,
...     StopLossDetails)
>>> token = "..."
>>> client = API(access_token=token)
>>> r = pf.accounts.AccountsMe()
>>> rv = client.request(r)
>>> # take the first account ...
>>> acct = rv['Data'][0]
>>> AccountKey = acct['AccountKey']

At time of writing EURUSD = 1.1250,
lets take profit at 1.14, GoodTillCancel (default)
lets take the loss when the price drops below at 1.12, GoodTillCancel (default)

TP-details can simply be constructed by using TakeProfitDetails:

>>> tpDetails = TakeProfitDetails(price=1.14)
>>> print(tpDetails.data)
{
  "OrderType": "Limit",
  "OrderDuration": {
      "DurationType": "GoodTillCancel"
  },
  "OrderPrice": "1.14000"
}

So, a MarketOrder with TP-details and SL-details:

>>> ordr = MarketOrderFxSpot(
...     Uic=21,
...     Amount=10000,
...     TakeProfitOnFill=TakeProfitDetails(price=1.14),
...     StopLosstOnFill=StopLosstDetails(price=1.12)
... )
>>> print(json.dumps(ordr.data, indent=4))
{
  "Uic": 21,
  "AssetType": "FxSpot",
  "Amount": 10000,
  "BuySell": "Buy",
  "OrderType": "Market",
  "AmountType": "Quantity",
  "OrderDuration": {
      DurationType": "FillOrKill"
  },
  "Orders": [
    {
      "OrderDuration": {
          DurationType": "GoodTillCancel"
      },
      "OrderType": "Limit",
      "OrderPrice": "1.14000",
      "BuySell": "Sell",
      "AssetType": "FxSpot",
      "Amount": 10000
    },
    {
      "OrderDuration": {
          DurationType": "GoodTillCancel"
      },
      "OrderType": "Stop",
      "OrderPrice": "1.12000",
      "BuySell": "Sell",
      "AssetType": "FxSpot",
      "Amount": 10000
    }
  ]
}

Before an order can be placed the account needs to be attached
to the orderbody also:

>>> ordr = tie_account_to_order(AccountKey=AccountKey,
...             MarketOrderFxSpot(
...                 Uic=21,
...                 Amount=10000,
...                 TakeProfitOnFill=TakeProfitDetails(price=1.14),
...                 StopLosstOnFill=StopLosstDetails(price=1.12)
...             ))
>>> print(json.dumps(ordr, indent=4))
{
  "Uic": 21,
  "AssetType": "FxSpot",
  "Amount": 10000,
  "BuySell": "Buy",
  "OrderType": "Market",
  "AmountType": "Quantity",
  "OrderDuration": {
      DurationType": "FillOrKill"
  },
  "Orders": [
    {
      "OrderDuration": {
          DurationType": "GoodTillCancel"
      },
      "OrderType": "Limit",
      "OrderPrice": "1.14000",
      "BuySell": "Sell",
      "AssetType": "FxSpot",
      "Amount": 10000,
      "AccountKey": "fOA0tvOyQqW2aHpWi9P5bw=="
    },
    {
      "OrderDuration": {
          DurationType": "GoodTillCancel"
      },
      "OrderType": "Stop",
      "OrderPrice": "1.12000",
      "BuySell": "Sell",
      "AssetType": "FxSpot",
      "Amount": 10000,
      "AccountKey": "fOA0tvOyQqW2aHpWi9P5bw=="
    }
  ],
  "AccountKey": "fOA0tvOyQqW2aHpWi9P5bw=="
}

Now the order can be placed:

>>> r = tr.orders.Order(data=ordr)
>>> rv = client.request(r)
{
  "OrderId": "76697286",
  "Orders": [
    {
      "OrderId": "76697287"
    },
    {
      "OrderId": "76697288"
    }
  ]
}
"""

from abc import abstractmethod
from .baseorder import BaseOrder
import saxo_openapi.definitions.orders as OD
from .helper import order_duration_spec


class OnFill(BaseOrder):
    """baseclass for onFill requests."""
    ALLOWED_DT = [OD.OrderDurationType.GoodTillCancel,
                  OD.OrderDurationType.GoodTillDate,
                  OD.OrderDurationType.DayOrder]

    @abstractmethod
    def __init__(self,
                 OrderType,
                 OrderDurationType=OD.OrderDurationType.GoodTillCancel,
                 GTDDate=None):
        super(OnFill, self).__init__()

        if OrderDurationType not in [OD.OrderDurationType.GoodTillCancel,
                                     OD.OrderDurationType.GoodTillDate,
                                     OD.OrderDurationType.DayOrder]:
            raise ValueError("OrderDurationType: {} invalid".format(
                             OrderDurationType))

        self._data.update({"OrderType": OrderType})
        self._data.update({"OrderDuration":
                           order_duration_spec(OrderDurationType,
                                               self.ALLOWED_DT,
                                               GTDDate)})


class TakeProfitDetails(OnFill):
    """Representation of the specification for a TakeProfitOrder.

    It is typically used to specify 'take profit details' for the
    'TakeProfitOnFill' parameter of an OrderRequest. From the
    details a Limit order will be created with the specified *price*.
    The order gets placed when the underlying order gets filled.

    The other way to create a TakeProfitOrder is to create it afterwards
    on an existing trade. In that case use TakeProfitOrderRequest on
    the trade.
    """

    def __init__(self,
                 price,
                 OrderDurationType=OD.OrderDurationType.GoodTillCancel,
                 GTDDate=None):
        """Instantiate TakeProfitDetails.

        Parameters
        ----------

        price : float or string (required)
            the price to trigger take profit order

        OrderDurationType : OrderDurationType (required)
            the duration, default is: OrderDurationType.GoodTillCancel

        GTDDate : string or datetime (optional)
            GTD-datetime is required if OrderDurationType.GoodTillDate

        """
        OrderType = OD.OrderType.Limit
        super(TakeProfitDetails, self).__init__(
              OrderType=OrderType,
              OrderDurationType=OrderDurationType,
              GTDDate=GTDDate)
        self._data.update({"OrderPrice": price})


class StopLossDetails(OnFill):
    """Representation of the specification for a StopLossOrder.

    It is typically used to specify 'stop loss details' for the
    'StopLossOnFill' parameter of an OrderRequest. From the
    details a Stop order will be created with the specified *price*.
    The order gets placed when the underlying order gets filled.

    The other way to create a StopLossOrder is to create it afterwards
    on an existing trade. In that case use StopLossOrderRequest on
    the trade.
    """

    def __init__(self,
                 price,
                 OrderDurationType=OD.OrderDurationType.GoodTillCancel,
                 GTDDate=None):
        """Instantiate StopLossDetails.

        Parameters
        ----------

        price : float or string (required)
            the price to trigger take profit order

        OrderDurationType : OrderDurationType (required)
            the duration, default is: OrderDurationType.GoodTillCancel

        GTDDate : string or datetim (optional)
            GTD-datetime is required if OrderDurationType.GoodTillDate

        """
        OrderType = OD.OrderType.Stop
        super(StopLossDetails, self).__init__(
            OrderDurationType=OrderDurationType,
            OrderType=OrderType,
            GTDDate=GTDDate)
        self._data.update({"OrderPrice": price})
