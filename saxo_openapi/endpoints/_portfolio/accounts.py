# -*- encoding: utf-8 -*-

"""Handle portfolio-account endpoints."""

from ..decorators import endpoint
from .base import Portfolio


@endpoint("openapi/port/v1/accounts/{AccountKey}")
class AccountDetails(Portfolio):
    """Get details about a single account."""

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
        >>> r = pf.AccountDetails(AccountKey='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        """
        super(AccountDetails, self).__init__(AccountKey)


@endpoint("openapi/port/v1/accounts/me")
class AccountList(Portfolio):
    """Get all accounts under a particular client to which the logged
    in user belongs.
    """

    def __init__(self):
        """Instantiate an AccountList request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.AccountList()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AccountList, self).__init__()


@endpoint("openapi/port/v1/accounts/")
class AccountListByClient(Portfolio):
    """Get all accounts owned by the specified client."""

    def __init__(self):
        """Instantiate an AccountList request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.AccountListByClient(params={...})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AccountListByClient, self).__init__()


@endpoint("openapi/port/v1/accounts/{AccountKey}", "PATCH")
class AccountUpdate(Portfolio):
    """Update account details. Particularly the user account shield value,
    the benchmark instrument or the account display name.
    """

    def __init__(self):
        """Instantiate an AccountUpdate request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.AccountUpdate(AccountKey='...', data={...})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AccountUpdate, self).__init__()


@endpoint("openapi/port/v1/accounts/{AccountKey}/reset", "PUT")
class AccountReset(Portfolio):
    """Reset the trial account. Cannot be used in live environment."""

    def __init__(self):
        """Instantiate an AccountReset request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.AccountReset(AccountKey='...')
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(AccountReset, self).__init__()


@endpoint("openapi/port/v1/accounts/subscriptions/", "POST")
class SubscriptionCreate(Portfolio):
    """Set up a subscription and returns an initial snapshot containing
    a list of accounts as specified by the parameters in the request.
    """

    def __init__(self):
        """Instantiate a SubscriptionCreate request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.SubscriptionCreate(data={...})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(SubscriptionCreate, self).__init__()


@endpoint("openapi/port/v1/accounts/subscriptions/{ContextId}/", "DELETE")
class SubscriptionRemoveByTag(Portfolio):
    """Remove all subscriptions for the current session on this resource
    marked with a specific tag, and frees all resources on the server.
    """

    def __init__(self):
        """Instantiate a SubscriptionRemoveByTag request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.SubscriptionRemoveByTag(params={'Tag': '...'})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(SubscriptionRemoveByTag, self).__init__()


@endpoint("openapi/port/v1/accounts/subscriptions/"
          "{ContextId}/{ReferenceId}/", "DELETE")
class SubscriptionRemoveById(Portfolio):
    """Remove subscription for the current session identified by
    subscription Id.
    """

    def __init__(self):
        """Instantiate a SubscriptionRemoveById request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = pf.SubscriptionRemoveById(params={'ContextId': '...',
        ...                                       'ReferenceId': '...'})
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))
        """
        super(SubscriptionRemoveById, self).__init__()
