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
ae_gui is currently unusable. It's currently just a mock up that has no
functionality. That should change soon.

Certain patterns pass through the parser without raising an error, but do not 
process correctly. Some examples:

* 2016:no.35(2016:Aug. 27)
* v 51 Nov.-Dec.1997
* no.51 12 Dec 2015
* v. 110 no. 9 (September-special issue)
* v 128 no. 3 (Supplement - Forty Years On)
* v 128 no. 3 (Supplement - Forty-Year Index)

