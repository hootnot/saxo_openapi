# -*- encoding: utf-8 -*-

"""Handle portfolio-balances endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.balances import responses


@endpoint("openapi/port/v1/balances/me")
class AccountBalancesMe(Portfolio):
    """Get balance data for a client or an account. Defaults to
    logged-in client.
    """

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate an AccountBalancesMe request.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.balances.AccountBalancesMe()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AccountBalancesMe_resp}

        """
        super(AccountBalancesMe, self).__init__()


@endpoint("openapi/port/v1/balances")
class AccountBalances(Portfolio):
    """Get balance data for a client, account group or an account."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an AccountBalance request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_AccountBalances_params}
        >>> r = pf.balances.AccountBalances(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AccountBalances_resp}

        """
        super(AccountBalances, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/balances/marginoverview/")
class MarginOverview(Portfolio):
    """Get margin overview for a client, account group or an account."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an MarginOverview request.

        Parameters
        ----------
        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_MarginOverview_params}
        >>> r = pf.balances.MarginOverview(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_MarginOverview_resp}

        """
        super(MarginOverview, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/balances/subscriptions", "POST", 201)
class BalanceSubscriptionCreate(Portfolio):
    """Set up a subscription and returns an initial snapshot of a balance."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate an BalanceSubscriptionCreate request.

        Parameters
        ----------
        data: dict (required)
            dict representing the data body parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_BalanceSubscriptionCreate_body}
        >>> r = pf.balances.BalanceSubscriptionCreate(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_BalanceSubscriptionCreate_resp}

        """
        super(BalanceSubscriptionCreate, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/balances/subscriptions/{ContextId}", "DELETE", 201)
class BalanceSubscriptionRemoveByTag(Portfolio):
    """Remove multiple subscriptions for the current session on this
    resource and frees all resources on the server.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params):
        """Instantiate an BalanceSubscriptionRemoveByTag request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        params: dict (required)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_BalanceSubscriptionRemoveByTag_params}
        >>> ContextId = "explorer_1551792578055"
        >>> r = pf.BalanceSubscriptionRemoveByTag(ContextId=ContextId,
        ...                                       params=params)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_code

        No data is returned.
        """
        super(BalanceSubscriptionRemoveByTag, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/balances/subscriptions/"
          "{ContextId}/{ReferenceId}", "DELETE", 201)
class BalanceSubscriptionRemoveById(Portfolio):
    """Removes subscription for the current session identified by
    subscription id.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate an BalanceSubscriptionRemoveById request.

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
        >>> ContextId = "explorer_1551792578055"
        >>> ReferenceId = "G_953"
        >>> r = pf.BalanceSubscriptionRemoveById(ContextId=ContextId,
        ...                                      ReferenceId=ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_code

        No data is returned.
        """
        super(BalanceSubscriptionRemoveById, self).__init__(
              ContextId=ContextId,
              ReferenceId=ReferenceId)
