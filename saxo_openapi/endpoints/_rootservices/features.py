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

        ::
            {_v3_availability_resp}

        """
        super(Availability, self).__init__()


@endpoint("openapi/root/v1/features/availability/subscriptions", "POST", 201)
class CreateAvailabilitySubscription(RootService):
    """Create a feature availability subscription."""

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate an AvailabilitySubscription request.

        Parameters
        ----------
        data : JSON (required)
            json body to send

        data example::
            {_v3_availability_subscr_body}

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices.features as rsft
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rsft.CreateAvailabilitySubscription(data=data)
        >>> rv = client.request(r)
        >>> print(rv)

        ::
            {_v3_availability_subscr_resp}

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
    RESPONSE_DATA = 'text'

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
        >>> params = {_v3_availability_subscr_remove_params}
        >>> r = rsft.RemoveAvailabilitySubscription(**params)
        >>> rv = client.request(r)

        Response is empty text string, status_code = 202 when accepted.

        """
        super(RemoveAvailabilitySubscription, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
