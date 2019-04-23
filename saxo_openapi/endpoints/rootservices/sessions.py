# -*- encoding: utf-8 -*-

"""Handle root-services sessions endpoints."""

from .base import RootService
from ..decorators import dyndoc_insert, endpoint
from .responses.sessions import responses


@endpoint("openapi/root/v1/sessions/capabilities/")
class GetSessionCapabilities(RootService):
    """Get the sessions capabilities."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a GetSessionCapabilities request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.sessions.GetSessionCapabilities()
        >>> rv = client.request(r)
        >>> print(rv)

        Output::

            {_v3_GetSessionCapabilities_resp}

        """
        super(GetSessionCapabilities, self).__init__()


@endpoint("openapi/root/v1/sessions/capabilities/", "PUT", 202)
class ChangeSessionCapabilities(RootService):
    """Change sessions capabilities."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a ChangeSessionCapabilities request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ChangeSessionCapabilities_body}
        >>> r = rs.sessions.ChangeSessionCapabilities(data=data)
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned
        """
        super(ChangeSessionCapabilities, self).__init__()
        self.data = data


@endpoint("openapi/root/v1/sessions/events/subscriptions/", "POST", 201)
class CreateSessionCapabilitiesSubscription(RootService):
    """Set up a new session capabilities subscription. The data stream will
    deliver updates from this point."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a ChangeSessionCapabilitiesSubscription request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateSessionCapabilitiesSubscription_body}
        >>> r = rs.sessions.ChangeSessionCapabilitiesSubscription(data=data)
        >>> rv = client.request(r)
        >>> print(rv)

        Output::

            {_v3_CreateSessionCapabilitiesSubscription_resp}

        """
        super(CreateSessionCapabilitiesSubscription, self).__init__()
        self.data = data


@endpoint("openapi/root/v1/sessions/events/subscriptions/"
          "{ContextId}/{ReferenceId}",
          "DELETE", 202)
class RemoveSessionCapabilitiesSubscription(RootService):
    """Removes the subscription identified by the specified reference id.
    (and streaming context id)."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveSessionCapabilitiesSubscription request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.sessions.RemoveSessionCapabilitiesSubscripion(
        ...      ContextId=ContextId,
        ...      ReferenceId=ReferenceId)
        >>> rv = client.request(r)
        >>> assert rv.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveSessionCapabilitiesSubscription, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
