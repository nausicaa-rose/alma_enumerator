# -*- coding: utf-8 -*-

from AE import get_info_from_description

def test_vol_no_mo_year_mo_year():
    assert get_info_from_description('v.153 no.6&7 Jun 2010 - Jul 2010') == {'chronology_i': '2010',
                                                                             'chronology_j': '06/07',
                                                                             'chronology_k': '',
                                                                             'enumeration_a': '153',
                                                                             'enumeration_b': '6/7',
                                                                             'pages': ''}
                                                                             
    assert get_info_from_description('v.67 no.2-3 Dec 2011 - Jan 2012') == {'chronology_i': '2011/2012',
                                                                            'chronology_j': '12/01',
                                                                            'chronology_k': '',
                                                                            'enumeration_a': '67',
                                                                            'enumeration_b': '2/3',
                                                                            'pages': ''}
                                                                            
    assert get_info_from_description('v.68 no.6 Nov 2015 - Dec 2015') == {'chronology_i': '2015',
                                                                          'chronology_j': '11/12',
                                                                          'chronology_k': '',
                                                                          'enumeration_a': '68',
                                                                          'enumeration_b': '6',
                                                                          'pages': ''}
                                                                          
    assert get_info_from_description('v.92 no.3-4 Fal 2011 - Win 2011') == {'chronology_i': '2011',
                                                                            'chronology_j': '23/24',
                                                                            'chronology_k': '',
                                                                            'enumeration_a': '92',
                                                                            'enumeration_b': '3/4',
                                                                            'pages': ''}

                                                                          
def test_vol_no_mo_day_year():
    assert get_info_from_description('v.468 no.7327 Dec 23/30 2010') == {'chronology_i': '2010',
                                                                         'chronology_j': '12',
                                                                         'chronology_k': '23/30',
                                                                         'enumeration_a': '468',
                                                                         'enumeration_b': '7327',
                                                                         'pages': ''}
                                                                         
    assert get_info_from_description('\v.523 no.7560 Jul 16 2015') == {'chronology_i': '2015',
                                                                       'chronology_j': '07',
                                                                       'chronology_k': '16',
                                                                       'enumeration_a': '523',
                                                                       'enumeration_b': '7560',
                                                                       'pages': ''}
                                                                       
    assert get_info_from_description('v 56 no. 11 (10 March 2003)') == {'chronology_i': '2003',
                                                                        'chronology_j': '03',
                                                                        'chronology_k': '10',
                                                                        'enumeration_a': '56',
                                                                        'enumeration_b': '11',
                                                                        'pages': ''}
                                                                        
    assert get_info_from_description('v.301 no.25&26 Dec 21/28 2015') == {'chronology_i': '2015',
                                                                          'chronology_j': '12',
                                                                          'chronology_k': '21/28',
                                                                          'enumeration_a': '301',
                                                                          'enumeration_b': '25/26',
                                                                          'pages': ''}
                                                                          
    assert get_info_from_description('v.306 no.20 Nov 23 2011 - Nov 30 2011') == {'chronology_i': '2011',
                                                                                  'chronology_j': '11',
                                                                                  'chronology_k': '23/30',
                                                                                  'enumeration_a': '306',
                                                                                  'enumeration_b': '20',
                                                                                  'pages': ''}
                                                                        
                                                                        
def test_vol_no_mo_year():
    assert get_info_from_description('v.157 no.6&7 Jun/Jul 2012') == {'chronology_i': '2012',
                                                                      'chronology_j': '06/07',
                                                                      'chronology_k': '',
                                                                      'enumeration_a': '157',
                                                                      'enumeration_b': '6/7',
                                                                      'pages': ''}
                                                                      
    assert get_info_from_description('v.43 no.2 Win 2016') == {'chronology_i': '2016', 
                                                               'chronology_j': '24', 
                                                               'chronology_k': '', 
                                                               'enumeration_a': '43', 
                                                               'enumeration_b': '2',
                                                               'pages': ''}
                                                               
    assert get_info_from_description('v 21 #3 SPR 1994') == {'chronology_i': '1994', 
                                                               'chronology_j': '21', 
                                                               'chronology_k': '', 
                                                               'enumeration_a': '21', 
                                                               'enumeration_b': '3',
                                                               'pages': ''}
                                                               
    assert get_info_from_description('v. 23 no. 3 (August 2008)') == {'chronology_i': '2008',
                                                                      'chronology_j': '08',
                                                                      'chronology_k': '',
                                                                      'enumeration_a': '23',
                                                                      'enumeration_b': '3',
                                                                      'pages': ''}    

    assert get_info_from_description('v 84 #6 JUN 1997 -ABSTRACTS') == {'chronology_i': '1997',
                                                                        'chronology_j': '06',
                                                                        'chronology_k': '',
                                                                        'enumeration_a': '84',
                                                                        'enumeration_b': '6',
                                                                        'pages': ''}                                                                      
                                                                      
                                                                              
