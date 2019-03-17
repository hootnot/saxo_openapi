# -*- encoding: utf-8 -*-

"""Handle trading-allocationkeys endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.allocationkeys import responses


@endpoint("openapi/trade/v1/allocationkeys", "GET")
class GetAllocationKeys(Trading):
    """Get a list of existing allocation keys. By default only Active
    allocation keys for the current client are returned.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a GetAllocationKeys request.

        Parameters
        ----------
        params : dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_GetAllocationKeys_params}
        >>> r = tr.allocationkeys.GetAllocationKeys(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_GetAllocationKeys_resp}

        """
        super(GetAllocationKeys, self).__init__()
        self.params = params


@endpoint("openapi/trade/v1/allocationkeys/{AllocationKeyId}", "GET")
class GetAllocationKeyDetails(Trading):
    """Get detailed information about an allocation key."""

    @dyndoc_insert(responses)
    def __init__(self, AllocationKeyId):
        """Instantiate a GetAllocationKeyDetails request.

        Parameters
        ----------
        AllocationKeyId : string (required)
            the allocation key id.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> AllocationKeyId = 227
        >>> r = tr.allocationkeys.GetAllocationKeyDetails(
        ...     AllocationKeyId=AllocationKeyId)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_GetAllocationKeyDetails_resp}

        """
        super(GetAllocationKeyDetails, self).__init__(
            AllocationKeyId=AllocationKeyId)


@endpoint("openapi/trade/v1/allocationkeys", "POST", 201)
class CreateAllocationKey(Trading):
    """Create an allocation key."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateAllocationKey request.

        Parameters
        ----------
        data : dict (required)
            dict representing the parameters of the requestbody.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateAllocationKey_body}
        >>> r = tr.allocationkeys.CreateAllocationKey(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_CreateAllocationKey_resp}

        """
        super(CreateAllocationKey, self).__init__()
        self.data = data


@endpoint("openapi/trade/v1/allocationkeys/{AllocationKeyId}", "DELETE", 204)
class DeleteAllocationKey(Trading):
    """Delete an allocation key."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, AllocationKeyId):
        """Instantiate a DeleteAllocationKey request.

        Parameters
        ----------
        AllocationKeyId : string (required)
            the allocation key id.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> AllocationKeyId = 227
        >>> r = tr.allocationkeys.DeleteAllocationKey(
        ...     AllocationKeyId=AllocationKeyId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status
        """
        super(DeleteAllocationKey, self).__init__(
            AllocationKeyId=AllocationKeyId)
