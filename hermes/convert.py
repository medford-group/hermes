import json

# Functions for data transformations not involving database


## Functions for creating data objects from ASE atoms objects
def atoms_to_dict(atoms):
    return {}

## Functions for creating data objects from calculator objects

def calc_to_dict(calc):
    # check to see if calc is espresso
    d = espresso_to_dict()
    #else raise error
    return d

def espresso_to_dict(esp_calc):
    d = {}
    return d


## Functions for transforming data between dictionary, json, etc.

def data_to_dict(atoms, calc, metadata):
    d = {}
    return d

def data_from_dict(d):
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

