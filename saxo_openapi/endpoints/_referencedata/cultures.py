# -*- encoding: utf-8 -*-

"""Handle referencedata-cultures endpoints."""

from ..decorators import endpoint
from .base import ReferenceData
from .responses.cultures import responses


@endpoint("openapi/ref/v1/cultures/")
class Cultures(ReferenceData):
    """Get a list all the cultures for user preference localization
    supported by Saxo Bank.
    """

    def __init__(self):
        """Instantiate a Cultures request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.Cultures()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(Cultures, self).__init__()
