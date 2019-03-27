# -*- encoding: utf-8 -*-

"""Handle root-services diagnostics endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class RootService(APIRequest):
    """RootService - baseclass to handle the rootservice endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @abstractmethod
    def __init__(self, ContextId=None, ReferenceId=None):
        """Instantiate a RootService APIRequest instance."""
        endpoint = self.ENDPOINT.format(ContextId=ContextId,
                                        ReferenceId=ReferenceId)
        super(RootService, self).__init__(endpoint,
                                          method=self.METHOD,
                                          expected_status=self.EXPECTED_STATUS)
