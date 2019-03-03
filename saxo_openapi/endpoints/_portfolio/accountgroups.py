# -*- encoding: utf-8 -*-

"""Handle portfolio-accountgroups endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.accountgroups import responses


@endpoint("openapi/port/v1/accountgroups/{AccountGroupKey}")
class AccountGroupDetails(Portfolio):
    """Get details about a single account group."""

    @dyndoc_insert(responses)
    def __init__(self, AccountGroupKey, params):
        """Instantiate an AccountGroupDetails request.

        Parameters
        ----------
        AccountGroupKey: string (required)
            the accountGroupKey
        params: dict (required)
            dict with querystring parameters

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = 'ClientKey': '...'
        >>> r = pf.accountgroups.AccountGroupDetails(AccountGroupKey="...",
        ...                                          params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::
            {_v3_acctgrpdetails_resp}

        """
        super(AccountGroupDetails, self).__init__(
            AccountGroupKey=AccountGroupKey)
        self.params = params


@endpoint("openapi/port/v1/accountgroups/me")
class AccountGroupsMe(Portfolio):
    """Get all accounts groups under a particular client to which the logged
    in user belongs.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an AccountGroups request.

        Parameters
        ----------
        params: dict (required)
            dict with querystring parameters

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = dict()
        >>> r = pf.accountgroups.AccountGroups(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::
            {_v3_acctgrpmelist_resp}

        """
        super(AccountGroupsMe, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/accountgroups/")
class AccountGroupsList(Portfolio):
    """Get a list of all account groups used by the specified client."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an AccountGroupsList request.

        Parameters
        ----------
        params: dict (required)
            dict with querystring parameters

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_acctgrplist_params}
        >>> r = pf.accountgroups.AccountGroupsList(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::
            {_v3_acctgrplist_resp}

        """
        super(AccountGroupsList, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/accountgroups/{AccountGroupKey}", "PATCH", 204)
class AccountGroupUpdate(Portfolio):
    """Update account group settings. Particularly the account group
    AccountValueProtectionLimit.
    """

    @dyndoc_insert(responses)
    def __init__(self, AccountGroupKey, data):
        """Instantiate an AccountGroupUpdate request.

        Parameters
        ----------
        AccountGroupKey: string (required)
            the accountGroupKey
        data: dict (required)
            dict with attributes

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_acctgrpupdate_body}
        >>> r = pf.accountgroups.AccountGroupUpdate(AccountGroupKey="...",
        ...                                         data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=2))

        ::
            {_v3_acctgrpupdate_resp}

        """
        super(AccountGroupUpdate, self).__init__(
            AccountGroupKey=AccountGroupKey)
        self.data = data
