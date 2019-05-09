# -*- encoding: utf-8 -*-

"""Handle ens - client activities endpoints."""

from .base import ENS
from ..decorators import dyndoc_insert, endpoint
from .responses.clientactivities import responses


@endpoint("openapi/ens/v1/activities/subscriptions", "POST", 201)
class CreateSubscriptionForClientEvents(ENS):
    """Set up an active subscription to listen client events."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateSubscriptionForClientEvents request.

        Parameters
        ----------
        data : dict (required)
            dict representing the data body, the subscription specification


        body example::

            data = {_v3_CreateSubscriptionForClientEvents_body}


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.eventnotificationservices as ens
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = ...
        >>> r = ens.clientactivities.CreateSubscriptionForClientEvents(data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))


        Output::

            {_v3_CreateSubscriptionForClientEvents_resp}

        """
        super(CreateSubscriptionForClientEvents, self).__init__()
        self.data = data


@endpoint("openapi/ens/v1/activities/subscriptions/{ContextId}/{ReferenceId}",
          "DELETE", 202)
class RemoveSubscription(ENS):
    """Remove subscription for the current session identified by subscription
    id."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveSubscription request.

        Parameters
        ----------
        ContextId : string (required)
            the ContextId of the subscription

        ReferenceId : string (required)
            the ReferenceId of the subscription


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.eventnotificationservices as ens
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ...
        >>> ReferenceId = ...
        >>> r = ens.clientactivities.RemoveSubscription(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_code


        No data is returned.
        """
        super(RemoveSubscription, self).__init__(
             ContextId=ContextId,
             ReferenceId=ReferenceId
        )


@endpoint("openapi/ens/v1/activities/subscriptions/{ContextId}", "DELETE", 202)
class RemoveSubscriptions(ENS):
    """Remove multiple/all subscriptions for the current session on this
    resource and free all resources on the server.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a RemoveSubscriptions request.

        Parameters
        ----------
        ContextId : string (required)
            the ContextId of the subscription

        params : dict (optional)
            dict with querystring parameters


        Example
        -------

        params = {_v3_RemoveSubscriptions_params}

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.eventnotificationservices as ens
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ...
        >>> r = ens.clientactivities.RemoveSubscriptions(ContextId,
        ...                                              params=params)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_code

        No data is returned.
        """
        super(RemoveSubscriptions, self).__init__(ContextId=ContextId)
        self.params = params


@endpoint("openapi/ens/v1/activities")
class GetActivities(ENS):
    """Return a list of activities specified by the parameters in the
    request."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a GetActivities request.

        Parameters
        ----------
        params : dict (required)
            dict with querystring parameters


        Example
        -------

        params = {_v3_GetActivities_params}

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.eventnotificationservices as ens
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = ens.clientactivities.GetActivities(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        """
        super(GetActivities, self).__init__()
        self.params = params
