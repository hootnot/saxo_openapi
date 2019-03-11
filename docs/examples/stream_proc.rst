Stream processing
=================

The SAXO OpenAPI offers steaming support using *websockets*.

Several endpoints offer streaming capabilities by creating *subscriptions*.
These subscriptions create messages that can be identified by the *referenceId*.


.. code-block:: python

   #!/usr/bin/env python3.6

   """Simple stream processing."""


   import asyncio
   import websockets
   from saxo_openapi.contrib.ws import stream


   async def echo(ContextId, token):
       hdrs = {
           "Authorization": "Bearer {}".format(token),
       }
       URL = "wss://streaming.saxotrader.com/sim/openapi/streamingws/connect?" + \
             "contextId={ContextId}".format(ContextId=ContextId)
       async with websockets.connect(URL, extra_headers=hdrs) as websocket:
           async for message in websocket:
               print(stream.decode_ws_msg(message))

   if __name__ == "__main__":
       import sys

       with open("token.txt") as I:
           token = I.read().strip()

       asyncio.get_event_loop().run_until_complete(Echo(ContextId=sys.argv[1],
                                                        token=token))


This code will read messages from a message stream. It must be started with a *ContextId*.

.. code-block:: bash

   $ python stream_example.py ctxt_20190311

Now the program runs, but no output appears. By using the explorer www.developer.saxo_ it is
possible to create one ore more subscriptions.

To create a subscription for price information:

  + click the *Trading* service group
  + click *Prices*
  + click POST /trade/v1/prices/subscriptions

.. code-block:: python

   {
       "Arguments": {
           "Uic": 21,
           "AssetType": "FxSpot"
       },
       "ContextId": "ctxt_20190311",
       "ReferenceId": "EUR_USD"
   }

Click SEND to submit the POST. Quotes for EUR_USD will show up in the stream.
Additional subscriptions can be added and the messages will appear in the stream by their
*referenceId*. The output shows EUR_USD price information and output of a subscription
for *account balance*.

 ::

   {'refid': b'acctbal', 'msgId': 5004, 'msg': {'InitialMargin': {'MarginAvailable': 98669.15, 'NetEquityForMargin': 100169.15}, 'MarginAvailableForTrading': 98669.15, 'MarginNetExposure': 100000.32, 'NetEquityForMargin': 100169.15, 'TotalValue': 100169.15, 'UnrealizedMarginOpenProfitLoss': 179.14, 'UnrealizedMarginProfitLoss': 179.14, 'UnrealizedPositionsValue': 174.14}}
   {'refid': b'EUR_USD', 'msgId': 5005, 'msg': {'LastUpdated': '2019-03-11T19:47:54.197000Z', 'Quote': {'Ask': 1.12491, 'Bid': 1.12471, 'Mid': 1.12481}}}
   {'refid': b'acctbal', 'msgId': 5006, 'msg': {'MarginNetExposure': 100000.88}}
   {'refid': b'acctbal', 'msgId': 5007, 'msg': {'MarginNetExposure': 100001.44}}
   {'refid': b'acctbal', 'msgId': 5008, 'msg': {'MarginNetExposure': 100002.0}}
   {'refid': b'EUR_USD', 'msgId': 5009, 'msg': {'LastUpdated': '2019-03-11T19:48:04.830000Z'}}
   {'refid': b'acctbal', 'msgId': 5010, 'msg': {'MarginNetExposure': 100001.44}}
   {'refid': b'acctbal', 'msgId': 5011, 'msg': {'InitialMargin': {'MarginAvailable': 98666.93, 'NetEquityForMargin': 100166.93}, 'MarginAvailableForTrading': 98666.93, 'MarginNetExposure': 100000, 'NetEquityForMargin': 100166.93, 'TotalValue': 100166.93, 'UnrealizedMarginOpenProfitLoss': 176.92, 'UnrealizedMarginProfitLoss': 176.92, 'UnrealizedPositionsValue': 171.92}}
   {'refid': b'EUR_USD', 'msgId': 5012, 'msg': {'LastUpdated': '2019-03-11T19:48:10.464000Z', 'Quote': {'Ask': 1.1249, 'Bid': 1.1247, 'Mid': 1.1248}}}
   {'refid': b'EUR_USD', 'msgId': 5013, 'msg': {'LastUpdated': '2019-03-11T19:48:12.482000Z', 'Quote': {'Ask': 1.12487, 'Bid': 1.12467, 'Mid': 1.12477}}}
   {'refid': b'acctbal', 'msgId': 5014, 'msg': {'InitialMargin': {'MarginAvailable': 98664.71, 'NetEquityForMargin': 100164.71}, 'MarginAvailableForTrading': 98664.71, 'MarginExposureCoveragePct': 100.16, 'MarginNetExposure': 100000.93, 'NetEquityForMargin': 100164.71, 'TotalValue': 100164.71, 'UnrealizedMarginOpenProfitLoss': 174.7, 'UnrealizedMarginProfitLoss': 174.7, 'UnrealizedPositionsValue': 169.7}}
   {'refid': b'EUR_USD', 'msgId': 5015, 'msg': {'LastUpdated': '2019-03-11T19:48:15.882000Z'}}
   {'refid': b'acctbal', 'msgId': 5016, 'msg': {'InitialMargin': {'MarginAvailable': 98666.93, 'NetEquityForMargin': 100166.93}, 'MarginAvailableForTrading': 98666.93, 'MarginNetExposure': 100002.59, 'NetEquityForMargin': 100166.93, 'TotalValue': 100166.93, 'UnrealizedMarginOpenProfitLoss': 176.92, 'UnrealizedMarginProfitLoss': 176.92, 'UnrealizedPositionsValue': 171.92}}
   {'refid': b'EUR_USD', 'msgId': 5017, 'msg': {'LastUpdated': '2019-03-11T19:48:23.501000Z', 'Quote': {'Ask': 1.12486, 'Bid': 1.12466, 'Mid': 1.12476}}}
   {'refid': b'acctbal', 'msgId': 5018, 'msg': {'InitialMargin': {'MarginAvailable': 98666.94, 'NetEquityForMargin': 100166.94}, 'MarginAvailableForTrading': 98666.94, 'MarginNetExposure': 100003.16, 'NetEquityForMargin': 100166.94, 'TotalValue': 100166.94, 'UnrealizedMarginOpenProfitLoss': 176.93, 'UnrealizedMarginProfitLoss': 176.93, 'UnrealizedPositionsValue': 171.93}}
   {'refid': b'EUR_USD', 'msgId': 5019, 'msg': {'LastUpdated': '2019-03-11T19:48:24.604000Z', 'Quote': {'Ask': 1.12487, 'Bid': 1.12467, 'Mid': 1.12477}}}
   {'refid': b'EUR_USD', 'msgId': 5020, 'msg': {'LastUpdated': '2019-03-11T19:48:26.716000Z'}}
   {'refid': b'acctbal', 'msgId': 5021, 'msg': {'MarginNetExposure': 100003.72}}
   {'refid': b'EUR_USD', 'msgId': 5022, 'msg': {'LastUpdated': '2019-03-11T19:48:27.088000Z', 'Quote': {'Ask': 1.12486, 'Bid': 1.12466, 'Mid': 1.12476}}}
   {'refid': b'acctbal', 'msgId': 5023, 'msg': {'MarginNetExposure': 100003.16}}


