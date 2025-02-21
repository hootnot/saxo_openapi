# -*- encoding: utf-8 -*-

"""Handle chart-charts endpoints."""

from .base import Charts
from ..decorators import dyndoc_insert, endpoint
from .responses.charts import responses


@endpoint("openapi/chart/v3/charts")
class GetChartData(Charts):
    """Return chart data as specified by request parameters."""

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a GetChartData request.

        Parameters
        ----------
        params : dict (required)
            dict representing the request parameters.
            Required in params: AssetType, Horizon and Uic


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.chart as chart
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_GetChartData_params}
        >>> r = chart.charts.GetChartData(params=params)
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_GetChartData_resp}

        """
        super(GetChartData, self).__init__()
        self.params = params


@endpoint("openapi/chart/v3/charts/subscriptions", "POST", 201)
class CreateChartDataSubscription(Charts):
    """Sets up a subscription and returns an initial snapshot of most recently
    completed samples specified by the parameters in the request.

    Subsequent samples are delivered over the streaming channel. Most often
    a single new sample or sample update is delivered at a time, but when a
    sample closes, you will typcially get two samples: The now closed bar, and
    the bar just opening.
    """

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateChartDataSubscription request.

        Parameters
        ----------
        data : dict (required)
            dict representing the data body, in this case an order spec.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.chart as ch
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateChartDataSubscription_body}
        >>> r = ch.charts.CreateChartDataSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::
            {_v3_CreateChartDataSubscription_resp}

        """
        super(CreateChartDataSubscription, self).__init__()
        self.data = data


@endpoint("openapi/chart/v3/charts/subscriptions/{ContextId}", "DELETE", 202)
class ChartDataRemoveSubscriptions(Charts):
    """Removes all subscriptions for the current session on this resource, and
    frees all resources on the server.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a ChartDataRemoveSubscriptions request.

        Parameters
        ----------
        ContextId: string (required)
            the ContextId

        params: dict (optional)
            dict representing the querystring parameters


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.chart as ch
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_ChartDataRemoveSubscriptions_params}
        >>> ContextId = ...
        >>> r = ch.charts.ChartDataRemoveSubscriptions(ContextId,
        ...                                            params=params)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.

        """
        super(ChartDataRemoveSubscriptions, self).__init__(ContextId=ContextId)
        self.params = params


@endpoint("openapi/chart/v3/charts/subscriptions/{ContextId}/{ReferenceId}",
          "DELETE", 202)
class ChartDataRemoveSubscription(Charts):
    """Removes subscriptions for the given reference id on this resource, and
    frees resources on the server.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a ChartDataRemoveSubscription request.

        Parameters
        ----------
        ContextId: string (required)
            the context id

        ReferenceId: string (required)
            the reference id


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.chart as ch
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ...
        >>> ReferenceId = ...
        >>> r = ch.charts.ChartDataRemoveSubscription(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.

        """
        super(ChartDataRemoveSubscription, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
