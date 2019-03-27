# -*- encoding: utf-8 -*-

"""Handle trading endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class Trading(APIRequest):
    """Trading - class to handle the trading endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @abstractmethod
    def __init__(self, **kwargs):
        """Instantiate a Trading APIRequest instance.

        Parameters
        ----------
        kwargs: kwargs (optional)
            optional keyword arguments to be provided by the derived
            request class

        """
        endpoint = self.ENDPOINT.format(**kwargs)
        super(Trading, self).__init__(endpoint,
                                      expected_status=self.EXPECTED_STATUS,
                                      method=self.METHOD)
