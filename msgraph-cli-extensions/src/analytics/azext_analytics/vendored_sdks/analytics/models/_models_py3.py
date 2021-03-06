# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._analytics_enums import *


class CollectionOfActivityStatistics(msrest.serialization.Model):
    """Collection of activityStatistics.

    :param value:
    :type value: list[~analytics.models.MicrosoftGraphActivityStatistics]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphActivityStatistics]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphActivityStatistics"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfActivityStatistics, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfActivityStatistics0(msrest.serialization.Model):
    """Collection of activityStatistics.

    :param value:
    :type value: list[~analytics.models.MicrosoftGraphActivityStatistics]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphActivityStatistics]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphActivityStatistics"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfActivityStatistics0, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfSharedInsight(msrest.serialization.Model):
    """Collection of sharedInsight.

    :param value:
    :type value: list[~analytics.models.MicrosoftGraphSharedInsight]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphSharedInsight]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphSharedInsight"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfSharedInsight, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfTrending(msrest.serialization.Model):
    """Collection of trending.

    :param value:
    :type value: list[~analytics.models.MicrosoftGraphTrending]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphTrending]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphTrending"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfTrending, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfUsedInsight(msrest.serialization.Model):
    """Collection of usedInsight.

    :param value:
    :type value: list[~analytics.models.MicrosoftGraphUsedInsight]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphUsedInsight]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphUsedInsight"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfUsedInsight, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


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
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = id


class MicrosoftGraphActivityStatistics(MicrosoftGraphEntity):
    """activityStatistics.

    :param id: Read-only.
    :type id: str
    :param activity:  Possible values include: "Email", "Meeting", "Focus", "Chat", "Call".
    :type activity: str or ~analytics.models.MicrosoftGraphAnalyticsActivityType
    :param start_date:
    :type start_date: ~datetime.date
    :param end_date:
    :type end_date: ~datetime.date
    :param time_zone_used:
    :type time_zone_used: str
    :param duration:
    :type duration: ~datetime.timedelta
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'activity': {'key': 'activity', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'date'},
        'end_date': {'key': 'endDate', 'type': 'date'},
        'time_zone_used': {'key': 'timeZoneUsed', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'duration'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        activity: Optional[Union[str, "MicrosoftGraphAnalyticsActivityType"]] = None,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        time_zone_used: Optional[str] = None,
        duration: Optional[datetime.timedelta] = None,
        **kwargs
    ):
        super(MicrosoftGraphActivityStatistics, self).__init__(id=id, **kwargs)
        self.activity = activity
        self.start_date = start_date
        self.end_date = end_date
        self.time_zone_used = time_zone_used
        self.duration = duration


class MicrosoftGraphInsightIdentity(msrest.serialization.Model):
    """insightIdentity.

    :param display_name: The display name of the user who shared the item.
    :type display_name: str
    :param id: The id of the user who shared the item.
    :type id: str
    :param address: The email address of the user who shared the item.
    :type address: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        address: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphInsightIdentity, self).__init__(**kwargs)
        self.display_name = display_name
        self.id = id
        self.address = address


class MicrosoftGraphOfficeGraphInsights(MicrosoftGraphEntity):
    """officeGraphInsights.

    :param id: Read-only.
    :type id: str
    :param trending: Calculated relationship identifying trending documents. Trending documents can
     be stored in OneDrive or in SharePoint sites.
    :type trending: list[~analytics.models.MicrosoftGraphTrending]
    :param shared: Calculated relationship identifying documents shared with a user. Documents can
     be shared as email attachments or as OneDrive for Business links sent in emails.
    :type shared: list[~analytics.models.MicrosoftGraphSharedInsight]
    :param used: Calculated relationship identifying documents viewed and modified by a user.
     Includes documents the user used in OneDrive for Business, SharePoint, opened as email
     attachments, and as link attachments from sources like Box, DropBox and Google Drive.
    :type used: list[~analytics.models.MicrosoftGraphUsedInsight]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'trending': {'key': 'trending', 'type': '[MicrosoftGraphTrending]'},
        'shared': {'key': 'shared', 'type': '[MicrosoftGraphSharedInsight]'},
        'used': {'key': 'used', 'type': '[MicrosoftGraphUsedInsight]'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        trending: Optional[List["MicrosoftGraphTrending"]] = None,
        shared: Optional[List["MicrosoftGraphSharedInsight"]] = None,
        used: Optional[List["MicrosoftGraphUsedInsight"]] = None,
        **kwargs
    ):
        super(MicrosoftGraphOfficeGraphInsights, self).__init__(id=id, **kwargs)
        self.trending = trending
        self.shared = shared
        self.used = used


