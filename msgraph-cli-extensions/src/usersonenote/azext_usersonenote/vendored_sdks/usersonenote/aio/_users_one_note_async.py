# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import UsersOneNoteConfiguration
from .operations_async import UserOperations
from .operations_async import UserOnenoteOperations
from .operations_async import UserOnenoteNotebookOperations
from .operations_async import UserOnenoteNotebookSectionGroupOperations
from .operations_async import UserOnenoteNotebookSectionGroupSectionOperations
from .operations_async import UserOnenoteNotebookSectionGroupSectionPageOperations
from .operations_async import UserOnenoteNotebookSectionOperations
from .operations_async import UserOnenoteNotebookSectionPageOperations
from .operations_async import UserOnenoteNotebookSectionParentSectionGroupOperations
from .operations_async import UserOnenotePageOperations
from .operations_async import UserOnenotePageParentNotebookOperations
from .operations_async import UserOnenotePageParentNotebookSectionGroupOperations
from .operations_async import UserOnenotePageParentNotebookSectionGroupSectionOperations
from .operations_async import UserOnenotePageParentNotebookSectionOperations
from .operations_async import UserOnenotePageParentNotebookSectionParentSectionGroupOperations
from .operations_async import UserOnenotePageParentSectionOperations
from .operations_async import UserOnenotePageParentSectionParentNotebookOperations
from .operations_async import UserOnenotePageParentSectionParentNotebookSectionGroupOperations
from .operations_async import UserOnenotePageParentSectionGroupOperations
from .operations_async import UserOnenotePageParentSectionGroupParentNotebookOperations
from .operations_async import UserOnenoteSectionGroupOperations
from .operations_async import UserOnenoteSectionGroupParentNotebookOperations
from .operations_async import UserOnenoteSectionGroupParentNotebookSectionOperations
from .operations_async import UserOnenoteSectionGroupParentNotebookSectionPageOperations
from .operations_async import UserOnenoteSectionGroupSectionOperations
from .operations_async import UserOnenoteSectionGroupSectionPageOperations
from .operations_async import UserOnenoteSectionGroupSectionPageParentNotebookOperations
from .operations_async import UserOnenoteSectionGroupSectionParentNotebookOperations
from .operations_async import UserOnenoteSectionOperations
from .operations_async import UserOnenoteSectionPageOperations
from .operations_async import UserOnenoteSectionPageParentNotebookOperations
from .operations_async import UserOnenoteSectionPageParentNotebookSectionGroupOperations
from .operations_async import UserOnenoteSectionParentNotebookOperations
from .operations_async import UserOnenoteSectionParentNotebookSectionGroupOperations
from .operations_async import UserOnenoteSectionParentSectionGroupOperations
from .operations_async import UserOnenoteSectionParentSectionGroupParentNotebookOperations
from .. import models


