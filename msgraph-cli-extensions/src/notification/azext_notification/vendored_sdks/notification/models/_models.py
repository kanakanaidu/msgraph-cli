# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfNotification(msrest.serialization.Model):
    """Collection of notification.

    :param value:
    :type value: list[~notification.models.MicrosoftGraphNotification]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphNotification]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfNotification, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class MicrosoftGraphNotification(MicrosoftGraphEntity):
    """notification.

    :param id: Read-only.
    :type id: str
    :param target_host_name:
    :type target_host_name: str
    :param expiration_date_time:
    :type expiration_date_time: ~datetime.datetime
    :param display_time_to_live:
    :type display_time_to_live: int
    :param priority:  Possible values include: "None", "High", "Low".
    :type priority: str or ~notification.models.MicrosoftGraphPriority
    :param group_name:
    :type group_name: str
    :param target_policy: targetPolicyEndpoints.
    :type target_policy: ~notification.models.MicrosoftGraphTargetPolicyEndpoints
    :param raw_content:
    :type raw_content: str
    :param visual_content: visualProperties.
    :type visual_content: ~notification.models.MicrosoftGraphVisualProperties
    """

    _validation = {
        'display_time_to_live': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'target_host_name': {'key': 'targetHostName', 'type': 'str'},
        'expiration_date_time': {'key': 'expirationDateTime', 'type': 'iso-8601'},
        'display_time_to_live': {'key': 'displayTimeToLive', 'type': 'int'},
        'priority': {'key': 'priority', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'target_policy': {'key': 'targetPolicy', 'type': 'MicrosoftGraphTargetPolicyEndpoints'},
        'raw_content': {'key': 'payload.rawContent', 'type': 'str'},
        'visual_content': {'key': 'payload.visualContent', 'type': 'MicrosoftGraphVisualProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphNotification, self).__init__(**kwargs)
        self.target_host_name = kwargs.get('target_host_name', None)
        self.expiration_date_time = kwargs.get('expiration_date_time', None)
        self.display_time_to_live = kwargs.get('display_time_to_live', None)
        self.priority = kwargs.get('priority', None)
        self.group_name = kwargs.get('group_name', None)
        self.target_policy = kwargs.get('target_policy', None)
        self.raw_content = kwargs.get('raw_content', None)
        self.visual_content = kwargs.get('visual_content', None)


class MicrosoftGraphTargetPolicyEndpoints(msrest.serialization.Model):
    """targetPolicyEndpoints.

    :param platform_types:
    :type platform_types: list[str]
    """

    _attribute_map = {
        'platform_types': {'key': 'platformTypes', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphTargetPolicyEndpoints, self).__init__(**kwargs)
        self.platform_types = kwargs.get('platform_types', None)


class MicrosoftGraphVisualProperties(msrest.serialization.Model):
    """visualProperties.

    :param title:
    :type title: str
    :param body:
    :type body: str
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'body': {'key': 'body', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphVisualProperties, self).__init__(**kwargs)
        self.title = kwargs.get('title', None)
        self.body = kwargs.get('body', None)


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~notification.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = kwargs['error']


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~notification.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)
