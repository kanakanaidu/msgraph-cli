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


helps['usersdevices'] = """
    type: group
    short-summary: usersdevices
"""

helps['usersdevices create-device'] = """
    type: command
    short-summary: "Create new navigation property to devices for users"
    parameters:
      - name: --alternative-security-ids
        short-summary: "For internal use only. Not nullable."
        long-summary: |
            Usage: --alternative-security-ids type=XX identity-provider=XX key=XX

            type: For internal use only
            identity-provider: For internal use only
            key: For internal use only

            Multiple actions can be specified by using more than one --alternative-security-ids argument.
      - name: --member-of
        short-summary: "Groups that this group is a member of. HTTP Methods: GET (supported for all groups). \
Read-only. Nullable."
        long-summary: |
            Usage: --member-of deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --member-of argument.
      - name: --registered-owners
        short-summary: "The user that cloud joined the device or registered their personal device. The registered \
owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable."
        long-summary: |
            Usage: --registered-owners deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --registered-owners argument.
      - name: --registered-users
        short-summary: "Collection of registered users of the device. For cloud joined devices and registered personal \
devices, registered users are set to the same value as registered owners at the time of registration. Read-only. \
Nullable."
        long-summary: |
            Usage: --registered-users deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --registered-users argument.
      - name: --transitive-member-of
        long-summary: |
            Usage: --transitive-member-of deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --transitive-member-of argument.
      - name: --extensions
        short-summary: "The collection of open extensions defined for the device. Read-only. Nullable."
        long-summary: |
            Usage: --extensions id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --extensions argument.
"""

helps['usersdevices get-device'] = """
    type: command
    short-summary: "Get devices from users"
"""

helps['usersdevices list-device'] = """
    type: command
    short-summary: "Get devices from users"
"""

helps['usersdevices update-device'] = """
    type: command
    short-summary: "Update the navigation property devices in users"
    parameters:
      - name: --alternative-security-ids
        short-summary: "For internal use only. Not nullable."
        long-summary: |
            Usage: --alternative-security-ids type=XX identity-provider=XX key=XX

            type: For internal use only
            identity-provider: For internal use only
            key: For internal use only

            Multiple actions can be specified by using more than one --alternative-security-ids argument.
      - name: --member-of
        short-summary: "Groups that this group is a member of. HTTP Methods: GET (supported for all groups). \
Read-only. Nullable."
        long-summary: |
            Usage: --member-of deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --member-of argument.
      - name: --registered-owners
        short-summary: "The user that cloud joined the device or registered their personal device. The registered \
owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable."
        long-summary: |
            Usage: --registered-owners deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --registered-owners argument.
      - name: --registered-users
        short-summary: "Collection of registered users of the device. For cloud joined devices and registered personal \
devices, registered users are set to the same value as registered owners at the time of registration. Read-only. \
Nullable."
        long-summary: |
            Usage: --registered-users deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --registered-users argument.
      - name: --transitive-member-of
        long-summary: |
            Usage: --transitive-member-of deleted-date-time=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --transitive-member-of argument.
      - name: --extensions
        short-summary: "The collection of open extensions defined for the device. Read-only. Nullable."
        long-summary: |
            Usage: --extensions id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --extensions argument.
"""
