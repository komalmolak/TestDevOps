import pandas as pd

import numpy as np

#dfmay = pd.read_excel(io="C:/Users/komalmo/OneDrive - AMDOCS/Backup Folders/Desktop/Python/Actual_rate.xlsx")
dfactual = pd.read_excel(io="Structured_Actual_RC.xlsx")

#dfjune = pd.read_excel(io="C:/Users/komalmo/OneDrive - AMDOCS/Backup Folders/Desktop/Python/Expected_Rate.xlsx")
dfexpected = pd.read_excel(io="Structued_Expected_RC.xlsx")

#print(dfmay.equals(dfjune))

comparevalues = dfactual.values == dfexpected.values

print(comparevalues)

rows,cols = np.where(comparevalues==False)

for item in zip(rows,cols):
    dfactual.iloc[item[0],item[1]] = ' {} --> {} '.format(dfactual.iloc[item[0], item[1]], dfexpected.iloc[item[0],item[1]])


dfactual.to_excel('outputRC.xlsx', index=False,header=True)
 