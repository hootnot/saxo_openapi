saxo_openapi
============

Python wrapper for SAXO Bank OpenAPI REST-API.

Currently this is code under development. There is no pypi-package yet.

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
     HistoricalPositions
     Performance

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
     Clients
     ClosedPositions
     Exposure
     NetPositions
     Orders
     Positions
     Users

   Reference Data
     AlgoStrategies
       Get all strategies
       Get details about a specific strategy
     Countries
     Cultures
     Currencies
     Exchanges
       Get all exchanges
       Get details about a specific exchange
     Instruments
       ...
     Languages
     StandardDates
       Get a list of forward tenor dates
       Get a list of FX option expiry dates
     TimeZones

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
     Positions
     Prices

   Value Add
     PriceAlerts
