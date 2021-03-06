# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_enum_type
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_groupsplanner.action import (
    AddDetailsCategoryDescriptions,
    AddCreatedByApplication
)


def load_arguments(self, _):

    with self.argument_context('groupsplanner get-planner') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner update-planner') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('plans', type=validate_file_or_dict, help='Read-only. Nullable. Returns the plannerPlans owned by '
                   'the group. Expected value: json-string/@json-file.')

    with self.argument_context('groupsplanner create-plan') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='Read-only. Date and time at which the plan is created. The Timestamp '
                   'type represents date and time information using ISO 8601 format and is always in UTC time. For '
                   'example, midnight UTC on Jan 1, 2014 would look like this: \'2014-01-01T00:00:00Z\'')
        c.argument('owner', type=str, help='ID of the Group that owns the plan. A valid group must exist before this '
                   'field can be set. After it is set, this property can’t be updated.')
        c.argument('title', type=str, help='Required. Title of the plan.')
        c.argument('contexts', type=validate_file_or_dict, help='Any object Expected value: json-string/@json-file.')
        c.argument('tasks', type=validate_file_or_dict, help='Read-only. Nullable. Collection of tasks in the plan. '
                   'Expected value: json-string/@json-file.')
        c.argument('buckets', type=validate_file_or_dict, help='Read-only. Nullable. Collection of buckets in the '
                   'plan. Expected value: json-string/@json-file.')
        c.argument('details_id', type=str, help='Read-only.')
        c.argument('details_shared_with', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')
        c.argument('details_category_descriptions', action=AddDetailsCategoryDescriptions, nargs='*', help=''
                   'plannerCategoryDescriptions')
        c.argument('details_context_details', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')
        c.argument('created_by_application', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_device', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_user', action=AddCreatedByApplication, nargs='*', help='identity')

    with self.argument_context('groupsplanner get-plan') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner list-plan') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner update-plan') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='Read-only. Date and time at which the plan is created. The Timestamp '
                   'type represents date and time information using ISO 8601 format and is always in UTC time. For '
                   'example, midnight UTC on Jan 1, 2014 would look like this: \'2014-01-01T00:00:00Z\'')
        c.argument('owner', type=str, help='ID of the Group that owns the plan. A valid group must exist before this '
                   'field can be set. After it is set, this property can’t be updated.')
        c.argument('title', type=str, help='Required. Title of the plan.')
        c.argument('contexts', type=validate_file_or_dict, help='Any object Expected value: json-string/@json-file.')
        c.argument('tasks', type=validate_file_or_dict, help='Read-only. Nullable. Collection of tasks in the plan. '
                   'Expected value: json-string/@json-file.')
        c.argument('buckets', type=validate_file_or_dict, help='Read-only. Nullable. Collection of buckets in the '
                   'plan. Expected value: json-string/@json-file.')
        c.argument('details_id', type=str, help='Read-only.')
        c.argument('details_shared_with', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')
        c.argument('details_category_descriptions', action=AddDetailsCategoryDescriptions, nargs='*', help=''
                   'plannerCategoryDescriptions')
        c.argument('details_context_details', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')
        c.argument('created_by_application', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_device', action=AddCreatedByApplication, nargs='*', help='identity')
        c.argument('created_by_user', action=AddCreatedByApplication, nargs='*', help='identity')

    with self.argument_context('groupsplanner create-bucket') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('name', type=str, help='Name of the bucket.')
        c.argument('plan_id', type=str, help='Plan ID to which the bucket belongs.')
        c.argument('order_hint', type=str, help='Hint used to order items of this type in a list view. The format is '
                   'defined as outlined here.')
        c.argument('tasks', type=validate_file_or_dict, help='Read-only. Nullable. The collection of tasks in the '
                   'bucket. Expected value: json-string/@json-file.')

    with self.argument_context('groupsplanner create-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('body', type=validate_file_or_dict, help='New navigation property Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner get-bucket') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-detail') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner list-bucket') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner list-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner update-bucket') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('name', type=str, help='Name of the bucket.')
        c.argument('plan_id', type=str, help='Plan ID to which the bucket belongs.')
        c.argument('order_hint', type=str, help='Hint used to order items of this type in a list view. The format is '
                   'defined as outlined here.')
        c.argument('tasks', type=validate_file_or_dict, help='Read-only. Nullable. The collection of tasks in the '
                   'bucket. Expected value: json-string/@json-file.')

    with self.argument_context('groupsplanner update-detail') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('shared_with', type=validate_file_or_dict,
                   help='Any object Expected value: json-string/@json-file.')
        c.argument('category_descriptions', action=AddDetailsCategoryDescriptions, nargs='*', help=''
                   'plannerCategoryDescriptions')
        c.argument('context_details', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner update-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('body', type=validate_file_or_dict, help='New navigation property values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner create-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('body', type=validate_file_or_dict, help='New navigation property Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner get-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner list-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner update-task') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('body', type=validate_file_or_dict, help='New navigation property values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner get-assigned-to-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-bucket-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-detail') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-progress-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner update-assigned-to-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('unassigned_order_hint', type=str, help='Hint value used to order the task on the AssignedTo view '
                   'of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee '
                   'dictionary does not provide an order hint for the user the task is assigned to. The format is '
                   'defined as outlined here.')
        c.argument('order_hints_by_assignee', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner update-bucket-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('order_hint', type=str, help='Hint used to order tasks in the Bucket view of the Task Board. The '
                   'format is defined as outlined here.')

    with self.argument_context('groupsplanner update-detail') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('description', type=str, help='Description of the task')
        c.argument('preview_type', arg_type=get_enum_type(['automatic', 'noPreview', 'checklist', 'description', ''
                                                           'reference']), help='')
        c.argument('references', type=validate_file_or_dict,
                   help='Any object Expected value: json-string/@json-file.')
        c.argument('checklist', type=validate_file_or_dict, help='Any object Expected value: json-string/@json-file.')

    with self.argument_context('groupsplanner update-progress-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_bucket_id', type=str, help='key: plannerBucket-id of plannerBucket')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('order_hint', type=str, help='Hint value used to order the task on the Progress view of the Task '
                   'Board. The format is defined as outlined here.')

    with self.argument_context('groupsplanner get-assigned-to-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-bucket-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-detail') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner get-progress-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('groupsplanner update-assigned-to-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('unassigned_order_hint', type=str, help='Hint value used to order the task on the AssignedTo view '
                   'of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee '
                   'dictionary does not provide an order hint for the user the task is assigned to. The format is '
                   'defined as outlined here.')
        c.argument('order_hints_by_assignee', type=validate_file_or_dict, help='Any object Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('groupsplanner update-bucket-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('order_hint', type=str, help='Hint used to order tasks in the Bucket view of the Task Board. The '
                   'format is defined as outlined here.')

    with self.argument_context('groupsplanner update-detail') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('description', type=str, help='Description of the task')
        c.argument('preview_type', arg_type=get_enum_type(['automatic', 'noPreview', 'checklist', 'description', ''
                                                           'reference']), help='')
        c.argument('references', type=validate_file_or_dict,
                   help='Any object Expected value: json-string/@json-file.')
        c.argument('checklist', type=validate_file_or_dict, help='Any object Expected value: json-string/@json-file.')

    with self.argument_context('groupsplanner update-progress-task-board-format') as c:
        c.argument('group_id', type=str, help='key: group-id of group')
        c.argument('planner_plan_id', type=str, help='key: plannerPlan-id of plannerPlan')
        c.argument('planner_task_id', type=str, help='key: plannerTask-id of plannerTask')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('order_hint', type=str, help='Hint value used to order the task on the Progress view of the Task '
                   'Board. The format is defined as outlined here.')
