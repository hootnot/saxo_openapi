# -*- coding: utf-8 -*-

import saxo_openapi.endpoints.portfolio as pf
from collections import namedtuple


def account_info(client):
    """account_info - fetch some key account information.

    Fetch accountinformation and return it as a namedtuple.

    Parameters
    ----------
    client: API client instance (required)
        the API client instance


    >>> from saxo_openapi.contrib import session
    >>> from saxo_openapi import API
    >>> client = API(access_token= ...)
    >>> ai = session.account_info(client)
    >>> print('ClientKey: ', ai.ClientKey)

    ClientKey: fOA0tvOyQqW2aHpWi9P5bw==
    """

    r = pf.accounts.AccountsMe()
    rv = client.request(r)
    t = namedtuple('AcctInfo', 'ClientId ClientKey AccountId AccountKey')
    ai = t(ClientId=rv['Data'][0]['ClientId'],
           ClientKey=rv['Data'][0]['ClientKey'],
           AccountId=rv['Data'][0]['AccountId'],
           AccountKey=rv['Data'][0]['AccountKey'])

    return ai
