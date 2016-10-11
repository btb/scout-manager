from spotseeker_restclient.dao import SPOTSEEKER_DAO
from spotseeker_restclient.spotseeker import Spotseeker
from spotseeker_restclient.exceptions import DataFailureException
from spotseeker_restclient.models.spot import SpotItem
from scout_manager.dao.space import process_extended_info, get_spot_by_id
import json


def delete_item(item_id, etag):
    spot_client = Spotseeker()
    spot = get_item_by_id(int(item_id))
    spot.items.remove(spot.item)
    json_data = spot.json_data_structure()
    spot_client.put_spot(spot.spot_id, json.dumps(json_data), etag)


def get_item_by_id(item_id):
    from scout.dao.item import add_item_info

    spot_client = Spotseeker()
    spot = None
    try:
        spots = spot_client.search_spots([
            ('item:id', item_id),
            ('extended_info:app_type', 'tech'),
        ])
        if spots:
            spot = process_extended_info(spots[0])
            spot = add_item_info(spot)
            spot = _filter_spot_items(item_id, spot)
    except DataFailureException:
        pass
        # TODO: consider logging on failure

    return spot


def _filter_spot_items(item_id, spot):
    for item in spot.items:
        if item.item_id == item_id:
            spot.item = item
    return spot


def create_item(form_data):
    json_data = _build_item_json(form_data)
    spot_client = Spotseeker()
    spot = _get_spot_json(json_data['spot_id'])
    json_data.pop('id')
    json_data.pop('spot_id')
    spot['items'].append(json_data)
    spot_client.put_spot(spot['id'], json.dumps(spot), spot['etag'])

    # spot = get_item_by_id(json_data["spot_id"])
    # etag = spot.etag
    # spot.items.append(json_data)
    # json_data = spot.json_data_structure()
    # spot_client.put_spot(spot.spot_id, json.dumps(json_data), etag)
    #
    # resp = spot_client.post_spot(json.dumps(json_data))
    # item_id = _get_item_id_from_url(resp['location'])
    #
    # if 'file' in form_data \
    #         and form_data['file'] is not None \
    #         and form_data['file'] != "undefined":
    #     spot_client.post_item_image(item_id, form_data['file'])


def _get_spot_json(spot_id):
    url = "/api/v1/spot/%s" % spot_id
    dao = SPOTSEEKER_DAO()
    resp, content = dao.getURL(url, {})

    if resp.status != 200:
        raise DataFailureException(url, resp.status, content)
    return json.loads(content)


def update_item(form_data, item_id, image=None):
    json_data = _build_item_json(form_data)
    spot_client = Spotseeker()
    # this is really hacky, but the etag seems to keep getting reset
    # between a GET and PUT
    spot = get_item_by_id(item_id)
    etag = spot.etag
#    spot_client.put_spot(spot.spot_id, json.dumps(json_data), etag)

    if 'removed_images' in json_data:
        for image in json_data['removed_images']:
            spot_client.delete_item_image(item_id, image['id'], image['etag'])

    if form_data['file'] is not None and form_data['file'] != "undefined":
        spot_client.post_item_image(item_id, form_data['file'])


def _build_item_json(form_data):
    json_data = json.loads(form_data['json'])

    extended_info = {}

    for key in list(json_data):
        if key.startswith('extended_info'):
            value = json_data[key]
            name = key.split(':', 1)[1]
            json_data.pop(key)
            if value != "None" and len(value) > 0:
                extended_info[name] = value

    json_data["extended_info"] = extended_info
    return json_data


"""
Core data
"""
# item.name
# item.category
# item.subcategory

"""
Core data... space location id
"""
# location/related space ?

"""
Images
"""
# photo/image model?

"""
Extended info... item information
"""
# i_context_type
# i_is_active
# i_is_stf

# i_description
# i_quantity
# i_model
# i_brand
# i_website

"""
Extended info... alerts, prereqs, and reservations
"""

# i_has_prereqs ("true")
# i_prereq_notes

# i_reservation_required ("true")
# i_reservation_notes

"""
Extended info... access restrictions
"""
# i_has_access_restriction ("true")
# i_access_notes

# i_access_limit_uwnetid ("true")
# i_access_limit_role ("true")
# i_access_limit_school ("true")
# i_access_limit_department ("true")

# i_access_role_students ("true")
# i_access_role_staff ("true")
# i_access_role_faculty ("true")

"""
Extended info... admin information
"""
# i_owner (group)
