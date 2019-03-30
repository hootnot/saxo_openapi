# -*- coding: utf-8 -*-

"""baseorder."""

import json
from abc import ABCMeta, abstractmethod


class BaseOrder(metaclass=ABCMeta):
    """baseclass for Order classes."""

    @abstractmethod
    def __init__(self):
        self._data = dict()

    def __repr__(self):
        return json.dumps(self.__dict__)

    @property
    def data(self):
        """data - return the JSON body.

        The data property returns a dict representing the
        JSON-body needed for the API-request. All values that are
        not set will be left out
        """
        d = dict()
        for k, v in self._data.items():
            # skip unset properties
            if v is None:
                continue

            d.update({k: v})

        return d

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
