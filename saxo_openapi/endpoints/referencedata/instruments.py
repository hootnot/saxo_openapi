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

        Output::

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

        Output::

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

        Output::

            {_v3_InstrumentDetails_resp}

        """
        super(InstrumentDetails, self).__init__(Uic=Uic,
                                                AssetType=AssetType)
        self.params = params


@endpoint("openapi/ref/v1/instruments/contractoptionspaces/{OptionRootId}")
class ContractoptionSpaces(ReferenceData):
    """Get contractoption data."""

    @dyndoc_insert(responses)
    def __init__(self, OptionRootId, params=None):
        """Instantiate a ContractoptionSpaces request.

        Parameters
        ----------
        OptionRootId: string (required)
            the OptionRootId

        params: dict (optional)
            dict representing querystring parameters


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> OptionRootId = 231
        >>> params = {_v3_ContractoptionSpaces_params}
        >>> r = rd.instruments.ContractoptionSpaces(
        ...                          OptionRootId=OptionRootId,
        ...                          params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_ContractoptionSpaces_resp}

        """
        super(ContractoptionSpaces, self).__init__(
            OptionRootId=OptionRootId)
        self.params = params


@endpoint("openapi/ref/v1/instruments/futuresspaces/{ContinuousFuturesUic}")
class FuturesSpaces(ReferenceData):
    """Get futures spaces data."""

    # @dyndoc_insert(responses)
    def __init__(self, ContinuousFuturesUic):
        """Instantiate a ContractoptionSpaces request.

        Parameters
        ----------
        ContinuousFuturesUic: string (required)
            the ContinuousFuturesUic


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContinuousFuturesUic = '...'
        >>> r = rd.instruments.FuturesSpaces(
        ...                   ContinuousFuturesUic=ContinuousFuturesUic)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_FuturesSpaces_resp}

        """
        super(FuturesSpaces, self).__init__(
            ContinuousFuturesUic=ContinuousFuturesUic)


@endpoint("openapi/ref/v1/instruments/tradingschedule/{Uic}/{AssetType}")
class TradingSchedule(ReferenceData):
    """Get TradingSchedule data."""

    # @dyndoc_insert(responses)
    def __init__(self, Uic, AssetType):
        """Instantiate a TradingSchedule request.

        Parameters
        ----------
        Uic: string (required)
            the Uic of the instrument

        AssetType: string (required)
            the AssetType of the instrument

        For one Uic multiple assettypes can be available trading
        on different times.


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> Uic = 21
        >>> AssetType = "FxSpot"
        >>> r = rd.instruments.ContractoptionSpaces(
        ...                          Uic=Uic,
        ...                          AssetType=AssetType)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_TradingSchedule_resp}

        """
        super(TradingSchedule, self).__init__(
            Uic=Uic,
            AssetType=AssetType)
