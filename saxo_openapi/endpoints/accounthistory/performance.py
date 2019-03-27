# -*- encoding: utf-8 -*-

"""Handle accounthistory-performance endpoints."""

from .base import AccountHistory
from ..decorators import dyndoc_insert, endpoint
from .responses.performance import responses


@endpoint("openapi/hist/v3/perf/{ClientKey}")
class AccountPerformance(AccountHistory):
    """Get a collection of performance metrics for a specific account.
    The account performance returns confidencial information that is only
    allowed to be viewed by the account owner / owners. The required fields
    are ClientKey and either StandardPeriod or FromDate/ToDate.
    """

    @dyndoc_insert(responses)
    def __init__(self, ClientKey, params=None):
        """Instantiate an AccountPerformance request.

        Parameters
        ----------
        ClientKey: string (required)
            the ClientKey

        params: dict (optional)
            dict with parameters representing the queringstring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.accounthistory as ah
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
        >>> params = {_v3_AccountPerformance_params}
        >>> r = ah.performance.AccountPerformance(ClientKey=ClientKey,
        ...                                       params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_AccountPerformance_resp}

        """
        super(AccountPerformance, self).__init__(ClientKey=ClientKey)
        self.params = params
