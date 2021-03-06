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


class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    NAME = "name"
    PLAN_ID = "planId"
    ORDER_HINT = "orderHint"
    TASKS = "tasks"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CREATED_BY = "createdBy"
    CREATED_BY_DESC = "createdBy desc"
    PLAN_ID = "planId"
    PLAN_ID_DESC = "planId desc"
    BUCKET_ID = "bucketId"
    BUCKET_ID_DESC = "bucketId desc"
    TITLE = "title"
    TITLE_DESC = "title desc"
    ORDER_HINT = "orderHint"
    ORDER_HINT_DESC = "orderHint desc"
    ASSIGNEE_PRIORITY = "assigneePriority"
    ASSIGNEE_PRIORITY_DESC = "assigneePriority desc"
    PERCENT_COMPLETE = "percentComplete"
    PERCENT_COMPLETE_DESC = "percentComplete desc"
    PRIORITY = "priority"
    PRIORITY_DESC = "priority desc"
    START_DATE_TIME = "startDateTime"
    START_DATE_TIME_DESC = "startDateTime desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DUE_DATE_TIME = "dueDateTime"
    DUE_DATE_TIME_DESC = "dueDateTime desc"
    HAS_DESCRIPTION = "hasDescription"
    HAS_DESCRIPTION_DESC = "hasDescription desc"
    PREVIEW_TYPE = "previewType"
    PREVIEW_TYPE_DESC = "previewType desc"
    COMPLETED_DATE_TIME = "completedDateTime"
    COMPLETED_DATE_TIME_DESC = "completedDateTime desc"
    COMPLETED_BY = "completedBy"
    COMPLETED_BY_DESC = "completedBy desc"
    REFERENCE_COUNT = "referenceCount"
    REFERENCE_COUNT_DESC = "referenceCount desc"
    CHECKLIST_ITEM_COUNT = "checklistItemCount"
    CHECKLIST_ITEM_COUNT_DESC = "checklistItemCount desc"
    ACTIVE_CHECKLIST_ITEM_COUNT = "activeChecklistItemCount"
    ACTIVE_CHECKLIST_ITEM_COUNT_DESC = "activeChecklistItemCount desc"
    APPLIED_CATEGORIES = "appliedCategories"
    APPLIED_CATEGORIES_DESC = "appliedCategories desc"
    ASSIGNMENTS = "assignments"
    ASSIGNMENTS_DESC = "assignments desc"
    CONVERSATION_THREAD_ID = "conversationThreadId"
    CONVERSATION_THREAD_ID_DESC = "conversationThreadId desc"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    PLAN_ID = "planId"
    BUCKET_ID = "bucketId"
    TITLE = "title"
    ORDER_HINT = "orderHint"
    ASSIGNEE_PRIORITY = "assigneePriority"
    PERCENT_COMPLETE = "percentComplete"
    PRIORITY = "priority"
    START_DATE_TIME = "startDateTime"
    CREATED_DATE_TIME = "createdDateTime"
    DUE_DATE_TIME = "dueDateTime"
    HAS_DESCRIPTION = "hasDescription"
    PREVIEW_TYPE = "previewType"
    COMPLETED_DATE_TIME = "completedDateTime"
    COMPLETED_BY = "completedBy"
    REFERENCE_COUNT = "referenceCount"
    CHECKLIST_ITEM_COUNT = "checklistItemCount"
    ACTIVE_CHECKLIST_ITEM_COUNT = "activeChecklistItemCount"
    APPLIED_CATEGORIES = "appliedCategories"
    ASSIGNMENTS = "assignments"
    CONVERSATION_THREAD_ID = "conversationThreadId"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    PLAN_ID = "planId"
    BUCKET_ID = "bucketId"
    TITLE = "title"
    ORDER_HINT = "orderHint"
    ASSIGNEE_PRIORITY = "assigneePriority"
    PERCENT_COMPLETE = "percentComplete"
    PRIORITY = "priority"
    START_DATE_TIME = "startDateTime"
    CREATED_DATE_TIME = "createdDateTime"
    DUE_DATE_TIME = "dueDateTime"
    HAS_DESCRIPTION = "hasDescription"
    PREVIEW_TYPE = "previewType"
    COMPLETED_DATE_TIME = "completedDateTime"
    COMPLETED_BY = "completedBy"
    REFERENCE_COUNT = "referenceCount"
    CHECKLIST_ITEM_COUNT = "checklistItemCount"
    ACTIVE_CHECKLIST_ITEM_COUNT = "activeChecklistItemCount"
    APPLIED_CATEGORIES = "appliedCategories"
    ASSIGNMENTS = "assignments"
    CONVERSATION_THREAD_ID = "conversationThreadId"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    UNASSIGNED_ORDER_HINT = "unassignedOrderHint"
    ORDER_HINTS_BY_ASSIGNEE = "orderHintsByAssignee"

