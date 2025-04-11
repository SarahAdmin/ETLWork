import pandas as pd

mdf = pd.read_excel('Excel example data (2).xlsx',sheet_name='Data 2')

columnToDelete1 = ['DOB']
mdf2 = mdf.drop(columnToDelete1, axis=1)
membersActive = mdf2.where(mdf['Status'] == 'Active').dropna()

print(membersActive.to_string())