def test_vol_mo_year_mo_year():
    assert get_info_from_description('no.44 Sum 2011/Spr 2012') == {'chronology_i': '2011/2012',
                                                                    'chronology_j': '22/21',
                                                                    'chronology_k': '',
                                                                    'enumeration_a': '44',
                                                                    'enumeration_b': '',
                                                                    'pages': ''}                                                                      

    assert get_info_from_description('v 63 October 1986-June 1987') == {'chronology_i': '1986/1987',
                                                                        'chronology_j': '10/06',
                                                                        'chronology_k': '',
                                                                        'enumeration_a': '63',
                                                                        'enumeration_b': '',
                                                                        'pages': ''}
                                                            
    assert get_info_from_description('v 9/10 JUN 1970-NOV 1971') == {'chronology_i': '1970/1971',
                                                                     'chronology_j': '06/11',
                                                                     'chronology_k': '',
                                                                     'enumeration_a': '9/10',
                                                                     'enumeration_b': '',
                                                                     'pages': ''}
                                                                     
                                                                                                                                            
def test_vol_mo_day_year():
    assert get_info_from_description('no.51 Dec 21 2015') == {'chronology_i': '2015',
                                                              'chronology_j': '12',
                                                              'chronology_k': '21',
                                                              'enumeration_a': '51',
                                                              'enumeration_b': '',
                                                              'pages': ''}                                                               
                                                                                                                           
                                                               
def test_vol_mo_year():
    assert get_info_from_description('no.52 Win 2013 - 2014') == {'chronology_i': '2013/2014',
                                                                  'chronology_j': '24',
                                                                  'chronology_k': '',
                                                                  'enumeration_a': '52',
                                                                  'enumeration_b': '',
                                                                  'pages': ''}
                                                                
    assert get_info_from_description('v 219-220 SEP-OCT 1968') == {'chronology_i': '1968', 
                                                                   'chronology_j': '09/10', 
                                                                   'chronology_k': '', 
                                                                   'enumeration_a': '219/220', 
                                                                   'enumeration_b': '',
                                                                   'pages': ''}

    assert get_info_from_description('Issue 39 (Winter 2009)') == {'chronology_i': '2009',
                                                                   'chronology_j': '24',
                                                                   'chronology_k': '',
                                                                   'enumeration_a': '39',
                                                                   'enumeration_b': '',
                                                                   'pages': ''}                                                               
                                                                    
    assert get_info_from_description('v 66 Oct/May 1964-65') == {'chronology_i': '1964/1965',
                                                                 'chronology_j': '10/05',
                                                                 'chronology_k': '',
                                                                 'enumeration_a': '66',
                                                                 'enumeration_b': '',
                                                                 'pages': ''}
                                                                 
    assert get_info_from_description('v 280 July-Dec.1997') == {'chronology_i': '1997',
                                                                'chronology_j': '07/12',
                                                                'chronology_k': '',
                                                                'enumeration_a': '280',
                                                                'enumeration_b': '',
                                                                'pages': ''}
                                                        
    assert get_info_from_description('v 78 Dec 1888- May 1889') == {'chronology_i': '1888/1889',
                                                                    'chronology_j': '12/05',
                                                                    'chronology_k': '',
                                                                    'enumeration_a': '78',
                                                                    'enumeration_b': '',
                                                                    'pages': ''}
                                                                   
                                                                   
def test_vol_no_year():
    assert get_info_from_description('v.85 no.6 2009 International focus issue') == {'chronology_i': '2009',
                                                                                     'chronology_j': '',
                                                                                     'chronology_k': '',
                                                                                     'enumeration_a': '85',
                                                                                     'enumeration_b': '6',
                                                                                     'pages': ''}
                                                                                     
