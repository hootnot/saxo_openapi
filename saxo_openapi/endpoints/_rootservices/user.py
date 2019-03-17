# -*- encoding: utf-8 -*-

"""Handle root-services user endpoints."""

from .base import RootService
from ..decorators import dyndoc_insert, endpoint
from .responses.user import responses


@endpoint("openapi/root/v1/user/")
class User(RootService):
    """Get information of current user."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a User request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.user.User()
        >>> rv = client.request(r)
        >>> print(rv)

        Output::

            {_v3_User_resp}

        """
        super(User, self).__init__()
