# -*- encoding: utf-8 -*-

"""Handle accounthistory endpoints."""

from ..apirequest import APIRequest
from abc import abstractmethod


class AccountHistory(APIRequest):
    """AccountHistory - class to handle the account-history endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @abstractmethod
    def __init__(self, **kwargs):
        """Instantiate an AccountHistory APIRequest instance.

        Parameters
        ----------
        The parameters defined by the derived class.

        """
        endpoint = self.ENDPOINT.format(**kwargs)
        super(AccountHistory, self).__init__(
            endpoint,
            expected_status=self.EXPECTED_STATUS,
            method=self.METHOD)
