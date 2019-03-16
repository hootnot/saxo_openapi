# -*- encoding: utf-8 -*-

"""Handle trading-infoprices endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.infoprices import responses


@endpoint("openapi/trade/v1/infoprices")
class InfoPrice(Trading):
    """Gets an info price for an instrument using the specified
    parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an InfoPrice request.

        Parameters
        ----------
        params : dict (required)
            dict representing the querystring parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_InfoPrice_params}
        >>> r = tr.infoprices.InfoPrice(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_InfoPrice_resp}

        """
        super(InfoPrice, self).__init__()
        self.params = params


@endpoint("openapi/trade/v1/infoprices/list")
class InfoPrices(Trading):
    """Gets a list of info prices for a list of instruments using the
    specified parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an InfoPrices request.

        Parameters
        ----------
        params : dict (required)
            dict representing the querystring parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_InfoPrices_params}
        >>> r = tr.infoprices.InfoPrices(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_InfoPrices_resp}

        """
        super(InfoPrices, self).__init__()
        self.params = params


@endpoint("openapi/trade/v1/infoprices/subscriptions", "POST", 201)
class CreateInfoPriceSubscription(Trading):
    """Sets up a subscription and returns an initial snapshot of an info
    price list specified by the parameters in the request."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateInfoPriceSubscription request.

        Parameters
        ----------
        data : dict (required)
            dict representing the parameters of the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateInfoPriceSubscription_body}
        >>> r = tr.infoprices.CreateInfoPriceSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

           {_v3_CreateInfoPriceSubscription_resp}

        """
        super(CreateInfoPriceSubscription, self).__init__()
        self.data = data


@endpoint("openapi/trade/v1/infoprices/subscriptions/{ContextId}",
          "DELETE", 202)
class RemoveInfoPriceSubscriptionsByTag(Trading):
    """Remove one or more infoprice subscriptions."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a RemoveInfoPriceSubscriptionsByTag request.

        Parameters
        ----------
        ContextId: string (required)
            the context id.

        params : dict (required)
            dict representing the querystring parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'ctxt_20190316'
        >>> params = {_v3_RemoveInfoPriceSubscriptionsByTag_params}
        >>> r = tr.infoprices.RemoveInfoPriceSubscriptionsByTag(
        ...     ContextId=ContextId,
        ...     params=params)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveInfoPriceSubscriptionsByTag, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/trade/v1/infoprices/subscriptions/"
          "{ContextId}/{ReferenceId}",
          "DELETE", 202)
class RemoveInfoPriceSubscriptionById(Trading):
    """Remove an info price subscription on a single instrument."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveInfoPricesSubscriptionById request.

        Parameters
        ----------
        ContextId: string (required)
            the context id.

        ReferenceId: string (required)
            the ReferenceId id.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'ctxt_20190316'
        >>> ReferenceId = 'pri_01'
        >>> r = tr.infoprices.RemoveInfoPriceSubscriptionById(
        ...     ContextId=ContextId,
        ...     ReferenceId=ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveInfoPriceSubscriptionById, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
