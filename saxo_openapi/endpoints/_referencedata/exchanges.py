# -*- encoding: utf-8 -*-
"""Handle referencedata-exchanges endpoints."""
from ..decorators import endpoint
from .base import ReferenceData
from .responses.exchanges import responses


@endpoint("openapi/ref/v1/exchanges/")
class ExchangeList(ReferenceData):
    """Retrieve a list of exchanges with detailed information about each.
    The response also contains links to other relevant data, such as their
    trade statuses.
    """

    def __init__(self, params=None):
        """Instantiate an ExchangeList request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.ExchangeList()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))
        """
        super(ExchangeList, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/exchanges/{ExchangeId}")
class ExchangeDetails(ReferenceData):
    """Retrieves detailed information about a specific exchange."""

    def __init__(self, ExchangeId):
        """Instantiate an ExchangeDetails request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.ExchangeDetails(ExchangeId='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        """
        super(ExchangeDetails, self).__init__(ExchangeId=ExchangeId)
