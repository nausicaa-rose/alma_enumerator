It can handle the basic pattern "v 10 no 1 Mar 2 2015"
with all fields being treated as optional, although there 
must be at least a volume or year it can handle the pattern 
"v 10 no 1 2 Mar 2015" with the same rules as above, except 
when there day is recorded but not the second level of 
enumeration. That is, "no. 1 2 Mar 2015" will be treated as 
if the first number is the volume number and the second, which
represents March 2, will be treated as the issue number.

# Can handle:

* v.43 no.2 Win 2016
* v 22 1994-95
* v 21 #3 SPR 1994
* v 219-220 SEP-OCT 1968
* v.468 no.7327 Dec 23/30 2010
* \v.523 no.7560 Jul 16 2015
* v. 23 no. 3 (August 2008)
* v 56 no. 11 (10 March 2003)
* no.51 Dec 12 2015
* no 86-89 1982
* v.68 no.6 Nov 2015 - Dec 2015
* Issue 39 (Winter 2009)
* v.85 no.6 2009 International focus issue
* no.44 Win 2011/Win 2012
* v 63 October 1986-June 1987
* v 46 July 2005-June 2006
* v 47 July 2006-June 2007
* v 84 #6 JUN 1997 -ABSTRACTS 
* Index no 1-570 (1948-1997)
* v 16 no 4 (Jun./Jul./Aug./Sep. 2007)
* v 149
* INDEX 1990
* v 283-288INDEX
* v.341 no.6237-6240
* no.52 Win 2013 - 2014
* January-March 2008
* 1998 JAN-JUN
* v 66 Oct/May 1964-65
* v.67 no.2-3 Dec 2011 - Jan 2012
* v.157 no.6&7 Jun/Jul 2012
* v.153 no.6&7 Jun 2010 - Jul 2010
* v 47 Fall 1998-Aug 1999
* v 9/10 JUN 1970-NOV 1971
* v.92 no.3-4 Fal 2011 - Win 2011
* 1967 December
* v 1-3 2000-2002 [not in tests]
* v 128 no. 3 (Supplement - Forty Years On) [not in tests]
* v 128 no. 3 (Supplement - Forty-Year Index) [not in tests]
* v.6 no.3 2013 [not in tests]
* v 51 Nov.-Dec.1997 [not in tests]
* v. 48 no. 2 (Great Homes - Annual) [not in tests]
* v 63 Jan.-Jun 1999 [not in tests]
* v 32 Dec 2004- Sept 2005  [not in tests]
* November 2014 Technology issue
* v. 110 no. 9 (September-special issue)
* v 280 July-Dec.1997
* v 78 Dec 1888- May 1889
* v.301 no.25&26 Dec 21/28 2015
* v.306 no.20 Nov 23 2011 - Nov 30 2011
* v 96 1999 pp 1811-3330
* v 89 March pp 1519-2510
* no.49 2010/ 2011
* v.44 no.3 Win 2014 - 2015
* v.301 no.21&22 Nov 23 2015 - Nov 30 2015
* v.302 no.2-3 Jan 11 2016 - Jan 18 2016
* v 49 #5 MAR 9,1984

# Identifies as error:

* v.30:no.7(2016:July/Aug.)
* v.30:no.8(2016:Sept.) 
* v.38:no.5(2017:June) 
* 2016:no.35(2016:Aug. 27) 
* v. 24 no. 1  Issue 171 (Jul. 2009)
* v 31 Oct. 06-June 07 
* v. 317 july 07
* v 67 #3 AUG 986
* n0.132-135
* v 23 no 36 9/12/97
* v 12 #1 FEB 2976
* 100,02/04,1997/1998,v 100 no 2 Feb 1997-v 101 no 2 April 
* v. 72 Sept 06-May 07
* v.306 no.19 Nov 162011

# Passes through, but doesn't process correctly:

