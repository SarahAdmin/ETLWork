import pandas as pd 

driveDF = pd.read_csv('drt121f-car-driving-tests-top-10-faults.csv',encoding='latin-1')
columnToDelete = ['Period']  
driveOne = driveDF.drop(columnToDelete,axis=1) 
driveOne = driveDF.duplicated() 

print(driveOne)
