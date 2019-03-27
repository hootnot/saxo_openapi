# -*- encoding: utf-8 -*-

"""Handle portfolio-netpositions endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.netpositions import responses


@endpoint("openapi/port/v1/netpositions/{NetPositionId}")
class SingleNetPosition(Portfolio):
    """Get a single net position."""

    @dyndoc_insert(responses)
    def __init__(self, NetPositionId, params):
        """Instantiate a SingleNetPosition request.

        Parameters
        ----------
        NetPositionId: string (required)
            the NetPositionId

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_SingleNetPosition_params}
        >>> NetPositionId = "GBPCAD__FxSpot"
        >>> r = pf.netpositions.SingleNetPosition(NetPositionId=NetPositionId,
        ...                                       params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_SingleNetPosition_resp}

        """
        super(SingleNetPosition, self).__init__(NetPositionId=NetPositionId)
        self.params = params


@endpoint("openapi/port/v1/netpositions/{NetPositionId}/details")
class SingleNetPositionDetails(Portfolio):
    """Get a single net position details."""

    @dyndoc_insert(responses)
    def __init__(self, NetPositionId, params):
        """Instantiate a SingleNetPositionDetails request.

        Parameters
        ----------
        NetPositionId: string (required)
            the NetPositionId

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_SingleNetPositionDetails_params}
        >>> NetPositionId = "GBPCAD__FxSpot"
        >>> r = pf.positions.SingleNetPositionDetails(
        ...          NetPositionId=NetPositionId,
        ...          params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_SingleNetPositionDetails_resp}

        """
        super(SingleNetPositionDetails, self).__init__(
            NetPositionId=NetPositionId)
        self.params = params


@endpoint("openapi/port/v1/netpositions/me")
class NetPositionsMe(Portfolio):
    """Get netpositions for the logged-in client."""

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a NetPositionsMe request.

        Parameters
        ----------
        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_NetPositionsMe_params}
        >>> r = pf.netpositions.NetPositionsMe(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_NetPositionsMe_resp}

        """
        super(NetPositionsMe, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/netpositions")
class NetPositionsQuery(Portfolio):
    """Get netpositions for a client, account group, account or position.
    Returns a list of net positions fulfilling the criteria specified by the
    query string parameters. Each net position may include all related sub
    positions if fieldGroups includes SubPositions.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a NetPositionsQuery request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_NetPositionsQuery_params}
        >>> r = pf.netpositions.NetPositionsQuery(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_NetPositionsQuery_resp}

        """
        super(NetPositionsQuery, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/netpositions/subscriptions", "POST", 201)
class NetPositionListSubscription(Portfolio):
    """Create a subscription on a list of net positions and make it active.

    Sets up a subscription and returns an initial snapshot of list of net
    positions specified by the parameters in the request.
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a NetPositionListSubscription request.

        Parameters
        ----------
        data: dict (required)
            dict representing the data body parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_NetPositionListSubscription_body}
        >>> r = pf.netpositions.NetPositionListSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_NetPositionListSubscription_resp}

        """
        super(NetPositionListSubscription, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/netpositions/subscriptions/{ContextId}/",
          "DELETE", 202)
class NetPositionSubscriptionRemoveMultiple(Portfolio):
    """Remove multiple all subscriptions for the current session on this
    resource, and frees all resources on the server.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a NetPositionSubscriptionRemoveMultiple request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_NetPositionSubscriptionRemoveMultiple_params}
        >>> ContextId = ...
        >>> r = pf.netpositions.NetPositionSubscriptionRemoveMultiple(
        ...         ContextId,
        ...         params=params)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status

        No data is returned.
        """
        super(NetPositionSubscriptionRemoveMultiple, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/positions/subscriptions/{ContextId}/{ReferenceId}",
          "DELETE", 202)
class NetPositionSubscriptionRemove(Portfolio):
    """Removes subscription for the current session identified by
    subscription id.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a NetPositionSubscriptionRemove request.

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
        >>> ContextId = ...
        >>> ReferenceId = ...
        >>> r = pf.netpositions.NetPositionSubscriptionRemove(
        ...         ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status

        No data is returned.
        """
        super(NetPositionSubscriptionRemove, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
