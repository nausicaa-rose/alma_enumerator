# -*- coding: utf-8 -*-

from settings import api_key
import requests
import re
from bs4 import BeautifulSoup

  ############################################           
 # Functions for getting record information #
############################################

def get_holdings(base_url, mms_id, api_key):
    """
    Get the holdings id(s) for the bib record via the Alma API.
    """
    holdings_list = []
    query = 'bibs/{}/holdings?apikey={}'
    r = requests.get(''.join([base_url, query.format(mms_id, api_key)]))
    soup = BeautifulSoup(r.text, 'lxml')
    holdings = soup.find_all('holding_id')
    for id in holdings:
        holdings_list.append(id.text)
        
    return holdings_list


def get_item_info(base_url, mms_id, holdings):
    """
    Get the enumeration, chronology, and item id for each item for each holdings
    record.
    """
    limit = 100
    offset = 0
    query = 'bibs/{}/holdings/{}/items?limit={}&offset={}&apikey={}'
    item_ids = []
    descriptions = []
    item_info = []

    for holdings_id in holdings:
        r = requests.get(''.join([base_url, query.format(mms_id, holdings_id, limit, offset, api_key)]))
        soup = BeautifulSoup(r.text, 'lxml')
        
        current_response = soup.find_all('item_data')
        items = current_response
        
        # Iterate through the entire list of items
        while True:
            if len(current_response) == limit:
                offset += limit
                r = requests.get(''.join([base_url, query.format(mms_id, holdings_id, limit, offset, api_key)]))
                soup = BeautifulSoup(r.text, 'lxml')
                current_response = soup.find_all('item_data')
                items += current_response
            else:
                break
                

        for item in items:
            item_ids.append(item.find('pid').text)
            descriptions.append(item.find('description').text)
        
        # Call get_info_from_description() function to parse the description
        # and return a dictionary with
        for d in descriptions:
            item_info.append(get_info_from_description(d)) 
        
        # Add the item ID to each item
        for i in range(len(item_ids)):
            item_info[i]['id'] = item_ids[i]
                   
    return item_info


