# -*- encoding: utf-8 -*-

"""Handle root-services diagnostics endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class RootService(APIRequest):
    """RootService - class to handle the rootservice endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self):
        """Instantiate a RootService APIRequest instance."""
        endpoint = self.ENDPOINT.format()
        super(RootService, self).__init__(endpoint, method=self.METHOD)
