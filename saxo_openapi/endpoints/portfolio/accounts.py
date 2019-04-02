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
        >>> AccountKey = 'f4xZWiYL6W1nMKpygBLLA=='
        >>> r = pf.accounts.AccountDetails(AccountKey=AccountKey)
        >>> rv = client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AccountDetails_resp}

        """
        super(AccountDetails, self).__init__(AccountKey=AccountKey)


@endpoint("openapi/port/v1/accounts/me")
class AccountsMe(Portfolio):
    """Get all accounts under a particular client to which the logged
    in user belongs.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate an AccountsMe request.

        Parameters
        ----------
        params : dict (optional)
             optional querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_AccountsMe_params}
        >>> r = pf.accounts.AccountsMe(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AccountsMe_resp}

        """
        super(AccountsMe, self).__init__()
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


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_AccountListByClient_params}
        >>> r = pf.accounts.AccountListByClient(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_AccountListByClient_resp}

        """
        super(AccountListByClient, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/accounts/{AccountKey}", "PATCH", 204)
class AccountUpdate(Portfolio):
    """Update account details. Particularly the user account shield value,
    the benchmark instrument or the account display name.
    """
    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, AccountKey, data):
        """Instantiate an AccountUpdate request.

        Parameters
        ----------
        AccountKey : string (required)
             the AccountKey

        data : dict (required)
             dict representing the requestbody.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_AccountUpdate_body}
        >>> AccountKey = '...'
        >>> r = pf.account.AccountUpdate(AccountKey=AccountKey, data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(AccountUpdate, self).__init__(AccountKey=AccountKey)
        self.data = data


@endpoint("openapi/port/v1/accounts/{AccountKey}/reset", "PUT", 204)
class AccountReset(Portfolio):
    """Reset the trial account. Cannot be used in live environment."""

    RESPONSE_DATA = None

    def __init__(self, AccountKey, data):
        """Instantiate an AccountReset request.

        Parameters
        ----------
        AccountKey : string (required)
             the AccountKey

        data : dict (required)
             dict representing the requestbody.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> data = {'NewBalance': '1000000'}
        >>> AccountKey = '...'
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.accounts.AccountReset(AccountKey=AccountKey, data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        No response data is returned.
        """
        super(AccountReset, self).__init__(AccountKey=AccountKey)
        self.data = data


@endpoint("openapi/port/v1/accounts/subscriptions/", "POST", 201)
class SubscriptionCreate(Portfolio):
    """Set up a subscription and returns an initial snapshot containing
    a list of accounts as specified by the parameters in the request.
    """

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a SubscriptionCreate request.

        Parameters
        ----------
        data : dict (required)
            dict representing the requestbody.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_SubscriptionCreate_body}
        >>> r = pf.accounts.SubscriptionCreate(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        Output::

           {_v3_SubscriptionCreate_resp}

        """
        super(SubscriptionCreate, self).__init__()
        self.data = data


@endpoint("openapi/port/v1/accounts/subscriptions/{ContextId}/",
          "DELETE", 202)
class SubscriptionRemoveByTag(Portfolio):
    """Remove all subscriptions for the current session on this resource
    marked with a specific tag, and frees all resources on the server.
    """

    RESPONSE_DATA = None

    def __init__(self, ContextId, params):
        """Instantiate a SubscriptionRemoveByTag request.

        Parameters
        ----------
        ContextId : string (required)
            the ContextId

        params : dict (required)
            dict with the querystring parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_SubscriptionRemoveByTag_params}
        >>> r = pf.accounts.SubscriptionRemoveByTag(ContextId, params=params)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(SubscriptionRemoveByTag, self).__init__(ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/accounts/subscriptions/"
          "{ContextId}/{ReferenceId}/", "DELETE", 202)
class SubscriptionRemoveById(Portfolio):
    """Remove subscription for the current session identified by
    subscription Id.
    """

    RESPONSE_DATA = None

    def __init__(self, ContextId, ReferenceId):
        """Instantiate a SubscriptionRemoveById request.

        Parameters
        ----------
        ContextId : string (required)
             the ContextId

        ReferenceId : string (required)
             the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'ctxt_20190314'
        >>> ReferenceId = 'sub_1'
        >>> r = pf.accounts.SubscriptionRemoveById(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(SubscriptionRemoveById, self).__init__(ContextId=ContextId,
                                                     ReferenceId=ReferenceId)
