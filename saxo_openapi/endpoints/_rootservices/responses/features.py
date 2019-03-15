# -*- coding: utf-8 -*-

"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement.
"""

responses = {
    "_v3_Availability": {
        "url": "/openapi/root/v1/features/availability",
        "response": [
           {'Available': True, 'Feature': 'News'},
           {'Available': True, 'Feature': 'GainersLosers'},
           {'Available': True, 'Feature': 'Calendar'},
           {'Available': True, 'Feature': 'Chart'}
        ]
    },
    "_v3_CreateAvailabilitySubscription": {
        "url": "/openapi/root/v1/features/availability/subscriptions",
        "body": {
            'RefreshRate': 5000,
            'ReferenceId': 'Features',
            'ContextId': '20190209072629616'
        },
        "response": {
            'ContextId': '20190209072629616',
            'InactivityTimeout': 30,
            'ReferenceId': 'Features',
            'RefreshRate': 0,
            'Snapshot': [
                {'Available': True, 'Feature': 'News'},
                {'Available': True, 'Feature': 'GainersLosers'},
                {'Available': True, 'Feature': 'Calendar'},
                {'Available': True, 'Feature': 'Chart'}],
            'State': 'Active'
        },
    },
    "_v3_RemoveAvailabilitySubscription": {
        "url": "/openapi/root/v1/features/availability/subscriptions/"
               "{ContextId}/{ReferenceId}",
        "route": {
            "ContextId": '20190209072629616',
            "ReferenceId": 'Features',
        },
        "response": ''
    },
}
