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

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_instruments_params}
        >>> r = rd.instruments.Instruments(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_instruments_resp}

        """
        super(Instruments, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/instruments/details")
class InstrumentsDetails(ReferenceData):
    """Get detailed information on a list of instruments."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an InstrumentsDetails request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_instrumentsdetails_params}
        >>> r = rd.instruments.InstrumentsDetails(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_instrumentsdetails_resp}

        """
        super(InstrumentsDetails, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/instruments/details/{Uic}/{AssetType}")
class InstrumentDetails(ReferenceData):
    """Get detailed information for a specific instrument."""

    @dyndoc_insert(responses)
    def __init__(self, Uic, AssetType, params):
        """Instantiate an InstrumentDetails request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_instrumentdetails_params}
        >>> r = rd.instruments.InstrumentDetails(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_instrumentdetails_resp}

        """
        super(InstrumentDetails, self).__init__(Uic=Uic,
                                                AssetType=AssetType)
        self.params = params
