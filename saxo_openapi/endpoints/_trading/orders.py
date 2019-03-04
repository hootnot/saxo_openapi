# -*- encoding: utf-8 -*-

"""Handle trading-orders endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.orders import responses


@endpoint("openapi/trade/v2/orders", "POST")
class Order(Trading):
    """Place a new order."""

    @dyndoc_insert(responses)
    def __init__(self, data=None):
        """Instantiate an Order request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_Order_body}
        >>> r = tr.orders.Order(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::
            {_v3_Order_resp}

        """
        super(Order, self).__init__()
        self.data = data


@endpoint("openapi/trade/v2/orders", "PATCH")
class ChangeOrder(Trading):
    """Change one or more existing orders."""

    @dyndoc_insert(responses)
    def __init__(self, data=None):
        """Instantiate a ChangeOrder request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ChangeOrder_body}
        >>> r = tr.orders.ChangeOrder(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Change the amount of an existing order:

        ::

           {_v3_ChangeOrder_resp}

        """
        super(ChangeOrder, self).__init__()
        self.data = data


@endpoint("openapi/trade/v2/orders/{OrderIds}", "DELETE")
class CancelOrders(Trading):
    """Cancel one or more orders."""

    @dyndoc_insert(responses)
    def __init__(self, OrderIds, params):
        """Instantiate a CancelOrders request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_CancelOrders_params}
        >>> OrderIds="76289286"
        >>> r = tr.orders.CancelOrders(OrderIds=OrderIds, params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::

           {_v3_CancelOrders_resp}

        """
        super(CancelOrders, self).__init__(OrderIds=OrderIds)
        self.params = params


@endpoint("openapi/trade/v2/orders/precheck", "POST")
class PrecheckOrder(Trading):
    """Precheck an order."""

    @dyndoc_insert(responses)
    def __init__(self, data=None):
        """Instantiate a PrecheckOrder request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_PrecheckOrder_body}
        >>> r = tr.orders.PrecheckOrder(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_PrecheckOrder_resp}

        """
        super(PrecheckOrder, self).__init__()
        self.data = data