* 1998,,2322992980002843,101/2,2
* v. 25 no. 4 (Supplement- Winter Bird Highlights v.2)
* v.302 no.21 & 22 May 23/30 2016 [error: 2nd issue # treated as chronology_k field]
* v. 8 no. 1/2 (Spring and Fall1998) (drops fall, should add splitting on word/number)
* no.51 12 Dec 2015 (12 is treated as enumeration_b rather than chronology_k)
* v.164 no.5 Dec/Jan 2015 - Dec/Jan 16 (chronology_j ends up being '12/01/12/01', when in reality it's should probably be '12/01')
* v 132 Dec 1915 May 1916 (Dec is treated like the entry for enumeration_b and 1915 ends up in chronology_k)
* v 19 07-08 (07-08 is treated like chronology_i instead of chronology_j)
* v 63 #1 P.1 JAN 1990 (P.1 is treated like chronology_k instead of enumeration_c)
* v 20-21 1983-1984, c 2 (1983-1984 treated like `enumeration_b`, c 2 treated like `chronology_i`)
* Apr 2015 150th Anniversary issue (Apr dropped, 2015 treated like `enumeration_a`, 150th treated like `chronology_i`)
* v 82 Nov. 2006-Jan. 1, 2007 (passes through correctly, but chronology_k will be unclear and should probably have been omitted from the description)
* v 71 FEB 20- APR 1995 (passes through correctly, but chronology_k will be unclear and should probably have been omitted from the description)
* v.14 Jul 1921-v.15 Nov. 1921 (second volume number treated like enumeration_b)
* v 22 1083 (1083 get's treated like enumeration_b because it doesn't fit year pattern)
* v 9 FAL1989-SUM 1990 (lack of space between FAL and 1989 weird chronology_i content '1989//1990' and no chronology_j)
* v 14 fall 06-summer 07 (07 treated like chronology_k and 06 treated like enumeration_b)
* suppl.17 Mar 2014 (17 treated like enumeration_a, not actually sure what 17 is supposed to indicate, may be date or alternate numbering scheme)
* no.3221 Mar 27/Apr 27 2013 - Mar 2/Apr 2 2013 -> 27,3221,2013,27/2/2,2322610670002843,03/04
* 30,2530,1999,no 2530 Dec.30, 1999-Jan 5,2000,52000,2322611330002843,12/01 
* no 3044 (20-26 September 2007)
* v 57 #1/SUP
* no 1006 MAR4 1991
* LABGUIDE AUG 15 1996
* v 8 Jan.3-17, Jan.31-June 1972
* no 92 v 12 no 2 2002 (issue #, vol, no.)
* v.11 no.2-3-v.12 no.1 (2008)
* v 10 no 3--v 11 no 1 Spring/Summer 2007
* v.44 no.3 Win 20 2015 - Win 20 2015
* v. 17 (v. 17 Index) (second 17 treated as enumeration_b)
* v 18 #7-10 V 19 #1-2 1974-5
* v.302 no.21 & 22 May 23/30 2016 [Should handle]

        Out[17]: 
        {'chronology_i': '2016',
         'chronology_j': '05',
         'chronology_k': '22/23/30',
         'enumeration_a': '302',
         'enumeration_b': '21'}

* 11TH ED 1915-DEC 1973 [Should ID as error]

         {'chronology_i': '1915/1973',
         'chronology_j': '12',
         'chronology_k': '',
         'enumeration_a': '11',
         'enumeration_b': ''}

* v 74 Dec. 21,1998-Jan. 4,1999 [Should handle]

        {'chronology_i': '',
         'chronology_j': '12/01',
         'chronology_k': '41999',
         'enumeration_a': '74',
         'enumeration_b': '211998'}
         no.220(2017:Spring)
 
* no.5 & 6 June & July 2016 [Should handle]

         {'chronology_i': '2016',
         'chronology_j': '06/07',
         'chronology_k': '',
         'enumeration_a': '5',
         'enumeration_b': '6'}
 
* Issue 40 (Spring 2009)";"Issue 40 (Spring 2009) [Should ID as error]

        {'chronology_i': '2009',
         'chronology_j': '21',
         'chronology_k': '',
         'enumeration_a': '40',
         'enumeration_b': '40'}

* v 97 2000 pp 1-1318 

        {'chronology_i': '2000',
         'chronology_j': '',
         'chronology_k': '',
         'enumeration_a': '97',
         'enumeration_b': '1/1318'}
 
* v 99 December 10, 2002 Suppl.4

         {'chronology_i': '2002',
         'chronology_j': '12',
         'chronology_k': '4',
         'enumeration_a': '99',
         'enumeration_b': '10'}

