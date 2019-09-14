saxo_openapi
============


Python wrapper for Saxo Bank OpenAPI REST-API (see `here
<https://www.developer.saxo/openapi/learn>`_)

Most endpoints are covered by *saxo_openapi*. Check `Covered endpoints`_ for details.

.. image:: https://travis-ci.org/hootnot/saxo_openapi.svg?branch=master
   :target: https://travis-ci.org/hootnot/saxo_openapi

.. image:: https://readthedocs.org/projects/saxo-openapi/badge/?version=latest
   :target: https://saxo-openapi.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/hootnot/saxo_openapi/badge.svg?branch=master
   :target: https://coveralls.io/github/hootnot/saxo_openapi?branch=master
   :alt: Coverage

.. image:: https://img.shields.io/pypi/v/saxo_openapi.svg
   :target: https://pypi.org/project/saxo-openapi
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/saxo_openapi.svg
   :target: https://pypi.org/project/saxo-openapi
   :alt: Python versions

.. image:: https://api.codacy.com/project/badge/Grade/edcfcf6a416a4f94bb710413a35daa83
   :target: https://www.codacy.com/app/hootnot/saxo_openapi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hootnot/saxo_openapi&amp;utm_campaign=Badge_Grade

Interactive
-----------

.. image:: https://jupyter.readthedocs.io/en/latest/_static/_images/jupyter.svg
   :target: ./jupyter
   :alt: Jupyter

Using the Jupyter `notebook`_ it is easy to experiment with the
*saxo_openapi* library.

.. _notebook: ./jupyter/index.ipynb

TOC
---

   + `Install`_
   + `Design`_
   + `Documentation`_
   + `Example`_
   + `Some Trading`_
       - `Or by using: contrib.orders`_
   + `Covered endpoints`_


Install
-------

.. code-block:: bash

   # Setup a virtual environment
   $ mkdir tst_saxo_openapi
   $ cd tst_saxo_openapi
   $ /usr/local/bin/python3.7 -m venv venv37
   $ . ./venv37/bin/activate
   (venv37) feite@oatr:~/tst_saxo_openapi$

   $ pip install saxo_openapi requests

   # get a token from developer.saxo
   # try some examples


To use the latest development version from github:

.. code-block:: bash

   $ pip install git+https://github.com/hootnot/saxo_openapi.git


.. note:: Only python3 is supported!


Design
------

The *saxo_openapi* covers each *endpoint* of the SAXO OpenAPI by a
*request class*.
Each request class representing an endpoint applies the following in a consistent way:

  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | **Endpoint parameters as documented by SAXO** | **saxo_openpi request class**                       | **Comment**                                            |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | *route* parameters                            | named parameters: required                          |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | example:                                      |                                                     |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | /port/v1/positions/me/?FieldGroups=...        | portfolio.PositionsMe()                             | No route params and no required params                 |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  |                                               |                                                     |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | *querystring* parameters                      | *params* dict: optional and/or required parameters. |                                                        |
  |                                               | If all parameters in params are optional the params |                                                        |
  |                                               | parameter is optional, otherwise it is required     |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | example:                                      |                                                     |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | /port/v1/positions/{PositionId}/?...          | pf.positions.SinglePosition(PositionId, params={..})| *PositionId*: required, *params*: required             |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  |                                               |                                                     |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | *body* parameters                             | *data* dict: optional and/or required parameters    |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | example:                                      |                                                     |                                                        |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+
  | /trade/v2/orders/                             | tr.orders.Order(data={..})                          | *data*: required                                       |
  +-----------------------------------------------+-----------------------------------------------------+--------------------------------------------------------+

Top `saxo_openapi`_

Documentation
-------------

SAXO Bank has a full documentation of their REST interface available
on  `https://www.developer.saxo/openapi/referencedocs`_.

The documentation of *saxo_openapi* is on `https://saxo-openapi.readthedocs.io/en/latest`_.
Each request-class is documented with a straightforward usage example.

