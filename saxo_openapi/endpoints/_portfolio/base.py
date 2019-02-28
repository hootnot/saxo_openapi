# -*- encoding: utf-8 -*-
"""Handle portfolio endpoints."""
from ..apirequest import APIRequest
from abc import abstractmethod


class Portfolio(APIRequest):
    """Portfolio - class to handle the portfolio endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self,
                 AccountKey=None,
                 AccountGroupKey=None,
                 ClientKey=None,
                 ContextId=None,
                 OrderId=None,
                 ReferenceId=None):
        """Instantiate a Portfolio APIRequest instance.

        Parameters
        ----------
        AccountKey : string
            the AccountKey.

        AccountGroupKey : string
            the AccountGroupKey.

        ClientKey : string
            the ClientKey.

        ContextId : string
            the ContextId.

        OrderId : string
            the OrderId.

        ReferenceId : string
            the ReferenceId.
        """
        endpoint = self.ENDPOINT.format(AccountKey=AccountKey,
                                        AccountGroupKey=AccountGroupKey,
                                        ClientKey=ClientKey,
                                        ContextId=ContextId,
                                        OrderId=OrderId,
                                        ReferenceId=ReferenceId)
        super(Portfolio, self).__init__(endpoint, method=self.METHOD)