def get_info_from_description(item):
    """
    This is where most of the magic happens. If something goes wrong,
    it probably went wrong here.
    
    This function parses item descriptions and is called by get_item_info(). 
    For those descriptions it can parse, it returns a dictionary with each field
    converted to a format compatible with Alma's enumeration and chronology fields.
    """
    item_info = {}
    info = item.split(' ')
    
    # This dictonary of patterns is used convert month and season words to numerals.
    # It's also used to identify descriptions with words that are not
    # month or season indicators.
    date_patterns = {
                     re.compile(r'(Jan\.?|January)', re.IGNORECASE):     '01',
                     re.compile(r'(Feb\.?|February)', re.IGNORECASE):    '02',
                     re.compile(r'(Mar\.?|March)', re.IGNORECASE):       '03',
                     re.compile(r'(Apr\.?|April)', re.IGNORECASE):       '04',
                     re.compile(r'May', re.IGNORECASE):                  '05',
                     re.compile(r'(Jun\.?|June)', re.IGNORECASE):        '06',
                     re.compile(r'(Jul\.?|July)', re.IGNORECASE):        '07',
                     re.compile(r'(Aug\.?|August)', re.IGNORECASE):      '08',
                     re.compile(r'(Sep\.?|Sept\.?|September)', re.IGNORECASE):   '09',
                     re.compile(r'(Oct\.?|October)', re.IGNORECASE):     '10',
                     re.compile(r'(Nov\.?|November)', re.IGNORECASE):    '11',
                     re.compile(r'(Dec\.?|December)', re.IGNORECASE):    '12',
                     re.compile(r'(Spr\.?|Spring)', re.IGNORECASE):      '21',
                     re.compile(r'(Sum\.?|Summer)', re.IGNORECASE):      '22',
                     re.compile(r'(Fal\.?|Fall|Autumn)', re.IGNORECASE): '23',
                     re.compile(r'(Win\.?|Winter)', re.IGNORECASE):      '24',
                     }                
    
    # This pattern is used to see if a field in info has numerals
    has_digitsp = re.compile(r'.*\d+')
    
    # This pattern is used to remove periods, parentheses, and commas that can
    # mess things up if they're left in.
    bad_charsp = re.compile(r'[\.\(\),\\:]')

    # This pattern matches hyphens and slashes and is used to recognize and edit
    # date and issue ranges like 1995-1999, 12/13, or 5&6.
    rp = re.compile(r'[-/&]')
    
    # This pattern matches a field that is a single hyphen, slash, or ampersand.
    r_exp = re.compile(r'^[-/&]$')
    
    # This pattern is used to catch strings like 2011-Win or 2011/Win.
    year_mop = re.compile(r'(\d+)(-|/)([a-zA-Z]+)')
    
    # This pattern is used to distinguish between years and volume/issue numbers,
    # but it may trip over long continuously numbered issues. The pattern also
    # assumes it won't be handling records from before the 19th century.
    is_yearp = re.compile(r'(18|19|20)\d\d')
    
    # Used to filter out Alma-generated descriptions. Since they already
    # have enumeration/chronology and have a funky format, we can ignore 
    # them for now.
    alma_generatedp = re.compile(r'.*:.*\(.*:.*\)')
    
    
    if alma_generatedp.match(item):
        item_info = handle_record_error(item, item_info)
    
    to_remove = []
    # Check each field in info
    for i in info:      
        # Scrub '.(),:' from text for better matching
        info[info.index(i)] = bad_charsp.sub('', i)
        i = bad_charsp.sub('', i)
               
        # Find fields that include only alphabetic characters
        if has_digitsp.match(i) == None and r_exp.match(i) == None:
            is_ok = False
            for key in date_patterns:
                # If the field is in date_patterns, it's an indicator of month
                # or season. Everything's good and we move on to the next field.
                if key.match(i):
                    is_ok = True
                    break
            
            # If the field didn't match any of the date_patterns, it is probably
            # a descriptive word like 'Abstracts', 'INDEX', etc, or a 
            # volume/number indicator like 'v.', 'no.', etc. If that's the 
            # case, add it to the removal list.
            if is_ok == False:
                to_remove.append(i)
    
    # Remove fields from info that we don't want.
    for i in to_remove:
        info.remove(i)
    
    # Sometimes, we might encounter a description like 'v 46 July 2005-June 2006',
    # where there is no space surrounding the hyphen (or slash), which produces
    # a field that looks like this '2005-June', which will not process correctly.
    # To deal with this we split the field to look like ('2005', '-', 'June'),
    # drop the original field, and put the three new fields in its place.
    for i in info:
        if year_mop.match(i) != None:
            index = info.index(i)
            head = info[0:index]
            tail = info[(index + 1):]
            body = list(year_mop.match(i).groups())
            info = head + body + tail
    
            
    # Now that we're done fiddling with fields, get the length of info
    i_len = len(info)
    
    # If the record has less than two or more than 7 fields, mark it as an 
    # error and return.
    if i_len < 1 or i_len > 7:
        item_info = handle_record_error(item, item_info)
    # If the record has already been identified as an error, do nothing and let
    # item_info be returned as it is.
    elif 'error' in item_info:
        pass
    else:       
        # Set the defaults for all the fields, so that in case there's nothing
        # to put in them, our CSV columns don't get messed up.
        item_info['enumeration_a'] = ''
        item_info['enumeration_b'] = ''
        item_info['chronology_i'] = ''
        item_info['chronology_j'] = ''
        item_info['chronology_k'] = ''
        
        # ['v.65', 'no.3', 'May', '2012', '-', 'Jun', '2012']
        if i_len == 7:
            item_info['enumeration_a'] = snarf_numerals(info[0])
            if has_digitsp.match(info[2]) == None and has_digitsp.match(info[5]) == None and rp.match(info[4]) != None:
                item_info['enumeration_b'] = snarf_numerals(info[1])
                
                if info[3] == info[6]:
                    item_info['chronology_i'] = snarf_numerals(info[6])
                else:
                    item_info['chronology_i'] = '/'.join([snarf_numerals(info[3]), snarf_numerals(info[6])])
                
                item_info['chronology_j'] = '/'.join([info[2], info[5]])
            else:
                item_info = handle_record_error(item, item_info)
       # ['no.42', 'Win', '2009', '-', 'Win', '2010']
        elif i_len == 6:
            item_info['enumeration_a'] = snarf_numerals(info[0])
            if has_digitsp.match(info[1]) == None and has_digitsp.match(info[4]) == None and rp.match(info[3]) != None:              
                if info[2] == info[5]:
                    item_info['chronology_i'] = snarf_numerals(info[5])
                else:
                    item_info['chronology_i'] = '/'.join([snarf_numerals(info[2]), snarf_numerals(info[5])])
                
                item_info['chronology_j'] = '/'.join([info[1], info[4]])
            else:
                item_info = handle_record_error(item, item_info)
        # If item has five fields, it will be treated as if it records volume, issue, day, month, year
        # ['v.43 'no.2', '4', 'Mar', '2009'] or ['v.43 'no.2', 'Mar', '4', '2009']
        elif i_len == 5:
            item_info['enumeration_a'] = snarf_numerals(info[0])
            item_info['enumeration_b'] = snarf_numerals(info[1])
            # This matches the date pattern Day Month Year, i.e. 
            # ['v.43 'no.2', '4', 'Mar', '2009']
            if has_digitsp.match(info[2]) != None and rp.match(info[3]) == None:
                item_info['chronology_k'] = snarf_numerals(info[2])
                item_info['chronology_j'] = info[3]
                item_info['chronology_i'] = snarf_numerals(info[4])
            # This matches the date pattern Month Day Year, i.e. 
            # ['v.43 'no.2', 'Mar', '4', '2009']
            elif has_digitsp.match(info[1]) != None:
                item_info['chronology_j'] = info[2]
                item_info['chronology_k'] = snarf_numerals(info[3])
                item_info['chronology_i'] = snarf_numerals(info[4])
            # This matches the date pattern Season Year - Year
            # i.e. ['no52', 'Win', '2013', '-', '2014']
            elif has_digitsp.match(info[1]) == None and rp.match(info[3]) != None:
                item_info['chronology_j'] = info[1]
                item_info['chronology_i'] = snarf_numerals('/'.join([info[2], info[4]]))
            else:
                handle_record_error(item, item_info)
                         
        # If the item does not record days, then treat it like it records 
        # issue, month, day, year or volume, issue, month, year
        elif i_len == 4:
            item_info['enumeration_a'] = snarf_numerals(info[0])
            # If info[1] is a string of alphabetic characters, then: issue, month, day, year
            if has_digitsp.match(info[1]) == None:
                item_info['chronology_j'] = info[1]
                item_info['chronology_k'] = snarf_numerals(info[2])
                item_info['chronology_i'] = snarf_numerals(info[3])
            # volume, issue, month, year
            else:
                item_info['enumeration_b'] = snarf_numerals(info[1])
                item_info['chronology_j'] = info[2]
                item_info['chronology_i'] = snarf_numerals(info[3])
        # If the item has three fields, treat it like it records volume, issue, 
        # year or volume, month, year
        elif i_len == 3:
            item_info['enumeration_a'] = snarf_numerals(info[0])
            # Match volume, issue, year
            if has_digitsp.match(info[1]):
                item_info['enumeration_b'] = snarf_numerals(info[1])
            # Fall back to volume, month, year
            else:
                item_info['chronology_j'] = info[1]
            item_info['chronology_i'] = snarf_numerals(info[2])
        # If this is a 2 field description (i.e. a bound volume or annual publication)
        # the second field should be the year(s), so set it to chronology_i.
        elif i_len == 2:
            # If both fields are numbers, then the pattern is either volume, year
            # or year, volume
            if has_digitsp.match(info[0]) != None and has_digitsp.match(info[1]) != None:
                if is_yearp.match(info[0]) != None:
                    item_info['enumeration_a'] = snarf_numerals(info[1])
                    item_info['chronology_i'] = snarf_numerals(info[0])
                else:
                    item_info['enumeration_a'] = snarf_numerals(info[0])
                    item_info['chronology_i'] = snarf_numerals(info[1])
            # If the first field has digits and the second doesn't, the pattern 
            # is probably year, months or volume months
            elif has_digitsp.match(info[0]) != None and has_digitsp.match(info[1]) == None:
                if is_yearp.match(info[0]):
                    item_info['chronology_i'] = snarf_numerals(info[0])
                else:
                    item_info['enumeration_a'] = snarf_numerals(info[0])
                    
                item_info['chronology_j'] = info[1]
            # If the first field doesn't have digits and the second does, the 
            # the pattern is probably months, year or maybe months volume
            elif has_digitsp.match(info[0]) == None and has_digitsp.match(info[1]) != None:
                # If it looks like a year, assign it to chronology_i
                if is_yearp.match(info[1]):
                    item_info['chronology_i'] = snarf_numerals(info[1])
                # Otherwise, assign it to enumeration_a
                else:
                    item_info['enumeration_a'] = snarf_numerals(info[1])
                    
                item_info['chronology_j'] = info[0]
        # Handle single field descriptions. These should be either volume or year(s).
        elif i_len == 1:
            if has_digitsp.match(info[0]):
                # Check to see if it looks like it's a year.
                if is_yearp.match(info[0]):
                    item_info['chronology_i'] = snarf_numerals(info[0])
                # If it doesn't look like a year, assume it's a volume number.
                else:
                    item_info['enumeration_a'] = snarf_numerals(info[0])
            # If the field isn't a string of numerals, something's probably
            # gone wrong. Mark it as an error.
            else:
                handle_record_error(item, item_info)
        # Make sure we convert the description field's representation of months,
        # Jan, Win, etc. to the appropriate digital representation: 01, 24, etc.
        # Splitting accounts for things formatted like Jan-Feb and Jan/Feb which
        # will be converted to 01/02.
        if item_info['chronology_j'] != '':
            mo_split = rp.split(item_info['chronology_j'])
            for i in range(len(mo_split)):
                for key in date_patterns:
                    if key.match(mo_split[i]):
                        mo_split[i] = date_patterns[key]
                        break
        
            # Recombine multiple dates
            if len(mo_split) > 1:
                item_info['chronology_j'] = '/'.join(mo_split)
            # Otherwise, just set chronology_j to the one date
            else:
                item_info['chronology_j'] = mo_split[0]

    # Make sure none of the values in item_info are a free-floating slash and
    # that no field begins or ends with a slash. If any of these conditions 
    # are true, mark the item as an error.
    for key in item_info:
        if item_info[key] == '/'or len(item_info[key]) > 0 and(item_info[key][0] == '/' or item_info[key][-1] == '/'):
            handle_record_error(item, item_info)
            break
        
    return item_info            

            
