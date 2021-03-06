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

from ._configuration import EducationConfiguration
from .operations import EducationRootOperations
from .operations import EducationOperations
from .operations import EducationClassOperations
from .operations import EducationClassAssignmentOperations
from .operations import EducationClassAssignmentSubmissionOperations
from .operations import EducationClassMemberOperations
from .operations import EducationClassSchoolOperations
from .operations import EducationClassTeacherOperations
from .operations import EducationMeOperations
from .operations import EducationMeAssignmentOperations
from .operations import EducationMeAssignmentSubmissionOperations
from .operations import EducationMeClassOperations
from .operations import EducationMeSchoolOperations
from .operations import EducationMeTaughtClassOperations
from .operations import EducationSchoolOperations
from .operations import EducationSchoolClassOperations
from .operations import EducationSchoolUserOperations
from .operations import EducationSynchronizationProfileOperations
from .operations import EducationUserOperations
from .operations import EducationUserAssignmentOperations
from .operations import EducationUserAssignmentSubmissionOperations
from .operations import EducationUserClassOperations
from .operations import EducationUserSchoolOperations
from .operations import EducationUserTaughtClassOperations
from . import models


class Education(object):
    """Education.

    :ivar education_root: EducationRootOperations operations
    :vartype education_root: education.operations.EducationRootOperations
    :ivar education: EducationOperations operations
    :vartype education: education.operations.EducationOperations
    :ivar education_class: EducationClassOperations operations
    :vartype education_class: education.operations.EducationClassOperations
    :ivar education_class_assignment: EducationClassAssignmentOperations operations
    :vartype education_class_assignment: education.operations.EducationClassAssignmentOperations
    :ivar education_class_assignment_submission: EducationClassAssignmentSubmissionOperations operations
    :vartype education_class_assignment_submission: education.operations.EducationClassAssignmentSubmissionOperations
    :ivar education_class_member: EducationClassMemberOperations operations
    :vartype education_class_member: education.operations.EducationClassMemberOperations
    :ivar education_class_school: EducationClassSchoolOperations operations
    :vartype education_class_school: education.operations.EducationClassSchoolOperations
    :ivar education_class_teacher: EducationClassTeacherOperations operations
    :vartype education_class_teacher: education.operations.EducationClassTeacherOperations
    :ivar education_me: EducationMeOperations operations
    :vartype education_me: education.operations.EducationMeOperations
    :ivar education_me_assignment: EducationMeAssignmentOperations operations
    :vartype education_me_assignment: education.operations.EducationMeAssignmentOperations
    :ivar education_me_assignment_submission: EducationMeAssignmentSubmissionOperations operations
    :vartype education_me_assignment_submission: education.operations.EducationMeAssignmentSubmissionOperations
    :ivar education_me_class: EducationMeClassOperations operations
    :vartype education_me_class: education.operations.EducationMeClassOperations
    :ivar education_me_school: EducationMeSchoolOperations operations
    :vartype education_me_school: education.operations.EducationMeSchoolOperations
    :ivar education_me_taught_class: EducationMeTaughtClassOperations operations
    :vartype education_me_taught_class: education.operations.EducationMeTaughtClassOperations
    :ivar education_school: EducationSchoolOperations operations
    :vartype education_school: education.operations.EducationSchoolOperations
    :ivar education_school_class: EducationSchoolClassOperations operations
    :vartype education_school_class: education.operations.EducationSchoolClassOperations
    :ivar education_school_user: EducationSchoolUserOperations operations
    :vartype education_school_user: education.operations.EducationSchoolUserOperations
    :ivar education_synchronization_profile: EducationSynchronizationProfileOperations operations
    :vartype education_synchronization_profile: education.operations.EducationSynchronizationProfileOperations
    :ivar education_user: EducationUserOperations operations
    :vartype education_user: education.operations.EducationUserOperations
    :ivar education_user_assignment: EducationUserAssignmentOperations operations
    :vartype education_user_assignment: education.operations.EducationUserAssignmentOperations
    :ivar education_user_assignment_submission: EducationUserAssignmentSubmissionOperations operations
    :vartype education_user_assignment_submission: education.operations.EducationUserAssignmentSubmissionOperations
    :ivar education_user_class: EducationUserClassOperations operations
    :vartype education_user_class: education.operations.EducationUserClassOperations
    :ivar education_user_school: EducationUserSchoolOperations operations
    :vartype education_user_school: education.operations.EducationUserSchoolOperations
    :ivar education_user_taught_class: EducationUserTaughtClassOperations operations
    :vartype education_user_taught_class: education.operations.EducationUserTaughtClassOperations
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
        self._config = EducationConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.education_root = EducationRootOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education = EducationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_class = EducationClassOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_class_assignment = EducationClassAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_class_assignment_submission = EducationClassAssignmentSubmissionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_class_member = EducationClassMemberOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_class_school = EducationClassSchoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_class_teacher = EducationClassTeacherOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_me = EducationMeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_me_assignment = EducationMeAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_me_assignment_submission = EducationMeAssignmentSubmissionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_me_class = EducationMeClassOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_me_school = EducationMeSchoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_me_taught_class = EducationMeTaughtClassOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_school = EducationSchoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_school_class = EducationSchoolClassOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_school_user = EducationSchoolUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_synchronization_profile = EducationSynchronizationProfileOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_user = EducationUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_user_assignment = EducationUserAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_user_assignment_submission = EducationUserAssignmentSubmissionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_user_class = EducationUserClassOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_user_school = EducationUserSchoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.education_user_taught_class = EducationUserTaughtClassOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Education
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