.. _`https://www.developer.saxo/openapi/referencedocs`: https://www.developer.saxo/openapi/referencedocs
.. _`https://saxo-openapi.readthedocs.io/en/latest`: https://saxo-openapi.readthedocs.io/en/latest

Top `saxo_openapi`_

Example
-------

.. code-block:: python

    from saxo_openapi import API
    import saxo_openapi.endpoints.rootservices as rs
    from pprint import pprint

    token = " ... [Paste your access token here - create a 24-hour token for testing on developer.saxo] ... "
    client = API(access_token=token)

    # lets make a diagnostics request, it should return '' with a state 200
    r = rs.diagnostics.Get()
    print("request is: ", r)
    rv = client.request(r)
    assert rv is None and r.status_code == 200
    print('diagnostics passed')

    # request available rootservices-features
    r = rs.features.Availability()
    rv = client.request(r)
    print("request is: ", r)
    print("response: ")
    pprint(rv, indent=2)
    print(r.status_code)

Output:

 ::

    request is:  openapi/root/v1/diagnostics/get/
    diagnostics passed
    request is:  openapi/root/v1/features/availability/
    response:
    [ {'Available': True, 'Feature': 'News'},
      {'Available': True, 'Feature': 'GainersLosers'},
      {'Available': True, 'Feature': 'Calendar'},
      {'Available': True, 'Feature': 'Chart'}]
    200

Top `saxo_openapi`_

Some Trading
------------

.. code-block:: python

   from saxo_openapi import API
   import saxo_openapi.endpoints.trading as tr
   import saxo_openapi.endpoints.portfolio as pf
   import json

   # Place your token in a file named: tok.txt
   tok = ""
   with open("tok.txt") as I:
       tok = I.read().strip()

   # Our client to process the requests
   client = API(access_token=tok)

   # Positions, probably none, but maybe you see positions
   # that you created by the explorer
   r = pf.positions.PositionsMe()
   rv = client.request(r)
   print(json.dumps(rv, indent=2))

   # Place some market orders
   MO = [
   {
       "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
       "Amount": "100000",
       "AssetType": "FxSpot",
       "BuySell": "Sell",
       "OrderType": "Market",
       "Uic": 21   # EURUSD
   },
   {
       "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
       "Amount": "80000",
       "AssetType": "FxSpot",
       "BuySell": "Buy",
       "OrderType": "Market",
       "Uic": 23   # GBPCAD
   },
   ]

   # create Order requests and process them
   for r in [tr.orders.Order(data=orderspec) for orderspec in MO]:
       client.request(r)

   # check for positions again
   r = pf.positions.PositionsMe()
   rv = client.request(r)
   print(json.dumps(rv, indent=2))


Output:

.. code-block:: python

   {
     "__count": 0,
     "Data": []
   }

