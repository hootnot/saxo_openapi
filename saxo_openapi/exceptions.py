# -*- coding: utf-8 -*-

"""Exceptions."""


class StreamTerminated(Exception):
    """StreamTerminated."""


class OpenAPIError(Exception):
    """Generic error class.

    In case of HTTP response codes >= 400 this class can be used
    to raise an exception representing that error.
    """

    def __init__(self, code, msg):
        """Instantiate an OpenAPIError.

        Parameters
        ----------
        code : int
            the HTTP-code of the response

        msg : str
            the message returned with the response
        """
        self.code = code
        self.msg = msg

        super(OpenAPIError, self).__init__(msg)
