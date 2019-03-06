# -*- encoding: utf-8 -*-

"""Handle referencedata-instruments endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.instruments import responses


@endpoint("openapi/ref/v1/instruments/")
class Instruments(ReferenceData):
    """Get a list of summary information for all instruments and options
    on the Saxo Trading platform restricted by the access rights of the user.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an Instruments request.

        Parameters
        ----------
        params: dict (required)
            dict reppresenting the querystring parameters

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_Instruments_params}
        >>> r = rd.instruments.Instruments(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_Instruments_resp}

        """
        super(Instruments, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/instruments/details")
class InstrumentsDetails(ReferenceData):
    """Get detailed information on a list of instruments."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an InstrumentsDetails request.

        Parameters
        ----------
        params: dict (required)
            dict reppresenting the querystring parameters

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_InstrumentsDetails_params}
        >>> r = rd.instruments.InstrumentsDetails(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_InstrumentsDetails_resp}

        """
        super(InstrumentsDetails, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/instruments/details/{Uic}/{AssetType}")
class InstrumentDetails(ReferenceData):
    """Get detailed information for a specific instrument."""

    @dyndoc_insert(responses)
    def __init__(self, Uic, AssetType, params=None):
        """Instantiate an InstrumentDetails request.

        Parameters
        ----------
        Uic: int (required)
            the Uic of the instrument
        AssetType: string (required)
            the AssetType specification
        params: dict (optional)
            dict representing querystring parameters

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> Uic = 22
        >>> AssetType = 'FxSpot'
        >>> params = {_v3_InstrumentDetails_params}
        >>> r = rd.instruments.InstrumentDetails(Uic=Uic,
        ...                                      AssetType=AssetType,
        ...                                      params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_InstrumentDetails_resp}

        """
        super(InstrumentDetails, self).__init__(Uic=Uic,
                                                AssetType=AssetType)
        self.params = params
