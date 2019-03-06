# -*- encoding: utf-8 -*-

"""Handle referencedata-countries endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.countries import responses


@endpoint("openapi/ref/v1/countries/")
class Countries(ReferenceData):
    """Retrieve a list all the countries supported by Saxo Bank."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Countries request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.countries.Countries()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_Countries_resp}

        """
        super(Countries, self).__init__()
