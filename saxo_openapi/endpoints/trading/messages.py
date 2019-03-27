# -*- encoding: utf-8 -*-

"""Handle trading-messages endpoints."""

from .base import Trading
from ..decorators import dyndoc_insert, endpoint
from .responses.messages import responses


@endpoint("openapi/trade/v1/messages")
class GetTradeMessages(Trading):
    """Get trade messages for the current user."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a GetTradeMessages request.

        Parameters
        ----------
        None


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = tr.messages.GetTradeMessages()
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_GetTradeMessages_resp}

        """
        super(GetTradeMessages, self).__init__()


@endpoint("openapi/trade/v1/messages/seen/{MessageId}", "PUT", 204)
class MarkMessageAsSeen(Trading):
    """Logically this is done by moving the message to the 'seen'
    collection."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, MessageId):
        """Instantiate a MarkMessageAsSeen request.

        Parameters
        ----------
        MessageId: string (required)
            the message-id of the message.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> MessageId = '...'
        >>> r = tr.messages.MarkMessageAsSeen(MessageId=MessageId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(MarkMessageAsSeen, self).__init__(
            MessageId=MessageId)


@endpoint("openapi/trade/v1/messages/subscriptions", "POST", 201)
class CreateTradeMessageSubscription(Trading):
    """Create a subscription on trade messages."""

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreateTradeMessageSubscription request.

        Parameters
        ----------
        data: dict (required)
            dict representing the parameters of the data body.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreateTradeMessageSubscription_body}
        >>> r = tr.messages.CreateTradeMessageSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        Output::

            {_v3_CreateTradeMessageSubscription_resp}

        """
        super(CreateTradeMessageSubscription, self).__init__()
        self.data = data


@endpoint("openapi/trade/v1/messages/subscriptions/"
          "{ContextId}/{ReferenceId}",
          "DELETE", 202)
class RemoveTradeMessageSubscriptionById(Trading):
    """Removes a trade message subscription for the current session."""

    RESPONSE_CODE = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a RemoveTradeMessageSubscriptionById request.

        Parameters
        ----------
        ContextId: string (required)
            the context-id

        ReferenceId: string (required)
            the reference-id


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'ctxt_20190317'
        >>> ReferenceId = '...'
        >>> r = tr.messages.RemoveTradeMessageSubscriptionById(
        ...         ContextId=ContextId,
        ...         ReferenceId=ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveTradeMessageSubscriptionById, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)


@endpoint("openapi/trade/v1/messages/subscriptions/{ContextId}", "DELETE", 202)
class RemoveTradeMessageSubscriptions(Trading):
    """Removes trade message subscriptions for the current session."""

    RESPONSE_CODE = None

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params):
        """Instantiate a RemoveTradeMessageSubscription request.

        Parameters
        ----------
        ContextId: string (required)
            the context-id

        ReferenceId: string (required)
            the reference-id


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.trading as tr
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = 'ctxt_20190317'
        >>> params = {_v3_RemoveTradeMessageSubscriptions_params}
        >>> r = tr.messages.RemoveTradeMessageSubscriptions(
        ...         ContextId=ContextId)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No data is returned.
        """
        super(RemoveTradeMessageSubscriptions, self).__init__(
            ContextId=ContextId)
        self.params = params
