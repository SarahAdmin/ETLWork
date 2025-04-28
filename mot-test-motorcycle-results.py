import pandas as pd 
motDF = pd.read_csv('dvsa-mot-01-mot-test-results-by-class-of-vehicle.csv',encoding='latin-1')
motorcycle_results = motDF.where(motDF['Class'] == 'Classes 1 & 2: Motorcycles').dropna() 
print('MOT Motorcycle Results')
print(motorcycle_results.to_string())