def test_vol_no_mo():
    assert get_info_from_description('v. 110 no. 9 (September-special issue)') == {'chronology_i': '',
                                                                                   'chronology_j': '09',
                                                                                   'chronology_k': '',
                                                                                   'enumeration_a': '110',
                                                                                   'enumeration_b': '9',
                                                                                   'pages': ''}  
                                                                                   
                                                                      

def test_mo_year():
    assert get_info_from_description('January-March 2008') == {'chronology_i': '2008',
                                                               'chronology_j': '01/03',
                                                               'chronology_k': '',
                                                               'enumeration_a': '',
                                                               'enumeration_b': '',
                                                               'pages': ''} 
                                                               
    assert get_info_from_description('November 2014 Technology issue') == {'chronology_i': '2014',
                                                                           'chronology_j': '11',
                                                                           'chronology_k': '',
                                                                           'enumeration_a': '',
                                                                           'enumeration_b': '',
                                                                           'pages': ''}                                                                                   

def test_year_mo():
    assert get_info_from_description('1967 December') == {'chronology_i': '1967',
                                                          'chronology_j': '12',
                                                          'chronology_k': '',
                                                          'enumeration_a': '',
                                                          'enumeration_b': '',
                                                          'pages': ''}
                                                               
                                                                                     
def test_vol_year():
    assert get_info_from_description('v 22 1994-95') == {'chronology_i': '1994/1995', 
                                                         'chronology_j': '', 
                                                         'chronology_k': '', 
                                                         'enumeration_a': '22', 
                                                         'enumeration_b': '',
                                                         'pages': ''}

    assert get_info_from_description('no 86-89 1982') == {'chronology_i': '1982',
                                                          'chronology_j': '',
                                                          'chronology_k': '',
                                                          'enumeration_a': '86/89',
                                                          'enumeration_b': '',
                                                          'pages': ''}
                                                          
                                                                                                              
def test_vol_no():
    assert get_info_from_description('v.341 no.6237-6240') == {'chronology_i': '',
                                                               'chronology_j': '',
                                                               'chronology_k': '',
                                                               'enumeration_a': '341',
                                                               'enumeration_b': '6237/6240',
                                                               'pages': ''}

                                                               
def test_vol():
    assert get_info_from_description('v 149') == {'chronology_i': '',
                                                  'chronology_j': '',
                                                  'chronology_k': '',
                                                  'enumeration_a': '149',
                                                  'enumeration_b': '',
                                                  'pages': ''}
                                                  
    assert get_info_from_description('v 283-288INDEX') == {'chronology_i': '',
                                                           'chronology_j': '',
                                                           'chronology_k': '',
                                                           'enumeration_a': '283/288',
                                                           'enumeration_b': '',
                                                           'pages': ''}

                                                           
def test_year():
    assert get_info_from_description('INDEX 1990') == {'chronology_i': '1990',
                                                       'chronology_j': '',
                                                       'chronology_k': '',
                                                       'enumeration_a': '',
                                                       'enumeration_b': '',
                                                       'pages': ''}
                                                       
                                                       
def test_pagination():                                                          
    assert get_info_from_description('v 96 1999 pp 1811-3330') == {'chronology_i': '1999',
                                                                   'chronology_j': '',
                                                                   'chronology_k': '',
                                                                   'enumeration_a': '96',
                                                                   'enumeration_b': '',
                                                                   'pages': '1811/3330'}
                                                                   
    assert get_info_from_description('v 89 March pp 1519-2510') == {'chronology_i': '',
                                                                   'chronology_j': '03',
                                                                   'chronology_k': '',
                                                                   'enumeration_a': '89',
                                                                   'enumeration_b': '',
                                                                   'pages': '1519/2510'}
                                                                   

def run_tests():                                                          
    test_vol_no_mo_year_mo_year()                                                        
    test_vol_no_mo_day_year()                                                        
    test_vol_no_mo_year()
    test_vol_mo_year_mo_year()
    test_vol_mo_day_year()
    test_vol_mo_year()
    test_vol_no_year()
    test_vol_no_mo()
    test_mo_year()
    test_year_mo()
    test_vol_year()
    test_vol_no()
    test_vol()
    test_year()
    test_pagination()
    
run_tests()