class MicrosoftGraphResourceReference(msrest.serialization.Model):
    """resourceReference.

    :param web_url: A URL leading to the referenced item.
    :type web_url: str
    :param id: The item's unique identifier.
    :type id: str
    :param type: A string value that can be used to classify the item, such as
     'microsoft.graph.driveItem'.
    :type type: str
    """

    _attribute_map = {
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        web_url: Optional[str] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphResourceReference, self).__init__(**kwargs)
        self.web_url = web_url
        self.id = id
        self.type = type


class MicrosoftGraphResourceVisualization(msrest.serialization.Model):
    """resourceVisualization.

    :param title: The item's title text.
    :type title: str
    :param type: The item's media type. Can be used for filtering for a specific file based on a
     specific type. See below for supported types.
    :type type: str
    :param media_type: The item's media type. Can be used for filtering for a specific type of file
     based on supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
    :type media_type: str
    :param preview_image_url: A URL leading to the preview image for the item.
    :type preview_image_url: str
    :param preview_text: A preview text for the item.
    :type preview_text: str
    :param container_web_url: A path leading to the folder in which the item is stored.
    :type container_web_url: str
    :param container_display_name: A string describing where the item is stored. For example, the
     name of a SharePoint site or the user name identifying the owner of the OneDrive storing the
     item.
    :type container_display_name: str
    :param container_type: Can be used for filtering by the type of container in which the file is
     stored. Such as Site or OneDriveBusiness.
    :type container_type: str
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'preview_image_url': {'key': 'previewImageUrl', 'type': 'str'},
        'preview_text': {'key': 'previewText', 'type': 'str'},
        'container_web_url': {'key': 'containerWebUrl', 'type': 'str'},
        'container_display_name': {'key': 'containerDisplayName', 'type': 'str'},
        'container_type': {'key': 'containerType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        title: Optional[str] = None,
        type: Optional[str] = None,
        media_type: Optional[str] = None,
        preview_image_url: Optional[str] = None,
        preview_text: Optional[str] = None,
        container_web_url: Optional[str] = None,
        container_display_name: Optional[str] = None,
        container_type: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphResourceVisualization, self).__init__(**kwargs)
        self.title = title
        self.type = type
        self.media_type = media_type
        self.preview_image_url = preview_image_url
        self.preview_text = preview_text
        self.container_web_url = container_web_url
        self.container_display_name = container_display_name
        self.container_type = container_type


class MicrosoftGraphSettings(msrest.serialization.Model):
    """settings.

    :param has_license:
    :type has_license: bool
    :param has_opted_out:
    :type has_opted_out: bool
    :param has_graph_mailbox:
    :type has_graph_mailbox: bool
    """

    _attribute_map = {
        'has_license': {'key': 'hasLicense', 'type': 'bool'},
        'has_opted_out': {'key': 'hasOptedOut', 'type': 'bool'},
        'has_graph_mailbox': {'key': 'hasGraphMailbox', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        has_license: Optional[bool] = None,
        has_opted_out: Optional[bool] = None,
        has_graph_mailbox: Optional[bool] = None,
        **kwargs
    ):
        super(MicrosoftGraphSettings, self).__init__(**kwargs)
        self.has_license = has_license
        self.has_opted_out = has_opted_out
        self.has_graph_mailbox = has_graph_mailbox


class MicrosoftGraphSharedInsight(MicrosoftGraphEntity):
    """sharedInsight.

    :param id: Read-only.
    :type id: str
    :param sharing_history:
    :type sharing_history: list[~analytics.models.MicrosoftGraphSharingDetail]
    :param resource_visualization: resourceVisualization.
    :type resource_visualization: ~analytics.models.MicrosoftGraphResourceVisualization
    :param resource_reference: resourceReference.
    :type resource_reference: ~analytics.models.MicrosoftGraphResourceReference
    :param id_resource_id: Read-only.
    :type id_resource_id: str
    :param id_last_shared_method_id: Read-only.
    :type id_last_shared_method_id: str
    :param shared_by: insightIdentity.
    :type shared_by: ~analytics.models.MicrosoftGraphInsightIdentity
    :param shared_date_time: The date and time the file was last shared. The timestamp represents
     date and time information using ISO 8601 format and is always in UTC time. For example,
     midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.
    :type shared_date_time: ~datetime.datetime
    :param sharing_subject: The subject with which the document was shared.
    :type sharing_subject: str
    :param sharing_type: Determines the way the document was shared, can be by a 'Link',
     'Attachment', 'Group', 'Site'.
    :type sharing_type: str
    :param sharing_reference: resourceReference.
    :type sharing_reference: ~analytics.models.MicrosoftGraphResourceReference
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'sharing_history': {'key': 'sharingHistory', 'type': '[MicrosoftGraphSharingDetail]'},
        'resource_visualization': {'key': 'resourceVisualization', 'type': 'MicrosoftGraphResourceVisualization'},
        'resource_reference': {'key': 'resourceReference', 'type': 'MicrosoftGraphResourceReference'},
        'id_resource_id': {'key': 'resource.id', 'type': 'str'},
        'id_last_shared_method_id': {'key': 'lastSharedMethod.id', 'type': 'str'},
        'shared_by': {'key': 'lastShared.sharedBy', 'type': 'MicrosoftGraphInsightIdentity'},
        'shared_date_time': {'key': 'lastShared.sharedDateTime', 'type': 'iso-8601'},
        'sharing_subject': {'key': 'lastShared.sharingSubject', 'type': 'str'},
        'sharing_type': {'key': 'lastShared.sharingType', 'type': 'str'},
        'sharing_reference': {'key': 'lastShared.sharingReference', 'type': 'MicrosoftGraphResourceReference'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        sharing_history: Optional[List["MicrosoftGraphSharingDetail"]] = None,
        resource_visualization: Optional["MicrosoftGraphResourceVisualization"] = None,
        resource_reference: Optional["MicrosoftGraphResourceReference"] = None,
        id_resource_id: Optional[str] = None,
        id_last_shared_method_id: Optional[str] = None,
        shared_by: Optional["MicrosoftGraphInsightIdentity"] = None,
        shared_date_time: Optional[datetime.datetime] = None,
        sharing_subject: Optional[str] = None,
        sharing_type: Optional[str] = None,
        sharing_reference: Optional["MicrosoftGraphResourceReference"] = None,
        **kwargs
    ):
        super(MicrosoftGraphSharedInsight, self).__init__(id=id, **kwargs)
        self.sharing_history = sharing_history
        self.resource_visualization = resource_visualization
        self.resource_reference = resource_reference
        self.id_resource_id = id_resource_id
        self.id_last_shared_method_id = id_last_shared_method_id
        self.shared_by = shared_by
        self.shared_date_time = shared_date_time
        self.sharing_subject = sharing_subject
        self.sharing_type = sharing_type
        self.sharing_reference = sharing_reference