class UsersOneNote(object):
    """UsersOneNote.

    :ivar user: UserOperations operations
    :vartype user: users_one_note.aio.operations_async.UserOperations
    :ivar user_onenote: UserOnenoteOperations operations
    :vartype user_onenote: users_one_note.aio.operations_async.UserOnenoteOperations
    :ivar user_onenote_notebook: UserOnenoteNotebookOperations operations
    :vartype user_onenote_notebook: users_one_note.aio.operations_async.UserOnenoteNotebookOperations
    :ivar user_onenote_notebook_section_group: UserOnenoteNotebookSectionGroupOperations operations
    :vartype user_onenote_notebook_section_group: users_one_note.aio.operations_async.UserOnenoteNotebookSectionGroupOperations
    :ivar user_onenote_notebook_section_group_section: UserOnenoteNotebookSectionGroupSectionOperations operations
    :vartype user_onenote_notebook_section_group_section: users_one_note.aio.operations_async.UserOnenoteNotebookSectionGroupSectionOperations
    :ivar user_onenote_notebook_section_group_section_page: UserOnenoteNotebookSectionGroupSectionPageOperations operations
    :vartype user_onenote_notebook_section_group_section_page: users_one_note.aio.operations_async.UserOnenoteNotebookSectionGroupSectionPageOperations
    :ivar user_onenote_notebook_section: UserOnenoteNotebookSectionOperations operations
    :vartype user_onenote_notebook_section: users_one_note.aio.operations_async.UserOnenoteNotebookSectionOperations
    :ivar user_onenote_notebook_section_page: UserOnenoteNotebookSectionPageOperations operations
    :vartype user_onenote_notebook_section_page: users_one_note.aio.operations_async.UserOnenoteNotebookSectionPageOperations
    :ivar user_onenote_notebook_section_parent_section_group: UserOnenoteNotebookSectionParentSectionGroupOperations operations
    :vartype user_onenote_notebook_section_parent_section_group: users_one_note.aio.operations_async.UserOnenoteNotebookSectionParentSectionGroupOperations
    :ivar user_onenote_page: UserOnenotePageOperations operations
    :vartype user_onenote_page: users_one_note.aio.operations_async.UserOnenotePageOperations
    :ivar user_onenote_page_parent_notebook: UserOnenotePageParentNotebookOperations operations
    :vartype user_onenote_page_parent_notebook: users_one_note.aio.operations_async.UserOnenotePageParentNotebookOperations
    :ivar user_onenote_page_parent_notebook_section_group: UserOnenotePageParentNotebookSectionGroupOperations operations
    :vartype user_onenote_page_parent_notebook_section_group: users_one_note.aio.operations_async.UserOnenotePageParentNotebookSectionGroupOperations
    :ivar user_onenote_page_parent_notebook_section_group_section: UserOnenotePageParentNotebookSectionGroupSectionOperations operations
    :vartype user_onenote_page_parent_notebook_section_group_section: users_one_note.aio.operations_async.UserOnenotePageParentNotebookSectionGroupSectionOperations
    :ivar user_onenote_page_parent_notebook_section: UserOnenotePageParentNotebookSectionOperations operations
    :vartype user_onenote_page_parent_notebook_section: users_one_note.aio.operations_async.UserOnenotePageParentNotebookSectionOperations
    :ivar user_onenote_page_parent_notebook_section_parent_section_group: UserOnenotePageParentNotebookSectionParentSectionGroupOperations operations
    :vartype user_onenote_page_parent_notebook_section_parent_section_group: users_one_note.aio.operations_async.UserOnenotePageParentNotebookSectionParentSectionGroupOperations
    :ivar user_onenote_page_parent_section: UserOnenotePageParentSectionOperations operations
    :vartype user_onenote_page_parent_section: users_one_note.aio.operations_async.UserOnenotePageParentSectionOperations
    :ivar user_onenote_page_parent_section_parent_notebook: UserOnenotePageParentSectionParentNotebookOperations operations
    :vartype user_onenote_page_parent_section_parent_notebook: users_one_note.aio.operations_async.UserOnenotePageParentSectionParentNotebookOperations
    :ivar user_onenote_page_parent_section_parent_notebook_section_group: UserOnenotePageParentSectionParentNotebookSectionGroupOperations operations
    :vartype user_onenote_page_parent_section_parent_notebook_section_group: users_one_note.aio.operations_async.UserOnenotePageParentSectionParentNotebookSectionGroupOperations
    :ivar user_onenote_page_parent_section_group: UserOnenotePageParentSectionGroupOperations operations
    :vartype user_onenote_page_parent_section_group: users_one_note.aio.operations_async.UserOnenotePageParentSectionGroupOperations
    :ivar user_onenote_page_parent_section_group_parent_notebook: UserOnenotePageParentSectionGroupParentNotebookOperations operations
    :vartype user_onenote_page_parent_section_group_parent_notebook: users_one_note.aio.operations_async.UserOnenotePageParentSectionGroupParentNotebookOperations
    :ivar user_onenote_section_group: UserOnenoteSectionGroupOperations operations
    :vartype user_onenote_section_group: users_one_note.aio.operations_async.UserOnenoteSectionGroupOperations
    :ivar user_onenote_section_group_parent_notebook: UserOnenoteSectionGroupParentNotebookOperations operations
    :vartype user_onenote_section_group_parent_notebook: users_one_note.aio.operations_async.UserOnenoteSectionGroupParentNotebookOperations
    :ivar user_onenote_section_group_parent_notebook_section: UserOnenoteSectionGroupParentNotebookSectionOperations operations
    :vartype user_onenote_section_group_parent_notebook_section: users_one_note.aio.operations_async.UserOnenoteSectionGroupParentNotebookSectionOperations
    :ivar user_onenote_section_group_parent_notebook_section_page: UserOnenoteSectionGroupParentNotebookSectionPageOperations operations
    :vartype user_onenote_section_group_parent_notebook_section_page: users_one_note.aio.operations_async.UserOnenoteSectionGroupParentNotebookSectionPageOperations
    :ivar user_onenote_section_group_section: UserOnenoteSectionGroupSectionOperations operations
    :vartype user_onenote_section_group_section: users_one_note.aio.operations_async.UserOnenoteSectionGroupSectionOperations
    :ivar user_onenote_section_group_section_page: UserOnenoteSectionGroupSectionPageOperations operations
    :vartype user_onenote_section_group_section_page: users_one_note.aio.operations_async.UserOnenoteSectionGroupSectionPageOperations
    :ivar user_onenote_section_group_section_page_parent_notebook: UserOnenoteSectionGroupSectionPageParentNotebookOperations operations
    :vartype user_onenote_section_group_section_page_parent_notebook: users_one_note.aio.operations_async.UserOnenoteSectionGroupSectionPageParentNotebookOperations
    :ivar user_onenote_section_group_section_parent_notebook: UserOnenoteSectionGroupSectionParentNotebookOperations operations
    :vartype user_onenote_section_group_section_parent_notebook: users_one_note.aio.operations_async.UserOnenoteSectionGroupSectionParentNotebookOperations
    :ivar user_onenote_section: UserOnenoteSectionOperations operations
    :vartype user_onenote_section: users_one_note.aio.operations_async.UserOnenoteSectionOperations
    :ivar user_onenote_section_page: UserOnenoteSectionPageOperations operations
    :vartype user_onenote_section_page: users_one_note.aio.operations_async.UserOnenoteSectionPageOperations
    :ivar user_onenote_section_page_parent_notebook: UserOnenoteSectionPageParentNotebookOperations operations
    :vartype user_onenote_section_page_parent_notebook: users_one_note.aio.operations_async.UserOnenoteSectionPageParentNotebookOperations
    :ivar user_onenote_section_page_parent_notebook_section_group: UserOnenoteSectionPageParentNotebookSectionGroupOperations operations
    :vartype user_onenote_section_page_parent_notebook_section_group: users_one_note.aio.operations_async.UserOnenoteSectionPageParentNotebookSectionGroupOperations
    :ivar user_onenote_section_parent_notebook: UserOnenoteSectionParentNotebookOperations operations
    :vartype user_onenote_section_parent_notebook: users_one_note.aio.operations_async.UserOnenoteSectionParentNotebookOperations
    :ivar user_onenote_section_parent_notebook_section_group: UserOnenoteSectionParentNotebookSectionGroupOperations operations
    :vartype user_onenote_section_parent_notebook_section_group: users_one_note.aio.operations_async.UserOnenoteSectionParentNotebookSectionGroupOperations
    :ivar user_onenote_section_parent_section_group: UserOnenoteSectionParentSectionGroupOperations operations
    :vartype user_onenote_section_parent_section_group: users_one_note.aio.operations_async.UserOnenoteSectionParentSectionGroupOperations
    :ivar user_onenote_section_parent_section_group_parent_notebook: UserOnenoteSectionParentSectionGroupParentNotebookOperations operations
    :vartype user_onenote_section_parent_section_group_parent_notebook: users_one_note.aio.operations_async.UserOnenoteSectionParentSectionGroupParentNotebookOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
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
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = UsersOneNoteConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote = UserOnenoteOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook = UserOnenoteNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_group = UserOnenoteNotebookSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_group_section = UserOnenoteNotebookSectionGroupSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_group_section_page = UserOnenoteNotebookSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section = UserOnenoteNotebookSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_page = UserOnenoteNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_parent_section_group = UserOnenoteNotebookSectionParentSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page = UserOnenotePageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook = UserOnenotePageParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_group = UserOnenotePageParentNotebookSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_group_section = UserOnenotePageParentNotebookSectionGroupSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section = UserOnenotePageParentNotebookSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_parent_section_group = UserOnenotePageParentNotebookSectionParentSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section = UserOnenotePageParentSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section_parent_notebook = UserOnenotePageParentSectionParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section_parent_notebook_section_group = UserOnenotePageParentSectionParentNotebookSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section_group = UserOnenotePageParentSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section_group_parent_notebook = UserOnenotePageParentSectionGroupParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group = UserOnenoteSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_parent_notebook = UserOnenoteSectionGroupParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_parent_notebook_section = UserOnenoteSectionGroupParentNotebookSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_parent_notebook_section_page = UserOnenoteSectionGroupParentNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_section = UserOnenoteSectionGroupSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_section_page = UserOnenoteSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_section_page_parent_notebook = UserOnenoteSectionGroupSectionPageParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_section_parent_notebook = UserOnenoteSectionGroupSectionParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section = UserOnenoteSectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_page = UserOnenoteSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_page_parent_notebook = UserOnenoteSectionPageParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_page_parent_notebook_section_group = UserOnenoteSectionPageParentNotebookSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_parent_notebook = UserOnenoteSectionParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_parent_notebook_section_group = UserOnenoteSectionParentNotebookSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_parent_section_group = UserOnenoteSectionParentSectionGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_parent_section_group_parent_notebook = UserOnenoteSectionParentSectionGroupParentNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "UsersOneNote":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
