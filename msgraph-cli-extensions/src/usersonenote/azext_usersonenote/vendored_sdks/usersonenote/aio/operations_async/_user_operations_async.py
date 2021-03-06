# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserOperations:
    """UserOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_one_note.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_onenote(
        self,
        user_id: str,
        select: Optional[List[Union[str, "models.Get1ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get2ItemsItem"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphOnenote":
        """Get onenote from users.

        Get onenote from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_one_note.models.Get1ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_one_note.models.Get2ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenote, or the result of cls(response)
        :rtype: ~users_one_note.models.MicrosoftGraphOnenote
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenote"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_onenote.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenote', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_onenote.metadata = {'url': '/users/{user-id}/onenote'}  # type: ignore

    async def update_onenote(
        self,
        user_id: str,
        id: Optional[str] = None,
        notebooks: Optional[List["models.MicrosoftGraphNotebook"]] = None,
        sections: Optional[List["models.MicrosoftGraphOnenoteSection"]] = None,
        section_groups: Optional[List["models.MicrosoftGraphSectionGroup"]] = None,
        pages: Optional[List["models.MicrosoftGraphOnenotePage"]] = None,
        resources: Optional[List["models.MicrosoftGraphOnenoteResource"]] = None,
        operations: Optional[List["models.MicrosoftGraphOnenoteOperation"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property onenote in users.

        Update the navigation property onenote in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param notebooks: The collection of OneNote notebooks that are owned by the user or group.
         Read-only. Nullable.
        :type notebooks: list[~users_one_note.models.MicrosoftGraphNotebook]
        :param sections: The sections in all OneNote notebooks that are owned by the user or group.
         Read-only. Nullable.
        :type sections: list[~users_one_note.models.MicrosoftGraphOnenoteSection]
        :param section_groups: The section groups in all OneNote notebooks that are owned by the user
         or group.  Read-only. Nullable.
        :type section_groups: list[~users_one_note.models.MicrosoftGraphSectionGroup]
        :param pages: The pages in all OneNote notebooks that are owned by the user or group.  Read-
         only. Nullable.
        :type pages: list[~users_one_note.models.MicrosoftGraphOnenotePage]
        :param resources: The image and other file resources in OneNote pages. Getting a resources
         collection is not supported, but you can get the binary content of a specific resource. Read-
         only. Nullable.
        :type resources: list[~users_one_note.models.MicrosoftGraphOnenoteResource]
        :param operations: The status of OneNote operations. Getting an operations collection is not
         supported, but you can get the status of long-running operations if the Operation-Location
         header is returned in the response. Read-only. Nullable.
        :type operations: list[~users_one_note.models.MicrosoftGraphOnenoteOperation]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOnenote(id=id, notebooks=notebooks, sections=sections, section_groups=section_groups, pages=pages, resources=resources, operations=operations)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_onenote.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOnenote')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_onenote.metadata = {'url': '/users/{user-id}/onenote'}  # type: ignore
