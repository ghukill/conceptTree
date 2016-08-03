# parse concepts in xslx

import json
import os
import sys

# OPENPYXL
from openpyxl import load_workbook

class ConceptNode(object):

    def __init__(self, name, children):
        self.name = name
        self.children = children

    def asDict(self):
        return {
            "name":self.name,
            "children":self.children
        }

def parse_concepts(f):
    # load workbook
    wb = load_workbook(f)

    # get active (only) sheet
    ws = wb.active

    # beging to build python dictionary
    concept_dict = {}


if __name__ == '__main__':
    parse_concepts(sys.argv[1])
