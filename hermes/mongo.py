# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:16:32 2017

@author: ray
"""

import os
#from dfttopif import directory_to_pif
import pprint
from pymongo import MongoClient
from datetime import datetime
from mongo_utils import user_authentication, get_Client_uri
import sys
import json

#def DFT_spider(database = 'PIFs', collection = 'DFT', username = None, password = None):
#    
#    if username == None or password == None:
#        username, password = user_authentication()
#    user_uri  = get_Client_uri(username, password)
#    client = MongoClient(user_uri)
#    db=client[database]
#    collection = db[collection]
#    pp = pprint.PrettyPrinter()
#    
#    for root, dirs, files in os.walk(".", topdown=False):
#        for directory in dirs:
#            try:
#                data = directory_to_pif(os.path.join(root,directory))
#                post = data.as_dictionary()
#                path = os.path.abspath(os.path.join(root,directory))
#                post['user_created'] = username
#                post['path'] = path
#                post['time_created'] = str(datetime.now())
#                pp.pprint('')
#                pp.pprint('found: ' + path)
#
#                temp_query = {'path': path}
#                temp = collection.find(temp_query).count()
#           
#                if temp == 0:
#                    collection.insert_one(post)
#                    pp.pprint('successfully inserted to database')
#                    pp.pprint('')
#                else:
#                    pp.pprint('** WARNING: director already in database **')
#                    pp.pprint('delete the existing document to update')
#                    pp.pprint('')
#                
#            except:
#                pass
#    
#    return

def DFT_query(database = 'medford-data', collection = 'DFT', query = {}, username = None, password = None,printout = False):
    result = []
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()
    for post in collection.find(query):
        if printout == True:
            pprint.pprint(post)
        result.append(post)
    pp.pprint('total documents found: ' + str(len(result)))
    return result
    
def DFT_delete(query,database = 'medford-data', collection = 'DFT', username = None, password = None):
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()
    delete_number = collection.find(query).count()
    pp.pprint('')
    pp.pprint('**** WARNING ****: you are about to delete {} documents!!'.format(delete_number))
    pp.pprint('You are abusolutly sure about what you are doing right?')
    
    if sys.version_info[0] == 3:
        if delete_number <= 3:
            check = input('y/n: ')
            if check == 'y':
                collection.delete_many(query)
                pp.pprint('Documents deleted')
            else:
                pp.pprint('Documents Not deleted')
    
        else:
            check = input('type [YesDelete] to delete: ')
            if check == 'YesDelete':
                collection.delete_many(query)
                pp.pprint('Documents deleted')
            else:
                pp.pprint('Documents Not deleted')     
    
    else:
        if delete_number <= 3:
            check = raw_input('y/n: ')
            if check == 'y':
                collection.delete_many(query)
                pp.pprint('Documents deleted')
            else:
                pp.pprint('Documents Not deleted')
    
        else:
            check = raw_input('type [YesDelete] to delete: ')
            if check == 'YesDelete':
                collection.delete_many(query)
                pp.pprint('Documents deleted')
            else:
                pp.pprint('Documents Not deleted')         
    return

def DFT_insert_one(post,database = 'medford-data', collection = 'DFT', username = None, password = None):
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()
    
    if 'user_created' not in post:
        post['user_created'] = username
    if 'time_created' not in post:
        post['time_created'] = str(datetime.now())
    collection.insert_one(post)
    pp.pprint('Document added')    
    
    return

def insert_json_file(filename,database = 'medford-data', collection = 'DFT', username = None, password = None):
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()    
    
    with open('data.json', 'r') as outfile:
        post = json.load(outfile)
        
    if 'user_created' not in post:
        post['user_created'] = username
    if 'time_created' not in post:
        post['time_created'] = str(datetime.now())
    collection.insert_one(post)
    pp.pprint('Document added') 
    
    return
    
    
    
#if __name__ == "__main__":
#    username, password = user_authentication()
#    data = {'test':'test'}
#    DFT_insert_one(data, database = 'medford-data', collection = 'DFT', username = username, password = password) 
#    DFT_query(database = 'medford-data', collection = 'DFT', query = {}, username = username, password = password,printout = True)
#    DFT_delete({},database = 'medford-data', collection = 'DFT', username = None, password = None)

#    DFT_spider(database = 'PIFs', collection = 'DFT', username = username, password = password)
#    DFT_query(database = 'PIFs', collection = 'DFT', query = {}, username = username, password = password,printout = True)
#    DFT_delete({'path':'/gpfs/pace1/project/chbe-medford/medford-share/users/bcomer3/espresso_rutile/espresso_Rutile/2_layer_runs/N/test/esp.log'},database = 'PIFs', collection = 'DFT', username = username, password = password)
#for post in collection.find():
#    pprint.pprint(post)