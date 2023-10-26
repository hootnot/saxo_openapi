# -*- encoding: utf-8 -*-

"""Handle referencedata-currencypairs endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.currencypairs import responses


@endpoint("openapi/ref/v1/currencypairs/")
class CurrencyPairs(ReferenceData):
    """Get data on currency pairs."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Currency Pairs request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.currencies.CurrencyPairs()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_CurrencyPairs_resp}

        """
        super(CurrencyPairs, self).__init__()
