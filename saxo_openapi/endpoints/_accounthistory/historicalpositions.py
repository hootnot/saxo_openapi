# -*- encoding: utf-8 -*-

"""Handle account endpoints."""

from .base import AccountHistory
from ..decorators import dyndoc_insert, endpoint
from .responses.historicalpositions import responses


@endpoint("openapi/hist/v3/positions/{ClientKey}")
class HistoricalPositions(AccountHistory):
    """Get a list of historical positions for a specific account owned
    by a client. The required fields are ClientKey and either StandardPeriod
    or FromDate/ToDate.
    """

    @dyndoc_insert(responses)
    def __init__(self, ClientKey, params):
        """Instantiate a HistoricalPositions request.

        Parameters
        ----------
        ClientKey: string (required)
            the ClientKey

        params: dict (required)
            dict with parameters representing the queringstring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.accounthistory as ah
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        >>> params = {_v3_HistoricalPositions_params}
        >>> r = ah.historicalpositions.HistoricalPositions(ClientKey=ClientKey,
        ...                                                params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_HistoricalPositions_resp}

        """
        super(HistoricalPositions, self).__init__(ClientKey=ClientKey)
        self.params = params
