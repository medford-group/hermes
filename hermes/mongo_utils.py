# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:57:55 2017

@author: ray
"""

from pymongo import MongoClient
import sys
import getpass


#client = MongoClient("mongodb://xlei38:`Kuyue5689740@54.201.152.64/PIFs")
#db=client['PIFs']
#collection = db['test']
#client = MongoClient('localhost', 27017)


def user_authentication():
    if sys.version_info[0] == 3:
        username = input('user name: ')
#        password = input('password: ')
        password= getpass.getpass('Password: ')
    else:
        username = raw_input('user name: ')
#        password = raw_input('password: ')
        password= getpass.getpass('Password: ')
    return username, password

def get_Client_uri(username,password):
#    return "mongodb://tester:password@54.201.152.64/test"
    return "mongodb://" + username + ":" + password + "@54.201.152.64/medford-data"