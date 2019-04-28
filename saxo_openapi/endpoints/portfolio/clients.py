# -*- encoding: utf-8 -*-

"""Handle portfolio-clients endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.clients import responses


@endpoint("openapi/port/v1/clients/me")
class ClientDetailsMe(Portfolio):
    """Get details about logged-in user's client."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a ClientDetailsMe request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.clients.ClientDetailsMe()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClientDetailsMe_resp}

        """
        super(ClientDetailsMe, self).__init__()


@endpoint("openapi/port/v1/clients/{ClientKey}")
class ClientDetails(Portfolio):
    """Get details about a client."""

    @dyndoc_insert(responses)
    def __init__(self, ClientKey):
        """Instantiate a ClientDetails request.

        Parameters
        ----------
        ClientKey: string (required)
            the ClientKey


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA'
        >>> r = pf.clients.ClientDetails(ClientKey=ClientKey)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClientDetails_resp}

        """
        super(ClientDetails, self).__init__(ClientKey=ClientKey)


@endpoint("openapi/port/v1/clients/me", "PATCH", 204)
class ClientDetailsUpdate(Portfolio):
    """Enables user of the client to switch position netting
    mode of its own.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a ClientDetailsUpdate request.

        Parameters
        ----------
        data: dict (required)
            dict with parameters representing the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ClientDetailsUpdate_body}
        >>> r = pf.clients.ClientDetailsUpdate(data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(ClientDetailsUpdate, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/clients/")
class ClientDetailsByOwner(Portfolio):
    """Get details about clients under a particular owner."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a ClientDetailsByOwner request.

        Parameters
        ----------
        params: dict (required)
            the dict representing the querystring parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ClientDetailsByOwner_params}
        >>> r = pf.clients.ClientDetailsByOwner(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_ClientDetailsByOwner_resp}

        """
        super(ClientDetailsByOwner, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/clients/", "PATCH", 204)
class ClientSwitchPosNettingMode(Portfolio):
    """Enables IB to switch position netting mode and change account
    value protection limit on behalf of its clients.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, params, data):
        """Instantiate a ClientSwitchPosNettingMode request.

        Parameters
        ----------
        params: dict (required)
            the dict representing the querystring parameters.

        data: dict (required)
            the dict representing the data body parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ClientSwitchPosNettingMode_params}
        >>> data = {_v3_ClientSwitchPosNettingMode_body}
        >>> r = pf.clients.ClientSwitchPosNettingMode(params=params, data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(ClientSwitchPosNettingMode, self).__init__()
        self.params = params
        self.data = data
