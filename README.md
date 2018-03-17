# ae: alma enumerator
## About
Alma Enumerator is set of Python scripts to update enumeration and chronology
information in Alma, an integrated library system made by Ex Libris. It parses
item record description fields, extracts enumeration and chronology information
and updates the item record's enumeration and chronology fields. This is 
particularly useful cases when a library has volume, issue and date information
saved in item description fields but not in the corresponding enumeration and
chronology fields.

## Requirements
* Python 3.5+ 
* External dependencies
    * [Requests](http://requests.readthedocs.io/en/master/) 
    * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Usage
First make sure your settings are correct in `settings.py`, including the API
key and the MMS ID of the title you wish to update. If you don't have an API
key, you'll need to get one from the [Ex Libris Developer Network](https://developers.exlibrisgroup.com/).

To use ae's graphical interface, run `ae_gui`. This will open up a window like
the one below:

![Example of ae_gui](/img/ae_gui_example.png)

Alma Enumerator can also be used on the command line. To get enumeration and 
chronology data out of item description fields, run `ae_fetch` or `ae fetch`.
To update items' enumeration and chronology fields, run `ae_update` or 
`ae update`.

`ae_fetch` saves the information it gets to a CSV file. It is always a good idea
to check `ae_fetch`'s output to make sure the data it has extracted from the item
descriptions is correct. The CSV file can be loaded into a spreadsheet 
application for easier viewing. If you do load it into a spreadsheet app, it's 
a good idea to have the program treat each column as plain text rather than
numerical data.

Additionally, whenever `ae_fetch` recognizes a pattern doesn't parse correctly,
it records the error in an error file and `ae_update` won't update the item
record in Alma. This way you can edit these records yourself.

Once everything checks out in the CSV, you can run `ae_update` to update the 
enumeration and chronology information for each item under the current title.

Then verify that your records updated correctly in Alma.

If you'd rather pass ae_fetch and ae_update command line arguments instead of
updating settings.py each time you make change `mms_id`, you can.

`ae_fetch` accepts:

    ae_fetch [-m | --mms-id <mms>] [-o | --output-file <of>] [-e | --error-file <ef>] [-a | --api-key <api>]

So you could specify an mms_id by typing `ae_fetch -m 999999999999999999` or
`ae_fetch --mms-id 999999999999999999` and `ae_fetch` would use the MMS ID 
provided while using settings.py for the output and error files and the API 
key.

`ae_update` accepts:

    ae_update [(-m | --mms-id) <mms>] [(-i | --input-file) <if>] [(-a | --api-key) <api>]
                                                      
If you're not comfortable working on the command line, run `ae_gui` or use 
an IDE like Spyder or PyCharm that will allow you to open and then run 
`ae_fetch` and `ae_update`.

![Example of running ae_update in Spyder](/img/spyder_run_example.png)

![Example of running ae_fetch in Pycharm](/img/pycharm_run_example.png)

If you're feeling daring you can also batch process files without checking the output
of `ae_fetch`, you can use `ae_batch` or `ae batch`. 

`ae_batch` accepts:
    ae_batch [-i | --input-file <if>] [-o | --output-file <of>] [-e | --error-file <ef>] (-a | --api-key <api>] <lf>      

Instead of taking a single MMS ID, ae_batch takes a file with one bibliographic 
MMS ID per line such as:

    1234567890
    0987654321
    0192837465
    1029384756

It then will download and process items associated with each MMS ID, just like 
`ae_fetch` before updating each item a la `ae_update`. This has the potential to 
speed up processing significantly, but at the risk of errors potentially going
uncaught.

## Known issues
Certain patterns pass through the parser without raising an error, but do not 
process correctly. Some examples:

* no.51 12 Dec 2015 (12 is treated as `enumeration_b` rather than `chronology_k`)
* v 19 07-08 (07-08 is treated like `enumeration_b` instead of `chronology_i`)
* v 63 #1 P.1 JAN 1990 (P.1 is treated like `chronology_k` instead of `enumeration_c`)
* v 20-21 1983-1984, c 2 (c 2 treated like `enumeration_b`)
* For more known issues see [notes.md](notes.md)

Because the updating function downloads the XML for each record, modifies it,
and uploads it back to the server one at a time, it is quite slow, especially when
processing large numbers of records.


