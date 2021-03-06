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

from knack.help_files import helps


helps['groupsplanner'] = """
    type: group
    short-summary: groupsplanner
"""

helps['groupsplanner get-planner'] = """
    type: command
    short-summary: "Get planner from groups"
"""

helps['groupsplanner update-planner'] = """
    type: command
    short-summary: "Update the navigation property planner in groups"
"""

helps['groupsplanner'] = """
    type: group
    short-summary: groupsplanner
"""

helps['groupsplanner create-plan'] = """
    type: command
    short-summary: "Create new navigation property to plans for groups"
    parameters:
      - name: --details-category-descriptions
        short-summary: "plannerCategoryDescriptions"
        long-summary: |
            Usage: --details-category-descriptions category1=XX category2=XX category3=XX category4=XX category5=XX \
category6=XX

            category1: The label associated with Category 1
            category2: The label associated with Category 2
            category3: The label associated with Category 3
            category4: The label associated with Category 4
            category5: The label associated with Category 5
            category6: The label associated with Category 6
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application id=XX display-name=XX

            id: Unique identifier for the identity.
            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device id=XX display-name=XX

            id: Unique identifier for the identity.
            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user id=XX display-name=XX

            id: Unique identifier for the identity.
            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
"""

helps['groupsplanner get-plan'] = """
    type: command
    short-summary: "Get plans from groups"
"""

helps['groupsplanner list-plan'] = """
    type: command
    short-summary: "Get plans from groups"
"""

helps['groupsplanner update-plan'] = """
    type: command
    short-summary: "Update the navigation property plans in groups"
    parameters:
      - name: --details-category-descriptions
        short-summary: "plannerCategoryDescriptions"
        long-summary: |
            Usage: --details-category-descriptions category1=XX category2=XX category3=XX category4=XX category5=XX \
category6=XX

            category1: The label associated with Category 1
            category2: The label associated with Category 2
            category3: The label associated with Category 3
            category4: The label associated with Category 4
            category5: The label associated with Category 5
            category6: The label associated with Category 6
      - name: --created-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-application id=XX display-name=XX

            id: Unique identifier for the identity.
            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
      - name: --created-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-device id=XX display-name=XX

            id: Unique identifier for the identity.
            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
      - name: --created-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --created-by-user id=XX display-name=XX

            id: Unique identifier for the identity.
            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
"""

helps['groupsplanner'] = """
    type: group
    short-summary: groupsplanner
"""

helps['groupsplanner create-bucket'] = """
    type: command
    short-summary: "Create new navigation property to buckets for groups"
"""

helps['groupsplanner create-task'] = """
    type: command
    short-summary: "Create new navigation property to tasks for groups"
"""

helps['groupsplanner get-bucket'] = """
    type: command
    short-summary: "Get buckets from groups"
"""

helps['groupsplanner get-detail'] = """
    type: command
    short-summary: "Get details from groups"
"""

helps['groupsplanner get-task'] = """
    type: command
    short-summary: "Get tasks from groups"
"""

helps['groupsplanner list-bucket'] = """
    type: command
    short-summary: "Get buckets from groups"
"""

helps['groupsplanner list-task'] = """
    type: command
    short-summary: "Get tasks from groups"
"""

helps['groupsplanner update-bucket'] = """
    type: command
    short-summary: "Update the navigation property buckets in groups"
"""

helps['groupsplanner update-detail'] = """
    type: command
    short-summary: "Update the navigation property details in groups"
    parameters:
      - name: --category-descriptions
        short-summary: "plannerCategoryDescriptions"
        long-summary: |
            Usage: --category-descriptions category1=XX category2=XX category3=XX category4=XX category5=XX \
category6=XX

            category1: The label associated with Category 1
            category2: The label associated with Category 2
            category3: The label associated with Category 3
            category4: The label associated with Category 4
            category5: The label associated with Category 5
            category6: The label associated with Category 6
"""

helps['groupsplanner update-task'] = """
    type: command
    short-summary: "Update the navigation property tasks in groups"
"""

helps['groupsplanner'] = """
    type: group
    short-summary: groupsplanner
"""

helps['groupsplanner create-task'] = """
    type: command
    short-summary: "Create new navigation property to tasks for groups"
"""

helps['groupsplanner get-task'] = """
    type: command
    short-summary: "Get tasks from groups"
"""

helps['groupsplanner list-task'] = """
    type: command
    short-summary: "Get tasks from groups"
"""

helps['groupsplanner update-task'] = """
    type: command
    short-summary: "Update the navigation property tasks in groups"
"""

helps['groupsplanner'] = """
    type: group
    short-summary: groupsplanner
"""

helps['groupsplanner get-assigned-to-task-board-format'] = """
    type: command
    short-summary: "Get assignedToTaskBoardFormat from groups"
"""

helps['groupsplanner get-bucket-task-board-format'] = """
    type: command
    short-summary: "Get bucketTaskBoardFormat from groups"
"""

helps['groupsplanner get-detail'] = """
    type: command
    short-summary: "Get details from groups"
"""

helps['groupsplanner get-progress-task-board-format'] = """
    type: command
    short-summary: "Get progressTaskBoardFormat from groups"
"""

helps['groupsplanner update-assigned-to-task-board-format'] = """
    type: command
    short-summary: "Update the navigation property assignedToTaskBoardFormat in groups"
"""

helps['groupsplanner update-bucket-task-board-format'] = """
    type: command
    short-summary: "Update the navigation property bucketTaskBoardFormat in groups"
"""

helps['groupsplanner update-detail'] = """
    type: command
    short-summary: "Update the navigation property details in groups"
"""

helps['groupsplanner update-progress-task-board-format'] = """
    type: command
    short-summary: "Update the navigation property progressTaskBoardFormat in groups"
"""

helps['groupsplanner'] = """
    type: group
    short-summary: groupsplanner
"""

helps['groupsplanner get-assigned-to-task-board-format'] = """
    type: command
    short-summary: "Get assignedToTaskBoardFormat from groups"
"""

helps['groupsplanner get-bucket-task-board-format'] = """
    type: command
    short-summary: "Get bucketTaskBoardFormat from groups"
"""

helps['groupsplanner get-detail'] = """
    type: command
    short-summary: "Get details from groups"
"""

helps['groupsplanner get-progress-task-board-format'] = """
    type: command
    short-summary: "Get progressTaskBoardFormat from groups"
"""

helps['groupsplanner update-assigned-to-task-board-format'] = """
    type: command
    short-summary: "Update the navigation property assignedToTaskBoardFormat in groups"
"""

helps['groupsplanner update-bucket-task-board-format'] = """
    type: command
    short-summary: "Update the navigation property bucketTaskBoardFormat in groups"
"""

helps['groupsplanner update-detail'] = """
    type: command
    short-summary: "Update the navigation property details in groups"
"""

helps['groupsplanner update-progress-task-board-format'] = """
    type: command
    short-summary: "Update the navigation property progressTaskBoardFormat in groups"
"""