.. code-block:: python

   {
     "__count": 2,
     "Data": [
       {
         "NetPositionId": "GBPCAD__FxSpot",
         "PositionBase": {
           "Uic": 23,
           "AccountId": "9226397",
           "Amount": 80000.0,
           "CanBeClosed": true,
           "SourceOrderId": "76306670",
           "ExecutionTimeOpen": "2019-03-05T22:39:43.738721Z",
           "Status": "Open",
           "IsMarketOpen": true,
           "CorrelationKey": "244b083d-7bce-4e4b-a01c-5117e5860321",
           "CloseConversionRateSettled": false,
           "ClientId": "9226397",
           "OpenPrice": 1.75937,
           "RelatedOpenOrders": [],
           "ValueDate": "2019-03-08T00:00:00.000000Z",
           "SpotDate": "2019-03-08",
           "AssetType": "FxSpot"
         },
         "PositionView": {
           "Exposure": 80000.0,
           "InstrumentPriceDayPercentChange": -0.04,
           "ConversionRateCurrent": 0.662245,
           "TradeCostsTotal": -14.07,
           "ExposureInBaseCurrency": 93196.8,
           "CurrentPriceType": "Bid",
           "TradeCostsTotalInBaseCurrency": -9.32,
           "ProfitLossOnTradeInBaseCurrency": -49.27,
           "CurrentPriceDelayMinutes": 0,
           "ConversionRateOpen": 0.662245,
           "ProfitLossOnTrade": -74.4,
           "ExposureCurrency": "GBP",
           "CurrentPrice": 1.75844,
           "CalculationReliability": "Ok"
         },
         "PositionId": "212702698"
       },
       {
         "NetPositionId": "EURUSD__FxSpot",
         "PositionBase": {
           "Uic": 21,
           "AccountId": "9226397",
           "Amount": -100000.0,
           "CanBeClosed": true,
           "SourceOrderId": "76306669",
           "ExecutionTimeOpen": "2019-03-05T22:39:43.546536Z",
           "Status": "Open",
           "IsMarketOpen": true,
           "CorrelationKey": "4dab5814-8b84-421e-859b-dfdbdbec06ec",
           "CloseConversionRateSettled": false,
           "ClientId": "9226397",
           "OpenPrice": 1.13054,
           "RelatedOpenOrders": [],
           "ValueDate": "2019-03-08T00:00:00.000000Z",
           "SpotDate": "2019-03-08",
           "AssetType": "FxSpot"
         },
         "PositionView": {
           "Exposure": -100000.0,
           "InstrumentPriceDayPercentChange": -0.01,
           "ConversionRateCurrent": 0.884455,
           "TradeCostsTotal": -11.3,
           "ExposureInBaseCurrency": -100000.0,
           "CurrentPriceType": "Ask",
           "TradeCostsTotalInBaseCurrency": -9.99,
           "ProfitLossOnTradeInBaseCurrency": -17.69,
           "CurrentPriceDelayMinutes": 0,
           "ConversionRateOpen": 0.884455,
           "ProfitLossOnTrade": -20.0,
           "ExposureCurrency": "EUR",
           "CurrentPrice": 1.13074,
           "CalculationReliability": "Ok"
         },
         "PositionId": "212702696"
       }
     ]
   }


Top `saxo_openapi`_

Or by using: contrib.orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The same orders but now using *MarketOrderFxSpot* to create the orderbodies.

.. code-block:: python

   from saxo_openapi import API
   import saxo_openapi.endpoints.trading as tr
   import saxo_openapi.endpoints.portfolio as pf
   from saxo_openapi.contrib.orders import tie_account_to_order, MarketOrderFxSpot
   from saxo_openapi.contrib.session import account_info
   import json

   # Place your token in a file named: token.txt
   token = ""
   with open("token.txt") as I:
       tok = I.read().strip()

   # client to process the requests
   client = API(access_token=token)
   ai = account_info(client)

   # Positions, probably none, but maybe you see positions
   # that you created by the explorer
   r = pf.positions.PositionsMe()
   rv = client.request(r)
   print(json.dumps(rv, indent=2))

   # Place some market orders, only Amount and Uic needed
   # the other body parameters will be generated by MarketOrderFxSpot
   MO = [
      {
          "Amount": -100000,    # negative amount indicates a Sell
          "Uic": 21   # EURUSD
      },
      {
          "Amount": 80000,      # positive amount indicates a buy
          "Uic": 23   # GBPCAD
      }]

   # create Order requests and process them
   for spec in MO:
       mospec = tie_account_to_order(ai.AccountKey, MarketOrderFxSpot(**spec))
       r = tr.orders.Order(data=mospec)
       client.request(r)

   # check for positions again
   r = pf.positions.PositionsMe()
   rv = client.request(r)
   print(json.dumps(rv, indent=2))


Top `saxo_openapi`_

Covered endpoints
-----------------

SAXO Bank organizes the endpoints in groups/subgroups, see:
`https://www.developer.saxo/openapi/referencedocs`_


