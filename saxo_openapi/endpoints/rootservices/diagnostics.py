# -*- encoding: utf-8 -*-

"""Handle root-services diagnostics endpoints."""

from .base import RootService
from ..decorators import endpoint


@endpoint("openapi/root/v1/diagnostics/get/")
class Get(RootService):
    """Send a GET request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Get request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Get()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Get, self).__init__()


@endpoint("openapi/root/v1/diagnostics/post/", "POST")
class Post(RootService):
    """Send a POST request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Post request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Post()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Post, self).__init__()


@endpoint("openapi/root/v1/diagnostics/put/", "PUT")
class Put(RootService):
    """Send a PUT request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Put request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Put()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Put, self).__init__()


@endpoint("openapi/root/v1/diagnostics/delete/", "DELETE")
class Delete(RootService):
    """Send a DELETE request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Delete request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Delete()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Delete, self).__init__()


@endpoint("openapi/root/v1/diagnostics/patch/", "PATCH")
class Patch(RootService):
    """Send a PATCH request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Patch request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Patch()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Patch, self).__init__()


@endpoint("openapi/root/v1/diagnostics/head/", "HEAD")
class Head(RootService):
    """Send a HEAD request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Head request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Head()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Head, self).__init__()


@endpoint("openapi/root/v1/diagnostics/options/", "OPTIONS")
class Options(RootService):
    """Send a OPTIONS request and get a 200 OK response back."""
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate a Options request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Options()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Options, self).__init__()


@endpoint("openapi/root/v1/diagnostics/echo/")
class Echo(RootService):
    """Send a any request and get a 200 OK response with verb, url,
    headers and body in the response body.
    """
    RESPONSE_DATA = None

    def __init__(self):
        """Instantiate an Echo request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.rootservices as rs
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = rs.diagnostics.Echo()
        >>> rv = client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(Echo, self).__init__()
