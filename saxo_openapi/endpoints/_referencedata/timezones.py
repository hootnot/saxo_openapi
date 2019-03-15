# -*- encoding: utf-8 -*-

"""Handle referencedata-timezones endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.timezones import responses


@endpoint("openapi/ref/v1/timezones/")
class TimeZones(ReferenceData):
    """Get a list all the time zones supported by Saxo Bank."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a TimeZones request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.timezones.TimeZones()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_TimeZones_resp}

        """
        super(TimeZones, self).__init__()
