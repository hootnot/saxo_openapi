# -*- encoding: utf-8 -*-

"""Handle portfolio-users endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.users import responses


@endpoint("openapi/port/v1/users/me")
class UsersMe(Portfolio):
    """Get details about the logged in user."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a UsersMe request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.users.UsersMe()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_UsersMe_resp}

        """
        super(UsersMe, self).__init__()


@endpoint("openapi/port/v1/users")
class Users(Portfolio):
    """Get all users under a particular owner."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a Users request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_Users_params}
        >>> r = pf.users.Users(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_Users_resp}

        """
        super(Users, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/users/{UserKey}")
class UserDetails(Portfolio):
    """Get the details about a user."""

    @dyndoc_insert(responses)
    def __init__(self, UserKey):
        """Instantiate a UserDetails request.

        Parameters
        ----------
        UserKey: string (required)
            the UserKey


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> UserKey = '...'
        >>> r = pf.users.Users(UserKey=UserKey)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_UserDetails_resp}

        """
        super(UserDetails, self).__init__(UserKey=UserKey)


@endpoint("openapi/port/v1/users/me", "PATCH", 204)
class UserUpdate(Portfolio):
    """Enables the user to update preferred language, culture and timezone."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a UserUpdate request.

        Parameters
        ----------
        data: dict (required)
            dict representing the data body parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_UserUpdate_body}
        >>> r = pf.users.UserUpdate(data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(UserUpdate, self).__init__()
        self.data = data