class MicrosoftGraphSharingDetail(msrest.serialization.Model):
    """sharingDetail.

    :param shared_by: insightIdentity.
    :type shared_by: ~analytics.models.MicrosoftGraphInsightIdentity
    :param shared_date_time: The date and time the file was last shared. The timestamp represents
     date and time information using ISO 8601 format and is always in UTC time. For example,
     midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z. Read-only.
    :type shared_date_time: ~datetime.datetime
    :param sharing_subject: The subject with which the document was shared.
    :type sharing_subject: str
    :param sharing_type: Determines the way the document was shared, can be by a 'Link',
     'Attachment', 'Group', 'Site'.
    :type sharing_type: str
    :param sharing_reference: resourceReference.
    :type sharing_reference: ~analytics.models.MicrosoftGraphResourceReference
    """

    _attribute_map = {
        'shared_by': {'key': 'sharedBy', 'type': 'MicrosoftGraphInsightIdentity'},
        'shared_date_time': {'key': 'sharedDateTime', 'type': 'iso-8601'},
        'sharing_subject': {'key': 'sharingSubject', 'type': 'str'},
        'sharing_type': {'key': 'sharingType', 'type': 'str'},
        'sharing_reference': {'key': 'sharingReference', 'type': 'MicrosoftGraphResourceReference'},
    }

    def __init__(
        self,
        *,
        shared_by: Optional["MicrosoftGraphInsightIdentity"] = None,
        shared_date_time: Optional[datetime.datetime] = None,
        sharing_subject: Optional[str] = None,
        sharing_type: Optional[str] = None,
        sharing_reference: Optional["MicrosoftGraphResourceReference"] = None,
        **kwargs
    ):
        super(MicrosoftGraphSharingDetail, self).__init__(**kwargs)
        self.shared_by = shared_by
        self.shared_date_time = shared_date_time
        self.sharing_subject = sharing_subject
        self.sharing_type = sharing_type
        self.sharing_reference = sharing_reference


