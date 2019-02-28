saxo_openapi
============

Python wrapper for SAXO Bank OpenAPI REST-API.

Currently this is code under development. There is no pypi-package yet.

Covered endpoints
-----------------

SAXO Bank organizes the endpoints in groups/subgroups, see:
`https://www.developer.saxo/openapi/referencedocs`_


.. _`https://www.developer.saxo/openapi/referencedocs`: https://www.developer.saxo/openapi/referencedocs

.. image:: https://coveralls.io/repos/github/hootnot/saxo_openapi/badge.svg?branch=master
   :target: https://coveralls.io/github/hootnot/saxo_openapi?branch=master
   :alt: Coverage

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
     Accounts          [.]
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
