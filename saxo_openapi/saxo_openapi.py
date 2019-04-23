# -*- coding: utf-8 -*-

"""SAXO API wrapper for SAXO Bank OpenAPI."""

import json
import requests
import logging
from .exceptions import OpenAPIError


ITER_LINES_CHUNKSIZE = 60

TRADING_ENVIRONMENTS = {
    'simulation': {
        'stream': 'https://streaming.saxotrader.com',
        'api': 'https://gateway.saxobank.com',
        'prefix': 'sim'
    },
    'live': {
        'stream': 'https://streaming.saxotrader.com',
        'api': 'https://gateway.saxobank.com'
    }
}

DEFAULT_HEADERS = {
    "Accept-Encoding": "gzip, deflate"
}

logger = logging.getLogger(__name__)


def mk_endpoint(endpoint, env, ep_type):

    if env == 'live':
        _endpoint = endpoint

    elif env == 'simulation':
        _endpoint = "{prefix}/{endpoint}".format(
            prefix=TRADING_ENVIRONMENTS[env]['prefix'],
            endpoint=endpoint)

    return "{}/{}".format(
        TRADING_ENVIRONMENTS[env][ep_type],
        _endpoint)


class API(object):
    r"""API - class to handle APIRequests objects to access API endpoints."""

    def __init__(self,
                 access_token,
                 environment='simulation',
                 headers=None,
                 request_params=None):
        """Instantiate an API-client instance of saxo_openapi API wrapper.

        Parameters
        ----------
        access_token : string
            Provide a valid access token.

        environment : dict
            Provide the environment for saxo_openapi REST api. Valid values:
            {'api': 'https://gateway.saxobank.com'}

        headers : dict (optional)
            Provide request headers to be set for a request.


        .. note::

            There is no need to set the 'Content-Type: application/json'
            for the endpoints that require this header. The API-request
            classes covering those endpoints will take care of the header.

        request_params : (optional)
            parameters to be passed to the request. This can be used to apply
            for instance a timeout value:

               request_params={"timeout": 0.1}

            See specs of the requests module for full details of possible
            parameters.

        .. warning::
            parameters belonging to a request need to be set on the
            requestinstance and are NOT passed via the client.

        """
        logger.info("setting up API-client for environment %s", environment)
        try:
            TRADING_ENVIRONMENTS[environment]
        except KeyError as e:  # noqa F841
            logger.error("unkown environment %s", environment)
            raise KeyError("Unknown environment: {}".format(environment))
        else:
            self.environment = environment

        self.access_token = access_token
        self.environment = environment
        self.client = requests.Session()
        self.client.stream = False
        self._request_params = request_params if request_params else {}

        # personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = 'Bearer '+self.access_token

        self.client.headers.update(DEFAULT_HEADERS)
        if headers:
            self.client.headers.update(headers)
            logger.info("applying headers %s", ",".join(headers.keys()))

    @property
    def request_params(self):
        """request_params property."""
        return self._request_params

    def __request(self, method, url, request_args, headers=None, stream=False):
        """__request.

        make the actual request. This method is called by the
        request method in case of 'regular' API-calls. Or indirectly by
        the __stream_request method if it concerns a 'streaming' call.
        """
        func = getattr(self.client, method)
        headers = headers if headers else {}
        response = None
        logger.info("performing (%s) request %s", method, url)
        try:
            response = func(url, stream=stream, headers=headers,
                            **request_args)
        except requests.RequestException as err:
            logger.error("request %s failed [%s]", url, err)
            raise err

        # Handle error responses
        if response.status_code >= 400:
            logger.error("request %s failed [%d,%s]",
                         url,
                         response.status_code,
                         response.content.decode('utf-8'))
            raise OpenAPIError(response.status_code,
                               response.reason,
                               response.content.decode('utf-8'))
        return response

    def __stream_request(self, method, url, request_args, headers=None):
        """__stream_request.

        make a 'stream' request. This method is called by
        the 'request' method after it has determined which
        call applies: regular or streaming.
        """
        headers = headers if headers else {}
        response = self.__request(method, url, request_args,
                                  headers=headers, stream=True)
        lines = response.iter_lines(ITER_LINES_CHUNKSIZE)
        for line in lines:
            if line:
                data = json.loads(line.decode("utf-8"))
                yield data

    def request(self, endpoint):
        """Perform a request for the APIRequest instance 'endpoint'.

        Parameters
        ----------
        endpoint : APIRequest
            The endpoint parameter contains an instance of an APIRequest
            containing the endpoint, method and optionally other parameters
            or body data.

        Raises
        ------
            OpenAPIError in case of HTTP response code >= 400
        """
        method = endpoint.method
        method = method.lower()
        params = None
        try:
            params = getattr(endpoint, "params")
        except AttributeError:
            # request does not have params
            params = {}

        headers = {}
        if hasattr(endpoint, "HEADERS"):
            headers = getattr(endpoint, "HEADERS")

        request_args = {}

        if method in ['get', 'delete', 'patch']:
            request_args['params'] = params

        if hasattr(endpoint, "data") and endpoint.data:
            request_args['json'] = endpoint.data

        # if any parameter for request then merge them
        request_args.update(self._request_params)

        # which API to access ?
        if not (hasattr(endpoint, "STREAM") and
                getattr(endpoint, "STREAM") is True):
            url = mk_endpoint(endpoint, self.environment, 'api')

            response = self.__request(method,
                                      url,
                                      request_args,
                                      headers=headers)
            if (hasattr(endpoint, "RESPONSE_DATA") and
                    getattr(endpoint, "RESPONSE_DATA") is None):
                content = None

            elif not (hasattr(endpoint, "RESPONSE_DATA") and
                      getattr(endpoint, "RESPONSE_DATA") == 'text'):
                # if not explicitely set to 'text' asume JSON
                content = response.content.decode('utf-8')
                content = json.loads(content)

            else:
                content = response.content.decode('utf-8')

            # update endpoint
            endpoint.response = content
            endpoint.status_code = response.status_code

            return content

        else:
            url = mk_endpoint(endpoint, self.environment, 'stream')
            endpoint.response = self.__stream_request(method,
                                                      url,
                                                      request_args,
                                                      headers=headers)
            return endpoint.response
