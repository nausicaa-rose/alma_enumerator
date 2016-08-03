#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:06:03 2016

@author: wt
"""

from .get_issue_info import get_info_from_description

def test_vol_no_mo_year():
    assert get_info_from_description('v.43 no.2 Win 2016') == {'chronology_i': '2016', 
                                                               'chronology_j': '24', 
                                                               'chronology_k': '', 
                                                               'enumeration_a': '43', 
                                                               'enumeration_b': '2'}
                                                               
    assert get_info_from_description('v 21 #3 SPR 1994') == {'chronology_i': '1994', 
                                                               'chronology_j': '21', 
                                                               'chronology_k': '', 
                                                               'enumeration_a': '21', 
                                                               'enumeration_b': '3'}
    

def test_vol_mo_year():
    assert get_info_from_description('v 219-220 SEP-OCT 1968') == {'chronology_i': '1968', 
                                                                    'chronology_j': '09/10', 
                                                                    'chronology_k': '', 
                                                                    'enumeration_a': '219/220', 
                                                                    'enumeration_b': ''}
                                                                    
def test_vol_year():
    assert get_info_from_description('v 22 1994-95') == {'chronology_i': '1994/95', 
                                                         'chronology_j': '', 
                                                         'chronology_k': '', 
                                                         'enumeration_a': '22', 
                                                         'enumeration_b': ''}
                                                         
test_vol_no_mo_year()
test_vol_mo_year()
test_vol_year()
                                                                    
                                                                    
                                                                    