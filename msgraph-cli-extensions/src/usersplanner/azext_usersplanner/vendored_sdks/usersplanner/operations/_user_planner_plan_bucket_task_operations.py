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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserPlannerPlanBucketTaskOperations(object):
    """UserPlannerPlanBucketTaskOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_planner.models
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

    def get_assigned_to_task_board_format(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum24"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat"
        """Get assignedToTaskBoardFormat from users.

        Get assignedToTaskBoardFormat from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_planner.models.Enum24]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat, or the result of cls(response)
        :rtype: ~users_planner.models.MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_assigned_to_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_assigned_to_task_board_format.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/assignedToTaskBoardFormat'}  # type: ignore

    def update_assigned_to_task_board_format(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        id=None,  # type: Optional[str]
        unassigned_order_hint=None,  # type: Optional[str]
        order_hints_by_assignee=None,  # type: Optional[object]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property assignedToTaskBoardFormat in users.

        Update the navigation property assignedToTaskBoardFormat in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param id: Read-only.
        :type id: str
        :param unassigned_order_hint: Hint value used to order the task on the AssignedTo view of the
         Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary
         does not provide an order hint for the user the task is assigned to. The format is defined as
         outlined here.
        :type unassigned_order_hint: str
        :param order_hints_by_assignee: Any object.
        :type order_hints_by_assignee: object
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat(id=id, unassigned_order_hint=unassigned_order_hint, order_hints_by_assignee=order_hints_by_assignee)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_assigned_to_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat')
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

    update_assigned_to_task_board_format.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/assignedToTaskBoardFormat'}  # type: ignore

    def get_bucket_task_board_format(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum25"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat"
        """Get bucketTaskBoardFormat from users.

        Get bucketTaskBoardFormat from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_planner.models.Enum25]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerBucketTaskBoardTaskFormat, or the result of cls(response)
        :rtype: ~users_planner.models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_bucket_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPlannerBucketTaskBoardTaskFormat', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_bucket_task_board_format.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/bucketTaskBoardFormat'}  # type: ignore

    def update_bucket_task_board_format(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        id=None,  # type: Optional[str]
        order_hint=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property bucketTaskBoardFormat in users.

        Update the navigation property bucketTaskBoardFormat in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param id: Read-only.
        :type id: str
        :param order_hint: Hint used to order tasks in the Bucket view of the Task Board. The format is
         defined as outlined here.
        :type order_hint: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat(id=id, order_hint=order_hint)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_bucket_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerBucketTaskBoardTaskFormat')
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

    update_bucket_task_board_format.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/bucketTaskBoardFormat'}  # type: ignore

    def get_detail(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum26"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerTaskDetails"
        """Get details from users.

        Get details from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_planner.models.Enum26]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerTaskDetails, or the result of cls(response)
        :rtype: ~users_planner.models.MicrosoftGraphPlannerTaskDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerTaskDetails"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_detail.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPlannerTaskDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_detail.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/details'}  # type: ignore

    def update_detail(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        id=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        preview_type=None,  # type: Optional[Union[str, "models.MicrosoftGraphPlannerPreviewType"]]
        references=None,  # type: Optional[object]
        checklist=None,  # type: Optional[object]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property details in users.

        Update the navigation property details in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param id: Read-only.
        :type id: str
        :param description: Description of the task.
        :type description: str
        :param preview_type:
        :type preview_type: str or ~users_planner.models.MicrosoftGraphPlannerPreviewType
        :param references: Any object.
        :type references: object
        :param checklist: Any object.
        :type checklist: object
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerTaskDetails(id=id, description=description, preview_type=preview_type, references=references, checklist=checklist)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_detail.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerTaskDetails')
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

    update_detail.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/details'}  # type: ignore

    def get_progress_task_board_format(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum27"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat"
        """Get progressTaskBoardFormat from users.

        Get progressTaskBoardFormat from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_planner.models.Enum27]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerProgressTaskBoardTaskFormat, or the result of cls(response)
        :rtype: ~users_planner.models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_progress_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPlannerProgressTaskBoardTaskFormat', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_progress_task_board_format.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/progressTaskBoardFormat'}  # type: ignore

    def update_progress_task_board_format(
        self,
        user_id,  # type: str
        planner_plan_id,  # type: str
        planner_bucket_id,  # type: str
        planner_task_id,  # type: str
        id=None,  # type: Optional[str]
        order_hint=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property progressTaskBoardFormat in users.

        Update the navigation property progressTaskBoardFormat in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param planner_plan_id: key: plannerPlan-id of plannerPlan.
        :type planner_plan_id: str
        :param planner_bucket_id: key: plannerBucket-id of plannerBucket.
        :type planner_bucket_id: str
        :param planner_task_id: key: plannerTask-id of plannerTask.
        :type planner_task_id: str
        :param id: Read-only.
        :type id: str
        :param order_hint: Hint value used to order the task on the Progress view of the Task Board.
         The format is defined as outlined here.
        :type order_hint: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat(id=id, order_hint=order_hint)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_progress_task_board_format.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'plannerPlan-id': self._serialize.url("planner_plan_id", planner_plan_id, 'str'),
            'plannerBucket-id': self._serialize.url("planner_bucket_id", planner_bucket_id, 'str'),
            'plannerTask-id': self._serialize.url("planner_task_id", planner_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerProgressTaskBoardTaskFormat')
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

    update_progress_task_board_format.metadata = {'url': '/users/{user-id}/planner/plans/{plannerPlan-id}/buckets/{plannerBucket-id}/tasks/{plannerTask-id}/progressTaskBoardFormat'}  # type: ignore
