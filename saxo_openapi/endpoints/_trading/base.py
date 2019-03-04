# -*- encoding: utf-8 -*-

"""Handle trading endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class Trading(APIRequest):
    """Trading - class to handle the trading endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self, **kwargs):
        """Instantiate a Trading APIRequest instance.

        Parameters
        ----------
        ClientKey : string (optional)
            the ClientKey

        """
        endpoint = self.ENDPOINT.format(**kwargs)
        super(Trading, self).__init__(endpoint, method=self.METHOD)
