# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:36:05 2017

@author: ray
"""

import sys
from mongo import insert_json_file
import pprint

filename = sys.argv[1]

push_setup = {}

try: 
    temp = sys.argv[2]
    pprint('Are you sure you want to insert the document to {} collection?'.format(temp))
    if sys.version_info[0] == 3:
        insert = input('y/n: ')

    else:
        insert = raw_input('y/n: ')
        
    if insert == 'y':
        collection = temp

except:
    collection = "DFT"

insert_json_file(filename,database = 'medford-data', collection = collection, username = None, password = None)