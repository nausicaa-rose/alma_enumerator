# -*- coding: utf-8 -*-

from settings import api_key, mms_id, output_file, base_url
from AE import get_holdings, get_item_info, write_header_to_csv, output_to_csv

# Get holdings id(s)
holdings = get_holdings(base_url, mms_id, api_key)

# For each holdings ID, write the ID to the output file, get the information
# for all of the holdings' items, write the field headers to the output file,
# then write the item information to the output file and write errors to the 
# error file.
for h in holdings:
    with open(output_file, 'a', encoding='utf-8') as fh:
        fh.write('{}\n'.format(h))

    item_info = get_item_info(base_url, mms_id, holdings)
    write_header_to_csv(output_file, item_info)
    output_to_csv(output_file, item_info)  