# -*- encoding: utf-8 -*-

"""Handle referencedata-languages endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.languages import responses


@endpoint("openapi/ref/v1/languages/")
class Languages(ReferenceData):
    """Get a list containing all the languages supported by Saxo Bank."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Languages request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.languages.Languages()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_Languages_resp}

        """
        super(Languages, self).__init__()
