# -*- encoding: utf-8 -*-
"""Handle account endpoints."""
from ..apirequest import APIRequest
from ..decorators import dyndoc_insert, endpoint
from ..responses.referencedata import responses
from abc import abstractmethod


class ReferenceData(APIRequest):
    """Reference - class to handle the reference endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    # @dyndoc_insert(responses)
    def __init__(self, ExchangeId=None, Name=None, Uic=None):
        """Instantiate a ReferenceData APIRequest instance.

        Parameters
        ----------
        ExchangeId : string (optional)
            exchange ID

        """
        endpoint = self.ENDPOINT.format(ExchangeId=ExchangeId,
                                        Uic=Uic,
                                        Name=Name)
        super(ReferenceData, self).__init__(endpoint, method=self.METHOD)


@endpoint("sim/openapi/ref/v1/algostrategies/")
class AlgoStrategies(ReferenceData):
    """Retrieve a list of strategies with detailed information about each
    strategy. The response also contains links to other relevant data, such
    as their parameters.
    """

    # @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate an AlgoStrategies request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.AlgoStrategies()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AlgoStrategies, self).__init__()
        self.params = params


@endpoint("sim/openapi/ref/v1/algostrategies/{Name}")
class AlgoStrategyDetails(ReferenceData):
    """Retrieve detailed information about a specific Strategy."""

    # @dyndoc_insert(responses)
    def __init__(self, Name):
        """Instantiate an AlgoStrategyDetails request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.AlgoStrategyDetails(Name='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AlgoStrategyDetails, self).__init__(Name=Name)


@endpoint("sim/openapi/ref/v1/countries/")
class Countries(ReferenceData):
    """Retrieve a list all the countries supported by Saxo Bank."""

    # @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Countries request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.Countries()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(Countries, self).__init__()


@endpoint("sim/openapi/ref/v1/cultures/")
class Cultures(ReferenceData):
    """Get a list all the cultures for user preference localization
    supported by Saxo Bank.
    """

    # @dyndoc_insert(responses)
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


@endpoint("sim/openapi/ref/v1/currencies/")
class Currencies(ReferenceData):
    """Get a list all supported currencies."""

    # @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate an AccountList request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.Currencies()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(Currencies, self).__init__()


@endpoint("sim/openapi/ref/v1/exchanges/")
class ExchangeList(ReferenceData):
    """Retrieve a list of exchanges with detailed information about each.
    The response also contains links to other relevant data, such as their
    trade statuses.
    """

    # @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate an ExchangeList request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.ExchangeList()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(ExchangeList, self).__init__()


@endpoint("sim/openapi/ref/v1/exchanges/{ExchangeId}")
class ExchangeDetails(ReferenceData):
    """Retrieves detailed information about a specific exchange."""

    # @dyndoc_insert(responses)
    def __init__(self, ExchangeId):
        """Instantiate an ExchangeDetails request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.ExchangeDetails(ExchangeId='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(ExchangeDetails, self).__init__(ExchangeId=ExchangeId)


@endpoint("sim/openapi/ref/v1/instruments/")
class Instruments(ReferenceData):
    """Get a list of summary information for all instruments and options
    on the Saxo Trading platform restricted by the access rights of the user.
    """

    # @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an Instruments request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.Instruments()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(Instruments, self).__init__()
        self.params = params


@endpoint("sim/openapi/ref/v1/instruments/details")
class InstrumentsDetails(ReferenceData):
    """Get detailed information on a list of instruments."""

    # @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an InstrumentsDetails request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.InstrumentsDetails(params={...})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(InstrumentsDetails, self).__init__()
        self.params = params


@endpoint("sim/openapi/ref/v1/languages/")
class Languages(ReferenceData):
    """Get a list containing all the languages supported by Saxo Bank."""

    # @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a Languages request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.Languages(params={...})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(Languages, self).__init__()


@endpoint("sim/openapi/ref/v1/standarddates/forwardtenor/{Uic}")
class ForwardTenorDates(ReferenceData):
    """Get a list of forward tenor dates for an UIC."""

    # @dyndoc_insert(responses)
    def __init__(self, Uic, params=None):
        """Instantiate a ForwardTenorDates request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.ForwardTenorDates(Uic='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(ForwardTenorDates, self).__init__(Uic=Uic)
        self.params = params


@endpoint("sim/openapi/ref/v1/standarddates/fxoptionexpiry/{Uic}")
class FXOptionExpiryDates(ReferenceData):
    """Get a list of FX option expiry dates for an UIC."""

    # @dyndoc_insert(responses)
    def __init__(self, Uic):
        """Instantiate a FXOptionExpiryDates request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.FXOptionExpiryDates(Uic='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(FXOptionExpiryDates, self).__init__(Uic=Uic)


@endpoint("sim/openapi/ref/v1/timezones/")
class TimeZones(ReferenceData):
    """Get a list all the time zones supported by Saxo Bank."""

    # @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a TimeZones request.

        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rd.TimeZones()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(TimeZones, self).__init__()
