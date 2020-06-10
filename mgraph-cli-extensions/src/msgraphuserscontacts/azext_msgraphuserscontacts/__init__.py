# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
from collections import OrderedDict

from knack import CLICommandsLoader

from msgraph.cli.core import GraphCommandsLoader
from azext_msgraphuserscontacts.generated._help import helps  # pylint: disable=unused-import
from knack.commands import CommandGroup


class UsersContactsCommandsLoader(GraphCommandsLoader):
    def load_command_table(self, args):
        from azext_msgraphuserscontacts.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_msgraphuserscontacts.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError:
            pass
        return self.command_table

    def load_arguments(self, command):
        from azext_msgraphuserscontacts.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_msgraphuserscontacts.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError:
            pass


COMMAND_LOADER_CLS = UsersContactsCommandsLoader
