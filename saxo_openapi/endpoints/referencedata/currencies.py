# -*- encoding: utf-8 -*-

"""Handle referencedata-currencies endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.currencies import responses


@endpoint("openapi/ref/v1/currencies/")
class Currencies(ReferenceData):
    """Get a list all supported currencies."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Currencies request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.currencies.Currencies()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_Currencies_resp}

        """
        super(Currencies, self).__init__()
