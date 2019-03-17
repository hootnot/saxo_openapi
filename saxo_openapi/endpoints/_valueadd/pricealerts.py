# -*- encoding: utf-8 -*-

"""Handle valueadd-pricealerts endpoints."""

from .base import ValueAdd
from ..decorators import dyndoc_insert, endpoint
from .responses.pricealerts import responses


@endpoint("openapi/vas/v1/pricealerts/definitions/")
class GetAllAlerts(ValueAdd):
    """Get an unsorted list of all the price alert definitions belonging to
    the current user where the state matches the specified value. The alerts
    might belong to different accounts, should the user have more than one.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a GetAllAlerts request.

        Parameters
        ----------
        data : dict (required)
            dict representing the querystring parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_GetAllAlerts_params}
        >>> r = va.pricealerts.GetAllAlerts(params=params)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_GetAllAlerts_resp}

        """
        super(GetAllAlerts, self).__init__()
        self.params = params


@endpoint("openapi/vas/v1/pricealerts/definitions/{AlertDefinitionId}")
class GetAlertDefinition(ValueAdd):
    """Gets the specified price alert for the current user."""

    @dyndoc_insert(responses)
    def __init__(self, AlertDefinitionId):
        """Instantiate a GetAlertDefinition request.

        Parameters
        ----------
        AlertDefinitionId: string (required)
            the alert definition id.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> AlertDefinitionId = 30384
        >>> r = va.pricealerts.GetAlertDefinition(AlertDefinitionId)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_GetAlertDefinition_resp}

        """
        super(GetAlertDefinition, self).__init__(
            AlertDefinitionId=AlertDefinitionId)


@endpoint("openapi/vas/v1/pricealerts/definitions/", "POST", 201)
class CreatePriceAlert(ValueAdd):
    """Create a new price alert definition. The created definition is
    returned with a couple of more properties, the price alert definition
    ID being one of them.
    """

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a CreatePriceAlert request.

        Parameters
        ----------
        data: dict (required)
            dict representing the body parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_CreatePriceAlert_body}
        >>> r = va.pricealerts.CreatePriceAlert(AlertDefinitionId)
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_CreatePriceAlert_resp}

        """
        super(CreatePriceAlert, self).__init__()
        self.data = data


@endpoint("openapi/vas/v1/pricealerts/definitions/{AlertDefinitionId}",
          "PUT", 204)
class UpdatePriceAlert(ValueAdd):
    """Update a price alert definition for the current user."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, AlertDefinitionId, data):
        """Instantiate an UpdatePriceAlert request.

        Parameters
        ----------
        data: dict (required)
            dict representing the body parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> AlertDefinitionId = 30384
        >>> data = {_v3_UpdatePriceAlert_body}
        >>> r = va.pricealerts.UpdatePriceAlert(AlertDefinitionId, data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(UpdatePriceAlert, self).__init__(
            AlertDefinitionId=AlertDefinitionId)
        self.data = data


@endpoint("openapi/vas/v1/pricealerts/definitions/{AlertDefinitionIds}",
          "DELETE", 204)
class DeletePriceAlert(ValueAdd):
    """Delete the specified price alert definitions. The alerts have to
    belong to the current user.
    """

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, AlertDefinitionIds):
        """Instantiate a DeletePriceAlert request.

        Parameters
        ----------
        AlertDefinitionIds: string (required)
            string with ','-delimited AlertDefinitionIds


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> AlertDefinitionIds = '30384,30386'
        >>> r = va.pricealerts.DeletePriceAlert(AlertDefinitionIds)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(DeletePriceAlert, self).__init__(
            AlertDefinitionIds=AlertDefinitionIds)


@endpoint("openapi/vas/v1/pricealerts/usersettings/")
class GetUserNotificationSettings(ValueAdd):
    """Get the current user's price alert notification settings."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a GetUserNotificationSettings request.

        Parameters
        ----------
        None


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> r = va.pricealerts.GetUserNotificationSettings()
        >>> client.request(r)
        >>> print(json.dumps(rv, indent=2))

        ::

            {_v3_GetUserNotificationSettings_resp}

        """
        super(GetUserNotificationSettings, self).__init__()


@endpoint("openapi/vas/v1/pricealerts/usersettings/", "PUT", 204)
class ModifyUserNotificationSettings(ValueAdd):
    """Modify the current user's price alert notification settings."""

    RESPONSE_DATA = None

    @dyndoc_insert(responses)
    def __init__(self, data):
        """Instantiate a ModifyUserNotificationSettings request.

        Parameters
        ----------
        data: dict (required)
            dict representing the body parameters.


        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.valueadd as va
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> data = {_v3_ModifyUserNotificationSettings_body}
        >>> r = va.pricealerts.ModifyUserNotificationSettings(data=data)
        >>> client.request(r)
        >>> assert r.status_code == r.expected_status

        No response data is returned.
        """
        super(ModifyUserNotificationSettings, self).__init__()
        self.data = data
