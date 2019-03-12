# -*- encoding: utf-8 -*-

"""Handle trading-positions endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.positions import responses


@endpoint("openapi/trade/v1/positions", "POST", 201)
class PositionByQuote(Trading):
    """Creates a new position by accepting a quote.

    The quote must be the most recent one and it must be tradable:
    (Quote.PriceType=PriceType.Tradable).
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a PositionByQuote request.

        Parameters
        ----------
        data : dict (required)
            dict representing the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_PositionByQuote_body}
        >>> r = tr.positions.PositionByQuote(data=data)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_PositionByQuote_resp}

        """
        super(PositionByQuote, self).__init__()
        self.data = data


@endpoint("openapi/trade/v1/positions/{PositionId}", "PATCH", 204)
class UpdatePosition(Trading):
    """Updates properties of an existing position. This is only relevant for
    FX Options, where you can update the Exercise method.
    """

    @dyndoc_insert(responses)
    def __init__(self, PositionId, data):
        """Instantiate an UpdatePosition request.

        Parameters
        ----------
        PositionId: string (required)
            the position id

        data : dict (required)
            dict representing the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_UpdatePosition_body}
        >>> PositionId = 1019942425
        >>> r = tr.positions.UpdatePosition(PositionId, data=data)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_UpdatePosition_resp}

        """
        super(UpdatePosition, self).__init__(PositionId=PositionId)
        self.data = data


@endpoint("openapi/trade/v1/positions/{PositionId}/exercise", "PUT", 204)
class ExercisePosition(Trading):
    """Forces exercise of a position. This is relevant for Futures Options,
    Stock Options, Stock Index Options.
    """

    @dyndoc_insert(responses)
    def __init__(self, PositionId, data):
        """Instantiate an ExercisePosition request.

        Parameters
        ----------
        PositionId: string (required)
            the position id

        data : dict (required)
            dict representing the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ExercisePosition_body}
        >>> PositionId = 1019942425
        >>> r = tr.positions.ExercisePosition(PositionId, data=data)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_ExercisePosition_resp}

        """
        super(ExercisePosition, self).__init__(PositionId=PositionId)
        self.data = data


@endpoint("openapi/trade/v1/positions/exercise", "PUT", 204)
class ExerciseAmount(Trading):
    """Forces exercise of an amount across all positions for the specified
    UIC. This is relevant for Futures Options, Stock Options, Stock Index
    Options.
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate an ExerciseAmount request.

        Parameters
        ----------
        data : dict (required)
            dict representing the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ExerciseAmount_body}
        >>> r = tr.positions.ExerciseAmount(data=data)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_ExerciseAmount_resp}

        """
        super(ExerciseAmount, self).__init__()
        self.data = data
