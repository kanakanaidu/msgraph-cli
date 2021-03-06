# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_notification.generated._client_factory import cf_user
    notification_user = CliCommandType(
        operations_tmpl='azext_notification.vendored_sdks.notification.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('notification', notification_user, client_factory=cf_user) as g:
        g.custom_command('create-notification', 'notification_create_notification')
        g.custom_command('get-notification', 'notification_get_notification')
        g.custom_command('list-notification', 'notification_list_notification')
        g.custom_command('update-notification', 'notification_update_notification')
