saxo_openapi
============

Python wrapper for SAXO Bank OpenAPI REST-API.

Currently this is code under development. There is no pypi-package yet.

.. image:: https://travis-ci.org/hootnot/saxo_openapi.svg?branch=master
   :target: https://travis-ci.org/hootnot/saxo_openapi

.. image:: https://readthedocs.org/projects/saxo-openapi/badge/?version=latest
   :target: https://saxo-openapi.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/hootnot/saxo_openapi/badge.svg?branch=master
   :target: https://coveralls.io/github/hootnot/saxo_openapi?branch=master
   :alt: Coverage


Install
-------

.. code-block:: bash

   $ pip install git+https://github.com/hootnot/saxo_openapi.git

Only python3 is supported.

Example:

.. code-block:: python

   import saxo_openapi import API
   import saxo_openapi.endpoints.rootservices as rs
   from pprint import pprint

   token = "... the token you can obtain at the developer portal ..."
   client = API(access_token=token)

   # lets make a diagnostics request, it should return '' with a state 200
   r = rs.diagnostics.Get()
   print("request is: ", r)
   rv = client.request(r)
   assert rv == '' and r.status_code == 200

   # request available rootservices-features
   r = rs.features.Availability()
   rv = client.request(r)
   print("request: ", r)
   print("response: ")
   pprint(rv, indent=2)
   print(r.status_code)


Output:

 ::

  request:  openapi/root/v1/features/availability/
  response:
  [ {'Available': True, 'Feature': 'News'},
    {'Available': True, 'Feature': 'GainersLosers'},
    {'Available': True, 'Feature': 'Calendar'},
    {'Available': True, 'Feature': 'Chart'}]
  200

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
     Charts

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
     Historical Report Data - Aggregated amounts
     Historical Report Data - Trades
     Trading Conditions

   Event Notification Services
     ClientActivities

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
       ContractoptionSpaces                       [ ]
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
     Subscriptions
     User

   Trading
     AllocationKeys
     InfoPrices
     Messages
     OptionChain
     v1 Orders
     v2 Orders
       Place a new order                         [x]
       Change one or more existing orders        [x]
       Cancel one or more orders                 [x]
       Precheck a single order                   [x]
     Positions
     Prices

   Value Add
     PriceAlerts
