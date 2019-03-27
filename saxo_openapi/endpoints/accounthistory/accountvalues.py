# -*- encoding: utf-8 -*-

"""Handle accounthistory-accountvalues endpoints."""

from .base import AccountHistory
from ..decorators import dyndoc_insert, endpoint
from .responses.accountvalues import responses


@endpoint("openapi/hist/v3/accountValues/{ClientKey}/")
class AccountSummary(AccountHistory):
    """Get 'rolled up performance' for the accounts of specified client."""

    @dyndoc_insert(responses)
    def __init__(self, ClientKey, params=None):
        """Instantiate an AccountSummary request.

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
        >>> r = ah.accountvalues.AccountSummary(ClientKey=ClientKey)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

            {_v3_AccountSummary_resp}

        """
        super(AccountSummary, self).__init__(ClientKey=ClientKey)
        self.params = params
