# -*- encoding: utf-8 -*-

"""Handle trading-prices endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.prices import responses


@endpoint("openapi/trade/v1/prices/subscriptions", "POST", 201)
class CreatePriceSubscription(Trading):
    """Sets up an active price subscription on an instrument and returns an
    initial snapshot of the most recent price.
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreatePriceSubscription request.

        Parameters
        ----------
        data : dict (required)
            dict representing the data body, in this case an order spec.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreatePriceSubscription_body}
        >>> r = tr.prices.CreatePriceSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_CreatePriceSubscription_resp}

        """
        super(CreatePriceSubscription, self).__init__()
        self.data = data


@endpoint("openapi/trade/v1/prices/subscriptions/{ContextId}/{ReferenceId}",
          "PUT", 204)
class MarginImpactRequest(Trading):
    """Request margin impact to come on one of the next following price
    updates.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a MarginImpactRequest request.

        Parameters
        ----------
        ContextId : string (required)
            the ContextId

        ReferenceId : string (required)
            the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = "ctxt_20190311"
        >>> ReferenceId = "EURUSD"
        >>> r = tr.prices.MarginImpactRequest(ContextId=ContextId,
        ...                                   ReferenceId=ReferenceId)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        No data is returned.
        """
        super(MarginImpactRequest, self).__init__(ContextId=ContextId,
                                                  ReferenceId=ReferenceId)


@endpoint("openapi/trade/v1/prices/subscriptions/{ContextId}/",
          "DELETE", 202)
class PriceSubscriptionRemoveByTag(Trading):
    """Remove multiple subscriptions for the given ContextId, optionally
    marked with a specific tag.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a PriceSubscriptionRemoveByTag request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_PriceSubscriptionRemoveByTag_params}
        >>> ContextId = ...
        >>> r = tr.prices.PriceSubscriptionRemoveByTag(ContextId,
        ...                                            params=params)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status

        No data is returned.
        """
        super(PriceSubscriptionRemoveByTag, self).__init__(ContextId=ContextId)
        self.params = params


@endpoint("openapi/trade/v1/prices/subscriptions/{ContextId}/{ReferenceId}",
          "DELETE", 202)
class PriceSubscriptionRemove(Trading):
    """Removes subscription for the current session identified by
    subscription id.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a PriceSubscriptionRemove request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        ReferenceId: string (required)
            the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ...
        >>> ReferenceId = ...
        >>> r = tr.prices.PriceSubscriptionRemove(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status

        No data is returned.
        """
        super(PriceSubscriptionRemove, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
