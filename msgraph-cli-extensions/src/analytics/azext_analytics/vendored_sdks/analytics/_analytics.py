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

from ._configuration import AnalyticsConfiguration
from .operations import ActivitystatisticActivityStatisticsOperations
from .operations import UserOperations
from .operations import UserAnalyticOperations
from .operations import UserInsightOperations
from .operations import UserInsightSharedOperations
from .operations import UserInsightTrendingOperations
from .operations import UserInsightUsedOperations
from . import models


class Analytics(object):
    """Analytics.

    :ivar activitystatistic_activity_statistics: ActivitystatisticActivityStatisticsOperations operations
    :vartype activitystatistic_activity_statistics: analytics.operations.ActivitystatisticActivityStatisticsOperations
    :ivar user: UserOperations operations
    :vartype user: analytics.operations.UserOperations
    :ivar user_analytic: UserAnalyticOperations operations
    :vartype user_analytic: analytics.operations.UserAnalyticOperations
    :ivar user_insight: UserInsightOperations operations
    :vartype user_insight: analytics.operations.UserInsightOperations
    :ivar user_insight_shared: UserInsightSharedOperations operations
    :vartype user_insight_shared: analytics.operations.UserInsightSharedOperations
    :ivar user_insight_trending: UserInsightTrendingOperations operations
    :vartype user_insight_trending: analytics.operations.UserInsightTrendingOperations
    :ivar user_insight_used: UserInsightUsedOperations operations
    :vartype user_insight_used: analytics.operations.UserInsightUsedOperations
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
        self._config = AnalyticsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.activitystatistic_activity_statistics = ActivitystatisticActivityStatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_analytic = UserAnalyticOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_insight = UserInsightOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_insight_shared = UserInsightSharedOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_insight_trending = UserInsightTrendingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_insight_used = UserInsightUsedOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Analytics
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)