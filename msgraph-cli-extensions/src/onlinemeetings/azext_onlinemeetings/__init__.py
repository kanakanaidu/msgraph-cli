# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msgraph.cli.core import AzCommandsLoader
from azext_onlinemeetings.generated._help import helps  # pylint: disable=unused-import
try:
    from azext_onlinemeetings.manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass


class OnlineMeetingsCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from msgraph.cli.core.commands import CliCommandType
        from azext_onlinemeetings.generated._client_factory import cf_onlinemeetings_cl
        onlinemeetings_custom = CliCommandType(
            operations_tmpl='azext_onlinemeetings.custom#{}',
            client_factory=cf_onlinemeetings_cl)
        parent = super(OnlineMeetingsCommandsLoader, self)
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=onlinemeetings_custom)

    def load_command_table(self, args):
        from azext_onlinemeetings.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_onlinemeetings.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError:
            pass
        return self.command_table

    def load_arguments(self, command):
        from azext_onlinemeetings.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_onlinemeetings.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError:
            pass


COMMAND_LOADER_CLS = OnlineMeetingsCommandsLoader
