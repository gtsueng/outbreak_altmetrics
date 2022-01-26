import os
import json

def load_annotations():
    HOME_DIR = '/opt/home/outbreak'
    altmetrics_file =  os.path.join(HOME_DIR, 'covid_altmetrics', 'results', 'altmetric_annotations.json')
    with open(altmetrics_file,'r') as inputfile:
        altdump = json.load(inputfile)
    for eachdict in altdump:
        yield(eachdict)