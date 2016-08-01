#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from settings import *
import requests
import re
from bs4 import BeautifulSoup

def get_info_from_csv(input_file):
    holdings_p = re.compile(r'^\d{16,16}$')
    header_p = re.compile(r'^[a-z_,]+$')
    items_p = re.compile(r'^[0-9,/]+$')
    item_info = {}
    with open(input_file, 'r', encoding='utf-8') as fh:
        lines = fh.readlines()

    """
    The loop below creates a data structure that looks like this:
        {holdings_id_number: 
            [ {id: number,
               enumeration_a: number,
               enumeration_b: number,
               chronology_i: number,
               ...
              },
              {id: number,
              ...
              }
            ],
         another_holdings_id_number:
             [ ... ],
        ...
        }
    Usually, this will create a dictionary with one holdings id
    and a list of item dictionaries, but some bibliographic records
    may have more than one holdings.
    """
    for line in lines:
        line = line.strip()
        if holdings_p.match(line):
            holdings_id = line
            item_info[holdings_id] = []
        elif header_p.match(line):
            keys = line.split(',')
        elif items_p.match(line):
            info = line.split(',')
            item_info[holdings_id].append(dict(zip(keys, info)))
            
    #print(item_info)
           
    return item_info

def get_item_xml(base_url, mms_id, holdings_id, item_id, api_key):
    query = 'bibs/{}/holdings/{}/items/{}?apikey={}'
    r = requests.get(''.join([base_url, query.format(mms_id, holdings_id, item_id, api_key)]))
    #print(r.status_code)
    item_xml = r.text
    
    print(item_xml)
    return item_xml

def update_item_xml(item_xml, item_info):
    soup = BeautifulSoup(item_xml, 'xml')
    for i in item_info:
        if soup.find(i):
            soup.find(i).string = item_info[i]
        else:
            # We don't need to update the item's ID, but we do want to update
            # all the other fields.
            if i != 'id':
                new_tag = soup.new_tag(i)
                new_tag.string = item_info[i]
                soup.find('item_data').find('description').insert_before(new_tag)
    
    new_xml = str(soup)
    #print(new_xml)
    
    return new_xml

def update_item(base_url, mms_id, holdings_id, item_id, api_key, item_xml):
    headers = {'content-type':'application/xml'}
    query = 'bibs/{}/holdings/{}/items/{}?apikey={}'
    
    url = ''.join([base_url, query.format(mms_id, holdings_id, item_id, api_key)])
    #print(url)
    #print(item_xml)
    r = requests.put(url, headers=headers, data=item_xml)
    print(r.status_code)
    print(r.text)


items_xml = []
    
items_to_update = get_info_from_csv(input_file)
#print(items_to_update)
#print(items_to_update['2220576350002843'][0]['id'])

for holdings in items_to_update:
    #print(holdings)
    for item in items_to_update[holdings]:
        #print(item['id'])
        xml = get_item_xml(base_url, mms_id, holdings, item['id'], api_key)
        updated_xml = update_item_xml(xml, item)
        update_item(base_url, mms_id, holdings, item['id'], api_key, updated_xml)
        

