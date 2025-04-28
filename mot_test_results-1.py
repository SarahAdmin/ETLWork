import pandas as pd 

motDF = pd.read_csv('dvsa-mot-01-mot-test-results-by-class-of-vehicle.csv',encoding='latin-1')

df_duplicated = motDF.duplicated() 

print(df_duplicated)
                    
