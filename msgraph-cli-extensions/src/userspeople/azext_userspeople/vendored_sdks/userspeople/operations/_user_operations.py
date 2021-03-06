# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserOperations(object):
    """UserOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_people.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_person(
        self,
        user_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Get6ItemsItem"]]]
        select=None,  # type: Optional[List[Union[str, "models.Get7ItemsItem"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPerson"]
        """Get people from users.

        Get people from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~users_people.models.Get6ItemsItem]
        :param select: Select properties to be returned.
        :type select: list[str or ~users_people.models.Get7ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPerson or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~users_people.models.CollectionOfPerson]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPerson"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_person.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfPerson', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_person.metadata = {'url': '/users/{user-id}/people'}  # type: ignore

    def create_person(
        self,
        user_id,  # type: str
        id=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        given_name=None,  # type: Optional[str]
        surname=None,  # type: Optional[str]
        birthday=None,  # type: Optional[str]
        person_notes=None,  # type: Optional[str]
        is_favorite=None,  # type: Optional[bool]
        email_addresses=None,  # type: Optional[List["models.MicrosoftGraphRankedEmailAddress"]]
        phones=None,  # type: Optional[List["models.MicrosoftGraphPhone"]]
        postal_addresses=None,  # type: Optional[List["models.MicrosoftGraphLocation"]]
        websites=None,  # type: Optional[List["models.MicrosoftGraphWebsite"]]
        title=None,  # type: Optional[str]
        company_name=None,  # type: Optional[str]
        yomi_company=None,  # type: Optional[str]
        department=None,  # type: Optional[str]
        office_location=None,  # type: Optional[str]
        profession=None,  # type: Optional[str]
        sources=None,  # type: Optional[List["models.MicrosoftGraphPersonDataSource"]]
        mailbox_type=None,  # type: Optional[str]
        person_type=None,  # type: Optional[str]
        user_principal_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPerson"
        """Create new navigation property to people for users.

        Create new navigation property to people for users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param display_name: The person's display name.
        :type display_name: str
        :param given_name: The person's given name.
        :type given_name: str
        :param surname: The person's surname.
        :type surname: str
        :param birthday: The person's birthday.
        :type birthday: str
        :param person_notes: Free-form notes that the user has taken about this person.
        :type person_notes: str
        :param is_favorite: true if the user has flagged this person as a favorite.
        :type is_favorite: bool
        :param email_addresses:
        :type email_addresses: list[~users_people.models.MicrosoftGraphRankedEmailAddress]
        :param phones: The person's phone numbers.
        :type phones: list[~users_people.models.MicrosoftGraphPhone]
        :param postal_addresses: The person's addresses.
        :type postal_addresses: list[~users_people.models.MicrosoftGraphLocation]
        :param websites: The person's websites.
        :type websites: list[~users_people.models.MicrosoftGraphWebsite]
        :param title:
        :type title: str
        :param company_name: The name of the person's company.
        :type company_name: str
        :param yomi_company: The phonetic Japanese name of the person's company.
        :type yomi_company: str
        :param department: The person's department.
        :type department: str
        :param office_location: The location of the person's office.
        :type office_location: str
        :param profession: The person's profession.
        :type profession: str
        :param sources:
        :type sources: list[~users_people.models.MicrosoftGraphPersonDataSource]
        :param mailbox_type:
        :type mailbox_type: str
        :param person_type: The type of person.
        :type person_type: str
        :param user_principal_name: The user principal name (UPN) of the person. The UPN is an
         Internet-style login name for the person based on the Internet standard RFC 822. By convention,
         this should map to the person's email name. The general format is alias@domain.
        :type user_principal_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPerson, or the result of cls(response)
        :rtype: ~users_people.models.MicrosoftGraphPerson
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPerson"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPerson(id=id, display_name=display_name, given_name=given_name, surname=surname, birthday=birthday, person_notes=person_notes, is_favorite=is_favorite, email_addresses=email_addresses, phones=phones, postal_addresses=postal_addresses, websites=websites, title=title, company_name=company_name, yomi_company=yomi_company, department=department, office_location=office_location, profession=profession, sources=sources, mailbox_type=mailbox_type, person_type=person_type, user_principal_name=user_principal_name)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPerson')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPerson', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_person.metadata = {'url': '/users/{user-id}/people'}  # type: ignore

    def get_person(
        self,
        user_id,  # type: str
        person_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Get2ItemsItem"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPerson"
        """Get people from users.

        Get people from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param person_id: key: person-id of person.
        :type person_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_people.models.Get2ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPerson, or the result of cls(response)
        :rtype: ~users_people.models.MicrosoftGraphPerson
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPerson"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'person-id': self._serialize.url("person_id", person_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPerson', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_person.metadata = {'url': '/users/{user-id}/people/{person-id}'}  # type: ignore

    def update_person(
        self,
        user_id,  # type: str
        person_id,  # type: str
        id=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        given_name=None,  # type: Optional[str]
        surname=None,  # type: Optional[str]
        birthday=None,  # type: Optional[str]
        person_notes=None,  # type: Optional[str]
        is_favorite=None,  # type: Optional[bool]
        email_addresses=None,  # type: Optional[List["models.MicrosoftGraphRankedEmailAddress"]]
        phones=None,  # type: Optional[List["models.MicrosoftGraphPhone"]]
        postal_addresses=None,  # type: Optional[List["models.MicrosoftGraphLocation"]]
        websites=None,  # type: Optional[List["models.MicrosoftGraphWebsite"]]
        title=None,  # type: Optional[str]
        company_name=None,  # type: Optional[str]
        yomi_company=None,  # type: Optional[str]
        department=None,  # type: Optional[str]
        office_location=None,  # type: Optional[str]
        profession=None,  # type: Optional[str]
        sources=None,  # type: Optional[List["models.MicrosoftGraphPersonDataSource"]]
        mailbox_type=None,  # type: Optional[str]
        person_type=None,  # type: Optional[str]
        user_principal_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property people in users.

        Update the navigation property people in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param person_id: key: person-id of person.
        :type person_id: str
        :param id: Read-only.
        :type id: str
        :param display_name: The person's display name.
        :type display_name: str
        :param given_name: The person's given name.
        :type given_name: str
        :param surname: The person's surname.
        :type surname: str
        :param birthday: The person's birthday.
        :type birthday: str
        :param person_notes: Free-form notes that the user has taken about this person.
        :type person_notes: str
        :param is_favorite: true if the user has flagged this person as a favorite.
        :type is_favorite: bool
        :param email_addresses:
        :type email_addresses: list[~users_people.models.MicrosoftGraphRankedEmailAddress]
        :param phones: The person's phone numbers.
        :type phones: list[~users_people.models.MicrosoftGraphPhone]
        :param postal_addresses: The person's addresses.
        :type postal_addresses: list[~users_people.models.MicrosoftGraphLocation]
        :param websites: The person's websites.
        :type websites: list[~users_people.models.MicrosoftGraphWebsite]
        :param title:
        :type title: str
        :param company_name: The name of the person's company.
        :type company_name: str
        :param yomi_company: The phonetic Japanese name of the person's company.
        :type yomi_company: str
        :param department: The person's department.
        :type department: str
        :param office_location: The location of the person's office.
        :type office_location: str
        :param profession: The person's profession.
        :type profession: str
        :param sources:
        :type sources: list[~users_people.models.MicrosoftGraphPersonDataSource]
        :param mailbox_type:
        :type mailbox_type: str
        :param person_type: The type of person.
        :type person_type: str
        :param user_principal_name: The user principal name (UPN) of the person. The UPN is an
         Internet-style login name for the person based on the Internet standard RFC 822. By convention,
         this should map to the person's email name. The general format is alias@domain.
        :type user_principal_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPerson(id=id, display_name=display_name, given_name=given_name, surname=surname, birthday=birthday, person_notes=person_notes, is_favorite=is_favorite, email_addresses=email_addresses, phones=phones, postal_addresses=postal_addresses, websites=websites, title=title, company_name=company_name, yomi_company=yomi_company, department=department, office_location=office_location, profession=profession, sources=sources, mailbox_type=mailbox_type, person_type=person_type, user_principal_name=user_principal_name)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'person-id': self._serialize.url("person_id", person_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPerson')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_person.metadata = {'url': '/users/{user-id}/people/{person-id}'}  # type: ignore
