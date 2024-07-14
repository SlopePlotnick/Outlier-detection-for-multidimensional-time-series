import pandas as pd
import numpy as np

df = pd.read_csv('result.csv')
rst = df.values
np.savetxt('detection-20242223571.txt', rst, fmt='%d')