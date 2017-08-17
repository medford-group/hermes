# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:36:05 2017

@author: ray
"""

import sys
from mongo import insert_json_file

filename = sys.argv[1]

insert_json_file(filename,database = 'medford-data', collection = 'DFT', username = None, password = None)