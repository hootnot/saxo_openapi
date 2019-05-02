# -*- coding: utf-8 -*-

from .baseorder import BaseOrder
from .helper import direction_from_amount, order_duration_spec
import saxo_openapi.definitions.orders as OD
from .mixin import OnFillHnd


class StopOrder(BaseOrder, OnFillHnd):
    """create a StopOrder.

    StopOrder is used to build the body for a StopOrder. The body can be
    used to pass to the Order endpoint.
    """

    # allowed OrderDurationTypes:
    ALLOWED_DT = [OD.OrderDurationType.DayOrder,
                  OD.OrderDurationType.GoodTillDate,
                  OD.OrderDurationType.GoodTillCancel]

    def __init__(self,
                 Uic,
                 Amount,
                 AssetType,
                 OrderPrice,
                 AmountType=OD.AmountType.Quantity,
                 TakeProfitOnFill=None,
                 StopLossOnFill=None,
                 TrailingStopLossOnFill=None,
                 OrderDurationType=OD.OrderDurationType.DayOrder,
                 GTDDate=None):
        """
        Instantiate a StopOrder.

        Parameters
        ----------

        Uic: int (required)
            the Uic of the instrument to trade

        Amount: decimal (required)
            the number of lots/shares/contracts or a monetary value
            if amountType is set to CashAmount

        OrderPrice: decimal (required)
            the price indicating the limitprice

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

        OrderDurationType: string, default DayOrder
            the order duration type, check SAXO Bank specs. for details

        GTDDate: datetime string (required if order duration is GoodTillDate)
            the GTD-datetime

        Example
        -------

        >>> import json
        >>> from saxo_openapi import API
        >>> import saxo_openapi.endpoints.trading as tr
        >>> from saxo_openapi.contrib.orders import StopOrder
        >>>
        >>> so = StopOrder(Uic=21,
        ...                 AssetType=OD.AssetType.FxSpot,
        ...                 Amount=10000,
        ...                 OrderPrice=1.1025)
        >>> print(json.dumps(so.data, indent=2))
        {
          "Uic": 21,
          "AssetType": "FxSpot",
          "Amount": 10000,
          "Price": 1.1025,
          "BuySell": "Buy",
          "OrderType": "Stop",
          "AmountType": "Quantity",
          "OrderDuration": {
             "DurationType": "DayOrder"
          }
        }
        >>> # now we have the order specification, create the order request
        >>> r = tr.orders.Order(data=so.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(rv)
        >>> print(json.dumps(rv, indent=4))
        {
           "OrderId": "76697286"
        }
        """

        super(StopOrder, self).__init__()

        # by default for a StopOrder
        da = {
            'OrderType': OD.OrderType.Stop,
            'AmountType': AmountType,
        }

        da.update({'OrderDuration': order_duration_spec(OrderDurationType,
                                                        self.ALLOWED_DT,
                                                        GTDDate)})

        # required
        self._data.update({"Uic": Uic})
        self._data.update({"AssetType": AssetType})
        self._data.update({"Amount": abs(Amount)})
        self._data.update({"OrderPrice": OrderPrice})
        self._data.update({"BuySell": direction_from_amount(Amount)})
        self._data.update(da)

        self.hndOnFill(
            TakeProfitOnFill=TakeProfitOnFill,
            StopLossOnFill=StopLossOnFill,
            TrailingStopLossOnFill=TrailingStopLossOnFill)

    @property
    def data(self):
        """data property.

        return the JSON body.
        """
        return super(StopOrder, self).data


class StopOrderFxSpot(StopOrder):
    """StopOrderFxSpot - StopOrder for FxSpot only.

    The StopOrderFxSpot lacks the AssetType parameter and only serves
    the AssetType FxSpot.
    """
    def __init__(self,
                 Uic,
                 Amount,
                 OrderPrice,
                 AmountType=OD.AmountType.Quantity,
                 TakeProfitOnFill=None,
                 StopLossOnFill=None,
                 TrailingStopLossOnFill=None,
                 OrderDurationType=OD.OrderDurationType.DayOrder,
                 GTDDate=None):
        """
        Instantiate a StopOrderFxSpot.

        Parameters
        ----------

        Uic: int (required)
            the Uic of the instrument to trade

        Amount: decimal (required)
            the number of lots/shares/contracts or a monetary value
            if amountType is set to CashAmount

        OrderPrice: decimal (required)
            the price indicating the limitprice

        AmountType: AmountType (optional)
            the amountType, defaults to Quantity, see AmountType for
            other options

        TakeProfitOnFill: TakeProfitDetails instance or dict
            the take-profit order specification

        StopLosstOnFill: StopLossDetails instance or dict
            the stoploss order specification

        TrailingStopLosstOnFill: TrailingStopLossDetails instance or dict
            the Trailingstoploss order specification

        OrderDurationType: string, default DayOrder
            the order duration type, check SAXO Bank specs. for details

        GTDDate: datetime string (required if order duration is GoodTillDate)
            the GTD-datetime

        Example
        -------

        >>> from saxo_openapi import API
        >>> from saxo_openapi.contrib.orders import (
        ...          tie_account_to_order,
        ...          StopOrderFxSpot)
        >>> token = "..."
        >>> client = API(access_token=token)
        >>> order = tie_account_to_order(
        ...     AccountKey,
        ...     StopOrderFxSpot(Uic=21, Amount=25000, OrderPrice=1.1025))
        >>> r = tr.orders.Order(data=order)
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=2))
        {
          "OrderId": "76703544"
        }
        """
        super(StopOrderFxSpot, self).__init__(
                 Uic=Uic,
                 Amount=Amount,
                 OrderPrice=OrderPrice,
                 AmountType=AmountType,
                 AssetType=OD.AssetType.FxSpot,
                 OrderDurationType=OrderDurationType,
                 TakeProfitOnFill=TakeProfitOnFill,
                 StopLossOnFill=StopLossOnFill,
                 TrailingStopLossOnFill=TrailingStopLossOnFill,
                 GTDDate=GTDDate)