def handle_record_error(item, item_info):
    print('{} appears to be irregular. Please correct by hand.'.format(item))
    item_info['error'] = item
    return item_info
    
    
def snarf_numerals(string):
    """
    This function is called by get_info_from_description(). It takes a string
    of arbitrary characters and returns only those characters that are numerals 
    or a slash. Hyphens in input are converted to slashes. All other characters
    are discarded. Input like 'v.40-41' would be returned as '40/41'.
    """
    # This pattern matches hyphens and slashes and is used to recognize and edit
    # date and issue ranges like 1995-1999 or 12/13.
    rp = re.compile(r'[-/&]')
    
    numerals = rp.sub('/', ''.join([x 
                                    for x 
                                    in string
                                    if x.isdigit() or rp.match(x) != None]))
        
    return numerals
        
        
def write_header_to_csv(output_file, item_info, delimeter=','):
    """
    Write out the field headers: id, enumeration_a, etc, to the output file.
    """
    with open(output_file, 'a', encoding='utf-8') as fh:
        fh.write('{}\n'.format(delimeter.join(item_info[0].keys())))
        
    
def output_to_csv(output_file, error_file, item_info, delimeter=','):
    """
    Write each item's info as a row in our output file. Write records with
    errors to our error file.
    """
    item_errors = []
    # Write out the data we were able to extract
    with open(output_file, 'a', encoding='utf-8') as fh:
        for item in item_info:
            # Collect the descriptions we couldn't handle for writing to a 
            # seperate file.
            if 'error' in item:
                item_errors.append(item)
            else:                
                fh.write('{}\n'.format(delimeter.join(item.values())))
                
    # Write out the item id and description for those descriptions that we couldn't handle
    with open(error_file, 'a', encoding='utf-8') as fh:
        for item in item_errors:
            fh.write('{}\n'.format(delimeter.join(item.values())))
            
            