.. _`https://www.developer.saxo/openapi/referencedocs`: https://www.developer.saxo/openapi/referencedocs

States:

  + [ ] not covered yet
  + [.] work in progress
  + [x] covered

 ::

   Account History
     Account Values
        AccountSummary          [x]
     HistoricalPositions
        HistoricalPositions     [x]
     Performance
        AccountPerformance      [x]

   Auto Trading
     Investments
     Trade Followers
     Trade Leaders

   Chart
     Charts                     [x]

   Client Management
     Signups v1
     Signups v2
     Users

   Client Reporting
     Historical Report Data - Account Statement
     Historical Report Data - Portfolio Management
     Historical Report Data - Trade Details
     Historical Report Data - Trades Executed
     Historical Report Data - Transaction
     Historical Report Data - Transaction Balance

   Client Services
     Audit Activities
     Audit OrderActivities
     CashManagement - InterAcountTransfer
     CashManagement - Wiretransfers
     ClientInfo
     Historical Report Data - Aggregated amounts
     Historical Report Data - Bookings
     Historical Report Data - Closed positions
     Historical Report Data - Trades
     Support - Cases

   Event Notification Services
     ClientActivities
       create a subscription for client events   [x]
       remove subscription                       [x]
       remove subscriptions                      [x]
       get activities for client/account         [x]

   Partner Integration (Beta/Early Preview)
     InteractiveIdVerification

   Platform
     Articles
       Get a specific article from sitecore           [ ]
       Get a list of articles from sitecore           [ ]
     ConfigurationInvestor
       Get the structure configuration for platform   [ ]
       Get a specific page for not loading full site  [ ]
     ConfigurationTrader
       Get the structure configuration for platform   [ ]
       Get a specific page for not loading full site  [ ]

   Portfolio
     AccountGroups
       AccountGroupDetails      [x]
       AccountGroupsMe          [x]
       AccountGroupsList        [x]
       AccountGroupUpdate       [x]

     Accounts
       AccountDetails           [x]
       AccountList              [x]
       AccountListByClient      [x]
       AccountUpdate            [x]
       Accountreset             [x]
       SubscriptionCreate       [x]
       SubscriptionRemoveByTag  [x]
       SubscriptionRemoveById   [x]

     Balances
       AccountBalancesMe                 [x]
       AccountBalances                   [x]
       MarginOverview                    [x]
       BalanceSubscriptionCreate         [x]
       BalanceSubscriptionRemoveByTag    [x]
       BalanceSubscriptionRemoveById     [x]

     Clients
       ClientDetailsMe                   [x]
       ClientDetails                     [x]
       ClientDetailsUpdate               [x]
       ClientDetailsByOwner              [x]
       ClientSwitchPosNettingMode        [x]

     ClosedPositions
       ClosedPositionList                     [x]
       ClosedPositionById                     [x]
       ClosedPositionDetails                  [x]
       ClosedPositionsMe                      [x]
       ClosedPositionSubscription             [x]
       ClosedPositionSubscriptionUpdate       [x]
       ClosedPositionSubscriptionsRemove      [x]
       ClosedPositionSubscriptionRemoveById   [x]

     Exposure
       NetInstrumentsExposureMe                  [x]
       NetInstrumentsExposure                    [x]
       CreateExposureSubscription                [x]
       RemoveExposureSubscriptionsByTag          [x]
       RemoveExposureSubscription                [x]
       CurrencyExposureMe                        [x]
       CurrencyExposureSpecific                  [x]
       FxSpotExposureMe                          [x]
       FxSpotExposurSpecific                     [x]

     NetPositions
       Get a single netposition                                            [x]
       Get detailed information for a single netposition                   [x]
       Get netpositions for the logged-in client                           [x]
       Get netpositions for a client, account group, account or a position [x]
       Create a netsubscription on a list of positions and make it active  [x]
       Remove multiple subscriptions                                       [x]
       Remove a subscription                                               [x]

     Orders
       GetOpenOrder                               [x]
       GetOpenOrdersMe                            [x]
       OrderDetails                               [x]
       GetAllOpenOrders                           [x]
       CreateOpenOrdersSubscription               [x]
       RemoveOpenOrderSubscriptionsByTag          [x]
       RemoveOpenOrderSubscription                [x]

     Positions
       Get a single position                                            [x]
       Get detailed information for a single position                   [x]
       Get positions for the logged-in client                           [x]
       Get positions for a client, account group, account or a position [x]
       Create a subscription on a list of positions and make it active  [x]
       Change the subscription page size                                [x]
       Remove multiple subscriptions                                    [x]
       Remove a subscription                                            [x]

     Users
       UsersMe                                    [x]
       Users                                      [x]
       UserDetails                                [x]
       UserUpdate                                 [x]

   Reference Data
     AlgoStrategies
       Get all strategies                         [x]
       Get details about a specific strategy      [x]
     Countries                                    [x]
     Cultures                                     [x]
     Currencies                                   [x]
     Exchanges
       Get all exchanges                          [x]
       Get details about a specific exchange      [x]
     Instruments
       Instruments                                [x]
       InstrumentsDetails                         [x]
       InstrumentDetails                          [x]
       ContractoptionSpaces                       [x]
       FuturesSpaces                              [ ]
       TradingSchedule                            [x]
     Languages                                    [x]
     StandardDates
       Get a list of forward tenor dates          [x]
       Get a list of FX option expiry dates       [x]
     TimeZones                                    [x]

   Root Services
     Diagnostics
       GET test endpoint      [x]
       POST test endpoint     [x]
       PUT test endpoint      [x]
       DELETE test endpoint   [x]
       PATCH test endpoint    [x]
       HEAD test endpoint     [x]
       OPTIONS test endpoint  [x]
       ECHO test endpoint     [x]

     Features
       Get availability of all features           [x]
       Create a feature availability subscription [x]
       Remove a feature availability subscription [x]
     Sessions
       Get Session capabilities                  [x]
       Change Session capabilities               [x]
       Create Session capabilities subscr.       [x]
       Remove Session capabilities subscr.       [x]
     Subscriptions
       Rmove multiple active subscr              [x]
     User                                        [x]

   Trading
     AllocationKeys
       Get a list of existing allocation keys    [x]
       Get detailed inform. about an alloc. key  [x]
       Create an allocation key                  [x]
       Delete an allocation key                  [x]
     InfoPrices
       Get an info price for a specific instrum. [x]
       Get info prices for a list of instruments [x]
       Create info pr subscr. on list of instr.  [x]
       Remove info pr subscr. on instruments     [x]
       Remove info pr subscr on an instrument    [x]
     Messages                                    [x]
     OptionChain
       Create options chain subscription         [x]
       Modify options chain subscription         [x]
       Remove options chain subscription         [x]
       ResetATM options chain subscription       [x]
     v1 Orders
     v2 Orders
       Place a new order                         [x]
       Change one or more existing orders        [x]
       Cancel one or more orders                 [x]
       Precheck a single order                   [x]
     Positions
       Create pos by quote                       [x]
       Update a position                         [x]
       Exercise a position                       [x]
       Exercise an amount                        [x]
     Prices
       CreatePriceSubscriptions                  [x]
       RequestMarginImpact                       [x]
       RemovePriceSubscriptionByTag              [x]
       RemovePriceSubscription                   [x]

   Value Add
     PriceAlerts
       Get all price alert definitions                   [x]
       Get a specific price alert definition             [x]
       Create a new price alert definition               [x]
       Update an existing price alert def.               [x]
       Delete price alert definitions                    [x]
       Get the current users's notification settings     [x]
       Modify the current users's notification settings  [x]

Top `saxo_openapi`_
