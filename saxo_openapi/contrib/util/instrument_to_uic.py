# -*- coding: utf-8 -*-

"""Utility classes and/or functions."""

from saxo_openapi.definitions.orders import AssetType
import saxo_openapi.endpoints.referencedata as rd


def InstrumentToUic(client, AccountKey, spec, assettype=AssetType.FxSpot):
    """replace the Instrument for a Uic in the spec dict.
    If there is no Instrument in spec the spec gets returned untouched.

    In case there are multiple entries returned and ValueError is raised.

    Parameters
    ----------

    client : API client instance (required)
        the API client instance

    AccountKey : string (required)
        the AccountKey of the account

    spec : dict (required)
        the dictionary to process. If it contains an 'Instrument' key, try
        to replace it by a Uic

    assettype : string (required: default 'FxSpot')
        the assettype used in the query with the Instrument

    Example
    -------

    >>> from saxo_openapi import API
    >>> from saxo_openapi.contrib.util import InstrumentToUic
    >>> from pprint import pprint
    >>> token = "..."
    >>> AccountKey = "..."
    >>> client = API(access_token=token)
    >>> spec = {'Instrument': 'EURUSD', 'Amount': 120000}
    >>> # find the Uic for Instrument
    >>> pprint(InstrumentToUic(client, AccountKey, spec=spec))
    {'Amount': 120000, 'Uic': 21}
    """

    if 'Instrument' in spec:
        params = {
            'AccountKey': AccountKey,
            'AssetTypes': assettype,
            'Keywords': spec.get('Instrument')
        }

        # create the request to fetch Instrument info
        r = rd.instruments.Instruments(params=params)
        rv = client.request(r)
        if len(rv['Data']) == 1:
            del spec['Instrument']
            spec.update({'Uic': rv['Data'][0]['Identifier']})

        else:
            raise ValueError("Got multiple instruments for: {}".format(
                             spec['Instrument']))

    return spec
