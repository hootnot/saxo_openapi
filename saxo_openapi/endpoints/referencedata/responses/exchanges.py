# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_ExchangeList": {
        "url": "/openapi/ref/v1/exchanges",
        "response": {
            "__count": 181,
            "Data": [
              {
                "AllDay": False,
                "CountryCode": "US",
                "Currency": "USD",
                "ExchangeId": "NYSE_ARCA",
                "ExchangeSessions": [
                  {
                    "EndTime": "2019-03-04T12:00:00.000000Z",
                    "StartTime": "2019-03-01T21:00:00.000000Z",
                    "State": "Closed"
                  },
                  {
                    "EndTime": "2019-03-04T14:30:00.000000Z",
                    "StartTime": "2019-03-04T12:00:00.000000Z",
                    "State": "PreTrading"
                  },
                  {
                    "EndTime": "2019-03-04T21:00:00.000000Z",
                    "StartTime": "2019-03-04T14:30:00.000000Z",
                    "State": "AutomatedTrading"
                  },
                  {
                    "EndTime": "2019-03-05T12:00:00.000000Z",
                    "StartTime": "2019-03-04T21:00:00.000000Z",
                    "State": "Closed"
                  }
                ],
                "Mic": "ARCX",
                "Name": "New York Stock Exchange (ARCA)",
                "TimeZone": 3,
                "TimeZoneAbbreviation": "EST",
                "TimeZoneOffset": "-05:00:00"
              },
              {
                "AllDay": False,
                "CountryCode": "SG",
                "Currency": "SGD",
                "ExchangeId": "SGX-DT",
                "ExchangeSessions": [
                  {
                    "EndTime": "2019-03-03T23:43:00.000000Z",
                    "StartTime": "2019-03-01T11:05:00.000000Z",
                    "State": "Closed"
                  },
                  {
                    "EndTime": "2019-03-04T11:05:00.000000Z",
                    "StartTime": "2019-03-03T23:43:00.000000Z",
                    "State": "AutomatedTrading"
                  },
                  {
                    "EndTime": "2019-03-04T23:43:00.000000Z",
                    "StartTime": "2019-03-04T11:05:00.000000Z",
                    "State": "Closed"
                  },
                  {
                    "EndTime": "2019-03-05T11:05:00.000000Z",
                    "StartTime": "2019-03-04T23:43:00.000000Z",
                    "State": "AutomatedTrading"
                  }
                ],
                "Mic": "XSES",
                "Name": "Singapore Exchange Derivatives Trading Ltd.",
                "TimeZone": 2,
                "TimeZoneAbbreviation": "SGT",
                "TimeZoneOffset": "08:00:00"
              },
              {
                "AllDay": False,
                "CountryCode": "CH",
                "Currency": "CHF",
                "ExchangeId": "SWX_ETF",
                "ExchangeSessions": [
                  {
                    "EndTime": "2019-03-04T05:00:00.000000Z",
                    "StartTime": "2019-03-01T16:35:00.000000Z",
                    "State": "Closed"
                  },
                  {
                    "EndTime": "2019-03-04T08:00:00.000000Z",
                    "StartTime": "2019-03-04T05:00:00.000000Z",
                    "State": "PreTrading"
                  },
                  {
                    "EndTime": "2019-03-04T16:30:00.000000Z",
                    "StartTime": "2019-03-04T08:00:00.000000Z",
                    "State": "AutomatedTrading"
                  },
                  {
                    "EndTime": "2019-03-04T16:35:00.000000Z",
                    "StartTime": "2019-03-04T16:30:00.000000Z",
                    "State": "CallAuctionTrading"
                  },
                  {
                    "EndTime": "2019-03-05T05:00:00.000000Z",
                    "StartTime": "2019-03-04T16:35:00.000000Z",
                    "State": "Closed"
                  }
                ],
                "Mic": "XSWX",
                "Name": "SIX Swiss Exchange (ETFs)",
                "TimeZone": 4,
                "TimeZoneAbbreviation": "CET",
                "TimeZoneOffset": "01:00:00"
              }]
        }
    },
    "_v3_ExchangeDetails": {
        "url": "/openapi/ref/v1/exchanges/{ExchangeId}",
        "response": {
            "AllDay": False,
            "CountryCode": "US",
            "Currency": "USD",
            "ExchangeId": "NYSE_ARCA",
            "ExchangeSessions": [
              {
                "EndTime": "2019-03-04T12:00:00.000000Z",
                "StartTime": "2019-03-01T21:00:00.000000Z",
                "State": "Closed"
              },
              {
                "EndTime": "2019-03-04T14:30:00.000000Z",
                "StartTime": "2019-03-04T12:00:00.000000Z",
                "State": "PreTrading"
              },
              {
                "EndTime": "2019-03-04T21:00:00.000000Z",
                "StartTime": "2019-03-04T14:30:00.000000Z",
                "State": "AutomatedTrading"
              },
              {
                "EndTime": "2019-03-05T12:00:00.000000Z",
                "StartTime": "2019-03-04T21:00:00.000000Z",
                "State": "Closed"
              }
            ],
            "Mic": "ARCX",
            "Name": "New York Stock Exchange (ARCA)",
            "TimeZone": 3,
            "TimeZoneAbbreviation": "EST",
            "TimeZoneOffset": "-05:00:00"
          }
    }
}
