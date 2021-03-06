# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_teamsteamwork_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.teamsteamwork import TeamsTeamwork
    return get_mgmt_service_client(cli_ctx,
                                   TeamsTeamwork,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user(cli_ctx, *_):
    return cf_teamsteamwork_cl(cli_ctx).user


def cf_user_teamwork(cli_ctx, *_):
    return cf_teamsteamwork_cl(cli_ctx).user_teamwork


def cf_user_teamwork_installed_app(cli_ctx, *_):
    return cf_teamsteamwork_cl(cli_ctx).user_teamwork_installed_app
