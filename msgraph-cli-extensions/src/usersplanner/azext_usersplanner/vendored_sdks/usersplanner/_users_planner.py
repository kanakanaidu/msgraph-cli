# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import UsersPlannerConfiguration
from .operations import UserOperations
from .operations import UserPlannerOperations
from .operations import UserPlannerPlanOperations
from .operations import UserPlannerPlanBucketOperations
from .operations import UserPlannerPlanBucketTaskOperations
from .operations import UserPlannerPlanTaskOperations
from .operations import UserPlannerTaskOperations
from . import models


class UsersPlanner(object):
    """UsersPlanner.

    :ivar user: UserOperations operations
    :vartype user: users_planner.operations.UserOperations
    :ivar user_planner: UserPlannerOperations operations
    :vartype user_planner: users_planner.operations.UserPlannerOperations
    :ivar user_planner_plan: UserPlannerPlanOperations operations
    :vartype user_planner_plan: users_planner.operations.UserPlannerPlanOperations
    :ivar user_planner_plan_bucket: UserPlannerPlanBucketOperations operations
    :vartype user_planner_plan_bucket: users_planner.operations.UserPlannerPlanBucketOperations
    :ivar user_planner_plan_bucket_task: UserPlannerPlanBucketTaskOperations operations
    :vartype user_planner_plan_bucket_task: users_planner.operations.UserPlannerPlanBucketTaskOperations
    :ivar user_planner_plan_task: UserPlannerPlanTaskOperations operations
    :vartype user_planner_plan_task: users_planner.operations.UserPlannerPlanTaskOperations
    :ivar user_planner_task: UserPlannerTaskOperations operations
    :vartype user_planner_task: users_planner.operations.UserPlannerTaskOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = UsersPlannerConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner = UserPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan = UserPlannerPlanOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan_bucket = UserPlannerPlanBucketOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan_bucket_task = UserPlannerPlanBucketTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_plan_task = UserPlannerPlanTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_task = UserPlannerTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> UsersPlanner
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
