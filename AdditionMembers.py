import pandas as pd

mdf = pd.read_excel('Excel example data (2).xlsx',sheet_name='Data 1')

columnToDelete1 = ['DOB']
mdf1 = mdf.drop(columnToDelete1, axis=1)
membersAddition = mdf1.where(mdf['Status'] == 'Addition').dropna()

print(membersAddition.to_string())