class Enum19(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ORDER_HINT = "orderHint"

class Enum20(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DESCRIPTION = "description"
    PREVIEW_TYPE = "previewType"
    REFERENCES = "references"
    CHECKLIST = "checklist"

class Enum21(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ORDER_HINT = "orderHint"

class Enum22(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    SHARED_WITH = "sharedWith"
    CATEGORY_DESCRIPTIONS = "categoryDescriptions"
    CONTEXT_DETAILS = "contextDetails"

class Enum23(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CREATED_BY = "createdBy"
    CREATED_BY_DESC = "createdBy desc"
    PLAN_ID = "planId"
    PLAN_ID_DESC = "planId desc"
    BUCKET_ID = "bucketId"
    BUCKET_ID_DESC = "bucketId desc"
    TITLE = "title"
    TITLE_DESC = "title desc"
    ORDER_HINT = "orderHint"
    ORDER_HINT_DESC = "orderHint desc"
    ASSIGNEE_PRIORITY = "assigneePriority"
    ASSIGNEE_PRIORITY_DESC = "assigneePriority desc"
    PERCENT_COMPLETE = "percentComplete"
    PERCENT_COMPLETE_DESC = "percentComplete desc"
    PRIORITY = "priority"
    PRIORITY_DESC = "priority desc"
    START_DATE_TIME = "startDateTime"
    START_DATE_TIME_DESC = "startDateTime desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DUE_DATE_TIME = "dueDateTime"
    DUE_DATE_TIME_DESC = "dueDateTime desc"
    HAS_DESCRIPTION = "hasDescription"
    HAS_DESCRIPTION_DESC = "hasDescription desc"
    PREVIEW_TYPE = "previewType"
    PREVIEW_TYPE_DESC = "previewType desc"
    COMPLETED_DATE_TIME = "completedDateTime"
    COMPLETED_DATE_TIME_DESC = "completedDateTime desc"
    COMPLETED_BY = "completedBy"
    COMPLETED_BY_DESC = "completedBy desc"
    REFERENCE_COUNT = "referenceCount"
    REFERENCE_COUNT_DESC = "referenceCount desc"
    CHECKLIST_ITEM_COUNT = "checklistItemCount"
    CHECKLIST_ITEM_COUNT_DESC = "checklistItemCount desc"
    ACTIVE_CHECKLIST_ITEM_COUNT = "activeChecklistItemCount"
    ACTIVE_CHECKLIST_ITEM_COUNT_DESC = "activeChecklistItemCount desc"
    APPLIED_CATEGORIES = "appliedCategories"
    APPLIED_CATEGORIES_DESC = "appliedCategories desc"
    ASSIGNMENTS = "assignments"
    ASSIGNMENTS_DESC = "assignments desc"
    CONVERSATION_THREAD_ID = "conversationThreadId"
    CONVERSATION_THREAD_ID_DESC = "conversationThreadId desc"

class Enum24(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    PLAN_ID = "planId"
    BUCKET_ID = "bucketId"
    TITLE = "title"
    ORDER_HINT = "orderHint"
    ASSIGNEE_PRIORITY = "assigneePriority"
    PERCENT_COMPLETE = "percentComplete"
    PRIORITY = "priority"
    START_DATE_TIME = "startDateTime"
    CREATED_DATE_TIME = "createdDateTime"
    DUE_DATE_TIME = "dueDateTime"
    HAS_DESCRIPTION = "hasDescription"
    PREVIEW_TYPE = "previewType"
    COMPLETED_DATE_TIME = "completedDateTime"
    COMPLETED_BY = "completedBy"
    REFERENCE_COUNT = "referenceCount"
    CHECKLIST_ITEM_COUNT = "checklistItemCount"
    ACTIVE_CHECKLIST_ITEM_COUNT = "activeChecklistItemCount"
    APPLIED_CATEGORIES = "appliedCategories"
    ASSIGNMENTS = "assignments"
    CONVERSATION_THREAD_ID = "conversationThreadId"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Enum25(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Enum26(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    PLAN_ID = "planId"
    BUCKET_ID = "bucketId"
    TITLE = "title"
    ORDER_HINT = "orderHint"
    ASSIGNEE_PRIORITY = "assigneePriority"
    PERCENT_COMPLETE = "percentComplete"
    PRIORITY = "priority"
    START_DATE_TIME = "startDateTime"
    CREATED_DATE_TIME = "createdDateTime"
    DUE_DATE_TIME = "dueDateTime"
    HAS_DESCRIPTION = "hasDescription"
    PREVIEW_TYPE = "previewType"
    COMPLETED_DATE_TIME = "completedDateTime"
    COMPLETED_BY = "completedBy"
    REFERENCE_COUNT = "referenceCount"
    CHECKLIST_ITEM_COUNT = "checklistItemCount"
    ACTIVE_CHECKLIST_ITEM_COUNT = "activeChecklistItemCount"
    APPLIED_CATEGORIES = "appliedCategories"
    ASSIGNMENTS = "assignments"
    CONVERSATION_THREAD_ID = "conversationThreadId"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Enum27(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Enum28(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    UNASSIGNED_ORDER_HINT = "unassignedOrderHint"
    ORDER_HINTS_BY_ASSIGNEE = "orderHintsByAssignee"

class Enum29(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ORDER_HINT = "orderHint"

class Enum30(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DESCRIPTION = "description"
    PREVIEW_TYPE = "previewType"
    REFERENCES = "references"
    CHECKLIST = "checklist"

class Enum31(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ORDER_HINT = "orderHint"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    CREATED_DATE_TIME = "createdDateTime"
    OWNER = "owner"
    TITLE = "title"
    CONTEXTS = "contexts"
    TASKS = "tasks"
    BUCKETS = "buckets"
    DETAILS = "details"

class Enum8(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    NAME = "name"
    NAME_DESC = "name desc"
    PLAN_ID = "planId"
    PLAN_ID_DESC = "planId desc"
    ORDER_HINT = "orderHint"
    ORDER_HINT_DESC = "orderHint desc"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    NAME = "name"
    PLAN_ID = "planId"
    ORDER_HINT = "orderHint"
    TASKS = "tasks"

class Get10ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    PLANS = "plans"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    PLANS = "plans"

class Get3ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"
    BUCKETS = "buckets"
    DETAILS = "details"

class Get4ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"

class Get5ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DETAILS = "details"
    ASSIGNED_TO_TASK_BOARD_FORMAT = "assignedToTaskBoardFormat"
    PROGRESS_TASK_BOARD_FORMAT = "progressTaskBoardFormat"
    BUCKET_TASK_BOARD_FORMAT = "bucketTaskBoardFormat"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CREATED_BY = "createdBy"
    CREATED_BY_DESC = "createdBy desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    OWNER = "owner"
    OWNER_DESC = "owner desc"
    TITLE = "title"
    TITLE_DESC = "title desc"
    CONTEXTS = "contexts"
    CONTEXTS_DESC = "contexts desc"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    CREATED_DATE_TIME = "createdDateTime"
    OWNER = "owner"
    TITLE = "title"
    CONTEXTS = "contexts"
    TASKS = "tasks"
    BUCKETS = "buckets"
    DETAILS = "details"

class Get8ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"
    BUCKETS = "buckets"
    DETAILS = "details"

class Get9ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"

class MicrosoftGraphPlannerPreviewType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTOMATIC = "automatic"
    NO_PREVIEW = "noPreview"
    CHECKLIST = "checklist"
    DESCRIPTION = "description"
    REFERENCE = "reference"
