# -*- encoding: utf-8 -*-

"""Handle referencedata-standarddates endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.standarddates import responses


@endpoint("openapi/ref/v1/standarddates/forwardtenor/{Uic}")
class ForwardTenorDates(ReferenceData):
    """Get a list of forward tenor dates for an UIC."""

    @dyndoc_insert(responses)
    def __init__(self, Uic, params=None):
        """Instantiate a ForwardTenorDates request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_forwardtenordt_params}
        >>> r = rd.ForwardTenorDates(Uic=22, params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_forwardtenordt_resp}

        """
        super(ForwardTenorDates, self).__init__(Uic=Uic)
        self.params = params


@endpoint("openapi/ref/v1/standarddates/fxoptionexpiry/{Uic}")
class FXOptionExpiryDates(ReferenceData):
    """Get a list of FX option expiry dates for an UIC."""

    @dyndoc_insert(responses)
    def __init__(self, Uic):
        """Instantiate a FXOptionExpiryDates request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.FXOptionExpiryDates(Uic='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::

            {_v3_fxoptionexpirydt_resp}

        """
        super(FXOptionExpiryDates, self).__init__(Uic=Uic)
