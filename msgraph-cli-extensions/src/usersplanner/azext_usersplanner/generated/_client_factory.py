# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_usersplanner_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.usersplanner import UsersPlanner
    return get_mgmt_service_client(cli_ctx,
                                   UsersPlanner,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user


def cf_user_planner(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user_planner


def cf_user_planner_plan(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user_planner_plan


def cf_user_planner_plan_bucket(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user_planner_plan_bucket


def cf_user_planner_plan_bucket_task(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user_planner_plan_bucket_task


def cf_user_planner_plan_task(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user_planner_plan_task


def cf_user_planner_task(cli_ctx, *_):
    return cf_usersplanner_cl(cli_ctx).user_planner_task