class MicrosoftGraphTrending(MicrosoftGraphEntity):
    """trending.

    :param id: Read-only.
    :type id: str
    :param weight: Value indicating how much the document is currently trending. The larger the
     number, the more the document is currently trending around the user (the more relevant it is).
     Returned documents are sorted by this value.
    :type weight: float
    :param resource_visualization: resourceVisualization.
    :type resource_visualization: ~analytics.models.MicrosoftGraphResourceVisualization
    :param resource_reference: resourceReference.
    :type resource_reference: ~analytics.models.MicrosoftGraphResourceReference
    :param last_modified_date_time:
    :type last_modified_date_time: ~datetime.datetime
    :param id_resource_id: Read-only.
    :type id_resource_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'weight': {'key': 'weight', 'type': 'float'},
        'resource_visualization': {'key': 'resourceVisualization', 'type': 'MicrosoftGraphResourceVisualization'},
        'resource_reference': {'key': 'resourceReference', 'type': 'MicrosoftGraphResourceReference'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'id_resource_id': {'key': 'resource.id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        weight: Optional[float] = None,
        resource_visualization: Optional["MicrosoftGraphResourceVisualization"] = None,
        resource_reference: Optional["MicrosoftGraphResourceReference"] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        id_resource_id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphTrending, self).__init__(id=id, **kwargs)
        self.weight = weight
        self.resource_visualization = resource_visualization
        self.resource_reference = resource_reference
        self.last_modified_date_time = last_modified_date_time
        self.id_resource_id = id_resource_id


class MicrosoftGraphUsageDetails(msrest.serialization.Model):
    """usageDetails.

    :param last_accessed_date_time: The date and time the resource was last accessed by the user.
     The timestamp represents date and time information using ISO 8601 format and is always in UTC
     time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z.
     Read-only.
    :type last_accessed_date_time: ~datetime.datetime
    :param last_modified_date_time: The date and time the resource was last modified by the user.
     The timestamp represents date and time information using ISO 8601 format and is always in UTC
     time. For example, midnight UTC on Jan 1, 2014 would look like this: 2014-01-01T00:00:00Z.
     Read-only.
    :type last_modified_date_time: ~datetime.datetime
    """

    _attribute_map = {
        'last_accessed_date_time': {'key': 'lastAccessedDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        last_accessed_date_time: Optional[datetime.datetime] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(MicrosoftGraphUsageDetails, self).__init__(**kwargs)
        self.last_accessed_date_time = last_accessed_date_time
        self.last_modified_date_time = last_modified_date_time


class MicrosoftGraphUsedInsight(MicrosoftGraphEntity):
    """usedInsight.

    :param id: Read-only.
    :type id: str
    :param last_used: usageDetails.
    :type last_used: ~analytics.models.MicrosoftGraphUsageDetails
    :param resource_visualization: resourceVisualization.
    :type resource_visualization: ~analytics.models.MicrosoftGraphResourceVisualization
    :param resource_reference: resourceReference.
    :type resource_reference: ~analytics.models.MicrosoftGraphResourceReference
    :param id_resource_id: Read-only.
    :type id_resource_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'last_used': {'key': 'lastUsed', 'type': 'MicrosoftGraphUsageDetails'},
        'resource_visualization': {'key': 'resourceVisualization', 'type': 'MicrosoftGraphResourceVisualization'},
        'resource_reference': {'key': 'resourceReference', 'type': 'MicrosoftGraphResourceReference'},
        'id_resource_id': {'key': 'resource.id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        last_used: Optional["MicrosoftGraphUsageDetails"] = None,
        resource_visualization: Optional["MicrosoftGraphResourceVisualization"] = None,
        resource_reference: Optional["MicrosoftGraphResourceReference"] = None,
        id_resource_id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphUsedInsight, self).__init__(id=id, **kwargs)
        self.last_used = last_used
        self.resource_visualization = resource_visualization
        self.resource_reference = resource_reference
        self.id_resource_id = id_resource_id


class MicrosoftGraphUserAnalytics(MicrosoftGraphEntity):
    """userAnalytics.

    :param id: Read-only.
    :type id: str
    :param settings: settings.
    :type settings: ~analytics.models.MicrosoftGraphSettings
    :param activity_statistics:
    :type activity_statistics: list[~analytics.models.MicrosoftGraphActivityStatistics]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'settings': {'key': 'settings', 'type': 'MicrosoftGraphSettings'},
        'activity_statistics': {'key': 'activityStatistics', 'type': '[MicrosoftGraphActivityStatistics]'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        settings: Optional["MicrosoftGraphSettings"] = None,
        activity_statistics: Optional[List["MicrosoftGraphActivityStatistics"]] = None,
        **kwargs
    ):
        super(MicrosoftGraphUserAnalytics, self).__init__(id=id, **kwargs)
        self.settings = settings
        self.activity_statistics = activity_statistics


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~analytics.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        *,
        error: "OdataErrorMain",
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = error


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
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


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
    :type details: list[~analytics.models.OdataErrorDetail]
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
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        details: Optional[List["OdataErrorDetail"]] = None,
        innererror: Optional[object] = None,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror
