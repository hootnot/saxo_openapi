# -*- encoding: utf-8 -*-

"""Handle portfolio-closedposition endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.closedpositions import responses


@endpoint("openapi/port/v1/closedpositions/")
class ClosedPositionList(Portfolio):
    """Returns a list of closed positions fulfilling the criteria
    specified by the query string parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a ClosedPositionList request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ClosedPositionList_params}
        >>> r = pf.closedpositions.ClosedPositionList(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClosedPositionList_resp}

        """
        super(ClosedPositionList, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/closedpositions/{ClosedPositionId}")
class ClosedPositionById(Portfolio):
    """Get a single position by the ClosedPositionId."""

    @dyndoc_insert(responses)
    def __init__(self, ClosedPositionId, params):
        """Instantiate a ClosedPositionById request.

        Parameters
        ----------
        ClosedPositionId: string (required)
            the ClosedPositionId

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ClosedPositionId = '212702698-212702774'
        >>> params = {_v3_ClosedPositionById_params}
        >>> r = pf.closedpositions.ClosedPositionById(
        ...                           ClosedPositionId=ClosedPositionId,
        ...                           params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClosedPositionById_resp}

        """
        super(ClosedPositionById, self).__init__(
            ClosedPositionId=ClosedPositionId)
        self.params = params


@endpoint("openapi/port/v1/closedpositions/{ClosedPositionId}/details/")
class ClosedPositionDetails(Portfolio):
    """Gets detailed information about a single position as specified by
    the query parameters
    """

    @dyndoc_insert(responses)
    def __init__(self, ClosedPositionId, params=None):
        """Instantiate a ClosedPositionDetails request.

        Parameters
        ----------
        ClosedPositionId: string (required)
            the ClosedPositionId

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ClosedPositionId = '212702698-212702774'
        >>> params = {_v3_ClosedPositionDetails_params}
        >>> r = pf.closedpositions.ClosedPositionDetails(
        ...                              ClosedPositionId=ClosedPositionId,
        ...                              params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClosedPositionDetails_resp}

        """
        super(ClosedPositionDetails, self).__init__(
            ClosedPositionId=ClosedPositionId)
        self.params = params


@endpoint("openapi/port/v1/closedpositions/me")
class ClosedPositionsMe(Portfolio):
    """Returns a list of closed positions fulfilling the criteria specified
    by the query string parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a ClosedPositionsMe request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ClosedPositionsMe_params}
        >>> r = pf.closedpositions.ClosedPositionsMe(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClosedPositionsMe_resp}

        """
        super(ClosedPositionsMe, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/closedpositions/subscriptions/", "POST", 201)
class ClosedPositionSubscription(Portfolio):
    """Sets up a subscription and returns an initial snapshot of list of
    closed positions specified by the parameters in the request.
    """

    @dyndoc_insert(responses)
    def __init__(self, data, params=None):
        """Instantiate a ClosedPositionSubscription request.

        Parameters
        ----------
        data: dict (required)
            dict representing the parameters of the data body

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ClosedPositionSubscription_params}
        >>> data = {_v3_ClosedPositionSubscription_body}
        >>> r = pf.closedpositions.ClosedPositionSubscription(
        ...               data=data,
        ...               params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        """
        super(ClosedPositionSubscription, self).__init__()
        self.data = data
        self.params = params


@endpoint("openapi/port/v1/closedpositions/subscriptions/"
          "{ContextId}/{ReferenceId}", "PATCH", 200)
class ClosedPositionSubscriptionUpdate(Portfolio):
    """Extends or reduces the page size, number of positions shown, on
    a running closed positions subscription. When expanding the page size,
    the subsequent closed positions are streamed so to avoid race conditions.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId, data):
        """Instantiate a ClosedPositionSubscriptionUpdate request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        ReferenceId: string (required)
            the ReferenceId

        data: dict (required)
            dict representing the parameters of the data body


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ClosedPositionSubscriptionUpdate_body}
        >>> ContextId = ''
        >>> ReferenceId = ''
        >>> r = pf.closedpositions.ClosedPositionSubscriptionUpdate(
        ...                                         ContextId=ContextId,
        ...                                         ReferenceId=ReferenceId,
        ...                                         data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        No data is returned.
        """
        super(ClosedPositionSubscriptionUpdate, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
        self.data = data


@endpoint("openapi/port/v1/closedpositions/"
          "subscriptions/{ContextId}", "DELETE", 202)
class ClosedPositionSubscriptionsRemove(Portfolio):
    """Removes multiple all subscriptions for the current session on this
    resource, and frees all resources on the server.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a ClosedPositionSubscriptionsRemove request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        params: dict (required)
            dict representing the parameters of the querystring


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.closedpositions.ClosedPositionSubscriptionsRemove(
        ...             ContextId=ContextId,
        ...             params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        No data is returned.
        """
        super(ClosedPositionSubscriptionsRemove, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/closedpositions/"
          "subscriptions/{ContextId}/{ReferenceId}", "DELETE", 202)
class ClosedPositionSubscriptionRemoveById(Portfolio):
    """Removes subscription for the current session identified by
    subscription id.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a ClosedPositionSubscriptionRemoveById request.

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
        >>> r = pf.closedpositions.ClosedPositionSubscriptionRemoveById(
        ...             ContextId=ContextId,
        ...             ReferenceId=ReferenceId)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        No data is returned.
        """
        super(ClosedPositionSubscriptionRemoveById, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
