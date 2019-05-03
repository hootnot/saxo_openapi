# -*- coding: utf-8 -*-

from datetime import datetime
import saxo_openapi.definitions.orders as OD


def direction_from_amount(Amount):
    """direction_from_amount - determine direction from the sign of the amount.

    if Amount > 0 : Buy
    if Amount < 0 : Sell
    """
    return OD.Direction.Buy if Amount > 0 else OD.Direction.Sell


def direction_invert(direction):
    """direction_invert - Buy  becomes Sell, Sell becomes Buy."""
    if direction not in [OD.Direction.Buy, OD.Direction.Sell]:
        raise ValueError("wrong value for direction: {}".format(direction))

    return OD.Direction.Buy if direction == OD.Direction.Sell \
        else OD.Direction.Sell


def tie_account_to_order(AccountKey, order):
    """tie_account_to_order - inject the AccountKey in the orderbody.

    An order specification is 'anonymous'. To apply it to an account it needs
    the AccountKey of the account.

    Parameters
    ----------
    AccountKey: string (required)
        the accountkey

    order: dict representing an orderbody or <...>Order instance
        the details of the order.
    """
    _r = order.copy() if isinstance(order, dict) else order.data.copy()

    # add the key to the orderbody, but ONLY if this is not a positionclose
    # body
    if "PositionId" not in _r:
        _r.update({'AccountKey': AccountKey})

    # and add it to related orders in Orders (if any)
    if 'Orders' in _r:
        for o in _r['Orders']:
            o.update({'AccountKey': AccountKey})

    return _r


def order_duration_spec(OrderDurationType, allowedDT, GTDDate=None):
    """order_duration_spec - create a SAXO order duration from a date.

    This function returns a dict containing the definition of the
    duration. In case of an order where the GTDDate is specified the
    definition is extended.

    Parameters
    ----------

    GTDDate: string or datetime (required if Dur.Type == GTD)
        the GTD-datetime


    Examples
    --------

    >>> duration = OD.OrderDurationType.GoodTillDate
    >>> d = order_duration_spec(duration, "2017-12-12"))
    >>> print(json.dumps(d, indent=2))
    {
      "DurationType": "GoodTillDate",
      "ExpirationDateContainsTime": true,
      "ExpirationDateTime": "2017-12-12T00:00"
    }
    # Or by using datetime ...
    >>> d = order_duration_spec(dt, datetime(2017, 12, 12))
    >>> print(json.dumps(d, indent=2))
    {
      "DurationType": "GoodTillDate",
      "ExpirationDateContainsTime": true,
      "ExpirationDateTime": "2017-12-12T00:00"
    }
    >>> duration = OD.OrderDurationType.GoodTillCancel
    >>> d = order_duration_spec(dt)
    >>> print(json.dumps(d, indent=2))
    {
      "DurationType": "GoodTillCancel"
    }

    """

    odspec = dict({'DurationType': OrderDurationType})

    # allowed OrderDurationTypes:
    if OrderDurationType not in allowedDT:
        raise ValueError("OrderDurationType: {} is not supported".format(
                         OrderDurationType))

    if OrderDurationType == OD.OrderDurationType.GoodTillDate:
        if not GTDDate:
            raise ValueError("Missing GTDDate")

        _gtdtime = GTDDate
        if isinstance(GTDDate, str):
            try:
                _gtdtime = datetime.strptime(GTDDate, "%Y-%m-%d")
            except ValueError:
                # a ValueError is raised in case of wrong format
                _gtdtime = datetime.strptime(GTDDate, "%Y-%m-%dT%H:%M")

        _gtdtime = _gtdtime.strftime("%Y-%m-%dT%H:%M")

        odspec.update({'ExpirationDateContainsTime': True,
                       'ExpirationDateTime': _gtdtime})

    return odspec
