# -*- encoding: utf-8 -*-

"""Handle referencedata-algostrategies endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import ReferenceData
from .responses.algostrategies import responses


@endpoint("openapi/ref/v1/algostrategies/")
class AlgoStrategies(ReferenceData):
    """Retrieve a list of strategies with detailed information about each
    strategy. The response also contains links to other relevant data, such
    as their parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate an AlgoStrategies request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_AlgoStrategies_params}
        >>> r = rd.algostrategies.AlgoStrategies(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AlgoStrategies_resp}

        """
        super(AlgoStrategies, self).__init__()
        self.params = params


@endpoint("openapi/ref/v1/algostrategies/{Name}")
class AlgoStrategyDetails(ReferenceData):
    """Retrieve detailed information about a specific Strategy."""

    @dyndoc_insert(responses)
    def __init__(self, Name):
        """Instantiate an AlgoStrategyDetails request.

        Parameters
        ----------
        Name: string (required)
            Name of the strategy


        >>> import json
        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.referencedata as rd
        >>> client = saxo_openapi.API(access_token=...)
        >>> Name = "Implementation Shortfall"
        >>> r = rd.algostrategies.AlgoStrategyDetails(Name=Name)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AlgoStrategyDetails_resp}

        """
        super(AlgoStrategyDetails, self).__init__(Name=Name)
