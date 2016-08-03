# parse xslx with pandas

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd

# load dataframe
tdf = pd.read_excel(sys.argv[1])

# build flare.json
flare = {}



