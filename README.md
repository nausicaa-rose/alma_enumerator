# ae: alma enumerator
## About

## Requirements
* Python 3 (Has been tested and works with Python 3.4 and 3.5. Probably works
  with earlier versions of Python 3.)
* External dependencies
    * [Requests](http://requests.readthedocs.io/en/master/) 
    * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
    * [DocOpt](http://docopt.org/) 

## Usage

## Known issues
This README is incomplete.

ae_gui is currently unusable. It's currently just a mock up that has no
functionality. That should change soon.

Certain patterns pass through the parser without raising an error, but do not 
process correctly. Some examples:

* no.51 12 Dec 2015 (12 is treated as enumeration_b rather than chronology_k)
* v.164 no.5 Dec/Jan 2015 - Dec/Jan 16 (chronology_j ends up being 
  '12/01/12/01', when in reality it's should probably be '12/01')
* v 132 Dec 1915 May 1916 (Dec is treated like the entry for enumeration_b and 
  1915 ends up in chronology_k)


