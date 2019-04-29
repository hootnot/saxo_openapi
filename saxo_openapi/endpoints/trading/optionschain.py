# -*- encoding: utf-8 -*-

"""Handle trading-optionschain endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.optionschain import responses


@endpoint("openapi/trade/v1/optionschain/subscriptions", "POST", 201)
class OptionsChainSubscriptionCreate(Trading):
    """Create an active options chain subscription."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a OptionsChainSubscriptionCreate request.

        Parameters
        ----------
        data : dict
            the dict representing the parameters of the request body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_OptionsChainSubscriptionCreate_body}
        >>> r = tr.optionschain.OptionsChainSubscriptionCreate(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_OptionsChainSubscriptionCreate_body}

        """
        super(OptionsChainSubscriptionCreate, self).__init__()
        self.data = data


@endpoint("openapi/trade/v1/optionschain/subscriptions"
          "{ContextId}/{ReferenceId}", "PATCH", 204)
class OptionsChainSubscriptionModify(Trading):
    """Modify an existing options chain subscription."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId, data):
        """Instantiate a OptionsChainSubscriptionModify request.

        Parameters
        ----------
        ContextId: string
            the ContextId

        ReferenceId: string
            the ReferenceId

        data : dict
            dict representing the parameters of the request body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ReferenceId = ...
        >>> ContextId = ...
        >>> data = {_v3_OptionsChainSubscriptionModify_body}
        >>> r = tr.optionschain.OptionsChainSubscriptionModify(
        ...     ReferenceId=ReferenceId,
        ...     ContextId=ContextId,
        ...     data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        Output::

            {_v3_OptionsChainSubscriptionModify_resp}

        """
        super(OptionsChainSubscriptionModify, self).__init__(
              ReferenceId=ReferenceId,
              ContextId=ContextId)
        self.data = data


@endpoint("openapi/trade/v1/optionschain/subscriptions/"
          "{ContextId}/{ReferenceId}", "DELETE", 202)
class OptionsChainSubscriptionRemove(Trading):
    """Remove an options chain subscription."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a OptionsChainSubscriptionRemove request.

        Parameters
        ----------
        ContextId: string
            the ContextId

        ReferenceId: string
            the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ReferenceId = ...
        >>> ContextId = ...
        >>> r = tr.optionschain.OptionsChainSubscriptionRemove(
        ...     ReferenceId=ReferenceId,
        ...     ContextId=ContextId
        ... )
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        Output::

            {_v3_OptionsChainSubscriptionRemove_resp}

        """
        super(OptionsChainSubscriptionRemove, self).__init__(
              ReferenceId=ReferenceId,
              ContextId=ContextId)


@endpoint("openapi/trade/v1/optionschain/subscriptions/"
          "{ContextId}/{ReferenceId}/ResetATM", "PUT", 204)
class OptionsChainSubscriptionResetATM(Trading):
    """Reset an options chain subscription 'At The Money'."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate an OptionsChainSubscriptionResetATM request.

        Parameters
        ----------
        ContextId: string
            the ContextId

        ReferenceId: string
            the ReferenceId


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ReferenceId = ...
        >>> ContextId = ...
        >>> r = tr.optionschain.OptionsChainSubscriptionResetATM(
        ...     ReferenceId=ReferenceId,
        ...     ContextId=ContextId
        ... )
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        Output::

            {_v3_OptionsChainSubscriptionResetATM_resp}

        """
        super(OptionsChainSubscriptionResetATM, self).__init__(
              ReferenceId=ReferenceId,
              ContextId=ContextId)
