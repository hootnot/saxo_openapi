# -*- encoding: utf-8 -*-

"""Handle portfolio-account endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.accounts import responses


@endpoint("openapi/port/v1/accounts/{AccountKey}")
class AccountDetails(Portfolio):
    """Get details about a single account."""

    @dyndoc_insert(responses)
    def __init__(self, AccountKey):
        """Instantiate an AccountDetails request.

        Parameters
        ----------
        AccountKey : string (required)
            Account key to perform the request on.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.AccountDetails(AccountKey=...)
        >>> rv = client.request(r)
        >>> pprint(rv)

        ::

           {_v3_acctdetails_resp}

        """
        super(AccountDetails, self).__init__(AccountKey=AccountKey)


@endpoint("openapi/port/v1/accounts/me")
class AccountList(Portfolio):
    """Get all accounts under a particular client to which the logged
    in user belongs.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate an AccountList request.

        Parameters
        ----------
        params : dict (optional)
             optional querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.AccountList()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::

           {_v3_acctlist_resp}

        """
        super(AccountList, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/accounts/")
class AccountListByClient(Portfolio):
    """Get all accounts owned by the specified client."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an AccountListByClient request.

        Parameters
        ----------
        params : dict (required)
             params must contain at least the ClientKey

        params = {_v3_acctlistbyclient_params}

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.AccountListByClient(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::

           {_v3_acctlistbyclient_resp}

        """
        super(AccountListByClient, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/accounts/{AccountKey}", "PATCH", 204)
class AccountUpdate(Portfolio):
    """Update account details. Particularly the user account shield value,
    the benchmark instrument or the account display name.
    """
    RESPONSE_DATA = "text"

    @dyndoc_insert(responses)
    def __init__(self, AccountKey, data):
        """Instantiate an AccountUpdate request.

        ::

           {_v3_acctupdate_body}

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.account.AccountUpdate(AccountKey='...', data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(AccountUpdate, self).__init__(AccountKey=AccountKey)
        self.data = data


@endpoint("openapi/port/v1/accounts/{AccountKey}/reset", "PUT", 204)
class AccountReset(Portfolio):
    """Reset the trial account. Cannot be used in live environment."""

    def __init__(self, AccountKey, data):
        """Instantiate an AccountReset request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> data = {'NewBalance': '1000000'}
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.AccountReset(AccountKey='...', data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AccountReset, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/accounts/subscriptions/", "POST", 201)
class SubscriptionCreate(Portfolio):
    """Set up a subscription and returns an initial snapshot containing
    a list of accounts as specified by the parameters in the request.
    """

    HEADERS = {"Content-Type": "application/json"}

    # @dyndoc_insert(responses)  WHY GIVES THIS ONE AN ERROR ?
    def __init__(self, data):
        """Instantiate a SubscriptionCreate request.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.SubscriptionCreate(data={...})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::

           {_v3_acctsubscrcreate_resp}

        """
        super(SubscriptionCreate, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/accounts/subscriptions/{ContextId}/",
          "DELETE", 202)
class SubscriptionRemoveByTag(Portfolio):
    """Remove all subscriptions for the current session on this resource
    marked with a specific tag, and frees all resources on the server.
    """

    RESPONSE_DATA = "text"

    def __init__(self, ContextId, params):
        """Instantiate a SubscriptionRemoveByTag request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.SubscriptionRemoveByTag(ContextId,
        ...                                         params={'Tag': '...'})
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status
        """
        super(SubscriptionRemoveByTag, self).__init__(ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/accounts/subscriptions/"
          "{ContextId}/{ReferenceId}/", "DELETE", 202)
class SubscriptionRemoveById(Portfolio):
    """Remove subscription for the current session identified by
    subscription Id.
    """

    RESPONSE_DATA = "text"

    def __init__(self, ContextId, ReferenceId):
        """Instantiate a SubscriptionRemoveById request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.SubscriptionRemoveById(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status
        """
        super(SubscriptionRemoveById, self).__init__(ContextId=ContextId,
                                                     ReferenceId=ReferenceId)
