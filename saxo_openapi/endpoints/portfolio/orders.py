# -*- encoding: utf-8 -*-

"""Handle portfolio-orders endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.orders import responses


@endpoint("openapi/port/v1/orders/{ClientKey}/{OrderId}")
class GetOpenOrder(Portfolio):
    """get a specific open order of a client. Unique id of the client.Unique
    id of the order.Specification of field groups to return. Default is empty.
    """

    @dyndoc_insert(responses)
    def __init__(self, ClientKey, OrderId, params=None):
        """Instantiate a GetOpenOrder request.

        Parameters
        ----------
        ClientKey: string (required)
             the ClientKey

        OrderId: string (required)
             the OrderId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        >>> OrderId = '76332324'
        >>> params = {_v3_GetOpenOrder_params}
        >>> r = pf.orders.GetOpenOrder(ClientKey=ClientKey,
        ...                            OrderId=OrderId,
        ...                            params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_GetOpenOrder_resp}

        """
        super(GetOpenOrder, self).__init__(ClientKey=ClientKey,
                                           OrderId=OrderId)
        self.params = params


@endpoint("openapi/port/v1/orders/me/")
class GetOpenOrdersMe(Portfolio):
    """get all the open orders on a client to which the logged in
    user belongs.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a GetOpenOrdersMe request.

        Parameters
        ----------
        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_GetOpenOrdersMe_params}
        >>> r = pf.orders.GetOpenOrdersMe(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_GetOpenOrdersMe_resp}

        """
        super(GetOpenOrdersMe, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/orders/{OrderId}/details/")
class OrderDetails(Portfolio):
    """Get detailed information about a single open order as specified
    by the query parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, OrderId, params=None):
        """Instantiate a OrderDetails request.

        Parameters
        ----------
        OrderId: string (required)
            the OrderId

        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> OrderId = '76332324'
        >>> params = {_v3_OrderDetails_params}
        >>> r = pf.orders.OrderDetails(OrderId=OrderId, params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_OrderDetails_resp}

        """
        super(OrderDetails, self).__init__(OrderId=OrderId)
        self.params = params


@endpoint("openapi/port/v1/orders/")
class GetAllOpenOrders(Portfolio):
    """all the open orders on an account or a client."""

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a GetAllOpenOrders request.

        Parameters
        ----------
        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_GetAllOpenOrders_params}
        >>> r = pf.orders.GetAllOpenOrders(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_GetAllOpenOrders_resp}

        """
        super(GetAllOpenOrders, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/orders/subscriptions", "POST", 201)
class CreateOpenOrdersSubscription(Portfolio):
    """Set up a subscription and returns an initial snapshot of list
    of orders specified by the parameters in the request.
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateOpenOrdersSubscription request.

        Parameters
        ----------
        data: dict (optional)
            dict representing the body with request parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateOpenOrdersSubscription_body}
        >>> r = pf.orders.CreateOpenOrdersSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_CreateOpenOrdersSubscription_resp}

        """
        super(CreateOpenOrdersSubscription, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/orders/subscriptions/{ContextId}/", "DELETE", 202)
class RemoveOpenOrderSubscriptionsByTag(Portfolio):
    """Remove multiple subscriptions for the current session on this
    resource. Optionally with with specified Tag.
    """

    RESPONSE_TYPE = 'text'

    def __init__(self, ContextId, params=None):
        """Instantiate a RemoveOpenOrderSubscriptionsByTag request.

        Parameters
        ----------
        ContextId: string (required)
           the ContextId

        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'explorer_1552035128308'
        >>> params = {_v3_RemoveOpenOrderSubscriptionsByTag_params}
        >>> r = pf.orders.RemoveOpenOrderSubscriptionsByTag(ContextId,
        ...                                                 params=params)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveOpenOrderSubscriptionsByTag, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/orders/subscriptions/"
          "{ContextId}/{ReferenceId}", "DELETE", 202)
class RemoveOpenOrderSubscription(Portfolio):
    """Remove a subscription for the current session identified by
    subscription id
    """

    RESPONSE_TYPE = 'text'

    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveOpenOrderSubscription request.

        Parameters
        ----------
        ContextId: string (required)
           the ContextId

        ReferenceId: string (required)
           the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'explorer_1552035128308'
        >>> ReferenceId = 'C_582'
        >>> r = pf.orders.RemoveOpenOrderSubscription(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveOpenOrderSubscription, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
