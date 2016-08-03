# -*- coding: utf-8 -*-

from settings import api_key, mms_id, input_file, base_url
from AE import get_info_from_csv, get_item_xml, update_item_xml, update_item

items_xml = []
    
items_to_update = get_info_from_csv(input_file)

for holdings in items_to_update:
    for item in items_to_update[holdings]:
        xml = get_item_xml(base_url, mms_id, holdings, item['id'], api_key)
        updated_xml = update_item_xml(xml, item)
        update_item(base_url, mms_id, holdings, item['id'], api_key, updated_xml)
        

