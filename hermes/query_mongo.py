# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:00:56 2017

@author: ray
"""

import sys
from mongo import Mongo_query
import pprint

argsdict = {}

for farg in sys.argv:
    if farg.startswith('--'):
        (arg,val) = farg.split("=")
        arg = arg[2:]

        if arg in argsdict:
            argsdict[arg].append(val)
        else:
            argsdict[arg] = [val] 


for key in argsdict:
    if len(argsdict[key]) == 1:
        argsdict[key] = argsdict[key][0]


query = argsdict
print query


result = Mongo_query(query = query)
pp = pprint.PrettyPrinter()

if len(result) <= 1:
    pp.pprint(result)
    
else:
    pp.pprint('There are total of {} documents found, Do you want to display them?'.format(len(result)))
    if sys.version_info[0] == 3:
        display = input('y/n: ')

    else:
        display = raw_input('y/n: ')
        
    if display == 'y':
        pp.pprint(result)
  
#print result