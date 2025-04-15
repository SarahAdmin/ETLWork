import pandas as pd 
members_df = pd.read_excel('Excel example data (2).xlsx',sheet_name='Data 2') 
duplicatedMembers = members_df.duplicated()
print(duplicatedMembers)

// the output returns boolean values // 
