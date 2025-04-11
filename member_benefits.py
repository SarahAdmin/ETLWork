import pandas as pd 

mdf = pd.read_excel('Excel example data (2).xlsx',sheet_name='Data 2') 

columnToDelete1 = ['DOB']
mdf1 = mdf.drop(columnToDelete1, axis=1) 
membersPayment = mdf1.where(mdf['Status'] == 'In Payment').dropna() 

print(membersPayment.to_string())
