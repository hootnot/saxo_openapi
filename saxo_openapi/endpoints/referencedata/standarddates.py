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

        Parameters
        ----------
        Uic: int (required)
            the Uic code of the instrument

        params: dict (required)
            dict with parameters representing the querystring


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ForwardTenorDates_params}
        >>> Uic = 22
        >>> r = rd.ForwardTenorDates(Uic=Uic, params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_ForwardTenorDates_resp}

        """
        super(ForwardTenorDates, self).__init__(Uic=Uic)
        self.params = params


@endpoint("openapi/ref/v1/standarddates/fxoptionexpiry/{Uic}")
class FXOptionExpiryDates(ReferenceData):
    """Get a list of FX option expiry dates for an UIC."""

    @dyndoc_insert(responses)
    def __init__(self, Uic):
        """Instantiate a FXOptionExpiryDates request.

        Parameters
        ----------
        Uic: int (required)
            the Uic code of the instrument


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> Uic = 22
        >>> r = rd.FXOptionExpiryDates(Uic=Uic)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_FXOptionExpiryDates_resp}

        """
        super(FXOptionExpiryDates, self).__init__(Uic=Uic)
