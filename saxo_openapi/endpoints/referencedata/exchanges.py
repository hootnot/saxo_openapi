# -*- encoding: utf-8 -*-

"""Handle referencedata-exchanges endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.exchanges import responses


@endpoint("openapi/ref/v1/exchanges/")
class ExchangeList(ReferenceData):
    """Retrieve a list of exchanges with detailed information about each.
    The response also contains links to other relevant data, such as their
    trade statuses.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate an ExchangeList request.

        Parameters
        ----------
        params: dict (optional)
            dict representing querystring parameters


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.ExchangeList()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_ExchangeList_resp}

        """
        super(ExchangeList, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/exchanges/{ExchangeId}")
class ExchangeDetails(ReferenceData):
    """Retrieves detailed information about a specific exchange."""

    @dyndoc_insert(responses)
    def __init__(self, ExchangeId):
        """Instantiate an ExchangeDetails request.

        Parameters
        ----------
        ExchangeId: string (required)
            the ExchangeId


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> ExchangeId = '...'
        >>> r = rd.ExchangeDetails(ExchangeId=ExchangeId)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_ExchangeDetails_resp}

        """
        super(ExchangeDetails, self).__init__(ExchangeId=ExchangeId)
