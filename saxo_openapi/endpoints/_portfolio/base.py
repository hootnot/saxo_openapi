# -*- encoding: utf-8 -*-

"""Handle portfolio endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class Portfolio(APIRequest):
    """Portfolio - class to handle the portfolio endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @abstractmethod
    def __init__(self, **kwargs):
        """Instantiate a Portfolio APIRequest instance.

        Parameters
        ----------
        kwargs: kwargs (optional)
            optional keyword arguments to be provided by the derived
            request class

        """
        endpoint = self.ENDPOINT.format(**kwargs)
        super(Portfolio, self).__init__(endpoint,
                                        method=self.METHOD,
                                        expected_status=self.EXPECTED_STATUS)
