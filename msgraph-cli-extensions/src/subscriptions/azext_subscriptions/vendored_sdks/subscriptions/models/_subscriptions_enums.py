# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    RESOURCE = "resource"
    CHANGE_TYPE = "changeType"
    CLIENT_STATE = "clientState"
    NOTIFICATION_URL = "notificationUrl"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    APPLICATION_ID = "applicationId"
    CREATOR_ID = "creatorId"
    INCLUDE_PROPERTIES = "includeProperties"
    INCLUDE_RESOURCE_DATA = "includeResourceData"
    LIFECYCLE_NOTIFICATION_URL = "lifecycleNotificationUrl"
    ENCRYPTION_CERTIFICATE = "encryptionCertificate"
    ENCRYPTION_CERTIFICATE_ID = "encryptionCertificateId"
    LATEST_SUPPORTED_TLS_VERSION = "latestSupportedTlsVersion"

class Get5ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    RESOURCE = "resource"
    RESOURCE_DESC = "resource desc"
    CHANGE_TYPE = "changeType"
    CHANGE_TYPE_DESC = "changeType desc"
    CLIENT_STATE = "clientState"
    CLIENT_STATE_DESC = "clientState desc"
    NOTIFICATION_URL = "notificationUrl"
    NOTIFICATION_URL_DESC = "notificationUrl desc"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    EXPIRATION_DATE_TIME_DESC = "expirationDateTime desc"
    APPLICATION_ID = "applicationId"
    APPLICATION_ID_DESC = "applicationId desc"
    CREATOR_ID = "creatorId"
    CREATOR_ID_DESC = "creatorId desc"
    INCLUDE_PROPERTIES = "includeProperties"
    INCLUDE_PROPERTIES_DESC = "includeProperties desc"
    INCLUDE_RESOURCE_DATA = "includeResourceData"
    INCLUDE_RESOURCE_DATA_DESC = "includeResourceData desc"
    LIFECYCLE_NOTIFICATION_URL = "lifecycleNotificationUrl"
    LIFECYCLE_NOTIFICATION_URL_DESC = "lifecycleNotificationUrl desc"
    ENCRYPTION_CERTIFICATE = "encryptionCertificate"
    ENCRYPTION_CERTIFICATE_DESC = "encryptionCertificate desc"
    ENCRYPTION_CERTIFICATE_ID = "encryptionCertificateId"
    ENCRYPTION_CERTIFICATE_ID_DESC = "encryptionCertificateId desc"
    LATEST_SUPPORTED_TLS_VERSION = "latestSupportedTlsVersion"
    LATEST_SUPPORTED_TLS_VERSION_DESC = "latestSupportedTlsVersion desc"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    RESOURCE = "resource"
    CHANGE_TYPE = "changeType"
    CLIENT_STATE = "clientState"
    NOTIFICATION_URL = "notificationUrl"
    EXPIRATION_DATE_TIME = "expirationDateTime"
    APPLICATION_ID = "applicationId"
    CREATOR_ID = "creatorId"
    INCLUDE_PROPERTIES = "includeProperties"
    INCLUDE_RESOURCE_DATA = "includeResourceData"
    LIFECYCLE_NOTIFICATION_URL = "lifecycleNotificationUrl"
    ENCRYPTION_CERTIFICATE = "encryptionCertificate"
    ENCRYPTION_CERTIFICATE_ID = "encryptionCertificateId"
    LATEST_SUPPORTED_TLS_VERSION = "latestSupportedTlsVersion"
