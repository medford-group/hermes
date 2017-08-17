import json
from collections import OrderedDict
import os
import datetime
from espresso import espresso

# Functions for data transformations not involving database


## Functions for creating data objects from ASE atoms objects
def atoms_to_dict(atoms):
    return {}

def dict_to_atoms(d):
    return {}

## Functions for creating data objects from calculator objects

def calc_to_dict(calc):
    # check to see if calc is espresso
    try:
       calc = calc.get_calculator()
    except:
        pass
    try:
       d = calc.todict()
    except:
       raise IOError('calculator does not have todict imprementation')
    return d
def dict_to_calc(calc_dict):
    d = espresso(**calc_dict)
    return d

## Functions for transforming data between dictionary, json, etc.

def data_to_dict(atoms, calc, metadata):
    
    atom_dict = atoms_to_dict(atoms)
    calc_dict = calc_to_dict(calc)
    if 'name' not in calc_dict.keys():
        calc_dict['name']= calc.__class__.__name__
    metadata_dict = OrderedDict(metadata)
    metadata_dict = ID_stamper(metadata_dict)
    metadata_dict['mtime']=datetime.datetime.utcnow()
    d = OrderedDict(atom_dict,calc_dict,metadata_dict)
    
    return d

def dict_to_data(d):
    atoms = {}
    calc = {}
    metadata = {}
    return atoms, calc, metadata

def dict_to_json(d, json_file):
    json.dump(d, open(json_file,'w'))

def data_from_json(j):
    json_file = open(j)
    json_data = json.load(json_file)
    a, c, m = from_dict(json_data)


def ID_stamper(metadata_dict):
    if 'USER' not in metadata_dict:
        metadata_dict['USER']=os.getenv('USER')
    if 'ctime' not in metadata_dict:
        metadata_dict['ctime']=datetime.datetime.utcnow()
    return metadata_dict
