#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration variables
#-------------------------

## For both get_issue_info.py and update_issue_info.py ##
# You'll need this to use Alma's API, you can create API keys by creating an
# account at https://developers.exlibrisgroup.com/ and going to your account's
# 'Applications' page
api_key=''

# This is the ID of the bib record for which you want to update item information.
# You'll need to change it for each bib record.
mms_id = ''

## For get_issue_info.py ##
# The location of the output file for the records that can be automatically updated.
# Whenever you start a new bib record, you'll want to make sure this file is empty.  
# On Windows, this path will look something like 'C::\\Users\\username\\path\\to\\folder'.
# On Mac OS X and Linux, it will look something like '/Users/username/path/to/directory'
# or '/home/username/path/to/directory/'. 
output_file = ''

# The location of the output file for records you'll need to update by hand.
error_file = ''

## For update_issue_info.py ##
# The location of the input file for the records that can be automatically updated. Unless
# you want to edit the output file and save it to with a new name, setting the input file to
# match the output file for get_issue_info.py is probably what you'll want.
  
input_file = output_file

#--- end configuration variables -------

# Base URL for requests. This shouldn't need to be changed.
base_url = 'https://api-na.hosted.exlibrisgroup.com/almaws/v1/'

