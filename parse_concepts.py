# parse concepts in xslx

import json
import os
import sys

# OPENPYXL
from openpyxl import load_workbook


def convert_data(data):                                     
    out = {'name': 'root', 'children': []}           

    for row in data:                                 
        out['children'].append({})                   
        current = out['children']                    
        for value in row:                            
            current[-1]['name'] = value.value              
            current[-1]['children'] = [{}]           

            current = current[-1]['children']        

    return out 


def parse_concepts(f,t):
    # load workbook
    wb = load_workbook(f)

    # get active (only) sheet
    ws = wb.active

    # convert
    # http://stackoverflow.com/a/38753169/1196358
    flare_dict = convert_data(ws.rows)
    
    # write to file    
    with open('assets/flare_json/%s' % t) as fhand:
        fhand.write(json.dumps(flare_dict))


if __name__ == '__main__':
    parse_concepts(sys.argv[1],sys.argv[2])
