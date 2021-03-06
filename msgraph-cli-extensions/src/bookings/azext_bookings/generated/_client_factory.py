# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_bookings_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.bookings import Bookings
    return get_mgmt_service_client(cli_ctx,
                                   Bookings,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_booking_business_booking_business(cli_ctx, *_):
    return cf_bookings_cl(cli_ctx).booking_business_booking_business


def cf_booking_business(cli_ctx, *_):
    return cf_bookings_cl(cli_ctx).booking_business


def cf_booking_business_appointment(cli_ctx, *_):
    return cf_bookings_cl(cli_ctx).booking_business_appointment


def cf_booking_business_calendar_view(cli_ctx, *_):
    return cf_bookings_cl(cli_ctx).booking_business_calendar_view


def cf_booking_currency_booking_currency(cli_ctx, *_):
    return cf_bookings_cl(cli_ctx).booking_currency_booking_currency