def fetch(mms_id, output_file, error_file, api_key, base_url):    
    # Get holdings id(s)
    holdings = get_holdings(base_url, mms_id, api_key)
    
    # Make sure the output file is empty.
    with open(output_file, 'w', encoding='utf-8') as fh:
        fh.truncate()
    
    # For each holdings ID, write the ID to the output file, get the information
    # for all of the holdings' items, write the field headers to the output file,
    # then write the item information to the output file and write errors to the 
    # error file.
    for h in holdings:
        with open(output_file, 'a', encoding='utf-8') as fh:
            fh.write('{}\n'.format(h))
    
        item_info = get_item_info(base_url, mms_id, holdings)
        write_header_to_csv(output_file, item_info)
        output_to_csv(output_file, error_file, item_info)
            
            
  ##################################           
 # Functions for updating records #
##################################

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
            
    return item_info
    

def get_item_xml(base_url, mms_id, holdings_id, item_id, api_key):
    query = 'bibs/{}/holdings/{}/items/{}?apikey={}'
    r = requests.get(''.join([base_url, query.format(mms_id, holdings_id, item_id, api_key)]))
    item_xml = r.text
    
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
    
    return new_xml
    

def update_item(base_url, mms_id, holdings_id, item_id, api_key, item_xml):
    headers = {'content-type':'application/xml'}
    query = 'bibs/{}/holdings/{}/items/{}?apikey={}'
    
    url = ''.join([base_url, query.format(mms_id, holdings_id, item_id, api_key)])
    requests.put(url, headers=headers, data=item_xml.encode('utf-8'))

    
def update(mms_id, input_file, api_key, base_url):
    items_to_update = get_info_from_csv(input_file)

    for holdings in items_to_update:
        for item in items_to_update[holdings]:
            xml = get_item_xml(base_url, mms_id, holdings, item['id'], api_key)
            updated_xml = update_item_xml(xml, item)
            update_item(base_url, mms_id, holdings, item['id'], api_key, updated_xml)