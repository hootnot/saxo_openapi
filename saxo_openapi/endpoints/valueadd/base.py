# -*- encoding: utf-8 -*-

"""Handle valueadd endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class ValueAdd(APIRequest):
    """ValueAdd - class to handle the valueadd endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @abstractmethod
    def __init__(self, **kwargs):
        """Instantiate a ValueAdd APIRequest instance.

        Parameters
        ----------
        kwargs: kwargs (optional)
            optional keyword arguments to be provided by the derived
            request class

        """
        endpoint = self.ENDPOINT.format(**kwargs)
        super(ValueAdd, self).__init__(endpoint,
                                       expected_status=self.EXPECTED_STATUS,
                                       method=self.METHOD)
