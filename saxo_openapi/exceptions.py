# -*- coding: utf-8 -*-

"""Exceptions."""


class StreamTerminated(Exception):
    """StreamTerminated."""


class OpenAPIError(Exception):
    """Generic error class.

    In case of HTTP response codes >= 400 this class can be used
    to raise an exception representing that error.
    """

    def __init__(self, code, reason, content=None):
        """Instantiate an OpenAPIError.

        Parameters
        ----------
        code : int (required)
            the HTTP-code of the response

        reason : str (required)
            the reason of the exceptions

        content : str (optional)
            the content
        """
        self.code = code
        self.reason = reason
        self.content = content

        message = 'HTTP error: {}, reason: {}'.format(code, reason)
        # if error content is returned, include in exception
        if self.content:
            message += ', errorcontent: {}'.format(content)

        super(OpenAPIError, self).__init__(message)
