# parse xslx


# # # OPENPYXL
# # openpyxl reqs
# from openpyxl import load_workbook
# 
# # load workbook
# wb = load_workbook('theme_connections.xlsx')
# 
# # get active (only) sheet
# ws = wb.active
# 
# # beging to build python dictionary
# theme_dict = {}


# PANDAS 
# panda reqs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd

# load dataframe
tdf = pd.read_excel('theme_connections.xlsx')

# build flare.json
flare = {}



