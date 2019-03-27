# -*- encoding: utf-8 -*-

"""Handle root-services subscriptions endpoints."""

from .base import RootService
from ..decorators import dyndoc_insert, endpoint
from .responses.subscriptions import responses


@endpoint("openapi/root/subscriptions/{ContextId}", "DELETE", 202)
class RemoveMultipleActiveSubscriptions(RootService):
    """Removes multiple subscriptions for the current session, and frees all
    resources on the server.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params):
        """Instantiate a User request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ''
        >>> params = {_v3_RemoveMultipleActiveSubscriptions_params}
        >>> r = rs.subscriptions.RemoveMultipleActiveSubscriptions(
        ...          ContextId, params=params)
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveMultipleActiveSubscriptions, self).__init__(
            ContextId=ContextId)
        self.params = params
