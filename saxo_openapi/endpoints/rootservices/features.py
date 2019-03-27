# -*- encoding: utf-8 -*-

"""Handle root-services features endpoints."""

from .base import RootService
from ..decorators import dyndoc_insert, endpoint
from .responses.features import responses


@endpoint("openapi/root/v1/features/availability/")
class Availability(RootService):
    """Get the availability of all features."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate an Availability request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices.features as rsft
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rsft.Availability()
        >>> rv = client.request(r)
        >>> print(rv)

        Output::

            {_v3_Availability_resp}

        """
        super(Availability, self).__init__()


@endpoint("openapi/root/v1/features/availability/subscriptions", "POST", 201)
class CreateAvailabilitySubscription(RootService):
    """Create a feature availability subscription."""

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate an CreateAvailabilitySubscription request.

        Parameters
        ----------
        data : JSON (required)
            json body to send


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices.features as rsft
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data =  {_v3_CreateAvailabilitySubscription_body}
        >>> r = rsft.CreateAvailabilitySubscription(data=data)
        >>> rv = client.request(r)
        >>> print(rv)

        Output::

            {_v3_CreateAvailabilitySubscription_resp}

        """
        super(CreateAvailabilitySubscription, self).__init__()
        self.data = data


@endpoint("openapi/root/v1/features/availability/subscriptions/"
          "{ContextId}/{ReferenceId}", "DELETE", 202)
class RemoveAvailabilitySubscription(RootService):
    """Removes the subscription identified by the specified reference id
    (and streaming context id).
    """
    # this endpoint returns an empty string as data: ''
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveAvailabilitySubscription request.

        Parameters
        ----------
        ContextId : string (required)
            the context-id

        ReferenceId : string (required)
            the reference-id


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices.features as rsft
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = '...'
        >>> ReferenceId = '...'
        >>> r = rsft.RemoveAvailabilitySubscription(ContextId=ContextId,
        ...                                         ReferenceId=ReferenceId)
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveAvailabilitySubscription, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
