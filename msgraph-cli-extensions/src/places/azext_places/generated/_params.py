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

from azext_places.action import (
    AddGeoCoordinates,
    AddAddress
)


def load_arguments(self, _):

    with self.argument_context('places delete') as c:
        c.argument('place_id', type=str, help='key: place-id of place')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('places create-place') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('display_name', type=str, help='')
        c.argument('geo_coordinates', action=AddGeoCoordinates, nargs='*', help='outlookGeoCoordinates')
        c.argument('phone', type=str, help='')
        c.argument('address', action=AddAddress, nargs='*', help='physicalAddress')

    with self.argument_context('places get-place') as c:
        c.argument('place_id', type=str, help='key: place-id of place')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('places list-place') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('places update-place') as c:
        c.argument('place_id', type=str, help='key: place-id of place')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('display_name', type=str, help='')
        c.argument('geo_coordinates', action=AddGeoCoordinates, nargs='*', help='outlookGeoCoordinates')
        c.argument('phone', type=str, help='')
        c.argument('address', action=AddAddress, nargs='*', help='physicalAddress')
