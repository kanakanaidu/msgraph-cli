# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._places_enums import *


class CollectionOfPlace(msrest.serialization.Model):
    """Collection of place.

    :param value:
    :type value: list[~places.models.MicrosoftGraphPlace]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlace]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlace"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlace, self).__init__(**kwargs)
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


class MicrosoftGraphOutlookGeoCoordinates(msrest.serialization.Model):
    """outlookGeoCoordinates.

    :param altitude: The altitude of the location.
    :type altitude: float
    :param latitude: The latitude of the location.
    :type latitude: float
    :param longitude: The longitude of the location.
    :type longitude: float
    :param accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be
     measured in meters, such as the latitude and longitude are accurate to within 50 meters.
    :type accuracy: float
    :param altitude_accuracy: The accuracy of the altitude.
    :type altitude_accuracy: float
    """

    _attribute_map = {
        'altitude': {'key': 'altitude', 'type': 'float'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'accuracy': {'key': 'accuracy', 'type': 'float'},
        'altitude_accuracy': {'key': 'altitudeAccuracy', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        altitude: Optional[float] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        accuracy: Optional[float] = None,
        altitude_accuracy: Optional[float] = None,
        **kwargs
    ):
        super(MicrosoftGraphOutlookGeoCoordinates, self).__init__(**kwargs)
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy
        self.altitude_accuracy = altitude_accuracy


class MicrosoftGraphPhysicalAddress(msrest.serialization.Model):
    """physicalAddress.

    :param type:  Possible values include: "unknown", "home", "business", "other".
    :type type: str or ~places.models.MicrosoftGraphPhysicalAddressType
    :param post_office_box:
    :type post_office_box: str
    :param street: The street.
    :type street: str
    :param city: The city.
    :type city: str
    :param state: The state.
    :type state: str
    :param country_or_region: The country or region. It's a free-format string value, for example,
     'United States'.
    :type country_or_region: str
    :param postal_code: The postal code.
    :type postal_code: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'post_office_box': {'key': 'postOfficeBox', 'type': 'str'},
        'street': {'key': 'street', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "MicrosoftGraphPhysicalAddressType"]] = None,
        post_office_box: Optional[str] = None,
        street: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        country_or_region: Optional[str] = None,
        postal_code: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPhysicalAddress, self).__init__(**kwargs)
        self.type = type
        self.post_office_box = post_office_box
        self.street = street
        self.city = city
        self.state = state
        self.country_or_region = country_or_region
        self.postal_code = postal_code


class MicrosoftGraphPlace(MicrosoftGraphEntity):
    """place.

    :param id: Read-only.
    :type id: str
    :param display_name:
    :type display_name: str
    :param geo_coordinates: outlookGeoCoordinates.
    :type geo_coordinates: ~places.models.MicrosoftGraphOutlookGeoCoordinates
    :param phone:
    :type phone: str
    :param address: physicalAddress.
    :type address: ~places.models.MicrosoftGraphPhysicalAddress
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'geo_coordinates': {'key': 'geoCoordinates', 'type': 'MicrosoftGraphOutlookGeoCoordinates'},
        'phone': {'key': 'phone', 'type': 'str'},
        'address': {'key': 'address', 'type': 'MicrosoftGraphPhysicalAddress'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        display_name: Optional[str] = None,
        geo_coordinates: Optional["MicrosoftGraphOutlookGeoCoordinates"] = None,
        phone: Optional[str] = None,
        address: Optional["MicrosoftGraphPhysicalAddress"] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlace, self).__init__(id=id, **kwargs)
        self.display_name = display_name
        self.geo_coordinates = geo_coordinates
        self.phone = phone
        self.address = address


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~places.models.OdataErrorMain
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
    :type details: list[~places.models.OdataErrorDetail]
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