Subscriptions using saxo_openapi
--------------------------------

Creating price-subscriptions using the *saxo_openapi* is easy too.


.. code-block:: python

   #!/usr/bin/env python3.6

   """Simple demo program that looks up the Uic for currencypairs entered by name.
   For each pair it creates a subscription for price information with the instrumentname
   as  Referenceid.

   The program asumes you have a file with the token locally in token.tok.

   Usage: price_subscr.py <contextid> EURUSD EURJPY EURGBP
   """
   from saxo_openapi import API
   import saxo_openapi.endpoints.trading as tr
   import saxo_openapi.endpoints.referencedata as rd
   import saxo_openapi.contrib.session as session
   import json

   def subscribe_for_prices(client, ContextId, instruments):
       """fetch instrument data by the name of the instrument and extract the Uic (Identifier)
       and use that to subscribe for prices.
       Use the name of the instrument as reference.
       """
       _ai = session.account_info(client=client)

       # body template for price subscription
       body = {
          "Arguments": {
              "Uic": "",
              "AssetType": "FxSpot"
          },
          "ContextId": "",
          "ReferenceId": ""
       }
       body.update({'ContextId': ContextId})

       for instrument in instruments:
           params = {'AccountKey': _ai.AccountKey,
                     'AssetTypes': 'FxSpot',
                     'Keywords': instrument
                    }
           # create the request to fetch Instrument info
           r = rd.instruments.Instruments(params=params)
           rv = client.request(r)
           if len(rv['Data']) == 1:
               body['Arguments'].update({'Uic': rv['Data'][0]['Identifier']})
               body.update({"ReferenceId": instrument})
               # print("Prepping: ")
               # print(json.dumps(body, indent=2))
               # create the request to fetch Instrument info
               r = tr.prices.CreatePriceSubscription(data=body)
               client.request(r)

               status = "succesful" if r.status_code == r.expected_status else "failed"
               print("Subscription for instrument: {} {}".format(instrument, status))

           else:
               print("Got multiple instruments for {}, can't choose...skip".format(instrument))


   if __name__ == "__main__":

       import sys
       with open("token.txt") as I:
           token = I.read().strip()
           client = API(access_token=token)
           ContextId = sys.argv[1]
           subscribe_for_prices(client, ContextId, sys.argv[2:])
           print("check the stream for data ...")


Now create the price subscriptions with the program above:

.. code-block:: bash

   $ python price_subscr.py ctxt_20190311 EURJPY EURGBP
   Subscription for instrument: EURJPY succesful
   Subscription for instrument: EURGBP succesful
   check the stream for data ...

The new instruments will show up in the stream output.

.. _www.developer.saxo: https://www.developer.saxo/openapi/explorer#
