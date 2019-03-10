# -*- encoding: utf-8 -*-

"""Handle portfolio-exposure endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.exposure import responses


@endpoint("openapi/port/v1/exposure/instruments/me")
class NetInstrumentsExposureMe(Portfolio):
    """Returns a list instruments and net exposures."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a NetInstrumentsExposureMe request.

        Parameters
        ----------
        None


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.exposure.NetInstrumentsExposureMe()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_NetInstrumentsExposureMe_resp}

        """
        super(NetInstrumentsExposureMe, self).__init__()


@endpoint("openapi/port/v1/exposure/instruments/")
class NetInstrumentExposureSpecific(Portfolio):
    """Returns a list instruments and net exposures."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a NetInstrumentExposureSpecific request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_NetInstrumentExposureSpecific_params}
        >>> r = pf.exposure.NetInstrumentExposureSpecific(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_NetInstrumentExposureSpecific_resp}

        """
        super(NetInstrumentExposureSpecific, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/exposure/instruments/subscriptions", "POST", 201)
class CreateExposureSubscription(Portfolio):
    """Sets up a subscription and returns an initial snapshot of list of
    instrument exposure specified by the parameters in the request.
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateExposureSubscription request.

        Parameters
        ----------
        data: dict (required)
            dict representing the body with request parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateExposureSubscription_body}
        >>> r = pf.exposure.CreateExposureSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_CreateExposureSubscription_resp}

        """
        super(CreateExposureSubscription, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/exposure/instruments/"
          "subscriptions/{ContextId}/", "DELETE", 202)
class RemoveExposureSubscriptionsByTag(Portfolio):
    """Removes multiple all subscriptions for the current session on
    this resource, and frees all resources on the server.
    """

    RESPONSE_TYPE = 'text'

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a RemoveExposureSubscriptionsByTag request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_RemoveExposureSubscriptionsByTag_params}
        >>> ContextId = 'explorer_1552035128308'
        >>> r = pf.exposure.RemoveExposureSubscriptionsByTag(ContextId,
        ...                                                  params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        No data returned.
        """
        super(RemoveExposureSubscriptionsByTag, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/exposure/instruments/"
          "subscriptions/{ContextId}/{ReferenceId}", "DELETE", 202)
class RemoveExposureSubscription(Portfolio):
    """Removes subscription for the current session identified by
    subscription id.
    """

    RESPONSE_TYPE = 'text'

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveExposureSubscription request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        ReferenceId: string (required)
            the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.exposure.RemoveExposureSubscription(ContextId, ReferenceId)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        No data returned.
        """
        super(RemoveExposureSubscription, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)


@endpoint("openapi/port/v1/exposure/currency/me")
class CurrencyExposureMe(Portfolio):
    """Returns a list of currencies and net exposures."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a CurrencyExposureMe request.

        Parameters
        ----------
        None


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.exposure.CurrencyExposureMe()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_CurrencyExposureMe_resp}

        """
        super(CurrencyExposureMe, self).__init__()


@endpoint("openapi/port/v1/exposure/currency/")
class CurrencyExposureSpecific(Portfolio):
    """Returns a list of currencies in which there is an exposure."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a CurrencyExposureSpecific request.

        Parameters
        ----------
        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_CurrencyExposureSpecific_params}
        >>> r = pf.exposure.CurrencyExposureSpecific(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_CurrencyExposureSpecific_resp}

        """
        super(CurrencyExposureSpecific, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/exposure/fxspot/me")
class FxSpotExposureMe(Portfolio):
    """Returns a list of currencies and net exposures."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a FxSpotExposureMe request.

        Parameters
        ----------
        None


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.exposure.FxSpotExposureMe()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_FxSpotExposureMe_resp}

        """
        super(FxSpotExposureMe, self).__init__()


@endpoint("openapi/port/v1/exposure/fxspot/")
class FxSpotExposureSpecific(Portfolio):
    """Returns a list of currencies in which there is an exposure."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a FxSpotExposureSpecific request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_FxSpotExposureSpecific_params}
        >>> r = pf.exposure.FxSpotExposureSpecific(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_FxSpotExposureSpecific_resp}

        """
        super(FxSpotExposureSpecific, self).__init__()
        self.params = params
